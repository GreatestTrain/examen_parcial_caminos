def D_p_hum(V: float, a: float = 3.4, t_p: float = 2.5) -> float:
    """Distancia de parada (para pavimentos húmedos).

    Args:
        V (float): Velocidad de diseño. (km/h)
        a (float): Deceleración en función del coeficiente de fricción de la pendiente. (m/s^2) (Defaults to 3.4)
        t_p (float): Tiempo de reacción. (s) (Defaults to 2.5)

    Returns:
        float: Distancia de parada. (m)
    """        
    return 0.278 * V * t_p + 0.039 * (V**2 / a)

def D_p_sup3(V: float, a: float = 3.4, i: float = 0.03, t_p: float = 2.5) -> float:
    """Distancia de parada (para vias con pendiente superior a 3%).

    Args:
        V (float): Velocidad de diseño. (km/h)
        a (float): Deceleración en función del coeficiente de fricción de la pendiente. (m/s^2) (Defaults to 3.4)
        i (float): Pendiente longitudinal. (Defaults to 0.03)
        t_p (float): Tiempo de reacción. (s) (Defaults to 2.5)

    Returns:
        float: Distancia de parada. (m)
    """        
    return 0.278 * V * t_p + ( V**2 / ( 254 * ((a/9.81) + i)) )

def Dp_(V: float, f_max: float, i: float = 0.03, t_p: float = 2.5) -> float:
    """Distancia de parada (general?).

    Args:
        V (float): Velocidad de diseño. (km/h)
        f_max (float): _description_
        i (float): Pendiente longitudinal. (Defaults to 0.03)
        t_p (float): Tiempo de reacción. (s) (Defaults to 2.5)

    Returns:
        float: _description_
    """    
    return (V * t_p) / 3.6 + V**2 / (254 * (f_max + i))