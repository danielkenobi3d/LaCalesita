import pymel.core as pm
from RMPY.core import rig_core
chain = pm.ls('chain_a_020', 'chain_a_025', 'chain_a_026', 'chain_a_027', 'chain_a_021', 'chain_a_022', 'chain_a_023', 'chain_a_024', 'chain_a_028', 'chain_a_029', 'chain_a_030', 'chain_a_031', 'chain_a_032', 'chain_a_033', 'chain_a_034', 'chain_a_035', 'chain_a_010', 'chain_a_009', 'chain_a_008', 'chain_a_007', 'chain_a_006', 'chain_a_036', 'chain_a_037', 'chain_a_038', 'chain_a_039', 'chain_a_040', 'chain_a_041', 'chain_a_042', 'chain_a_043', 'chain_a_044', 'chain_a_045', 'chain_a_046', 'chain_a_047', 'chain_a_005', 'chain_a_004', 'chain_a_003', 'chain_a_002', 'chain_a_011', 'chain_a_012', 'chain_a_013', 'chain_a_014', 'chain_a_015', 'chain_a_016', 'chain_a_017', 'chain_a_018', 'chain_a_019')
pm.select(chain)
vertex_points = [[613, 833],[373, 139]]
created_locators = []
for each_geo in chain:
    for each_vtx_list in vertex_points:
        short_vertex_list = [each_geo.vtx[each] for each in each_vtx_list]
        space_loc =rig_core.space_locator.point_base(short_vertex_list)
        created_locators.append(space_loc)
print(created_locators)

