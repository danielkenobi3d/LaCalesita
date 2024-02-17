from RMPY.rig import rigLaces
from RMPY.rig import rigLaceRing
from RMPY.rig import rigSplineIK
import pymel.core as pm


rope_root = pm.ls('C_rope00_reference_grp')[0]
rope = rigLaces.RigLaces()
rope.create_point_base(*rope_root.getChildren())

joints_on_curve_rig = rigSplineIK.RigSplineIK()
joints_on_curve_rig.create_curve_base(rope.curve, number_of_joints=50)