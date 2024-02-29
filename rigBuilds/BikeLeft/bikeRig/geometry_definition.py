constraints = {
    "parent": {},
    'point': {},
    'scale': {},
    'parentScale': {
                  'C_object00_seat_jnt': ['structure_03', 'saddle_base_l', 'saddle_base_r', 'saddle'],
                  'L_object00_pedal_jnt': ['peddle_l']
                   },

    }

import pymel.core as pm
def create_constraints(constraints):
    constraint_functions = {'parent': [pm.parentConstraint],
                            'point': [pm.pointConstraint],
                            'scale': [pm.scaleConstraint],
                            'parentScale':[pm.parentConstraint, pm.scaleConstraint]}
    for each in constraints.keys():
        if each == 'parent':
            for each_parent in constraints[each]:
                for each_child in constraints[each][each_parent]:
                    pm.parentConstraint(each_parent,each_child, mo=True)

