import { defineFeature, loadFeature } from "jest-cucumber";
const feature = loadFeature("./features/gameWord.feature");
const { getWebdriver, By } = require("./webdriver");

jest.setTimeout(30000);

defineFeature(feature, (test) => {
  let driver;

  beforeEach(async () => {
    driver = await getWebdriver();
    await driver.get("https://ahorcardo-agiles.netlify.app?palabra=test");
  });

  afterEach(async () => {
    if (driver) {
      await new Promise((r) => setTimeout(r, 2000));
      await driver.close();
    }
  });

  test("Guess a correct word", ({ given, and, when, then }) => {
    given("I click login as anonimous", async () => {
      //try {
      const button = await driver.findElement(By.css("#loginAnonBtn"));
      button.click();
      await new Promise((r) => setTimeout(r, 250));
      //} catch (error) {
      //  console.error("I set franco as username", error);
      //}
    });

    when("I select a difficulty", async () => {
      //try {
      const select = await driver.findElement(By.css("#difSelector"));
      select.click();
      await new Promise((r) => setTimeout(r, 250));
      const selectOpt = await driver.findElement(By.css("button"));
      selectOpt.click();
      await new Promise((r) => setTimeout(r, 250));
      const okButton = await driver.findElement(
        By.css(".alert-button-role-cancel +button")
      );
      okButton.click();
      await new Promise((r) => setTimeout(r, 250));
      //} catch (error) {
      //  console.error("12345 as password", error);
      //}
    });

    and("I click play", async () => {
      //try {
      const button = await driver.findElement(By.css("#jugarBtn"));
      button.click();
      await new Promise((r) => setTimeout(r, 250));
      //} catch (error) {
      //  console.error("I click login", error);
      //}
    });

    then("The game starts", async () => {
      //try {
      await driver.wait(function () {
        return driver
          .findElements(By.id("palabraTxt"))
          .then((found) => !!found.length);
      }, 5000);
      //} catch (error) {
      //  console.error("I should see Difficulty Selection Page", error);
      //}
    });

    when("I click risk a word", async () => {
      //try {
      const button = await driver.findElement(By.css("#arriesgaPalabraRadio"));
      button.click();
      await new Promise((r) => setTimeout(r, 250));
      //} catch (error) {
      //  console.error("I should see Difficulty Selection Page", error);
      //}
    });

    and("I guess test as word", async () => {
      //try {
      await driver.wait(function () {
        return driver
          .findElements(By.css("#inputPalabra input"))
          .then((found) => !!found.length);
      }, 5000);
      await new Promise((r) => setTimeout(r, 250));
      const input = await driver.findElement(By.css("#inputPalabra input"));
      input.sendKeys("test");
      await new Promise((r) => setTimeout(r, 250));
      const button = await driver.findElement(By.css("#verificarBtn"));
      button.click();
      await new Promise((r) => setTimeout(r, 250));
      //} catch (error) {
      //  console.error("I should see Difficulty Selection Page", error);
      //}
    });

    then("I see Ganaste!", async () => {
      await new Promise((r) => setTimeout(r, 1000));
      await driver.wait(function () {
        return driver
          .findElement(By.css(`h1`))
          .then((found) =>
            found.getText().then((text) => text.includes("Ganaste!"))
          );
      }, 5000);
      await new Promise((r) => setTimeout(r, 2000));
      const button = await driver.findElement(By.css("#cerrarCesionBtn"));
      button.click();
      await new Promise((r) => setTimeout(r, 1000));
    });
  });

  test("Guess a wrong word", ({ given, and, when, then }) => {
    given("I click login as anonimous", async () => {
      const button = await driver.findElement(By.css("#loginAnonBtn"));
      button.click();
      await new Promise((r) => setTimeout(r, 250));
    });

    when("I select a difficulty", async () => {
      const select = await driver.findElement(By.css("#difSelector"));
      select.click();
      await new Promise((r) => setTimeout(r, 250));
      const selectOpt = await driver.findElement(By.css("button"));
      selectOpt.click();
      await new Promise((r) => setTimeout(r, 250));
      const okButton = await driver.findElement(
        By.css(".alert-button-role-cancel +button")
      );
      okButton.click();
      await new Promise((r) => setTimeout(r, 250));
    });

    and("I click play", async () => {
      const button = await driver.findElement(By.css("#jugarBtn"));
      button.click();
      await new Promise((r) => setTimeout(r, 250));
    });
    
    then("The game starts", async () => {
      await driver.wait(function () {
        return driver
          .findElements(By.id("palabraTxt"))
          .then((found) => !!found.length);
      }, 5000);
    });

    when("I click risk a word", async () => {
      const button = await driver.findElement(By.css("#arriesgaPalabraRadio"));
      button.click();
      await new Promise((r) => setTimeout(r, 250));
    });

    and("I guess prueba as word", async () => {
      await driver.wait(function () {
        return driver
          .findElements(By.css("#inputPalabra input"))
          .then((found) => !!found.length);
      }, 5000);
      await new Promise((r) => setTimeout(r, 250));
      const input = await driver.findElement(By.css("#inputPalabra input"));
      input.sendKeys("prueba");
      await new Promise((r) => setTimeout(r, 250));
      const button = await driver.findElement(By.css("#verificarBtn"));
      button.click();
      await new Promise((r) => setTimeout(r, 250));
    });

    then("I see prueba in wrong risked words list", async () => {
      await new Promise((r) => setTimeout(r, 1000));
      await driver.wait(function () {
        return driver
          .findElement(By.css(`#palabrasErroneasLbl`))
          .then((found) =>
            found
              .getText()
              .then((text) => text.includes("Palabras erróneas: Prueba"))
          );
      }, 5000);
      await new Promise((r) => setTimeout(r, 2000));
      const button = await driver.findElement(By.css("#salirBtn"));
      button.click();
    });
  });
});