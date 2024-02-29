from LaCalesita.rigBuilds.BikeLeft.bikeRig import bike_left_body
from bgb_short.pipeline import environment
from RMPY.core import data_save_load
from RMPY.core import search_hierarchy
import pymel.core as pm
import importlib
from pathlib import Path
importlib.reload(bike_left_body)
def custom_rig():
    bike_left_body.build()
    pm.parent('ChildA_Bike_LP', 'rig')


def load_skinning_data():
    env = environment.Environment()
    root_node = pm.ls('ChildA_Bike_LP')[0]
    print(root_node)
    list_of_objects = search_hierarchy.shape_type_in_hierarchy(root_node)
    for each in list_of_objects:
        if Path(f'{env.data}/skinClusters/{each}.json').exists():
            data_save_load.load_skin_cluster(each)
