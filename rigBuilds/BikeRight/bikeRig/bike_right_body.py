from RMPY.rig import rigWorld
from RMPY.rig import rigSingleJoint
from RMPY.rig import rigWheel
import pymel.core as pm

def build():
    # creating main joints of bike and wheels
    rig_world = rigWorld.RigWorld()
    cog = rigSingleJoint.RigSingleJoint()
    cog.create_point_base('C_COG_reference_pnt', centered=True)
    handle_bar_rig = rigSingleJoint.RigSingleJoint()
    handle_bar_rig.create_point_base('C_handleBar_reference_pnt')

    r_miniwheel_rig = rigSingleJoint.RigSingleJoint()
    r_miniwheel_rig.create_point_base('R_miniWheel_reference_pnt')
    r_miniwheel_rotation_rig = rigWheel.RigWheel(rig_system=r_miniwheel_rig.rig_system)
    r_miniwheel_rotation_rig.create_point_base('R_miniWheel_reference_pnt')
    r_miniwheel_rotation_rig.set_parent(r_miniwheel_rig)
    r_miniwheel_rotation_rig.rig_system.settings.radius.set(22)

    l_miniwheel_rig = rigSingleJoint.RigSingleJoint()
    l_miniwheel_rig.create_point_base('L_miniWheel_reference_pnt')
    l_miniwheel_rotation_rig = rigWheel.RigWheel(rig_system=l_miniwheel_rig.rig_system)
    l_miniwheel_rotation_rig.create_point_base('L_miniWheel_reference_pnt')
    l_miniwheel_rotation_rig.set_parent(l_miniwheel_rig)
    l_miniwheel_rotation_rig.rig_system.settings.radius.set(22)

    handle_bar_rig.set_parent(cog)
    cog.set_parent(rig_world)
    r_miniwheel_rig.set_parent(cog)
    l_miniwheel_rig.set_parent(cog)

    # creating the pedals
    # you will need a main control for both pedals that will rotate on the center.
    pedals_wheel_rig = rigSingleJoint.RigSingleJoint()
    pedals_wheel_rig.create_point_base('C_mainStar_FrontWheel_reference_pnt', type='circular')
    pedals_wheel_rig.set_parent(handle_bar_rig)

    pedals_wheel_rotation_rig = rigSingleJoint.RigSingleJoint()
    pedals_wheel_rotation_rig = rigWheel.RigWheel(rig_system=pedals_wheel_rotation_rig.rig_system)
    pedals_wheel_rotation_rig.create_point_base('C_mainStar_FrontWheel_reference_pnt')
    pedals_wheel_rotation_rig.set_parent(pedals_wheel_rig)
    pedals_wheel_rotation_rig.rig_system.settings.radius.set(38)

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
    pm.orientConstraint(handle_bar_rig.tip, l_offset_group, mo=True)

    # and we do the same for the right pedal
    # we create an offset group for the pedal.
    r_offset_group = r_pedal_rig.create.group.point_base(r_pedal_rig.controls[0], name='offset')
    # we orient Constraint this offset group with the cog
    pm.orientConstraint(handle_bar_rig.tip, r_offset_group, mo=True)


if __name__ == '__main__':
    build()





