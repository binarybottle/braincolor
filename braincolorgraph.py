#! /usr/bin/env python
#                                                      22 October 2010
# Read in weighted connection matrix (Excel file) and convert to weighted graph.
# Plot the colormap for the whole graph    
# Define colormap as uniformly distributed colors in CIELch color space
# Plot whole graph, with subgraphs in different colors
# Define colormap as uniformly distributed colors in CIELch color space
# Compute the differences between every pair of colors in the colormap
# Convert subgraph into an adjacency matrix (1 for adjacent pair of regions)
# Compute permutations of colors and color pair differences
# Plot the reordered colormap for the subgraph    
# Draw a figure of the colored subgraph
# Generate XML output       
#
# (c) Copyright 2010 . arno klein . arno@binarybottle.com . MIT license
#

import sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import re
import itertools
from colormath.color_objects import LCHuvColor
from elementtree import ElementTree as et
import xlrd

# Procedures
plot_whole_colormap = 0
plot_whole_graph = 0 
plot_colormap = 0
plot_graph = 1
make_xml = 0

# Files
in_xml = 'input/parcLabels.xml'
out_xml = 'output/parcLabels.xml'
in_table = 'input/average_parc_Connectivity.xls'
row1 = 1
col1 = 4
everyother = 2

# Color parameters
Lumas_init = np.arange(40,70,10)
init_angle = 0
chroma = 100
number_min = 10
number_max = 60
number_step = 10

# Convert weighted connection matrix to weighted graph
book = xlrd.open_workbook(in_table)
sheet = book.sheets()[0]
roi_numbers = sheet.col_values(0)[1:sheet.ncols:everyother] 
roi_abbrs = sheet.col_values(1)[1:sheet.ncols:everyother]
roi_names = sheet.col_values(2)[1:sheet.ncols:everyother]
roi_numbers = [str(s).strip() for s in roi_numbers]
roi_abbrs = [str(s).strip() for s in roi_abbrs]
roi_names = [str(s).strip().strip('Right ') for s in roi_names]
iA = 0
A = np.zeros(((sheet.nrows-row1)/everyother,(sheet.ncols-col1)/everyother))
for irow in range(row1,sheet.nrows,everyother):
    Arow = [s.value for s in sheet.row(irow)[col1:]]
    A[iA] = Arow[0:len(Arow):everyother]
    iA += 1
G = nx.from_numpy_matrix(A)
Ntotal = G.number_of_nodes()
for inode in range(Ntotal):
    G.node[inode]['abbr'] = roi_abbrs[inode] 
    G.node[inode]['name'] = roi_names[inode] 
    G.node[inode]['lobe'] = roi_numbers[inode].split('.')[0]
    G.node[inode]['sub']  = roi_numbers[inode].split('.')[1]
    G.node[inode]['code'] = np.int(G.node[inode]['lobe']+G.node[inode]['sub'])

# Secondary parameters
color_angle = 360.0/Ntotal
if plot_colormap + plot_graph + make_xml > 0:
    run_permutations = 1
else: 
    run_permutations = 0

# Plot the colormap for the whole graph    
if plot_whole_colormap:
    fig1 = plt.figure(figsize=(5,10))
    # Define colormap as uniformly distributed colors in CIELch color space
    Lumas = Lumas_init.copy()
    while len(Lumas) < Ntotal: 
        Lumas = np.hstack((Lumas,Lumas_init))
    hues = np.arange(init_angle, init_angle + Ntotal*color_angle, color_angle)
    for iN in range(Ntotal):
        ax = plt.subplot(Ntotal, 1, iN+1)
        plt.axis("off")
        lch = LCHuvColor(Lumas[iN], chroma, hues[iN]) #print(lch)
        rgb = lch.convert_to('rgb', debug=False)
        plt.barh(0,50,1,0, color=[rgb.rgb_r/255.,rgb.rgb_g/255.,rgb.rgb_b/255.])
        
# Plot whole graph, with subgraphs in different colors
if plot_whole_graph:
    pos = nx.graphviz_layout(G,prog="neato")
    subG = nx.connected_component_subgraphs(G)
    colors = ['cyan','pink','yellow','tan','white']
    for i, g in enumerate(subG):
        nx.draw(g, pos, node_size=1200, node_color=colors[i])

if make_xml:
    tree = et.ElementTree(file=in_xml)
    
# Loop through subgraphs
for number_start in range(number_min,number_max,number_step):   
    outlist = [n for n,d in G.nodes_iter(data=True) \
               if (np.int(d['code'])>number_start) and \
                  (np.int(d['code'])<number_start+number_step)] 
    N = len(outlist)
    if N > 0:
        g = G.subgraph(outlist)
                
        # Define colormap as uniformly distributed colors in CIELch color space
        Lumas = Lumas_init.copy()
        while len(Lumas) < N: 
            Lumas = np.hstack((Lumas,Lumas_init))
        hues = np.arange(init_angle, init_angle + N*color_angle, color_angle)
        init_angle += N*color_angle
    
        # Compute the differences between every pair of colors in the colormap
        if run_permutations:
            # Convert subgraph into an adjacency matrix (1 for adjacent pair of regions)
            neighbor_matrix = np.array(nx.to_numpy_matrix(g))
            matrix_sum = np.sum(neighbor_matrix, axis=0)
            neighbor_matrix = neighbor_matrix * (matrix_sum * np.ones((N,N))).transpose()

            # Compute permutations of colors and color pair differences
            DEmax = 0
            permutations = [np.array(s) for s in itertools.permutations(range(0,N),N)]
            permutation_max = np.zeros(N)
            for ipermutations in range(len(permutations)):
                permutation = permutations[ipermutations]
                color_delta_matrix = np.zeros(np.shape(neighbor_matrix))   
                for i1, icolor1 in enumerate(permutation):
                    lch1 = LCHuvColor(Lumas[icolor1],chroma,hues[icolor1]) 
                    for i2, icolor2 in enumerate(permutation):
                        if (i2 > i1) and (neighbor_matrix[i1,i2] > 0):
                            lch2 = LCHuvColor(Lumas[icolor2],chroma,hues[icolor2])
                            DE = lch1.delta_e(lch2, mode='cie2000')
                            color_delta_matrix[i1,i2] = DE   
                DE = np.sum((color_delta_matrix * neighbor_matrix))
                # Store the color permutation with the minimum adjacency cost
                if DE > DEmax:
                    DEmax = DE
                    permutation_max = permutation
                    #color_delta_matrix_max = color_delta_matrix
               
        # Plot the reordered colormap for the subgraph    
        if plot_colormap:
            fig3 = plt.figure(figsize=(5,10))
            fig3.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)
            for iN in range(N):
                ax = plt.subplot(N, 1, iN+1)
                plt.axis("off")
                ic = permutation_max[iN]
                lch = LCHuvColor(Lumas[ic],chroma,hues[ic]) #print(lch)
                rgb = lch.convert_to('rgb', debug=False)
                plt.barh(0,50,1,0, color=[rgb.rgb_r/255.,rgb.rgb_g/255.,rgb.rgb_b/255.])
        # Draw a figure of the colored subgraph
        if plot_graph:
            pos = nx.graphviz_layout(G,prog="neato")  #nx.spring_layout(G)
            #nx.draw(G, pos, node_size=1200, node_color='cyan') #, hold=True)
            node_labels = []    
            print('HEY')
            for node in g.nodes(data=True):
                node_labels.append(node['abbr'])

            for iN in range(N):
                ic = permutation_max[iN]
                node_label = node_labels[ic]
                lch = LCHuvColor(Lumas[ic],chroma,hues[ic]) #print(lch)
                rgb = lch.convert_to('rgb', debug=False)
                color = [rgb.rgb_r/255.,rgb.rgb_g/255.,rgb.rgb_b/255.]
                nx.draw_networkx_nodes(g, pos, node_size=1200, nodelist=[g.node.keys()[iN]], node_color=color, labels=node_label)
                nx.draw_networkx_edges(g, pos, alpha=0.75, width=2)
                nx.draw_networkx_labels(g, pos, font_size=10, font_color='white')
            #sys.exit()
            
        # Generate XML output       
        """
        <LabelList>
        <Label>
          <Name>3rd Ventricle</Name>
          <Number>4</Number>
          <RGBColor>204 182 142</RGBColor>
        </Label>
        """
        if make_xml:
            for iN in range(N):
                ic = np.int(permutation_max[iN])
                lch = LCHuvColor(Lumas[ic],chroma,hues[ic]) #print(lch)
                rgb = lch.convert_to('rgb', debug=False)
                color = [rgb.rgb_r, rgb.rgb_g, rgb.rgb_b]
                color = ' '.join([str(s) for s in color])
                
                for elem in tree.getiterator()[0]:
                    if g.nodes()[ic] in elem.getchildren()[0].text:
                        elem.getchildren()[2].text = color
if make_xml:
    tree.write(out_xml)
