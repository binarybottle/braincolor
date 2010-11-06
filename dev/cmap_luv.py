
import sys
import Image
import numpy as np
import matplotlib.colors as clr
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from colormath.color_objects import XYZColor
from colormath.color_objects import LuvColor
from colormath.color_objects import LCHuvColor

N = 62 # number of desired maximally distinct colors in CIELUV
incr_distance = 0.1
use_full_cie1976 = 0

u_range = [-100,100]  # [-134,220]
v_range = [-100,100]  # [-140,122]

use_full_cie1976 = 0
if use_full_cie1976:
    pass
else:
    """
    srgb_red_xyz = [0.6400,0.3300,0.0300]
    srgb_green_xyz = [0.3000,0.6000,0.0600]
    srgb_blue_xyz = [0.1500,0.0600,0.7900]
    srgb_white_xyz = [0.3127,0.3290,0.3583]
    red_xyz = XYZColor(srgb_red_xyz[0],srgb_red_xyz[1],srgb_red_xyz[2])
    green_xyz = XYZColor(srgb_green_xyz[0],srgb_green_xyz[1],srgb_green_xyz[2])
    blue_xyz = XYZColor(srgb_blue_xyz[0],srgb_blue_xyz[1],srgb_blue_xyz[2])
    red_xyz2luv = red_xyz.convert_to('luv', debug=False)
    green_xyz2luv = green_xyz.convert_to('luv', debug=False)
    blue_xyz2luv = blue_xyz.convert_to('luv', debug=False)
    red_luv[i,0] = red_xyz2luv.luv_l
    green_luv[i,1] = green_xyz2luv.luv_u
    blue_luv[i,2] = blue_xyz2luv.luv_v
    """
     
    c = 100
    #while len(c) < N:
    #    c = np.hstack((c,c))
    L = np.arange(20,80,20)
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
        lch = LCHuvColor(L[i],c,D[i]) 
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
     
     
if use_full_cie1976:
    est_distance = (u_range[1]-u_range[0] + 1)*(v_range[1]-v_range[0] + 1)/N
    decr_distance = 0   
    while 1 > 0:                             
        d = est_distance - decr_distance
        u1 = np.arange(u_range[0],u_range[1],d)
        u2 = np.arange(u_range[0]+np.round(d/2),u_range[1],d)
        h = d * 0.8660254037844386 #np.sqrt(0.75)
        v1 = np.arange(v_range[0],v_range[1],2*h)
        v2 = np.arange(v_range[0]+h,v_range[1],2*h)
        o1 = np.ones(len(u1))
        o2 = np.ones(len(u2))
        for i in range(len(v1)):
            if i==0:
                uv = np.vstack((u1,v1[i]*o1)).transpose()
            else:
                uv = np.vstack((uv,np.vstack((u1,v1[i]*o1)).transpose())) 
        for i in range(len(v2)):
            uv = np.vstack((uv,np.vstack((u2,v2[i]*o2)).transpose())) 
        
        len_uv = np.shape(uv)[0]
        print(str(len_uv) + ' points, distance = ' + str(d))
        if len_uv >= N:
            break
        else:
            decr_distance += incr_distance
       
    #plt.plot(uv[:,0],uv[:,1],'bo')
    npts = len_uv
    rgb = np.zeros((len_uv,3))
    for i in range(len_uv):
        luv = LuvColor(L,uv[i,0],uv[i,1])
        luv2rgb = luv.convert_to('rgb', debug=False)
        rgb[i,0] = luv2rgb.rgb_r / 255.
        rgb[i,1] = luv2rgb.rgb_g / 255.
        rgb[i,2] = luv2rgb.rgb_b / 255.
    print(rgb)
    
    fig = plt.figure(figsize=(5,10))
    fig.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)
    for i in range(npts):
        ax = plt.subplot(npts, 1, i+1)
        plt.axis("off")
        plt.barh(0,100,1,0, color=rgb[i,:])
        pos = list(ax.get_position().bounds)
        fig.text(pos[0] - 0.01, pos[1], str(rgb[i,:]), fontsize=11, horizontalalignment='right')
    plt.show()
