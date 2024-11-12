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
            if asiento != None:
                contador += 1
        return contador

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            print(1)
            return "Las piezas no son originales"
        
        for asiento in self.asientos:
            if asiento is not None:
                if asiento.registro != self.registro:
                    print(3)
                    return "Las piezas no son originales"
            
        return "Auto original"
    

a1 = Auto("model 3", 33000, [Asiento("blanco", 5000, 32),None, None, Asiento("blanco", 5000, 32), None],
"tesla", Motor(4, "electrico", 32), 32)
a2 = Auto("model 3", 33000, [Asiento("blanco", 5000, 40),None, None, Asiento("blanco", 5000, 32), None],
"tesla", Motor(4, "electrico", 32), 32)

ok = False
		
if(a1.verificarIntegridad() == "Auto original" and 
        a2.verificarIntegridad() == "Las piezas no son originales"):
    ok = True
print(ok)
