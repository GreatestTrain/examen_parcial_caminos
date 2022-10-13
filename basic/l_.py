"""
Páginas 107 - 109
"""

def l_min_s(V: float) -> float:
    return 1.39 * V

def l_min_o(V: float) -> float:
    return 2.78 * V

def l_max(V: float) -> float:
    return 16.70 * V

def l_min(V: float, shape: str) -> float:
    if isinstance(shape, str):
        match shape:
            case 's': return l_min_s(V)
            case 'o': return l_min_o(V)
            case _: raise Exception('shape ({}) argument must be in ("s", "o")'.format(shape))
    else:
        raise Exception('shape argument must be of type str')