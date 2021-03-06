""" Make the diagram """

import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import matplotlib.pyplot as plt
plt.rc("font", family="serif")
plt.rc("text", usetex=True)
from astropy.cosmology import Planck15
from astropy.table import Table
from classes import *
import sys
sys.path.append("/Users/annaho/Dropbox/Projects/Research/Koala/code")
from classes import *

fig, ax = plt.subplots(1,1, figsize=(8,6))

catsize = 12
srcsize = 10

ax.text(1.1, -23, "ZTF Phase I", fontsize=20)

snia(ax)
ax.text(16, -20.8, "2035 Ia SNe", color='Goldenrod',
        fontsize=catsize, horizontalalignment='center', rotation=20)
#, bbox=dict(facecolor='white', edgecolor='grey'))

kilonova(ax)
novae(ax)
longsne(ax)

fast_sublum(ax)
lbv(ax)
ax.text(110, -15, "5 LBVs", color='mediumseagreen',
        fontsize=catsize, horizontalalignment='center')

tde(ax)
ax.text(
        100, -22.5, "22 TDEs",
        fontsize=catsize, color='black')

core_collapse(ax)
ax.text(
        40, -16, "1078 CC SNe",
        fontsize=catsize, color='cornflowerblue')#,
        #bbox=dict(edgecolor='orange', facecolor='white'))

slsne(ax)
ax.text(50,-22, '58 SLSNe', fontsize=catsize, color='#7570b3',
        horizontalalignment='right')#, bbox=dict(facecolor='white',
            #edgecolor='purple'))

fbots(ax)
ax.text(4,-19.5,"5 FBOTs",fontsize=catsize,color='Crimson')

ilrt(ax)
ax.text(90, -12, "3 Intermediate\nLuminosity\nRed Transients",
        horizontalalignment='left', fontsize=catsize,color='blue')

#ax.plot([10, 100],[-10.5, -10.5],c='grey', lw=0.5, ls=':')

lrne(ax)
ax.text(26, -12.5, "2 Luminous\nRed Novae",
        horizontalalignment='right', fontsize=catsize, color='#d95f02')

gap(ax)
ax.text(29, -15.1, "8 Ca-rich Transients",
        horizontalalignment='center', fontsize=catsize,color='black')
#ax.text(4, -17, ".Ia Explosions",
#        horizontalalignment='right', fontsize=catsize,color='black')

#ax.text(400, -7.5, "Classical Novae",
#        horizontalalignment='right', verticalalignment='top', 
#        fontsize=catsize, color='black')

# for st in search_terms:
#     dat = np.loadtxt("%s.txt" %st, dtype=str)
#     if np.logical_and(dat.ndim == 1, len(dat) > 0):
#         z = dat[1].astype(float)
#         m = dat[2].astype(float)
#         M = m - Planck15.distmod(z=z).value
#         dur = dat[3].astype(float) + dat[4].astype(float)
#         ax.scatter(dur, M, label=st)
#     if dat.ndim > 1:
#         z = dat[:,1].astype(float)
#         m = dat[:,2].astype(float)
#         M = m - Planck15.distmod(z=z).value
#         dur = dat[:,3].astype(float) + dat[:,4].astype(float)
#         ax.scatter(dur, M, label=st)
    
ax.set_xlabel("Time Above Half-Max (rest-frame days)", fontsize=16)
ax.set_xlim(1,500)
ax.set_xscale('log')
ax.set_ylim(-4.7, -24)
ax.set_ylabel("Peak Luminosity ($M_V$)", fontsize=16)

# Axis showing luminosity in erg/s
ax2 = ax.twinx()
# Conversion from M_bol to L_bol, in erg/s
y_f = lambda y_i: 1E7 * 10**((y_i-71.2)/(-2.5))
ymin, ymax = ax.get_ylim()
ax2.set_ylim((y_f(ymin), y_f(ymax)))
ax2.plot([],[])
ax2.set_ylabel("Peak Luminosity (erg/s)", 
        fontsize=16, rotation=270, verticalalignment='bottom')
ax2.tick_params(axis='both', labelsize=14)
ax2.set_yscale('log')
ax.tick_params(axis='both', labelsize=14)

# Make an inset for fast transients
# axins = inset_axes(
#         ax, 2, 2, loc=1,
#         bbox_to_anchor=(0.4,0.8),
#         bbox_transform=ax.transAxes)
# axins.set_xlim(1,5)
# axins.set_ylim(-18,-22)
# #mark_inset(ax, axins, loc1=1, loc2=4, fc="none", ec="0.5")
# axins.tick_params(axis='both', labelsize=12)
# plot_ibn(axins)
# fbot(axins)
# kepler(axins)
# ptf09uj(axins)
# cow(axins)
# asu(axins)
# koala(axins)
# gep(axins)

# Display
#ax.legend(loc='lower left', fontsize=10, frameon=False)
plt.tight_layout()
#plt.show()
plt.savefig("tau_mv.eps", dpi=500)
