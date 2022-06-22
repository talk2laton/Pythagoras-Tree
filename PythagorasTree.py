# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 18:17:14 2022

@author: Lateef Kareem
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(autoscale_on=False, xlim=(-4, 4), ylim=(0, 4.5))
ax.set_aspect('equal'); ax.grid(); 
f1 = 0.6*0.6; f2 = 0.6*0.8;
Tree, S, E = [], [], [0];

def animate(n):
    if (n == 0):
        mom, = ax.fill([1,1,0,0], [0,1,1,0], color = 'g', edgecolor = 'k');
        Tree.append(mom); 
    else:
        for j in range(S[-1], E[-1], 1):
            mom = Tree[j];
            xy = mom.get_xy();
            x, y = xy[:,0], xy[:,1];
            dx, dy = x[2]-x[1], y[2]-y[1];
            px, py = x[1] + f1*dx + f2*dy, y[1] + f1*dy - f2*dx;
            Tree.append(Square([x[1], y[1]], [px, py]));
            Tree.append(Square([px, py], [x[2], y[2]]));
    S.append(E[-1]); E.append(len(Tree));
    return Tree;

def Square(p1, p2):
    v1 = [p2[0]-p1[0],p2[1]-p1[1]]; v2 = [v1[1], -v1[0]];
    x = [p1[0], p1[0]+v2[0], p1[0]+v1[0]+v2[0], p2[0]];
    y = [p1[1], p1[1]+v2[1], p1[1]+v1[1]+v2[1], p2[1]];
    hndl, = ax.fill(x, y, color = 'g', edgecolor = 'k');
    return hndl;

ani = animation.FuncAnimation(fig, animate,  frames = 13, blit = True);
ani.save('PythagorasTree.mp4', fps = 2)
plt.show()