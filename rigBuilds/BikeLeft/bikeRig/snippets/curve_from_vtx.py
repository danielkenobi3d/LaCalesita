from RMPY.core import rig_core as rm
import pymel.core as pm
selection = pm.ls(selection=True)
rm.curve.point_base(*selection, periodic=True, ep=True)
