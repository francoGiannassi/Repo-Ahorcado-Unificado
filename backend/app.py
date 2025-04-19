from flask import Flask, jsonify, request
from flask_cors import CORS
from ahorcado import Ahorcado
from usuario import Usuario

app = Flask(__name__)
CORS(app)

ahorcado = Ahorcado()

@app.route("/initPlayers")
def init():
    ahorcado.limpiarUsuarios()
    ahorcado.setUsuarios([Usuario("juan2",".",200),Usuario("fede3",".",100),Usuario("diego1",".",300),Usuario("pedro7",".",150),Usuario("julian9",".",50),
                                Usuario("damian4",".",250),Usuario("victor11",".",350),Usuario("roberto10",".",25),Usuario("david14",".",125),
                                    Usuario("rodrigo22",".",54),Usuario("alberto44",".",293),Usuario("pablo76",".",36)])
    return "done"

@app.route("/")
def index():
    return "index"

@app.route("/login/<nombreUsuario>/<contraUsuario>")
def login(nombreUsuario, contraUsuario):
    error = ""
    if ahorcado.getUsuarioActual().esNombreUsuarioCorrecto(str(nombreUsuario)):
        ahorcado.getUsuarioActual().setNombre(str(nombreUsuario))
    else:
        error = 'Invalid username '
    if ahorcado.getUsuarioActual().esContraseniaCorrecta(str(contraUsuario)):
        ahorcado.getUsuarioActual().setContrasenia(str(contraUsuario))
    else: 
        error += 'Invalid password' 
    if error == "":
        return jsonify({"nombre": ahorcado.getUsuarioActual().getNombre(), "contrasenia": ahorcado.getUsuarioActual().getContrasenia(), "puntuacion": ahorcado.getUsuarioActual().getPuntuacionMaxima()})
    return jsonify({"Error": error})

@app.route("/setPalabra/<dificultad>")
def setPalabra(dificultad):
    ahorcado.setPalabrasFaciles(["Ola","Rio","Casa","Via","Sol"])
    ahorcado.setPalabrasIntermedias(["Juego","Ahorcado","Visual","Estudio","Codigo"])
    ahorcado.setPalabrasDificiles(["Otorrinolaringologo","Desoxirribonucleico","Onomatopeya","Electroencefalografista"])  
    palabraTest = request.args.get("palabra") 
    if palabraTest !=None:
        ahorcado.setPalabra(palabraTest)
    else:
        if str(dificultad) == "facil":
            ahorcado.setPalabra(ahorcado.seleccionarPalabraRandom(ahorcado.palabrasFaciles)) 
        elif str(dificultad) == "medio":
            ahorcado.setPalabra(ahorcado.seleccionarPalabraRandom(ahorcado.palabrasIntermedias))
        elif str(dificultad) == "dificil":
            ahorcado.setPalabra(ahorcado.seleccionarPalabraRandom(ahorcado.palabrasDificiles))
    print(ahorcado.getPalabra())
    return jsonify({"palabra": ahorcado.getPalabra(), "palabraParcial": ahorcado.getPalabraParcial()})

@app.route("/juego/<opcion>/<txt>")
def verificar(opcion, txt):
    if str(opcion) == "Letra":
        ahorcado.ingresaLetra(txt)
    elif str(opcion) == "Palabra":
        ahorcado.arriesgaPalabra(txt)
    return jsonify({"estado": ahorcado.getEstadoFinalJuego(), "palabraParcial": ahorcado.getPalabraParcial(), "intentosRestantes": ahorcado.getIntentosRestantes(), "letrasIncorrectas": ahorcado.getLetrasIncorrectasMinus(), "palabrasArriesgadasIncorrectas": ahorcado.getPalabrasArriesgadasIncorrectas()})

@app.route("/darPista")
def darPista():
    ahorcado.ingresaLetra(ahorcado.darPista())
    return jsonify({"estado": ahorcado.getEstadoFinalJuego(), "palabraParcial": ahorcado.getPalabraParcial(), "pistasRestantes": 3 - ahorcado.getNroPistas()})

@app.route("/resultado")
def getResultado():
        if(ahorcado.usuarioActual.getNombre() != ""):
            if ahorcado.esPuntuacionActualMayorAMaxima():
                ahorcado.usuarioActual.setPuntuacionMaxima(ahorcado.calcularResultadoFinal())    
            return jsonify({"puntuacion": ahorcado.calcularResultadoFinal(), "ranking": ahorcado.rankingJugadorActual() ,"puntuacionMaxima": ahorcado.usuarioActual.getPuntuacionMaxima()})
        return jsonify({"puntuacion": ahorcado.calcularResultadoFinal()})

@app.route("/clearAll")
def limpiarTodo():
    ahorcado.limpiarVariables()
    return "done"

@app.route("/top10")
def top10():
    return jsonify({"top10": ahorcado.top10()})

@app.route("/retryGame")
def retry():
    ahorcado.nuevoJuego()
    return "done"

if __name__ == "__main__":
    app.run(debug=True)