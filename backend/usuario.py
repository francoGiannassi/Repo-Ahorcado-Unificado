class Usuario:

    nombre = ""
    contrasenia = ""
    puntuacionMaxima = 0


    def __init__(self, nombre="", contrasenia="", puntuacionMaxima=0):
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.puntuacionMaxima = puntuacionMaxima

    def __repr__(self):
        return repr((self.nombre, self.puntuacionMaxima))

    def esNombreUsuarioCorrecto(self,nombre):
        if len(nombre) <= 8:
            return True
        else:
            return False

    def esContraseniaCorrecta(self,contrasenia):
        if len(contrasenia) <= 15:
            return True
        else:
            return False

    def setNombre(self,nombre):
        if self.esNombreUsuarioCorrecto(nombre):
            self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setContrasenia(self,contrasenia):
        if self.esContraseniaCorrecta(contrasenia):
            self.contrasenia = contrasenia

    def getContrasenia(self):
        return self.contrasenia

    def setPuntuacionMaxima(self, puntuacion):
        self.puntuacionMaxima = puntuacion
    
    def getPuntuacionMaxima(self):
        return self.puntuacionMaxima
