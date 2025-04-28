import { defineFeature, loadFeature } from "jest-cucumber";
const feature = loadFeature("./features/gameWord.feature");
const { getWebdriver, By } = require("./webdriver");

jest.setTimeout(30000);

defineFeature(feature, (test) => {
  let driver;

  beforeEach(async () => {
    driver = await getWebdriver();
    await driver.get("http://localhost:8080?palabra=test");
  });

  afterEach(async () => {
    if (driver) {
      await new Promise((r) => setTimeout(r, 2000));
      await driver.close();
    }
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