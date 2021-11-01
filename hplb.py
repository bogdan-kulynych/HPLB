import rpy2

from rpy2.robjects import r as R
from rpy2.robjects import packages as rpackages
from rpy2.robjects import numpy2ri


try:
    devtools = rpackages.importr("devtools")
except:
    utils = rpackages.importr("utils")
    utils.install_packages("devtools")

devtools.install_local(".")
hplb = rpackages.importr("HPLB")


def compute_hplb(test_decisions, test_outputs, estimator_type="adapt", alpha=0.01):
    numpy2ri.activate()
    result = hplb.HPLB(
            test_decisions, test_outputs, estimator_type=estimator_type, alpha=alpha)
    numpy2ri.deactivate()
    result = dict(zip(result.names, map(list, list(result))))
    return result["tvhat"][0]


# import numpy as np
# test_decisions = np.array([0, 1, 1, 1, 0, 1] * 100)
# test_outputs = np.array(  [0, 1, 0, 1, 1, 1] * 100)
# print("RESULT:", compute_hplb(test_decisions, test_outputs))
