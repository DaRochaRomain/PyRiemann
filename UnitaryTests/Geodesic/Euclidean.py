import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.Geodesic import Geodesic
from Utils.CovMat import CovMat

from oldPyRiemann.geodesic import geodesic_euclid

m1 = CovMat.random(100)
m2 = CovMat.random(100)


def test_geodesic_euclidean():
    old_dist = geodesic_euclid(m1, m2, 0.5)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Geodesic.euclidean(m1, m2, 0.5)

    return _get_state(old_dist, new_dist, "geodesic riemannian")


def _get_state(old, new, func_name):
    if abs(old.numpy_array.sum() - new.numpy_array.sum()) < 1e-10:
        print("%s : PASS" % func_name)
        return True
    else:
        print("%s : FAIL" % func_name)
        return False
