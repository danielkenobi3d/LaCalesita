from RMPY.rig import rigWorld
from RMPY.rig import rigSingleJoint
import pymel.core as pm

def build() :
     #creating main joints of bus and wheels
    rig_world = rigWorld.RigWorld()
    cog = rigSingleJoint.RigSingleJoint()
    cog.create_point_base('C_COG_reference_pnt', centered=True)

if __name__ == '__main__':
    build()
