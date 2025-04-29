import unittest
from ahorcado import Ahorcado
from usuario import Usuario

class TestsLogIn(unittest.TestCase):
    
    def test_valida_usuario_anonimo(self):
        ahorcado = Ahorcado()
        ahorcado.getUsuarioActual().setNombre("")
        self.assertEqual("",ahorcado.getUsuarioActual().getNombre())
        
    def test_nombre_usuario_incorrecto(self):
        ahorcado = Ahorcado()
        ahorcado.getUsuarioActual().setNombre("Franco@123")
        self.assertFalse(ahorcado.getUsuarioActual().esNombreUsuarioCorrecto("Franco@123"))
    
    def test_nombre_usuario_correcto(self):
        ahorcado = Ahorcado()
        ahorcado.getUsuarioActual().setNombre("Franco")
        self.assertTrue(ahorcado.getUsuarioActual().esNombreUsuarioCorrecto("Franco"))
    
    def test_valida_existencia_del_nombre(self):
        ahorcado = Ahorcado()
        us = Usuario()
        us.setNombre("Franco")
        ahorcado.getUsuarioActual().setNombre("Franco")
        self.assertTrue(ahorcado.existeUsuario(us.getNombre()))

    def test_valida_no_existencia_del_nombre(self):
        ahorcado = Ahorcado()
        us = Usuario()
        us.setNombre("Franco12")
        ahorcado.getUsuarioActual().setNombre("Franco")
        self.assertFalse(ahorcado.existeUsuario(us.getNombre()))

    def test_valida_contrasenia_correcta(self):
        ahorcado = Ahorcado()
        us = Usuario()
        us.setContrasenia("hola#123")
        self.assertTrue(ahorcado.getUsuarioActual().esContraseniaCorrecta("hola#123"))

    def test_valida_contrasenia_incorrecta(self):
        ahorcado = Ahorcado()
        us = Usuario()
        us.setContrasenia("holaaa#123456789")
        self.assertFalse(ahorcado.getUsuarioActual().esContraseniaCorrecta("holaaa#123456789"))


class TestsConfiguracion(unittest.TestCase):
    
    def test_valida_ninguna_palabra_cargada(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("")
        self.assertIn("", ahorcado.getPalabra())

    def test_valida_una_palabra_cargada(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabrasIntermedias(["Juego","Ahorcado","Visual","Estudio","Codigo"])
        self.assertIn("Ahorcado", ahorcado.getPalabrasIntermedias())

    def test_valida_dificultad_facil(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabrasFaciles(["Ola","Rio","Casa","Via","Sol"])
        self.assertIn("Ola",ahorcado.getPalabrasFaciles())

    def test_valida_dificultad_intermedia(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabrasIntermedias(["Juego","Ahorcado","Visual","Estudio","Codigo"])
        self.assertIn("Codigo",ahorcado.getPalabrasIntermedias())

    def test_valida_dificultad_dificil(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabrasDificiles(["Otorrinolaringologo","Desoxirribonucleico","Onomatopeya","Electroencefalografista"])
        self.assertIn("Onomatopeya",ahorcado.getPalabrasDificiles())

    def test_valida_palabra_random_seleccionada(self):
        ahorcado = Ahorcado()
        listaDificil = ["Otorrinolaringologo","Desoxirribonucleico","Onomatopeya","Electroencefalografista"]
        ahorcado.setPalabrasDificiles(listaDificil)
        self.assertIn(ahorcado.seleccionarPalabraRandom(listaDificil),ahorcado.getPalabrasDificiles())

class TestsJuego(unittest.TestCase):

    def test_valida_letra_correcta(self):
        ahorcado7 = Ahorcado()
        ahorcado7.setPalabra("Ahorcado")
        ahorcado7.ingresaLetra("a")
        self.assertIn("a",ahorcado7.getLetrasCorrectas())
    
    def test_valida_letra_incorrecta(self):
        ahorcado9 = Ahorcado()
        ahorcado9.setPalabra("Ahorcado")
        ahorcado9.ingresaLetra("e")
        self.assertIn("e",ahorcado9.getLetrasIncorrectas())

    def test_valida_letra_mayuscula(self):
        ahorcado8 = Ahorcado()
        ahorcado8.setPalabra("Ahorcado")
        ahorcado8.ingresaLetra("H")
        self.assertIn("H",ahorcado8.getLetrasCorrectas())

    def test_valida_caracter_no_alfabetico(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("$")
        self.assertIn("$",ahorcado.getLetrasIncorrectas())
    
    def test_valida_caracter_vacio(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("")
        self.assertIn("",ahorcado.getLetrasIncorrectas())

    def test_es_letra_correcta(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("c")
        self.assertTrue(ahorcado.esLetraCorrecta("c"))
    
    def test_es_letra_incorrecta(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("t")
        self.assertFalse(ahorcado.esLetraCorrecta("t"))
    
    def test_es_letra_repetida(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("h")
        self.assertTrue(ahorcado.esLetraRepetida("h"))

    def test_es_letra_no_repetida(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("h")
        self.assertFalse(ahorcado.esLetraRepetida("o"))

    def test_palabra_parcial_correcta(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("A")
        ahorcado.ingresaLetra("H")
        ahorcado.ingresaLetra("C")
        ahorcado.ingresaLetra("D")
        self.assertEqual(ahorcado.getPalabraParcial(),"Ah--cad-")
    
    def test_valida_conteo_intentos_fallidos(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("f")
        ahorcado.ingresaLetra("i")
        ahorcado.ingresaLetra("m")
        self.assertEqual(ahorcado.getIntentosFallidos(),3)

    def test_valida_tope_maximo_intentos_fallidos(self):
        ahorcado11 = Ahorcado()
        ahorcado11.limpiarLetras()
        ahorcado11.setPalabra("Ahorcado")
        ahorcado11.ingresaLetra("f")
        ahorcado11.ingresaLetra("i")
        ahorcado11.ingresaLetra("m")
        ahorcado11.ingresaLetra("u")
        ahorcado11.ingresaLetra("j")
        ahorcado11.ingresaLetra("k")
        ahorcado11.ingresaLetra("p")
        self.assertEqual(ahorcado11.getIntentosFallidos(),7)

    def test_valida_intentos_restantes(self):
        ahorcado11 = Ahorcado()
        ahorcado11.limpiarLetras()
        ahorcado11.setPalabra("Ahorcado")
        ahorcado11.ingresaLetra("f")
        ahorcado11.ingresaLetra("i")
        ahorcado11.ingresaLetra("m")
        self.assertEqual(ahorcado11.getIntentosRestantes(),4)

    def test_valida_intentos_restantes_no_sean_menores_a_0(self):
        ahorcado11 = Ahorcado()
        ahorcado11.limpiarLetras()
        ahorcado11.setPalabra("Ahorcado")
        ahorcado11.ingresaLetra("f")
        ahorcado11.ingresaLetra("i")
        ahorcado11.ingresaLetra("m")
        ahorcado11.ingresaLetra("t")
        ahorcado11.ingresaLetra("u")
        ahorcado11.ingresaLetra("p")
        ahorcado11.ingresaLetra("w")
        ahorcado11.ingresaLetra("v")
        ahorcado11.ingresaLetra("l")
        self.assertEqual(ahorcado11.getIntentosRestantes(),0)

    def test_palabra_a_arriesgar_es_alfabetica(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarLetras()
        ahorcado.setPalabra("Ahorcado")
        self.assertTrue(ahorcado.esPalabraPermitida("Ahorcado"))
    
    def test_palabra_a_arriesgar_es_no_alfabetica(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarLetras()
        ahorcado.setPalabra("Ahorcado")
        self.assertFalse(ahorcado.esPalabraPermitida("Ahorcado9#"))

    def test_palabra_arriesgada_acertada(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarLetras()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.arriesgaPalabra("Ahorcado")
        self.assertTrue(ahorcado.esPalabraFinal())
    
    def test_palabra_arriesgada_no_acertada(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarLetras()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.arriesgaPalabra("Ahocado")
        self.assertFalse(ahorcado.esPalabraFinal())

    def test_valida_letras_incorrectas_cargadas(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarLetras()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("p")
        ahorcado.ingresaLetra("m")
        ahorcado.ingresaLetra("o")
        ahorcado.ingresaLetra("f")
        ahorcado.ingresaLetra("a")
        ahorcado.ingresaLetra("u")
        lista = ["p","m","f","u"]
        self.assertEqual(lista,ahorcado.getLetrasIncorrectasMinus())

    def test_valida_palabras_arriesgadas_incorrectas_cargadas(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarPalabrasArriesgadasIncorrectas()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.arriesgaPalabra("Ahcado")
        ahorcado.arriesgaPalabra("Ahorcado")
        ahorcado.arriesgaPalabra("Ahocardo")
        lista = ["Ahcado","Ahocardo"]
        self.assertEqual(lista,ahorcado.getPalabrasArriesgadasIncorrectas())

    def test_valida_letra_de_pista(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarPalabrasArriesgadasIncorrectas()
        ahorcado.limpiarLetras()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("a")
        ahorcado.ingresaLetra("h")
        pistasPosibles = ["o","r","c","d","o"]
        self.assertIn(ahorcado.darPista(),pistasPosibles)

    def test_valida_numero_de_pistas(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarPalabrasArriesgadasIncorrectas()
        ahorcado.limpiarLetras()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("a")
        ahorcado.ingresaLetra("h")
        ahorcado.darPista()
        ahorcado.darPista()
        self.assertEqual(2,ahorcado.getNroPistas())

class TestsResultadoFinal(unittest.TestCase):

    def test_valida_partida_perdida(self):
        ahorcado11 = Ahorcado()
        ahorcado11.limpiarLetras()
        ahorcado11.setPalabra("Ahorcado")
        ahorcado11.ingresaLetra("f")
        ahorcado11.ingresaLetra("i")
        ahorcado11.ingresaLetra("m")
        ahorcado11.ingresaLetra("u")
        ahorcado11.ingresaLetra("j")
        ahorcado11.ingresaLetra("k")
        ahorcado11.ingresaLetra("p")
        self.assertEqual("Perdido",ahorcado11.getEstadoFinalJuego())

    def test_valida_partida_ganada(self):
        ahorcado3 = Ahorcado()
        ahorcado3.setPalabra("Ahorcado")
        ahorcado3.ingresaLetra("a")
        ahorcado3.ingresaLetra("h")
        ahorcado3.ingresaLetra("o")
        ahorcado3.ingresaLetra("r")
        ahorcado3.ingresaLetra("c")
        ahorcado3.ingresaLetra("d")
        self.assertEqual("Ganado",ahorcado3.getEstadoFinalJuego())

    def test_valida_resultado_final_partida_perdida(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.limpiarLetras()
        ahorcado.ingresaLetra("f")
        ahorcado.ingresaLetra("i")
        ahorcado.ingresaLetra("m")
        ahorcado.ingresaLetra("u")
        ahorcado.ingresaLetra("j")
        ahorcado.ingresaLetra("k")
        ahorcado.ingresaLetra("p")
        self.assertEqual(ahorcado.calcularResultadoFinal(),0)

    def test_valida_resultado_final_partida_ganada(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.limpiarLetras()
        ahorcado.ingresaLetra("a")
        ahorcado.ingresaLetra("h")
        ahorcado.ingresaLetra("o")
        ahorcado.ingresaLetra("r")
        ahorcado.ingresaLetra("c")
        ahorcado.ingresaLetra("d")
        self.assertEqual(ahorcado.calcularResultadoFinal(),65)

    def test_valida_resultado_final_partida_ganada_palabra_arriesgada(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.limpiarLetras()
        ahorcado.arriesgaPalabra("Ahorcado")
        self.assertEqual(ahorcado.calcularResultadoFinal(),784)

    def test_valida_resultado_final_partida_ganada_palabra_arriesgada_con_3_intentos_fallidos_de_letras(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.limpiarLetras()
        ahorcado.ingresaLetra("f")
        ahorcado.ingresaLetra("t")
        ahorcado.ingresaLetra("m")
        ahorcado.arriesgaPalabra("Ahorcado")
        self.assertEqual(ahorcado.calcularResultadoFinal(),64)
    
    def test_valida_resultado_final_partida_ganada_palabra_arriesgada_con_3_intentos_acertados_de_letras(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.limpiarLetras()
        ahorcado.ingresaLetra("a")
        ahorcado.ingresaLetra("h")
        ahorcado.ingresaLetra("o")
        ahorcado.arriesgaPalabra("Ahorcado")
        self.assertEqual(ahorcado.calcularResultadoFinal(),196)

    def test_valida_resultado_final_partida_ganada_palabra_arriesgada_con_intento_fallido_palabra(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.limpiarLetras()
        ahorcado.arriesgaPalabra("Ahocado")
        ahorcado.arriesgaPalabra("Ahorcado")
        self.assertEqual(ahorcado.calcularResultadoFinal(),200)

    def test_valida_cambio_puntuacion_maxima_por_una_nueva_mejor(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.limpiarLetras()
        ahorcado.getUsuarioActual().setPuntuacionMaxima(300)
        ahorcado.arriesgaPalabra("Ahorcado")
        self.assertTrue(ahorcado.esPuntuacionActualMayorAMaxima())

    def test_valida_no_cambio_puntuacion_maxima_por_una_nueva_peor(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.limpiarLetras()
        ahorcado.getUsuarioActual().setPuntuacionMaxima(300)
        ahorcado.ingresaLetra("f")
        ahorcado.ingresaLetra("i")
        ahorcado.ingresaLetra("m")
        ahorcado.ingresaLetra("u")
        ahorcado.arriesgaPalabra("Ahorcado")
        self.assertFalse(ahorcado.esPuntuacionActualMayorAMaxima())
    
    
class TestsRanking(unittest.TestCase):

    def test_valida_1er_posicion_top10(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarUsuarios()
        ahorcado.setUsuarios([Usuario("juan2","",200),Usuario("fede3","",100),Usuario("diego1","",300),Usuario("pedro7","",150),Usuario("julian9","",50),
                                    Usuario("damian4","",250),Usuario("victor11","",350),Usuario("roberto10","",25),Usuario("david14","",125)])
        ahorcado.getUsuarioActual().setNombre("franco1")                                
        ahorcado.getUsuarioActual().setPuntuacionMaxima(400)
        self.assertEqual(ahorcado.rankingJugadorActual(),1)

    def test_valida_posicion_intermedia_top10(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarUsuarios()
        ahorcado.setUsuarios([Usuario("juan2","",200),Usuario("fede3","",100),Usuario("diego1","",300),Usuario("pedro7","",150),Usuario("julian9","",50),
                                    Usuario("damian4","",250),Usuario("victor11","",350),Usuario("roberto10","",25),Usuario("david14","",125)])
        ahorcado.getUsuarioActual().setNombre("franco1")                                
        ahorcado.getUsuarioActual().setPuntuacionMaxima(175)
        self.assertEqual(ahorcado.rankingJugadorActual(),5)

    def test_valida_ultima_posicion_top10(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarUsuarios()
        ahorcado.setUsuarios([Usuario("juan2","",200),Usuario("fede3","",100),Usuario("diego1","",300),Usuario("pedro7","",150),Usuario("julian9","",50),
                                    Usuario("damian4","",250),Usuario("victor11","",350),Usuario("roberto10","",25),Usuario("david14","",125)])
        ahorcado.getUsuarioActual().setNombre("franco1")                                
        ahorcado.getUsuarioActual().setPuntuacionMaxima(15)
        self.assertEqual(ahorcado.rankingJugadorActual(),10)

    def test_valida_posicion_fuera_limites_top_10_puesto_13(self):
        ahorcado = Ahorcado()
        ahorcado.limpiarUsuarios()
        ahorcado.setUsuarios([Usuario("juan2","",200),Usuario("fede3","",100),Usuario("diego1","",300),Usuario("pedro7","",150),Usuario("julian9","",50),
                                Usuario("damian4","",250),Usuario("victor11","",350),Usuario("roberto10","",25),Usuario("david14","",125),
                                    Usuario("rodrigo22","",54),Usuario("alberto44","",293),Usuario("pablo76","",36)])
        ahorcado.getUsuarioActual().setNombre("franco1")                                
        ahorcado.getUsuarioActual().setPuntuacionMaxima(15)
        self.assertEqual(ahorcado.rankingJugadorActual(),13)





