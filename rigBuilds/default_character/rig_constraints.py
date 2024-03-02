import pymel.core as pm
from bgb_short.pipeline import environment
import importlib

def matrix_constraint(parent, child):
    parent = pm.ls(parent)[0]
    child = pm.ls(child)[0]
    if child.getParent():
        mult_matrix = pm.createNode('multMatrix')
        parent.worldMatrix[0] >> mult_matrix.matrixIn[0]
        child.getParent().worldInverseMatrix[0]>> mult_matrix.matrixIn[1]
        mult_matrix.matrixSum >> child.offsetParentMatrix
    else:
        parent.worldMatrix[0] >> child.offsetParentMatrix


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

if __name__ == '__main__':
    selection = pm.ls(selection=True)
    matrix_constraint(*selection)