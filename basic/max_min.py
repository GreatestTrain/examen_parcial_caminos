def f_max(V: float) -> float:
    """Coeficiente de fricción máximo.

    Args:
        V (float): Velocidad de diseño. (km/h)

    Returns:
        float: Fricción máxima. (???)
    """    
    return 0.2 - (V/1250)

def R_min(V: float, e_max: float, f_max: float) -> float:
    """Radio minimo de curvatura.

    Args:
        V (float): Velocidad de diseño. (km/h)
        e_max (float): Valor de peralte máximo (en decimales).
        f_max (float): Valor máximo de fricción.

    Returns:
        float: Radio mínimo de curvatura. (m)
    """
    return V**2 / (127 * ( e_max + f_max ))

