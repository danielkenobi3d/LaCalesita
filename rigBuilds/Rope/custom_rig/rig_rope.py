from RMPY.rig import rigLaceRing
from RMPY.rig import rigBase
from RMPY.rig import rigSplineIK
from RMPY.rig import rigFK
from RMPY.rig import rigSinFunction
import importlib
importlib.reload(rigSplineIK)
importlib.reload(rigLaceRing)
import pymel.core as pm
from RMPY.core import data_save_load
from bgb_short.pipeline import environment
from pathlib import Path

class RigSpineModel(rigBase.BaseModel):
    def __init__(self):
        self.rig_lace_base = None
        self.rig_spline_ik = None
        self.rig_sin = None
        self.rig_fk = None
        self.offset_groups_list = None

class RigRope(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ik_points_root = pm.ls('C_IKRope00_reference_grp')[0]
        self.fk_points_root = pm.ls('C_rope00_reference_grp')[0]
    def build(self):
        number_of_joints = 100

        self._model.rig_lace_base = rigLaceRing.LaceRing(self.rig_system)
        self.rig_lace_base.create_point_base(*self.ik_points_root.getChildren(), centered=True,
                                             create_path_surface=True,
                                             joint_number=0, nurbs_to_poly_output=True, curve_distance=5, size=4)

        self._model.rig_spline_ik = rigSplineIK.RigSplineIK(rig_system=self.rig_system)
        self.rig_spline_ik.create_curve_base(self.rig_lace_base.lace_rig.curve, equidistant_points=True,
                                             number_of_joints=number_of_joints, create_up_vectors=True, stretchy_ik=False)
        self._model.rig_fk = rigFK.RigFK()
        self.rig_fk.create_point_base(*self.fk_points_root.getChildren())
        pm.skinCluster(self.rig_fk.joints, self.rig_lace_base.geometry_output)
        load_skinning_data(self.rig_lace_base.geometry_output)

def load_skinning_data(list_of_objects):
    env = environment.Environment()
    for each in list_of_objects:
        if Path(f'{env.data}/skinClusters/{each}.json').exists():
            data_save_load.load_skin_cluster(each)

if __name__ == '__main__':
    rig = RigRope()
    rig.build()





