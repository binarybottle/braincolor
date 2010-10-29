
import sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import itertools
from colormath.color_objects import LCHuvColor
from braingraph import G

plot_original_graph = 0
plot_colormap = 0
plot_graph = 1

run_permutations = 0
  
Ntotal = G.number_of_nodes()
color_angle = 360.0/Ntotal
Lumas_init = np.arange(20,80,20)
incr_Luma = 5
init_angle = 0
chroma = 90
number_min = 100
number_max = 600
step = 10

# Plot whole graph, with subgraphs in different colors
if plot_original_graph:
    #neighbor_matrix_all = nx.to_numpy_matrix(G)
    fig1 = plt.figure(figsize=(10,10))
    pos = nx.graphviz_layout(G,prog="neato")
    subG = nx.connected_component_subgraphs(G)
    colors = ['cyan','pink','yellow','tan','white']
    for i, g in enumerate(subG):
        nx.draw(g, pos, node_size=1200, node_color=colors[i])

# Loop through subgraphs
for number_start in range(number_min,number_max,step):   
    outlist = [n for n,d in G.nodes_iter(data=True) \
               if ('lobe' in d.keys()) and \
               (np.int(d['num'])>number_start) and \
               (np.int(d['num'])<number_start+step)] 
    N = len(outlist)
    if N > 0:
        g = G.subgraph(outlist)
                
        # Define colormap as uniformly distributed colors in CIELch color space
        Lumas = Lumas_init.copy()
        while len(Lumas) < N: 
            Lumas_init += incr_Luma
            Lumas = np.hstack((Lumas,Lumas_init))
        hues = np.arange(init_angle, init_angle + N*color_angle, color_angle)
        init_angle += N*color_angle
    
        # Compute the differences between every pair of colors in the colormap
        if run_permutations:
            # Convert subgraph into an adjacency matrix (1 for adjacent pair of regions)
            neighbor_matrix = np.array(nx.to_numpy_matrix(g))
    
            # Compute permutations of colors and color pair differences
            DEmin = np.Inf
            permutations = [np.array(s) for s in itertools.permutations(range(0,N),N)]
            for ipermutations in range(len(permutations)):
                permutation = permutations[ipermutations]
                color_delta_matrix = np.zeros(np.shape(neighbor_matrix))   
                for i1, icolor1 in enumerate(permutation):
                    lch1 = LCHuvColor(Lumas[icolor1],chroma,hues[icolor1]) 
                    for i2, icolor2 in enumerate(permutation):
                        if i2 > i1:
                            lch2 = LCHuvColor(Lumas[icolor2],chroma,hues[icolor2])
                            DE = lch1.delta_e(lch2, mode='cie2000')
                            color_delta_matrix[i1,i2] = DE   
                DE = np.sum((color_delta_matrix * neighbor_matrix))
                # Store the color permutation with the minimum adjacency cost
                if DE < DEmin:
                    DEmin = DE
                    permutation_min = permutation
               
        # Plot the reordered colormap for the subgraph    
        if plot_colormap:
            fig3 = plt.figure(figsize=(5,10))
            fig3.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)
            for iN in range(N):
                ax = plt.subplot(N, 1, iN+1)
                plt.axis("off")
                ic = permutation_min[iN]
                lch = LCHuvColor(Lumas[ic],chroma,hues[ic]) #print(lch)
                rgb = lch.convert_to('rgb', debug=False)
                plt.barh(0,50,1,0, color=[rgb.rgb_r/255.,rgb.rgb_g/255.,rgb.rgb_b/255.])
                pos = list(ax.get_position().bounds)
    
        # Draw a figure of the colored subgraph
        if plot_graph:
            fig4 = plt.figure(figsize=(10,10))
            pos = nx.graphviz_layout(G,prog="neato")
            subG = nx.connected_component_subgraphs(G)
            colors = ['cyan','pink','yellow','tan','white']
            for i, g in enumerate(subG):
                if i==0:
                    #nx.draw(g, pos, node_size=1200, node_color=colors[i])
                    for iN in range(N):
                        ic = permutation_min[iN]
                        lch = LCHuvColor(Lumas[ic],chroma,hues[ic]) #print(lch)
                        rgb = lch.convert_to('rgb', debug=False)
                        color = [rgb.rgb_r/255.,rgb.rgb_g/255.,rgb.rgb_b/255.]
                        nx.draw_networkx_nodes(g, pos, node_size=1200, nodelist=[g.node.keys()[iN]], node_color=color)
                        nx.draw_networkx_edges(g, pos, alpha=0.75, width=2)
                else:
                    nx.draw(g, pos, node_size=1200, node_color=colors[i])
            
                sys.exit()

