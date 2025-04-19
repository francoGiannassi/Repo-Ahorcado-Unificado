from ahorcado import Ahorcado
from usuario import Usuario

if __name__ == "__main__":
    volverAJugar = "s"
    while volverAJugar == "s":
        ahorcado = Ahorcado()
        ahorcado.limpiarVariables()
        ahorcado.setPalabrasFaciles(["Ola","Rio","Casa","Via","Sol"])
        ahorcado.setPalabrasIntermedias(["Juego","Ahorcado","Visual","Estudio","Codigo"])
        ahorcado.setPalabrasDificiles(["Otorrinolaringologo","Desoxirribonucleico","Onomatopeya","Electroencefalografista"])
        ahorcado.limpiarUsuarios()
        ahorcado.setUsuarios([Usuario("juan2","",200),Usuario("fede3","",100),Usuario("diego1","",300),Usuario("pedro7","",150),Usuario("julian9","",50),
                                Usuario("damian4","",250),Usuario("victor11","",350),Usuario("roberto10","",25),Usuario("david14","",125),
                                    Usuario("rodrigo22","",54),Usuario("alberto44","",293),Usuario("pablo76","",36)])
        ahorcado.jugar()
        ahorcado.limpiarVariables()
        volverAJugar = input("¿Desea volver a jugar? (s/n): ")
