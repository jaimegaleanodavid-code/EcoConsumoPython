def validar_nombre(nombre: str) -> tuple[bool, str]:

    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        return False, "El nombre del aparato no puede estar vacío."
    return True, nombre_limpio


def validar_potencia(potencia_str: str) -> tuple[bool, float | str]:
    
    try:
        potencia = float(potencia_str)
        if potencia <= 0:
            return False, "La potencia debe ser un número mayor que 0."
        return True, potencia
    except ValueError:
        return False, "Debes ingresar un valor numérico válido para la potencia."


def validar_horas(horas_str: str) -> tuple[bool, float | str]:
    
    try:
        horas = float(horas_str)
        if not (0 < horas <= 24):
            return False, "Las horas de uso diario deben estar entre 1 y 24."
        return True, horas
    except ValueError:
        return False, "Debes ingresar un valor numérico válido para las horas."


def validar_dias(dias_str: str) -> tuple[bool, int | str]:
    
    try:
        dias = int(dias_str)
        if not (1 <= dias <= 31):
            return False, "Los días de uso deben estar entre 1 y 31."
        return True, dias
    except ValueError:
        return False, "Debes ingresar un número entero válido para los días."