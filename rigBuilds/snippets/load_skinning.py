from RMPY.core import data_save_load
from bgb_short.pipeline import environment
import pymel.core as pm
from pathlib import Path


def load_skinning_data():
    env = environment.Environment()
    list_of_objects = pm.ls(selection=True)
    for each in list_of_objects:
        if Path(f'{env.data}/skinClusters/{each}.json').exists():
            data_save_load.load_skin_cluster(each)
if __name__=='__main__':
    load_skinning_data()
