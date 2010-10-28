
import Image
import numpy as np
import matplotlib.colors as clr
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from colormath.color_objects import xyYColor

N = 100.0 # number of desired maximally distinct colors in CIELUV
uniformly_distribute_points = 1

if uniformly_distribute_points: 
    point_shift = 1
else:
    from kdtree import distance_matrix
    ntrials = 10
    add_incr = 10
    
img = Image.open("CIE/CIE_1976_UCS_mask.png")
mask = np.array(img)[:,:,0]/255
npixels = np.prod(img.size)
npixelsY = img.size[1]
npixelsX = img.size[0]
#white_point = [0.2009,0.4610]
cie_scale = 0.6/npixelsY
L = 0.5

if uniformly_distribute_points: 
    # Assuming the masked area covers mask_fraction of the mask image,
    # then a uniform grid spacing is: N/mask_fraction = #pixels / (distance between points)^2
    est_distance = np.int(np.round(np.sqrt(npixels/N)))
    decr_distance = 0   
    while 1 > 0:                             
        d = est_distance - decr_distance
        array1 = np.arange(0,npixelsX,d)
        array2 = np.arange(np.round(d/2),npixelsX,d)
        h = d * 0.8660254037844386 #np.sqrt(0.75)
        mask_points = np.zeros((npixelsY,npixelsX))
        for i in range(0,npixelsY,2*h):
            mask_points[i,array1] = 1
        for i in range(h,npixelsY,2*h):
            mask_points[i,array2] = 1
        mask_points = mask * mask_points
        print(str(np.sum(mask_points > 0)) + ' points, distance = ' + str(d))
        if np.sum(mask_points > 0) >= N:
             break
        else:
             decr_distance += 1

    mask_points = mask * mask_points 
    #plt.imshow(mask_points, cmap=cm.gray)
    #plt.show()
    
    [maskx,masky] = np.where(mask_points == 1)
    u = cie_scale*maskx
    v = cie_scale*masky # uv = np.vstack((u,v)).transpose()
    npts = len(u)
    x = np.zeros(npts)
    y = np.zeros(npts)
    for i in range(npts):
        x[i] = 9*u[i]/(6*u[i] - 16*v[i] + 12)
        y[i] = 4*v[i]/(6*u[i] - 16*v[i] + 12)  #[L*13*(s*cie_scale - white_point[1]) for s in y]
    rgb = np.zeros((npts,3))
    for i in range(0,npts):
        xyy = xyYColor(x[i],y[i],L)
        xyy2rgb = xyy.convert_to('rgb', target_rgb='srgb', target_illuminant=('Native'), debug=False)
        rgb[i,0] = xyy2rgb.rgb_r / 255.
        rgb[i,1] = xyy2rgb.rgb_g / 255.
        rgb[i,2] = xyy2rgb.rgb_b / 255.
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
        
 
else:
    # Assuming the masked area covers 1/3 of the mask image,
    # then a uniform grid spacing is: 3*N = #pixels / (distance between points)^2
    # use 1/10th of this expected spacing: 
    mask_min_distance = np.sqrt(npixels/(10*N))
    
    mask_points = np.zeros((np.shape(mask)[0], np.shape(mask)[1], ntrials))
    mask_distances = np.zeros(ntrials)
    for i in range(ntrials):
        add_npoints = 0   
        while 1 > 0:                             
            random_xy = np.random.rand(npixelsY,npixelsX) > float(1 - (N+add_npoints)/npixels)
            mask_points_xy = mask * random_xy
            add_npoints += add_incr
            if np.sum(mask_points_xy > 0) >= N:
                d = np.array(np.where(mask_points_xy > 0))
                d = d.reshape(d.shape[1],d.shape[0])
                min_distance = np.sort(np.unique(distance_matrix(d,d).ravel()))[1]
                print('Trial ' + str(i) + ': ' + str(np.sum(mask_points_xy > 0)) + ' points, min_distance = ' + str(min_distance))
                if min_distance > mask_min_distance:
                    mask_points[:,:,i] = mask_points_xy
                    mask_distances[i] = min_distance
                    print('Trial ' + str(i) + ': ' + str(np.sum(mask_points_xy > 0)) + ' points, min_distance = ' + str(min_distance))
                    break
                else:
                    add_npoints -= add_incr
            else: 
                print('Trial ' + str(i) + ': ' + str(np.sum(mask_points_xy > 0)) + ' points')
       
    imask = np.where(mask_distances==np.min(mask_distances)) 
    plt.imshow(mask_points[:,:,imask], cmap=cm.gray)
    plt.show()
        

