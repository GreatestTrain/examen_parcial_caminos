import numpy as np
from .st import st_vec
import copy

def diag_(array):
    """Una función que calcula la diagonal de un punto a otro.

    Args:
        array (np.ndarray): Una matriz que contiene 2 filas con un radio y un ángulo (en radianes) cada uno.

    Returns:
        diag: La diagonal acumulada generada y el ángulo acumulado.
    """    
    assert array.shape == (2,2), "Array shape must be 2 x 2."
    sum_ = np.sum(array, axis=0)
    angle = (np.pi) - sum_[1]
    side = sum_[0]
    return np.array(( (side * np.sin(array[0,1]) / np.sin(angle), sum_[1])))

def diag_vec(array, st_= False):
    """Una función que calcula las diagonales generadas acumuladas de una lista de subtangentes y ángulos.

    Args:
        array (np.ndarray): Lista de radios y angulos
        st_ (bool, optional): Determina si se debe calcular las subtangentes previamente. Defaults to False.

    Returns:
        _type_: _description_
    """    
    if array.shape[0] == 1:
        return np.stack((st_vec(array), array[0,1].reshape(1)), axis=1)
    llist = []
    array_ = copy.deepcopy(array)
    if st_:
        array_[:,0] = st_vec(array)
    for i in range(array_.shape[0] - 1):
        op = array_[i:i+2,:]
        diag__ = diag_(op)
        array_[i+1,0] += diag__[0]
        array_[i+1,1] = diag__[1]
        llist.append(diag__)
    return np.array(llist)