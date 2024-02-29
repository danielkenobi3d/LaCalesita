from bgb_short.pipeline import environment
from bgb_short.pipeline.mgear import io
import pymel.core as pm
import importlib
from RMPY.rig import rigFacial
from RMPY.rig import rigBlendShapeControls


def custom_rig():
    pm.parent('GrandPa_grp', 'rig')


def custom_finalize():
    pass
