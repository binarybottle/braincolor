#! /usr/bin/env python
#                                                      
# 1. Read in an Excel file with a weighted connection matrix,
#    where each row and column represents a region of the brain, and values
#    are a function of how much of the adjacent regions' boundaries are shared. 
# 2. Convert the matrix to a NetworkX weighted graph.
# 3. Create a colormap for the number of brain regions, with hues that are 
#    uniformly distributed about a cylindrical color space, such as CIELch.
# 4. Plot the colormap, the graph, or output a modified XML file.
#
# The graph is plotted as a collection of subgraphs, with each subgraph 
# representing a collection of adjacent regions within a lobe, and assigned
# adjacent colors in the color space.  
# All permutations are computed for the colors of each subgraph, 
# and the winning permutation is the one that maximizes the
# discriminability of the colors of nodes of highest degree.
# This is performed by mulfiplying the connection matrix for each subgraph
# by the color difference matrix for each permutation. 
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

# Choose one procedure to run:
plot_graph = 0
plot_subgraphs = 1
make_xml = 0
plot_colormap = 0
plot_subcolormaps = 0

# Files
in_xml = 'input/parcLabels.xml'
out_xml = 'output/parcLabels.xml'
in_table = 'input/average_parc_Connectivity.xls'
row1 = 1  # first row with data
col1 = 4  # first column with data
everyother = 2  # use <everyother> alternate rows/columns;
                # set to 2 for redundant labels across brain hemispheres
use_weights = 1

# Color parameters
Lumas_init = np.arange(40,70,10)  # vary luminance values for adjacent colors
chroma = 100  # color "saturation" level
code_min = 10
code_max = 60
code_step = 1

# Convert weighted connection matrix to weighted graph
book = xlrd.open_workbook(in_table)
sheet = book.sheets()[0]
roi_abbrs = sheet.col_values(0)[1:sheet.ncols:everyother]
roi_names = sheet.col_values(1)[1:sheet.ncols:everyother]
roi_numbers = sheet.col_values(2)[1:sheet.ncols:everyother] 
roi_numbers = [str(s).strip() for s in roi_numbers]
roi_abbrs = [str(s).strip() for s in roi_abbrs]
roi_names = [str(s).strip().strip('Right ') for s in roi_names]
iA = 0
A = np.zeros(((sheet.nrows-row1)/everyother,(sheet.ncols-col1)/everyother))
for irow in range(row1,sheet.nrows,everyother):
    Arow = [s.value for s in sheet.row(irow)[col1:]]
    A[iA] = Arow[0:len(Arow):everyother]
    iA += 1
A = A/np.max(A)  # normalize weights
G = nx.from_numpy_matrix(A)
Ntotal = G.number_of_nodes()
for inode in range(Ntotal):
    G.node[inode]['abbr'] = roi_abbrs[inode] 
    G.node[inode]['name'] = roi_names[inode] 
    G.node[inode]['lobe'] = roi_numbers[inode].split('.')[0]
    G.node[inode]['sub']  = roi_numbers[inode].split('.')[1]
    G.node[inode]['code'] = np.int(G.node[inode]['lobe']+G.node[inode]['sub'])

# Secondary parameters
init_angle = 0
color_angle = 360.0/Ntotal

# Plot the colormap for the whole graph    
if plot_colormap:
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
        
# Plot graph
if plot_graph:
    labels={}
    for i in range(Ntotal):
        labels[i] = G.node[i]['abbr']
    pos = nx.graphviz_layout(G,prog="neato")
    #pos = nx.spring_layout(G)
    colors=range(G.number_of_edges())
    nx.draw(G,pos,node_color='#333399',node_size=600,edge_color=colors,width=3,edge_cmap=plt.cm.Blues,with_labels=False)
    nx.draw_networkx_labels(G, pos, labels, font_size=8, font_color='white')
    plt.axis('off')
    
if make_xml:
    tree = et.ElementTree(file=in_xml)
    
# Loop through subgraphs
if plot_graph + plot_subcolormaps + plot_subgraphs + make_xml > 0:
    run_permutations = 1
    for code_start in range(code_min,code_max,code_step):   
        outlist = [n for n,d in G.nodes_iter(data=True) \
                   if (np.int(d['code'])>code_start) and \
                      (np.int(d['code'])<=code_start+code_step)] 
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
                #matrix_sum = np.sum(neighbor_matrix, axis=0)
                #neighbor_matrix = neighbor_matrix * (matrix_sum * np.ones((N,N))).transpose()
                if use_weights:
                    pass
                else:
                    neighbor_matrix = (neighbor_matrix > 0).astype(np.uint8)
    
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
                    # Store the color permutation with the maximum adjacency cost
                    if DE > DEmax:
                        DEmax = DE
                        permutation_max = permutation
                        #color_delta_matrix_max = color_delta_matrix
            # Plot the reordered colormap for the subgraph    
            if plot_subcolormaps:
                fig3 = plt.figure(figsize=(5,10))
                fig3.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)
                for iN in range(N):
                    ax = plt.subplot(N, 1, iN+1)
                    plt.axis("off")
                    ic = np.int(permutation_max[iN])
                    lch = LCHuvColor(Lumas[ic],chroma,hues[ic]) #print(lch)
                    rgb = lch.convert_to('rgb', debug=False)
                    plt.barh(0,50,1,0, color=[rgb.rgb_r/255.,rgb.rgb_g/255.,rgb.rgb_b/255.])
                    
            # Color subgraphs
            if plot_graph:
                for iN in range(N):
                    ic = np.int(permutation_max[iN])
                    lch = LCHuvColor(Lumas[ic],chroma,hues[ic]) #print(lch)
                    rgb = lch.convert_to('rgb', debug=False)
                    color = [rgb.rgb_r/255.,rgb.rgb_g/255.,rgb.rgb_b/255.]
                    nx.draw_networkx_nodes(g,pos,node_size=600,nodelist=[g.node.keys()[iN]],node_color=color)

            # Draw a figure of the colored subgraph
            if plot_subgraphs:
                labels={}
                for iN in range(N):
                    labels[iN] = g.node[g.nodes()[iN]]['abbr']
                pos = nx.graphviz_layout(g,prog="neato")
                #pos = nx.spring_layout(G)
                colors=range(g.number_of_edges())
                nx.draw(g,pos,node_size=600,edge_color=colors,width=3,edge_cmap=plt.cm.Blues,with_labels=False)
                nx.draw_networkx_labels(g,pos,labels,font_size=8,font_color='white')
                plt.axis('off')
                #sys.exit()
                for iN in range(N):
                    ic = np.int(permutation_max[iN])
                    lch = LCHuvColor(Lumas[ic],chroma,hues[ic]) #print(lch)
                    rgb = lch.convert_to('rgb', debug=False)
                    color = [rgb.rgb_r/255.,rgb.rgb_g/255.,rgb.rgb_b/255.]
                    nx.draw_networkx_nodes(g,pos,node_size=600,nodelist=[g.node.keys()[iN]],node_color=color)
                sys.exit()
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
