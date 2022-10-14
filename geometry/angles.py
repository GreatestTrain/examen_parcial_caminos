import numpy as np

pi_2 = np.pi / 2

def gamma(D: float, radio: float):
    return D / (2 * radio)

def diff_points(initial_point, final_point):
    return np.diff(np.stack((initial_point, final_point), axis=1), axis=1)
def angle_between_2(initial_point, final_point):
    pendiente_ = diff_points(initial_point, final_point)
    return np.arctan(pendiente_[1] / pendiente_[0])
def az_between_2(initial_point, final_point):
    return pi_2 - angle_between_2(initial_point, final_point)
def euclid_diff(initial_point, final_point):
    array = diff_points(initial_point, final_point)
    return np.sqrt(np.sum(array**2))

def ll(radio: float, angle: float):
    return np.sin(angle) * radio * 2

def ll_np(array):
    return np.sin(array[1]) * array[0] * 2

def coor_p_to_p(p_init, length, azimut):
    return p_init + length*np.array([np.sin(azimut), np.cos(azimut)]).ravel()

def gamma(D, radio):
    return D / 2 * radio

# def lc()