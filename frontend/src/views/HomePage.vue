<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar color="primary">
        <ion-title>Ahorcado</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" color="light">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Ahorcado</ion-title>
        </ion-toolbar>
      </ion-header>

      <div id="container">
        <div id="Login" v-if="tabActual === 'Login'">
          <ion-card
            ><ion-card-title class="ion-margin-top">Ahorcado</ion-card-title>
            <ion-card-content>
              <ion-item>
                <ion-label position="floating">Nombre de Usuario</ion-label>
                <ion-input
                  type="text"
                  v-model="nombreUsuario"
                  id="username"
                ></ion-input>
              </ion-item>
              <ion-item>
                <ion-label position="floating">Contraseña</ion-label>
                <ion-input
                  type="password"
                  v-model="contraUsuario"
                  id="password"
                ></ion-input>
              </ion-item>
              <ion-text v-if="error !== ''" color="danger" id="loginError">
                {{ error }}
              </ion-text>
              <ion-row class="ion-margin-top ion-justify-content-end">
                <ion-button @click="loguearse" id="loginBtn"
                  >Iniciar Sesión</ion-button
                >
                <ion-button @click="loguearseAnonimo"
                  >Ingresar como Anónimo</ion-button
                >
              </ion-row>
            </ion-card-content>
          </ion-card>
        </div>
        <div id="Dificultad" v-if="tabActual === 'Dificultad'">
          <ion-card
            ><ion-card-title class="ion-margin-top">Dificultad</ion-card-title>
            <ion-card-content>
              <ion-item>
                <ion-label position="floating">Nivel de Dificultad</ion-label>
                <ion-select v-model="dificultad" id="difSelector">
                  <ion-select-option value="facil">Fácil</ion-select-option>
                  <ion-select-option value="medio">Medio</ion-select-option>
                  <ion-select-option value="dificil">Difícil</ion-select-option>
                </ion-select>
              </ion-item>
              <ion-row class="ion-margin-top ion-justify-content-end">
                <ion-button @click="jugar">Iniciar Juego</ion-button>
              </ion-row>
            </ion-card-content>
          </ion-card>
        </div>
        <div id="Juego" v-if="tabActual === 'Juego'">
          <ion-card>
            <ion-card-title class="ion-margin-top">
              <ion-text color="primary">
                <h1>{{ palabraParcial }}</h1>
              </ion-text>
            </ion-card-title>
            <ion-card-content>
              <ion-label>{{
                "Intentos Restantes: " + intentosRestantes
              }}</ion-label>
              <br />
              <ion-label class="ion-margin-top"
                >{{ "Letras erróneas: " + letrasErroneas }}
              </ion-label>
              <br />
              <ion-label class="ion-margin-top">{{
                "Palabras erróneas: " + palabrasErroneas
              }}</ion-label>
              <ion-item v-if="inputActual === 'Letra'">
                <ion-label position="floating">Ingresa una Letra</ion-label>
                <ion-input type="text" v-model="letra"></ion-input>
              </ion-item>
              <ion-item v-if="inputActual === 'Palabra'">
                <ion-label position="floating">Arriesga una Palabra</ion-label>
                <ion-input type="text" v-model="palabraArriesgada"></ion-input>
              </ion-item>
              <ion-row class="ion-margin-top ion-align-items-center">
                <ion-radio-group
                  style="margin-right: 256px"
                  v-model="inputActual"
                >
                  <ion-label style="margin-right: 4px"
                    >Ingresa una Letra</ion-label
                  >
                  <ion-radio
                    value="Letra"
                    style="margin-right: 8px"
                  ></ion-radio>
                  <ion-label style="margin-right: 4px"
                    >Arriesga una Palabra</ion-label
                  >
                  <ion-radio value="Palabra"></ion-radio>
                </ion-radio-group>
                <ion-button
                  @click="pedirPista"
                  :disabled="pistasRestantes === 0"
                  size="auto"
                  >Pedir Pista</ion-button
                >
                <ion-button @click="verificar" size="auto"
                  >Verificar</ion-button
                >
              </ion-row>
            </ion-card-content>
          </ion-card>
        </div>
        <div
          id="Resultado y Ranking"
          v-if="tabActual === 'Resultado y Ranking'"
        >
          <ion-card style="margin-top: 480px">
            <ion-card-title
              v-if="estadoJuego === 'Ganado'"
              class="ion-margin-top"
              ><h1>
                {{ "Ganaste! Resultado: " + resultado + " puntos" }}
              </h1>
              <h2 v-if="nombreUsuario !== ''">
                {{ "Tu ranking es: " + rankingUsuario }}
              </h2></ion-card-title
            >
            <ion-card-title
              v-if="estadoJuego === 'Perdido'"
              class="ion-margin-top"
              ><h1>
                {{ "La palabra era " + palabra + ". Vuelve a intentarlo" }}
              </h1></ion-card-title
            >
            <ion-card-content
              ><ion-label><b>Top 10</b></ion-label>
              <ion-list v-for="jug in top10" :key="jug"
                ><ion-item>{{ jug }}</ion-item></ion-list
              >
              <ion-row class="ion-margin-top ion-justify-content-end">
                <ion-button @click="retry">Volver a Jugar</ion-button>
                <ion-button @click="cerrarSesion">Salir</ion-button>
              </ion-row>
            </ion-card-content>
          </ion-card>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script lang="js">
import {
  IonContent,
  IonHeader,
  IonRadioGroup,
  IonRadio,
  IonCard,
  IonCardTitle,
  IonCardContent,
  IonLabel,
  IonText,
  IonList,
  IonInput,
  IonSelect,
  IonSelectOption,
  IonRow,
  IonItem,
  IonButton,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "HomePage",
  components: {
    IonContent,
    IonHeader,
    IonCard,
    IonRadioGroup,
    IonRadio,
    IonCardTitle,
    IonCardContent,
    IonRow,
    IonList,
    IonText,
    IonSelect,
    IonSelectOption,
    IonLabel,
    IonInput,
    IonItem,
    IonButton,
    IonPage,
    IonTitle,
    IonToolbar,
  },
  data: () => ({
    tabActual: "Login",
    estadoJuego: "Inicio",
    nombreUsuario: "",
    contraUsuario: "",
    error: "",
    usuario: {},
    dificultad: "",
    palabra: "",
    palabraParcial: "",
    letrasErroneas: [],
    palabrasErroneas: [],
    intentosRestantes: 7,
    resultado: 0,
    pistasRestantes: 3,
    inputActual: "Letra",
    letra: "",
    rankingUsuario: "",
    palabraArriesgada: "",
    top10: [],
  }),

  computed: {},

  watch: {},

  async mounted() {
    await fetch(process.env.API_URL + "initPlayers", {
      method: "GET",
      headers: new Headers({
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      }),
    });
  },

  methods: {
    async loguearse() {
      if (this.nombreUsuario === "" || this.contraUsuario === "") {
        alert("Ingrese un nombre de usuario/contraseña");
        return;
      }
      const response = await fetch(
        process.env.API_URL + "login/" +
          this.nombreUsuario.toString() +
          "/" +
          this.contraUsuario.toString(),
        {
          method: "GET",
          headers: new Headers({
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
          }),
        }
      );
      const responseJson = await response.json().catch((err) => {
        alert(err);
      });
      if (responseJson.Error) {
        this.error = responseJson.Error;
      } else {
        this.usuario = responseJson;
        this.tabActual = "Dificultad";
      }
    },

    loguearseAnonimo() {
      this.tabActual = "Dificultad";
    },

    async jugar() {
      if (this.dificultad === "") {
        alert("Seleccione una dificultad");
        return;
      }
      const palabraTest = this.$route.query.palabra;
      const response = await fetch(
        process.env.API_URL + "setPalabra/" +
          this.dificultad.toString() +
          (palabraTest ? "?palabra=" + palabraTest : ""),
        {
          method: "GET",
          headers: new Headers({
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
          }),
        }
      );
      const responseJson = await response.json().catch((err) => {
        alert(err);
      });
      this.palabra = responseJson.palabra;
      this.palabraParcial = responseJson.palabraParcial;
      this.tabActual = "Juego";
      this.estadoJuego = "En Juego";
    },

    async verificar() {
      if (this.letra === "" && this.palabraArriesgada === "") {
        if (this.inputActual === "Letra") {
          alert("Ingrese una letra");
          return;
        }
        if (this.inputActual === "Palabra") {
          alert("Ingrese una palabra");
          return;
        }
        return;
      }
      const txt =
        this.inputActual.toString() === "Letra"
          ? this.letra.toString()
          : this.palabraArriesgada.toString();
      const response = await fetch(
        process.env.API_URL + "juego/" +
          this.inputActual.toString() +
          "/" +
          txt,
        {
          method: "GET",
          headers: new Headers({
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
          }),
        }
      );
      const responseJson = await response.json().catch((err) => {
        alert(err);
      });
      if (responseJson.Error) {
        alert(responseJson.Error);
      } else {
        this.palabraParcial = responseJson.palabraParcial;
        this.letrasErroneas = responseJson.letrasIncorrectas;
        this.palabrasErroneas = responseJson.palabrasArriesgadasIncorrectas;
        this.intentosRestantes = responseJson.intentosRestantes;
        this.estadoJuego = responseJson.estado;
        if (
          this.estadoJuego === "Ganado" ||
          this.estadoJuego === "Perdido" ||
          this.intentosRestantes === 0
        ) {
          this.tabActual = "Resultado y Ranking";
          await this.calcularResultado();
          await this.getTop10();
        }
      }
    },
    async pedirPista() {
      const response = await fetch(process.env.API_URL + "darPista", {
        method: "GET",
        headers: new Headers({
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        }),
      });
      const responseJson = await response.json().catch((err) => {
        alert(err);
      });
      if (responseJson.Error) {
        alert(responseJson.Error);
      } else {
        this.pistasRestantes = responseJson.pistasRestantes;
        this.palabraParcial = responseJson.palabraParcial;
        this.estadoJuego = responseJson.estado;
        if (
          this.estadoJuego === "Ganado" ||
          this.estadoJuego === "Perdido" ||
          this.intentosRestantes === 0
        ) {
          this.tabActual = "Resultado y Ranking";
          await this.calcularResultado();
          await this.getTop10();
        }
      }
    },
    async calcularResultado() {
      const response = await fetch(process.env.API_URL + "resultado", {
        method: "GET",
        headers: new Headers({
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        }),
      });
      const responseJson = await response.json().catch((err) => {
        alert(err);
      });
      if (responseJson.Error) {
        alert(responseJson.Error);
      } else {
        this.resultado = responseJson.puntuacion;
        this.usuario["puntuacion"] = responseJson.puntuacionMaxima;
        this.rankingUsuario = responseJson.ranking;
      }
    },
    async getTop10() {
      const response = await fetch(process.env.API_URL + "top10", {
        method: "GET",
        headers: new Headers({
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        }),
      });
      const responseJson = await response.json().catch((err) => {
        alert(err);
      });
      if (responseJson.Error) {
        alert(responseJson.Error);
      } else {
        this.top10 = responseJson.top10.split("\n");
      }
    },
    async retry() {
      await fetch(process.env.API_URL + "retryGame", {
        method: "GET",
        headers: new Headers({
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        }),
      });
      this.estadoJuego = "Inicio";
      this.dificultad = "";
      this.palabra = "";
      this.palabraParcial = "";
      this.pistasRestantes = 3;
      this.letrasErroneas = [];
      this.palabrasErroneas = [];
      this.intentosRestantes = 7;
      this.error = "";
      this.rankingUsuario = "";
      this.resultado = 0;
      this.inputActual = "Letra";
      this.letra = "";
      this.palabraArriesgada = "";
      this.tabActual = "Dificultad";
    },
    async cerrarSesion() {
      await fetch(process.env.API_URL + "clearAll", {
        method: "GET",
        headers: new Headers({
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        }),
      });
      this.estadoJuego = "Inicio";
      this.nombreUsuario = "";
      this.contraUsuario = "";
      this.usuario = {};
      this.dificultad = "";
      this.palabra = "";
      this.error = "";
      this.pistasRestantes = 3;
      this.palabraParcial = "";
      this.letrasErroneas = [];
      this.rankingUsuario = "";
      this.palabrasErroneas = [];
      this.intentosRestantes = 7;
      this.resultado = 0;
      this.inputActual = "Letra";
      this.letra = "";
      this.palabraArriesgada = "";
      this.tabActual = "Login";
    },
  },
});
</script>

<style scoped>
#container {
  text-align: center;

  position: absolute;
  left: 256px;
  right: 256px;
  top: 50%;
  transform: translateY(-50%);
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;

  color: #8c8c8c;

  margin: 0;
}

#container a {
  text-decoration: none;
}
</style>
