from .diag import diag_vec
from .st import st_vec
import numpy as np

def pc_calc(data, pi=0):
    """Una función que calcula la cota progresiva del punto de comienzo de una serie de radios y ángulos. (Sentido horario)

    Args:
        data (np.ndarray): 
        pi (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
    """    
    acc_inv = st_vec(data)[0]
    acc_inv += diag_vec(data[::-1], st_=True)[-1,0]
    acc_inv = pi - acc_inv
    return acc_inv

def p_total(data, pi=0, ci=None):
    """Una función que calcula las cotas progresivas dada una serie de radios y ángulos. (Sentido horario)

    Args:
        data (np.ndarray): Array de datos que contiene un radio y un ángulo (en radianes) en cada una de sus filas.
        pi (int, optional): Cota acumulada del punto intermedio

    Returns:
        np.ndarray: Cotas acumuladas.
    """    
    pc_ = pc_calc(data, pi)
    prod_ = np.prod(data, axis=1)
    acc_ = np.add.accumulate(prod_)
    result = np.insert(acc_ + pc_, 0, pc_, axis=0)
    if ci != None and not pi:
        result += np.abs(np.min(result)) + ci
    return result
