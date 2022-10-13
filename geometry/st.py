import numpy as np
from .utils import vectorize

def st(radio: float, angulo: float) -> float:
    """Función que calcula la subtangente dado un radio y un angulo.

    Args:
        radio (float): radio en unidades deseadas.
        angulo (float): angulo en radianes.

    Returns:
        float: subtangente en las unidades del radio.
    """
    result = radio * np.tan( angulo )
    return result

def st_np(array: np.ndarray) -> np.ndarray:
    """Función que calcula las subtangentes dado unos radios y un angulos.
    Args:
        np.ndarray: [radio(float), angulo(float)]
    Returns:
        np.ndarray: subtangentes en las unidades del radio.
    """
    assert array.shape[0] == 2, "El array ingresado debe tener una longitud de 2"
    result = array[0] * np.tan( array[1] / 2 )
    return result

st_vec = vectorize(2)(st_np)