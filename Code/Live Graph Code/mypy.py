import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
import os


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    graph_data = open('/home/obin/Desktop/Project/sdd.txt','r').read()
    lines = graph_data.split('\n')
    
    
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            
            if(float(y)>10):
                
                m=1
                
            
            else:
                m=0
           
    ll=[5,20]
    
    plt.xlim(i-10,i+8)
    plt.xlabel('Date_Index')
    plt.ylabel('Usage (KW)')
    
    
    ax1.plot(int(x), float(y),linestyle='solid',marker='o', markerfacecolor='red',markersize=ll[m])
    if ll[m]==20:
        duration = .5  # second
        freq = 3276 # Hz
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        os.system('spd-say "outlier at %d"'%(i+8))
    
ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()
