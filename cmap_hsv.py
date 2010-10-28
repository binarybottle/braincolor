
import sys
import Image
import numpy as np
import matplotlib.colors as clr
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from colormath.color_objects import HSVColor

N = 62 # number of desired maximally distinct colors in CIELUV
incr_distance = 0.1

use_hsv = 1
if use_hsv:
     
    c = 1
    #while len(c) < N:
    #    c = np.hstack((c,c))
    L = np.arange(0.20,0.79,0.20)
    nL = len(L)
    #L = (L*np.ones((np.ceil(N/np.float(nL)),nL))).transpose().ravel()
    while len(L) < N:
        L = np.hstack((L,L))
    d = nL * 360/N
    D = np.arange(0,360,d)
    nD = len(D)
    D = (D*np.ones((np.ceil(N/np.float(nD)),nD))).transpose().ravel()
    #while len(D) < N:
    #    D = np.hstack((D,D))
    rgb = np.zeros((N,3))
    for i in range(N):
        lch = HSVColor(D[i],c,L[i]) 
        print(lch)
        lch2rgb = lch.convert_to('rgb', debug=False)
        rgb[i,0] = lch2rgb.rgb_r / 255.
        rgb[i,1] = lch2rgb.rgb_g / 255.
        rgb[i,2] = lch2rgb.rgb_b / 255.
    print(rgb)
    
    fig = plt.figure(figsize=(5,10))
    fig.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)
    for i in range(N):
        ax = plt.subplot(N, 1, i+1)
        plt.axis("off")
        plt.barh(0,100,1,0, color=rgb[i,:])
        pos = list(ax.get_position().bounds)
        fig.text(pos[0] - 0.01, pos[1], str(rgb[i,:]), fontsize=11, horizontalalignment='right')
    plt.show()
