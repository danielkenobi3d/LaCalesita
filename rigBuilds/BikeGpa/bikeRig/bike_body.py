from RMPY.rig import rigWorld
from RMPY.rig import rigSingleJoint
from RMPY.rig import rigWheel
import pymel.core as pm
import importlib
importlib.reload(rigWheel)
def build():
    # creating main joints of bike and wheels
    rig_world = rigWorld.RigWorld()
    cog = rigSingleJoint.RigSingleJoint()
    cog.create_point_base('C_COG_reference_pnt', centered=True)

    handle_bar_rig = rigSingleJoint.RigSingleJoint()
    handle_bar_rig.create_point_base('C_handleBar_reference_pnt')
    r_handle_bar_rig = rigSingleJoint.RigSingleJoint()
    r_handle_bar_rig.create_point_base('R_handleBar_reference_pnt')
    l_handle_bar_rig = rigSingleJoint.RigSingleJoint()
    l_handle_bar_rig.create_point_base('L_handleBar_reference_pnt')

    seat_rig = rigSingleJoint.RigSingleJoint()
    seat_rig.create_point_base('C_seat_reference_pnt')
    front_wheel_rig = rigSingleJoint.RigSingleJoint()
    front_wheel_rig.create_point_base('C_frontWheel_reference_pnt')

    front_wheel_rotation_rig = rigWheel.RigWheel(rig_system=front_wheel_rig.rig_system)
    front_wheel_rotation_rig.create_point_base('C_frontWheel_reference_pnt')
    front_wheel_rotation_rig.set_parent(front_wheel_rig)
    front_wheel_rotation_rig.rig_system.settings.radius.set(38)

    back_wheel_rig = rigSingleJoint.RigSingleJoint()
    back_wheel_rig.create_point_base('C_backWheel_reference_pnt')

    back_wheel_rotation_rig = rigWheel.RigWheel(rig_system=back_wheel_rig.rig_system)
    back_wheel_rotation_rig.create_point_base('C_backWheel_reference_pnt')
    back_wheel_rotation_rig.set_parent(back_wheel_rig)
    back_wheel_rotation_rig.rig_system.settings.radius.set(38)

    handle_bar_rig.set_parent(cog)
    r_handle_bar_rig.set_parent(handle_bar_rig)
    l_handle_bar_rig.set_parent(handle_bar_rig)
    seat_rig.set_parent(cog)
    cog.set_parent(rig_world)
    front_wheel_rig.set_parent(handle_bar_rig)
    back_wheel_rig.set_parent(cog)

    # creating the pedals
    # you will need a main control for both pedals that will rotate on the center.
    pedals_wheel_rig = rigSingleJoint.RigSingleJoint()
    pedals_wheel_rig.create_point_base('C_mainStar_reference_pnt', type='circular')
    pedals_wheel_rig.set_parent(cog)

    # then we create both pedals
    l_pedal_rig = rigSingleJoint.RigSingleJoint()
    l_pedal_rig.create_point_base('L_pedal00_reference_pnt', centered=True)
    l_pedal_rig.set_parent(pedals_wheel_rig)
    r_pedal_rig = rigSingleJoint.RigSingleJoint()
    r_pedal_rig.create_point_base('R_pedal00_reference_pnt', centered=True)
    r_pedal_rig.set_parent(pedals_wheel_rig)

    # The thing with the pedals is that in position they should follow the pedal wheel,
    # but in orientation they should follow the cog
    # we create an offset group on the left pedal.
    l_offset_group = l_pedal_rig.create.group.point_base(l_pedal_rig.controls[0], name='offset')

    # we orient Constraint this offset group with the cog
    pm.orientConstraint(cog.tip, l_offset_group, mo=True)

    # and we do the same for the right pedal
    # we create an offset group for the pedal.
    r_offset_group = r_pedal_rig.create.group.point_base(r_pedal_rig.controls[0], name='offset')
    # we orient Constraint this offset group with the cog
    pm.orientConstraint(cog.tip, r_offset_group, mo=True)


if __name__ == '__main__':
    build()





