from usuario import Usuario
import random

class Ahorcado:   
    # Variables
    palabra = ""
    palabrasFaciles = []
    palabrasIntermedias = []
    palabrasDificiles = []

    usuarioActual = Usuario()
    usuarios = []
    usuarios.append(usuarioActual)

    letrasCorrectas = []
    letrasIncorrectas = []
    palabrasArriesgadasIncorrectas = []

    intentosFallidos = 0
    intentosTotales = 0

    palabraArriesgadaAcertada = False

    nroPistas = 0

    # Juego
    def jugar(self):
        print("Ahorcado")
        print("1 - Loguearse")
        print("2 - Ingresar como anónimo")
        op = int(input("Opción: "))
        if op == 1:
            self.getUsuarioActual().setNombre(input("Nombre de Usuario: "))
            self.getUsuarioActual().setContrasenia(input("Contraseña: "))
        elif op == 2:
            self.getUsuarioActual().setNombre("")  

        print("Dificultad:")
        print("1 - Facil")
        print("2 - Intermedio")
        print("3 - Dificil")

        dif = int(input("Opción: "))
        if dif == 1:
            self.setPalabra(self.seleccionarPalabraRandom(self.palabrasFaciles)) 
        elif dif == 2:
            self.setPalabra(self.seleccionarPalabraRandom(self.palabrasIntermedias))
        elif dif == 3:
            self.setPalabra(self.seleccionarPalabraRandom(self.palabrasDificiles))
            
        print("")
        print("Arranca el Juego!! Suerte!!")
        while self.getEstadoFinalJuego() == "En Juego":
            print(self.getPalabraParcial())
            letra_op = input("Ingresa una letra (0 - arriesga palabra, 1 - dar una pista): " if self.getNroPistas() < 3 else "Ingresa una letra (0 - arriesga palabra): ")
            if letra_op != str(0) and letra_op != str(1):
                self.ingresaLetra(letra_op)
            elif letra_op == str(0):
                self.arriesgaPalabra(input("Ingresa la palabra a arriesgar: "))
            elif letra_op == str(1):
                self.ingresaLetra(self.darPista())
                print("Pistas Restantes: " + str(3 - self.getNroPistas()))
            print("Intentos Restantes: ", self.getIntentosRestantes())
            print("")
            if len(self.getLetrasIncorrectasMinus()) > 0:
                print("Letras Incorrectas: " + str(self.getLetrasIncorrectasMinus()))
            if len(self.getPalabrasArriesgadasIncorrectas()) > 0:
                print("Palabras Arriesgadas Incorrectas: " + str(self.getPalabrasArriesgadasIncorrectas()))
            print("")
            
        cartel = ""
        print("")
        print(self.getPalabra().upper())
        print("")
        if self.getEstadoFinalJuego() == "Ganado":
            cartel = "Ganaste!"
        elif self.getEstadoFinalJuego() == "Perdido":
            cartel = "Perdiste!"
        print(cartel)
        print("")
        print(self.calcularResultadoFinal()," puntos")
        print("")
        if(self.usuarioActual.getNombre() != ""):
            if self.esPuntuacionActualMayorAMaxima():
                self.usuarioActual.setPuntuacionMaxima(self.calcularResultadoFinal())    
            print("Estas en el puesto ",self.rankingJugadorActual()," del ranking")
            print("")
            print("Top 10:")
            print(self.top10())
        
    def getEstadoFinalJuego(self):
        if self.intentosFallidos == 7:
            return "Perdido"
        elif self.esPalabraFinal():
            return "Ganado"
        else: 
            return "En Juego"

    #Palabras
    def getPalabra(self):
        return self.palabra

    def setPalabra(self,palabra):
        self.palabra = palabra

    def getPalabraParcial(self):
        palabraParcial = ""
        for letra in self.palabra:
            if letra in self.letrasCorrectas:
                palabraParcial += letra.lower()
            else: 
                palabraParcial += "-"
                
        return palabraParcial.capitalize()

    def getPalabrasFaciles(self):
        return self.palabrasFaciles

    def setPalabrasFaciles(self,palabras):
        self.palabrasFaciles = palabras

    def getPalabrasIntermedias(self):
        return self.palabrasIntermedias

    def setPalabrasIntermedias(self,palabras):
        self.palabrasIntermedias = palabras

    def getPalabrasDificiles(self):
        return self.palabrasDificiles

    def setPalabrasDificiles(self,palabras):
        self.palabrasDificiles = palabras

    def seleccionarPalabraRandom(self,palabras):
        palabra = random.choice(palabras)
        return palabra
   
    def esPalabraFinal(self):
        if self.getPalabra().lower() == self.getPalabraParcial().lower():
            return True
        else:
            return False
    
    def arriesgaPalabra(self, palabra):
        if self.esPalabraPermitida(palabra):
            if palabra.lower() == self.palabra.lower():
                for letra in palabra:
                    self.letrasCorrectas.append(letra.lower())
                    self.letrasCorrectas.append(letra.upper())
                self.palabraArriesgadaAcertada = True
            else:
                self.sumarIntentoFallido()
                self.sumarIntentoFallido()
                self.palabrasArriesgadasIncorrectas.append(palabra.capitalize())
                self.palabraArriesgadaAcertada = False
            self.sumarIntentoTotal()

    def esPalabraPermitida(self, palabra):
        if palabra.isalpha() and palabra != "":
            return True
        else:
            return False

    def esPalabraArriesgadaAcertada(self):
        return self.palabraArriesgadaAcertada
        
    def getPalabrasArriesgadasIncorrectas(self):
        return self.palabrasArriesgadasIncorrectas

    def limpiarPalabrasArriesgadasIncorrectas(self):
        self.palabrasArriesgadasIncorrectas = []

    #Usuarios
    def getUsuarioActual(self):
        return self.usuarioActual
    
    def getUsuarios(self):
        return self.usuarios

    def limpiarUsuarios(self):
        self.usuarios = []
        self.usuarios.append(self.usuarioActual)

    def setUsuarios(self,usuarios):
        for us in usuarios:
            self.usuarios.append(us)

    def getNombresUsuarios(self):
        nombres = []
        for us in self.usuarios:
            nombres.append(us.getNombre())
        return nombres

    def existeUsuario(self,nombre):
        if nombre in self.getNombresUsuarios():
            return True
        else:
            return False

    #Letras
    def ingresaLetra(self, letra):
        if not self.esLetraRepetida(letra):
            if letra == "" or not letra.isalpha():
                self.letrasIncorrectas.append(letra)
            elif self.esLetraCorrecta(letra):
                self.letrasCorrectas.append(letra.lower())
                self.letrasCorrectas.append(letra.upper())
                self.sumarIntentoTotal()
            else:
                self.letrasIncorrectas.append(letra.lower())
                self.letrasIncorrectas.append(letra.upper())
                if not self.getIntentosRestantes() <= 0:
                    self.sumarIntentoFallido()
                    self.sumarIntentoTotal()
        
    def getLetrasCorrectas(self):
        return self.letrasCorrectas

    def getLetrasIncorrectas(self):
        return self.letrasIncorrectas

    def getLetrasIncorrectasMinus(self):
        lista = []
        for letra in self.letrasIncorrectas:
            if letra.islower() and letra.isalpha():
                lista.append(letra)
        return lista

    def esLetraCorrecta(self, letra):
        if letra.lower() in self.palabra.lower():
            return True
        else:
            return False
    
    def esLetraRepetida(self, letra):
        if letra in self.getLetrasCorrectas() or letra in self.getLetrasIncorrectas():
            return True
        else:
            return False
    
    def limpiarLetras(self):
        self.letrasCorrectas = []
        self.letrasIncorrectas = []

    def darPista(self):
        letraElegida = ""
        palabraDescompuesta = []
        for letra in self.palabra:
            palabraDescompuesta.append(letra)
        seEligioLetra = False
        if self.nroPistas >= 3:
            letraElegida = "No se pueden dar más pistas"
        else:
            while not seEligioLetra:
                letraElegida = random.choice(palabraDescompuesta)
                if letraElegida not in self.letrasCorrectas:
                    seEligioLetra = True
            self.nroPistas+=1
        return letraElegida

    def getNroPistas(self):
        return self.nroPistas

    #Intentos
    def sumarIntentoTotal(self):
        self.intentosTotales+=1

    def getIntentosTotales(self):
        return self.intentosTotales

    def sumarIntentoFallido(self):
        self.intentosFallidos+=1
    
    def getIntentosFallidos(self):
        if self.intentosFallidos <= 7:
            return self.intentosFallidos
        else:
            return 7

    def getIntentosRestantes(self):
        return 7 - self.getIntentosFallidos()

    #Resultado Final
    def calcularResultadoFinal(self):
        largoPalabra = len(self.palabra)
        resultado = largoPalabra*(self.getIntentosRestantes() ** 2)/(self.getIntentosTotales())
        if self.palabraArriesgadaAcertada:
            resultado = resultado*2
        return round(resultado)

    def esPuntuacionActualMayorAMaxima(self):
        if self.calcularResultadoFinal() > self.usuarioActual.getPuntuacionMaxima():
            return True
        else:
            return False

    #Ranking
    def puestosOrdenadosRanking(self):
        ranking = self.getUsuarios()
        ranking.sort(key=lambda u : u.puntuacionMaxima, reverse=True)
        return ranking
    
    def rankingJugadorActual(self):
        for i, us in enumerate(self.puestosOrdenadosRanking()):
            if us.getNombre() == self.getUsuarioActual().getNombre() and us.getPuntuacionMaxima() == self.getUsuarioActual().getPuntuacionMaxima() and us.getContrasenia() == self.getUsuarioActual().getContrasenia():
                return i+1

    def top10(self):
        lista = self.puestosOrdenadosRanking()[:10]
        top10 = ""
        for i, puesto in enumerate(lista):
            top10 += str(i+1) + " - " + puesto.getNombre() + " - " + str(puesto.getPuntuacionMaxima()) + "\n"
        return top10
    
    #Varios

    def limpiarVariables(self):
        self.palabra = ""
        self.palabrasFaciles = []
        self.palabrasIntermedias = []
        self.palabrasDificiles = []

        self.usuarioActual = Usuario()
        self.usuarios.append(self.usuarioActual)

        self.letrasCorrectas = []
        self.letrasIncorrectas = []
        self.palabrasArriesgadasIncorrectas = []

        self.intentosFallidos = 0
        self.intentosTotales = 0

        self.palabraArriesgadaAcertada = False

        self.nroPistas = 0

    def nuevoJuego(self):
        self.palabra = ""
        self.palabrasFaciles = []
        self.palabrasIntermedias = []
        self.palabrasDificiles = []

        self.letrasCorrectas = []
        self.letrasIncorrectas = []
        self.palabrasArriesgadasIncorrectas = []

        self.intentosFallidos = 0
        self.intentosTotales = 0

        self.palabraArriesgadaAcertada = False

        self.nroPistas = 0
        

        