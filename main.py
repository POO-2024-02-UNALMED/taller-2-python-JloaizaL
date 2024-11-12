class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, nuevoColor):
        colPer = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        if nuevoColor in colPer:
            self.color = nuevoColor

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo):
        if nuevoTipo in ["electrico", "gasolina"]:
            self.tipo = nuevoTipo

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1
    
    def cantidadAsientos(self):
        contador = 0
        for asiento in self.asientos:
            if asiento != "null":
                contador += 1
        return contador

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        
        for asiento in self.asientos:
            if asiento.registro != "null" and asiento.registro != self.registro:
                return "Las piezas no son originales"
            
        return "Auto original"