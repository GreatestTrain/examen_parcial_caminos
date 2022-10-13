import numpy as np
import copy

def st(array):
    """Una función que calcula la subtangente con un array que contiene la longitud del radio y el ángulo (en radianes).

    Args:
        array (np.ndarray): Array de dos elementos que contiene un radio y un ángulo.

    Returns:
        subtangente: La subtangente generada.
    """    
    if isinstance(array, np.ndarray):
        assert array.shape == (2,), 'array shape must be (2,)'
    else:
        assert len(array) == 2
    result = array[0] * np.tan( array[1]/2 )
    return result
# st_vec = lambda matrix: np.apply_along_axis(st, 1, matrix)
def st_vec(matrix):
    """Una función vectorizada que calcula las subtangentes de una matriz de forma (n,2).

    Args:
        matrix (np.ndarray): Matriz con radios y ángulos en cada columna.

    Returns:
        np.ndarray: Lista de subtangentes.
    """    
    return np.apply_along_axis(st, 1, matrix)

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
        array (np.ndarray): Lista de angulos y 
        st_ (bool, optional): Determina si se debe calcular las subtangentes previamente. Defaults to False.

    Returns:
        _type_: _description_
    """    
    llist = []
    array_ = copy.deepcopy(array)
    if st_:
        array_[:,0] = np.stack((st_vec(array), array[0,1]), axis=0)
    for i in range(array_.shape[0] - 1):
        op = array_[i:i+2,:]
        diag__ = diag_(op)
        array_[i+1,0] += diag__[0]
        array_[i+1,1] = diag__[1]
        llist.append(diag__)
    return np.array(llist)

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

def p_total(data, pi=0):
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
    return np.insert(acc_ + pc_, 0, pc_, axis=0)

def gen_marks(array: np.ndarray, prec = 10):
    """Generador de cotas progresivas con una diferencia de <prec> en cada una.
    Args:
        array (np.ndarray): Array que contiene las cotas progresivas originales.
        prec (int, optional): Precisión de las cotas

    Returns:
        marks: np.ndarray con las cotas generadas.
    """    
    start = ((array[0] // prec) + 1) * prec
    end = ((array[-1] // prec) + 1) * prec
    arange = np.arange(start, end, prec)
    return np.unique(np.sort(np.concatenate([arange, array])), axis=0)
def diff_marks(array):
    "Generador de cotas progresivas diferenciales."
    return np.append( (0), np.ediff1d(array))

def expand__(matrix, prec=10, pi=0):
    matrix = copy.deepcopy(matrix)
    pc = p_total(matrix, pi)
    marks = gen_marks(pc, prec=prec)
    pc = pc[1:]
    # matrix = np.concatenate((matrix, ZERO_PAR))
    matrix = np.concatenate((matrix, pc.reshape(-1,1)), axis=1)
    llist = []
    iiter = iter(matrix)
    vector = next(iiter)
    for mark in marks[:-1]:
        if mark == vector[2]:
            vector = next(iiter)
            # continue
        llist.append( np.append(vector[:2], mark))
    to_return = np.append( np.array(llist), ((0,0,marks[-1]),), axis=0)
    diff__ = diff_marks(to_return[:,-1]).reshape(-1,1)
    # print(diff__.shape, to_return.shape) # debug
    return np.append( to_return, (diff__.reshape(-1,1)), axis = 1)

def gamma(array): # TO DO
    "Function that calculates gamma value. Angle must be in radians."
    assert array.shape[0] == 2
    if array[0] == 0:
        return np.float_(0)
    return array[1] / (2 * array[0])

def gamma_vec(matrix):
    return np.apply_along_axis(gamma, 1, matrix)