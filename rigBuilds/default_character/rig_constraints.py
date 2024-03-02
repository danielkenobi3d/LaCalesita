import pymel.core as pm
from bgb_short.pipeline import environment
import importlib

def matrix_constraint(parent, child):
    pass

def create_constraints():
    env = environment.Environment()
    geo_definition =env.get_variables_from_path('geo_definition')
    importlib.reload(geo_definition)
    constraint_functions = {'parent': [pm.parentConstraint],
                            'point': [pm.pointConstraint],
                            'scale': [pm.scaleConstraint],
                            'parentScale': [pm.parentConstraint, pm.scaleConstraint],
                            'skin': [pm.skinCluster],
                            'matrix': [matrix_constraint]}
    from pprint import pprint as pp
    if 'constraints' in dir(geo_definition):
        pp(geo_definition.constraints)
        for each in geo_definition.constraints.keys():
            for each_parent in geo_definition.constraints[each]:
                for each_child in geo_definition.constraints[each][each_parent]:
                    for each_function in constraint_functions[each]:
                        each_function(each_parent, each_child, mo=True)
