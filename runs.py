import os
import numpy as np

alphas = np.linspace(0.1, 1.0, 5)
l1_ratios = np.linspace(0.1, 1.0, 5)


for alpha in alphas:
    for l1 in l1_ratios:
        os.system(f"python simple_ml_model2.py -a {alpha} -l1 {l1}")


