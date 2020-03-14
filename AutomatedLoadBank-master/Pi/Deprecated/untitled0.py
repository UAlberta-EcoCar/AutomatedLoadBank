import tkinter as tk
from PIL import ImageTk, Image
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

fig=plt.figure(1)
plt.clf()
x=[1,2,3]
y=[4,5,6]
plt.plot(x,y)
fig.patch.set_facecolor('green')
plt.savefig("Test Graph.jpeg",dpi=300)
