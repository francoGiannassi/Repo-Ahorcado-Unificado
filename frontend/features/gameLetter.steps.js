import { defineFeature, loadFeature } from "jest-cucumber";
const feature = loadFeature("./features/gameLetter.feature");
const { getWebdriver, By } = require("./webdriver");

jest.setTimeout(60000);

defineFeature(feature, (test) => {
  let driver;

  beforeEach(async () => {
    driver = await getWebdriver();
    await driver.get("hhttps://ahorcardo-agiles.netlify.app?palabra=test");
  });

  afterEach(async () => {
    if (driver) {
      await new Promise((r) => setTimeout(r, 2000));
      await driver.close();
    }
  });

  test("Guess a correct letter", ({ given, and, when, then }) => {
    given("I click login as anonimous", async () => {
      const button = await driver.wait(
        async () => {
          const element = await driver.findElement(By.css("#loginAnonBtn"));
          return (await element.isDisplayed()) ? element : null;
        },
        20000,
        "Login button is not interactable"
      );
      await button.click();
    });
  
    when("I select a difficulty", async () => {
      const select = await driver.wait(
        async () => {
          const element = await driver.findElement(By.css("#difSelector"));
          return (await element.isDisplayed()) ? element : null;
        },
        20000,
        "Difficulty selector is not interactable"
      );
      await select.click();
      const selectOpt = await driver.findElement(By.css("button"));
      await selectOpt.click();
      const okButton = await driver.findElement(By.css(".alert-button-role-cancel +button"));
      await okButton.click();
    });
  
    and("I click play", async () => {
      const button = await driver.wait(
        async () => {
          const element = await driver.findElement(By.css("#jugarBtn"));
          return (await element.isDisplayed()) ? element : null;
        },
        20000,
        "Play button is not interactable"
      );
      await button.click();
    });
  
    then("The game starts", async () => {
      await driver.wait(
        async () => {
          return driver
            .findElements(By.id("palabraTxt"))
            .then((found) => !!found.length);
        },
        20000,
        "Game did not start"
      );
    });
  
    when("I guess E as letter", async () => {
      const input = await driver.wait(
        async () => {
          const element = await driver.findElement(By.css("#inputLetra input"));
          return (await element.isDisplayed()) ? element : null;
        },
        20000,
        "Input field is not interactable"
      );
      await input.sendKeys("e");
      const button = await driver.findElement(By.css("#verificarBtn"));
      await button.click();
    });
  
    then("I see E in the word to guess", async () => {
      await driver.wait(
        async () => {
          return driver
            .findElement(By.css(`h1`))
            .then((found) => found.getText().then((text) => text.includes("e")));
        },
        20000,
        "Letter E is not visible in the word"
      );
      const button = await driver.findElement(By.css("#salirBtn"));
      await button.click();
    });
  });
});