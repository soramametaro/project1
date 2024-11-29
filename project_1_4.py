import numpy as np


def guess_category(dv, v):
    cos_sim_dic = {}
    for d in dv.keys():
        dv_array = np.array(dv[d], dtype=np.float64)
        v_array = np.array(v, dtype=np.float64)
        cos_sim_dic[d] = cos_sim(dv_array, v_array)
    return (max(cos_sim_dic, key=cos_sim_dic.get))
