from RMPY.rig import rigLaceRing
from RMPY.rig import rigBase
from RMPY.rig import rigSplineIK
from RMPY.rig import rigFK
from RMPY.rig import rigSinFunction
import importlib
importlib.reload(rigSplineIK)
importlib.reload(rigLaceRing)
import pymel.core as pm


class RigSpineModel(rigBase.BaseModel):
    def __init__(self):
        self.rig_lace_base = None
        self.rig_spline_ik = None
        self.rig_sin = None
        self.rig_fk = None
        self.offset_groups_list = None

class RigSpine(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_point_base(self, *points, **kwargs):
        number_of_joints = kwargs.pop('number_of_joints', 40)
        self._model.rig_lace_base = rigLaceRing.LaceRing(self.rig_system)
        self.rig_lace_base.create_point_base(*points, centered=True,
                                             create_path_surface=True,
                                             joint_number=0, nurbs_to_poly_output=True)

        self._model.rig_spline_ik = rigSplineIK.RigSplineIK(rig_system=self.rig_system)
        self.rig_spline_ik.create_curve_base(self.rig_lace_base.lace_rig.curve, equidistant_points=True,
                                             number_of_joints=number_of_joints, create_up_vectors=True, stretchy_ik=False)


if __name__ == '__main__':
    selection = pm.ls(selection=True)
    rig = RigSpine()
    rig.create_point_base(*selection)





