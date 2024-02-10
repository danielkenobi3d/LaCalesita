from RMPY.rig import rigWorld
from RMPY.rig import rigSingleJoint
def build():
    rig_world = rigWorld.RigWorld()
    cog = rigSingleJoint.RigSingleJoint()
    cog.create_point_base('C_COG_reference_pnt')
    handle_bar_rig = rigSingleJoint.RigSingleJoint()
    handle_bar_rig.create_point_base('C_handleBar_reference_pnt')
    seat_rig = rigSingleJoint.RigSingleJoint()
    seat_rig.create_point_base('C_seat_reference_pnt')
    handle_bar_rig.set_parent(cog)
    seat_rig.set_parent(cog)
    cog.set_parent(rig_world)

