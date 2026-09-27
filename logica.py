from collections import deque


class PilaAparatos:
    def __init__(self):
        self._elementos = deque()

    def push(self, elemento):
        self._elementos.append(elemento)

    def pop(self):
        if not self.is_empty():
            return self._elementos.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self._elementos[-1]
        return None

    def is_empty(self):
        return len(self._elementos) == 0

    def size(self):
        return len(self._elementos)

    def clear(self):
        self._elementos.clear()

    def obtener_lista(self):
        return list(self._elementos)


def calcular_consumo(potencia: float, horas: float, dias: int) -> float:
    return (potencia * horas * dias) / 1000.0


def crear_registro_aparato(nombre: str, potencia: float, horas: float, dias: int) -> dict:
   
    consumo = calcular_consumo(potencia, horas, dias)
    return {
        "nombre": nombre,
        "potencia": potencia,
        "horas": horas,
        "dias": dias,
        "consumo": consumo
    }


def obtener_total_consumo(pila: PilaAparatos) -> float:
    
    return sum(aparato["consumo"] for aparato in pila.obtener_lista())


def obtener_aparato_mayor_consumo(pila: PilaAparatos) -> dict | None:
   
    if pila.is_empty():
        return None
    return max(pila.obtener_lista(), key=lambda x: x["consumo"])