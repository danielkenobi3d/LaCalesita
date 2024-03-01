from RMPY.rig import rigWorld
from RMPY.rig import rigSingleJoint
import pymel.core as pm

def build() :
     #creating main joints of bus and wheels
    rig_world = rigWorld.RigWorld()
    cog = rigSingleJoint.RigSingleJoint()
    cog.create_point_base('C_COG_reference_pnt', centered=True)

    r_frontwheel_rig = rigSingleJoint.RigSingleJoint()
    r_frontwheel_rig.create_point_base('R_frontWheel_reference_pnt')
    l_frontwheel_rig = rigSingleJoint.RigSingleJoint()
    l_frontwheel_rig.create_point_base('L_frontWheel_reference_pnt')

    r_backwheel_rig = rigSingleJoint.RigSingleJoint()
    r_backwheel_rig.create_point_base('R_backWheel_reference_pnt')
    l_backwheel_rig = rigSingleJoint.RigSingleJoint()
    l_backwheel_rig.create_point_base('L_backWheel_reference_pnt')

    cog.set_parent(rig_world)
    r_frontwheel_rig.set_parent(cog)
    l_frontwheel_rig.set_parent(cog)
    r_backwheel_rig.set_parent(cog)
    l_backwheel_rig.set_parent(cog)

if __name__ == '__main__':
    build()
