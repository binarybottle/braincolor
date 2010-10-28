
import sys
import Image
import numpy as np
import matplotlib.colors as clr
import matplotlib.cm as cm
import matplotlib.pyplot as plt

N = 62 # number of desired maximally distinct colors in CIELUV

use_rgb = 1
if use_rgb:
     
    d = pow(255/62.0, 3.0)
    rgb = np.zeros((N,3))
    i = 0
    for r in range(0,255,d):
        for g in range(0,255,d):
            for b in range(0,255,d):
                if i >= N:
                    break
                else:
                    rgb[i,0] = r/255.0
                    rgb[i,1] = g/255.0
                    rgb[i,2] = b/255.0
                    i += 1
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
