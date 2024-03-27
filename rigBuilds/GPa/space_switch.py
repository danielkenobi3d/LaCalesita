import pymel.core as pm

L_bike_ctl, make_circle = pm.circle(name= 'L_bike_ctl')
pm.matchTransform(L_bike_ctl,'arm_L0_ikcns_ctl')

L_arm_constraint_2 = pm.parentConstraint(L_bike_ctl,'arm_L0_ik_cns')
L_arm_switch = pm.ls('armUI_L0_ctl')[0]
L_dictionnary = L_arm_switch.arm_ikref.getEnums()
print(L_dictionnary.keys())
list_of_keys = L_dictionnary.keys()
list_of_keys.append('Handlebar')
L_arm_switch.arm_ikref.setEnums(list_of_keys)

L_condition_bike=pm.createNode('condition')
L_condition_bike.secondTerm.set(6)
L_condition_bike.colorIfTrue.set([1,1,1])
L_condition_bike.colorIfFalse.set([0,0,0])

L_arm_constraint_1 = pm.ls('armUI_L0_ctl')[0]
L_arm_constraint_1.arm_ikref>>L_condition_bike.firstTerm
L_condition_bike.outColorR>>L_arm_constraint_2.getWeightAliasList()[-1]

R_bike_ctl, make_circle = pm.circle(name= 'R_bike_ctl')
pm.matchTransform(R_bike_ctl,'arm_R0_ikcns_ctl')

R_arm_constraint_2 = pm.parentConstraint(R_bike_ctl,'arm_R0_ik_cns')
R_arm_switch = pm.ls('armUI_R0_ctl')[0]
R_dictionnary = R_arm_switch.arm_ikref.getEnums()
print(R_dictionnary.keys())
list_of_keys = R_dictionnary.keys()
list_of_keys.append('Handlebar')
R_arm_switch.arm_ikref.setEnums(list_of_keys)

R_condition_bike=pm.createNode('condition')
R_condition_bike.secondTerm.set(6)
R_condition_bike.colorIfTrue.set([1,1,1])
R_condition_bike.colorIfFalse.set([0,0,0])

R_arm_constraint_1 = pm.ls('armUI_R0_ctl')[0]
R_arm_constraint_1.arm_ikref>>R_condition_bike.firstTerm
R_condition_bike.outColorR>>R_arm_constraint_2.getWeightAliasList()[-1]



