#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from matplotlib.projections.geo import HammerAxes
import matplotlib.projections as mprojections
from matplotlib.axes import Axes
from matplotlib.patches import Wedge
import matplotlib.spines as mspines

class LowerHammerAxes(HammerAxes):
    name = 'lower_hammer'
    def cla(self):
        HammerAxes.cla(self)
        Axes.set_xlim(self, -np.pi, np.pi)
        Axes.set_ylim(self, -np.pi / 2.0, 0)

    def _gen_axes_patch(self):
        return Wedge((0.5, 0.5), 0.5, 180, 360)

    def _gen_axes_spines(self):
        path = Wedge((0, 0), 1.0, 180, 360).get_path()
        spine = mspines.Spine(self, 'circle', path)
        spine.set_patch_circle((0.5, 0.5), 0.5)
        return {'wedge':spine}

mprojections.register_projection(LowerHammerAxes) # 投影クラス登録

#################
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='lower_hammer') # 登録した投影クラスを使用
ax.grid(True)
plt.show()


# In[ ]:




