from basic import max_min, dp, l_, da
from IPython.display import Latex, display_latex

def f_max_solver(velocidad: float, precision: int =3, verbose: bool = True):
    result = max_min.f_max(V=velocidad)
    if verbose == 2:
        display_latex(Latex(f"$ f_{{max}} = 0.2 - \\frac{{ V_d }}{{ 1250 }} $"))
    string = f"$ f_{{max}} = 0.2 - \\frac{{ {velocidad} }}{{ 1250 }} \\\\ f_{{max}} = {round(result, precision)} $"
    if verbose:
        display_latex(Latex(string))
    return result

def r_min_solver(velocidad: float, e_max: float, f_max: float, precision: int = 3, verbose: bool = True):
    result = max_min.R_min(V=velocidad, e_max = e_max, f_max = f_max)
    if verbose == 2:
        display_latex(Latex(f"$ R_{{min}} = \\frac{{ V_d^2 }}{{ 127 ( e_{{max}} + f_{{max}} ) }} $"))
    string = f"$ R_{{min}} = \\frac{{ {velocidad}^2 }}{{ 127 ( {e_max} + {round(f_max, precision)} ) }} \\\\ R_{{min}} = {round(result, precision)} $"
    if verbose:
        display_latex(Latex(string))
    return result

def distancia_parado_solver(velocidad: float, f_max: float, i: float, tiempo_de_percepcion: float = 2.5, precision: int = 3, verbose: bool = True):
    result = dp.Dp_(V=velocidad, f_max=f_max, i=i, t_p=tiempo_de_percepcion)
    if verbose == 2:
        display_latex(Latex(f"$ D_p = \\frac{{ V_d \cdot t_p }}{{ 3.6 }} + \\frac{{ V_d^2 }}{{ 254 (f_{{max}} \pm i) }} $"))
    string = f"$ D_p = \\frac{{ {velocidad} \cdot {tiempo_de_percepcion} }}{{ 3.6 }} + \\frac{{ {velocidad}^2 }}{{ 254 ( {round(f_max, precision)} \pm {i}) }} \\\\ D_p = {round(result, precision)} $"
    if verbose:
        display_latex(Latex(string))
    # Dp_neg = dp.Dp_(V=velocidad, f_max=f_max, i=-i, t_p=tiempo_de_percepcion)
    return result

def lll_solver(velocidad: float, shape: str = "s", check_for = None, precision: int = 3, verbose: bool = True):
    l_min = l_.l_min(V=velocidad, shape=shape)
    l_max = l_.l_max(V=velocidad)
    if verbose:
        match shape:
            case "s": string = "$ l_{{min}} = 1.39 V = {round(l_min, precision)} $"
            case "o": string = "$ l_{{min}} = 2.78 V = {round(l_min, precision)} $"
        display_latex(Latex(string))
        display_latex(Latex(f"$ l_{{max}} = 16.70 V = {round(l_max, precision)} $"))
    if check_for:
        check_for = float(check_for)
        display_latex(Latex(f"$ {round(l_min, precision)} < {round(check_for, precision)} < {round(l_max, precision)} $"))
        if l_min < check_for and check_for < l_max:
            display_latex(Latex(f"$ \\textbf{{ \\text{{Si cumple!}} }}$"))
            return l_min, l_max, True
        else:
            display_latex(Latex(f"$ \\textbf{{ \\text{{No cumple!}} }}$"))
            return l_min, l_max, False
    return l_min, l_max

def d1_solver(velocidad: float, t_1: float, a: float, m: float = 15., precision: int = 3, verbose: bool = True):
    result = da.d1(V=velocidad, t_1=t_1, m=m, a=a)
    if verbose == 2:
        display_latex(f"$ D_1 = 0.278 \\times t_1 \\left(V - m + \\frac{{ a \cdot t_1 }}{{ 2 }} \\right) $")
    if verbose:
        string = f"$ D_1 = 0.278 \\times {t_1} \\left({velocidad} - {m} + \\frac{{ {a} \\cdot {t_1} }}{{ 2 }} \\right) \\\\ D_1 = {round(result, precision) }$"
        display_latex(Latex(string))
    return result

def d2_solver(velocidad: float, t_2: float, precision: int = 3, verbose: bool = True):
    result = da.d2(velocidad, t_2)
    if verbose == 2:
        display_latex(Latex(f"$ D_2 = 0.278 \\cdot V \\cdot t_2 $"))
    if verbose:
        string = f"$ D_2 = 0.278 \\times {velocidad} \\times {t_2} \\\\ D_2 = {round(result, precision)} $"
        display_latex(Latex(string))
    return result

def d3_solver(selection: bool|str|float = False, random_state: int = 42, precision: int = 3, verbose: bool = True):
    result = da.d3(selection=selection, random_state=random_state)
    if verbose:
        display_latex(Latex(f"$ D_3 \\ \\text{{entre 30 y 90 m}}  $"))
        display_latex(Latex(f"$ D_3 = {result} $"))
    return result

def d4_solver(velocidad: float, t_2: float, precision: int = 3, verbose: bool = True):
    result = da.d4(V=velocidad, t_2=t_2)
    if verbose:
        display_latex(Latex(f"$ D_4 = \\frac{{2}}{{3}} D_2 $"))
        display_latex(Latex(f"$ D_4 = {round(result, precision)} $"))
    return result

def da_solver(velocidad: float, t_1: float, t_2: float, m: float, a: float, selection_3: bool|float|str = "max", random_state: int = 42, precision: int = 3, verbose: bool = True):
    result = d1_solver(velocidad=velocidad, t_1=t_1, a=a, m=m, precision=precision, verbose=verbose) + \
            d2_solver(velocidad=velocidad, t_2=t_2, precision=precision, verbose=verbose) + \
            d3_solver(selection=selection_3, random_state=random_state, precision=precision, verbose=verbose) + \
            d4_solver(velocidad=velocidad, t_2=t_2, precision=precision, verbose=verbose)
    
    if verbose:
        display_latex(Latex(f"$ D_a = D_1 + D_2 + D_3 + D_4 $"))
        display_latex(Latex(f"$ D_a = {round(result,precision)} $"))
    return result
            
def check_dp_da(dp: float, da: float, verbose: bool = True):
    result = dp > da
    if verbose:
        display_latex(Latex(f"$ D_p > D_a ??? $"))
        display_latex(Latex(f"$ \\text{{ {result} }} $"))
    return result