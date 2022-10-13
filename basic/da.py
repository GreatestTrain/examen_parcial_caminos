from numpy.random import randn

def d1(V: float, t_1: float, a: float, m: float = 15.) -> float:
    return 0.278 * t_1 * ( V - m + a * t_1 / 2)

def d2(V: float, t_2: float) -> float:
    return 0.278 * V * t_2

def d3(selection: float|bool|str = False, random_state: int = 42) -> float:
    match selection:
        case 'min': return 30
        case 'max': return 90
        case False: return 90
        case _: return selection

def d4(V: float, t_2: float) -> float:
    return 2/3 * d2(V=V, t_2=t_2)

def Da(V: float, t_1: float, t_2: float, m: float, a: float, selection_3: float|bool|str, random_state: int = 42) -> float:
    return d1(V, t_1, m, a) + d2(t_2) + d3(selection_3, random_state) + d4(t_2)