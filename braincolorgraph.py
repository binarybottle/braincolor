
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import itertools
from colormath.color_objects import LCHuvColor
from braingraph import G

plot_initial_graph = 0
plot_initial_colormap = 0
plot_graph = 0
plot_colormap = 1

color_differences = 1  
color_permutations = 1  

Nregions = [7,6,4,3,2, 4,3,1, 4,2, 4,1,3, 3,2] # number of desired maximally distinct colors in CIELUV
incr_Luma = 5

# Plot whole graph, with subgraphs in different colors
if plot_initial_graph:
    #neighbor_matrix_all = nx.to_numpy_matrix(G)
    pos = nx.graphviz_layout(G,prog="neato")
    subG = nx.connected_component_subgraphs(G)
    colors = ['cyan','pink','yellow','tan','white']
    for i, g in enumerate(subG):
        nx.draw(g, pos, node_size=1200, node_color=colors[i])

# Loop through subgraphs
Ntotal = sum(Nregions)
for iN, N in enumerate(Nregions):
    if iN == 1:
        break 
    color_angle = 360.0/pow(N,2)  # print(N, color_angle)
    
    # Define colormap as uniformly distirbuted colors in CIELch color space
    chroma = 90
    Lumas_init = np.arange(20,80,20)
    nLumas = len(Lumas_init)
    Lumas = Lumas_init.copy()
    while len(Lumas) < N: 
        Lumas_init += incr_Luma
        Lumas = np.hstack((Lumas,Lumas_init))
    hue_angles = np.arange(0, color_angle, nLumas*color_angle/N)
    nangles = len(hue_angles)
    hue_angles = (hue_angles*np.ones((np.ceil(N/np.float(nangles)),nangles))).ravel()

    # Plot the initial colormap for the subgraph    
    if plot_initial_colormap:
        fig = plt.figure(figsize=(5,10))
        fig.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)
        for i in range(N):
            ax = plt.subplot(N, 1, i+1)
            plt.axis("off")
            lch = LCHuvColor(Lumas[i],chroma,hue_angles[i]) #print(lch)
            rgb = lch.convert_to('rgb', debug=False)
            plt.barh(0,100,1,0, color=[rgb.rgb_r/255.,rgb.rgb_g/255.,rgb.rgb_b/255.])
            pos = list(ax.get_position().bounds)
    
    # Compute the differences between every pair of colors in the colormap
    if color_differences:
        # Convert subgraph into an adjacency matrix (1 for adjacent pair of regions)
        outlist = [n for n,d in G.nodes_iter(data=True) \
                   if ('lobe' in d.keys()) and (d['lobe']=='FL') and (d['sub']=='lateral surface')]
        g = G.subgraph(outlist)
        neighbor_matrix = np.array(nx.to_numpy_matrix(g))
                
        # Find color differences
        color_delta_matrix = np.zeros(np.shape(neighbor_matrix))   
        for i in range(N):
            lch1 = LCHuvColor(Lumas[i],chroma,hue_angles[i]) 
            for j in range(N):
                if j > i:
                    lch2 = LCHuvColor(Lumas[j],chroma,hue_angles[j])
                    DE = lch1.delta_e(lch2, mode='cie2000')
                    color_delta_matrix[i,j] = DE
        
    # Store the color permutation with the minimum adjacency cost
    if color_permutations:
        DEmin = np.Inf
        color_permutations = [np.array(s) for s in itertools.permutations(range(0,N),N)]
        for ip in range(len(color_permutations)):
            color_permutation = color_permutations[ip]
            DE = np.sum((color_delta_matrix[color_permutation] * neighbor_matrix))
            if DE < DEmin:
                DEmin = DE
                color_permutation_min = color_permutation
           
    # Plot the reordered colormap for the subgraph    
    if plot_colormap:
        fig = plt.figure(figsize=(5,10))
        fig.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)
        for ip in range(N):
            ax = plt.subplot(N, 1, ip+1)
            plt.axis("off")
            ic = color_permutation_min[ip]
            lch = LCHuvColor(Lumas[ic],chroma,hue_angles[ic]) #print(lch)
            rgb = lch.convert_to('rgb', debug=False)
            plt.barh(0,100,1,0, color=[rgb.rgb_r/255.,rgb.rgb_g/255.,rgb.rgb_b/255.])
            pos = list(ax.get_position().bounds)

    # Draw a figure of the colored subgraph
    if plot_graph:
        pos = nx.graphviz_layout(G,prog="neato")
        subG = nx.connected_component_subgraphs(G)
        colors = ['cyan','pink','yellow','tan','white']
        for i, g in enumerate(subG):
            if i==0:
                nx.draw(g, pos, node_size=1200, node_color=colors[i])
            else:
                nx.draw(g, pos, node_size=1200, node_color=colors[i])
        


