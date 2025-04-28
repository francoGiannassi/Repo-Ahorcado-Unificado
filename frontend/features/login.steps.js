import { defineFeature, loadFeature } from "jest-cucumber";
const feature = loadFeature("./features/login.feature");
const { getWebdriver, By } = require("./webdriver");

jest.setTimeout(30000);

defineFeature(feature, (test) => {
  let driver;

  beforeEach(async () => {
    driver = await getWebdriver();
    await driver.get("https://localhost:8080/");
  });

  afterEach(async () => {
    if (driver) {
      await new Promise((r) => setTimeout(r, 2000));
      await driver.close();
    }
  });

  test("Login successful", ({ given, and, when, then }) => {
    given("I set franco as username", async () => {
        await driver.wait(async () => {
          return driver
            .findElements(By.id("username"))
            .then((found) => !!found.length);
        }, 10000);
        const input = await driver.findElement(By.css("#username input"));
        await input.sendKeys("franco");
    });

    and("12345 as password", async () => {
        const input = await driver.findElement(By.css("#password input"));
        await input.sendKeys("12345");
    });

    when("I click login", async () => {
        const button = await driver.findElement(By.css("#loginBtn"));
        await button.click();
    });

    then("I should see Difficulty Selection Page", async () => {
        await driver.wait(async () => {
          return driver
            .findElements(By.id("difSelector"))
            .then((found) => !!found.length);
        }, 10000);
    });
  });

  test("Login unsuccessful", ({ given, and, when, then }) => {
    given("I set franco as username", async () => {
      await driver.wait(async () => {
        return driver
          .findElements(By.id("username"))
          .then((found) => !!found.length);
      }, 10000);
      const input = await driver.findElement(By.css("#username input"));
      await input.sendKeys("franco");
    });

    and("asdasdasd123123123 as password", async () => {
      const input = await driver.findElement(By.css("#password input"));
      await input.sendKeys("asdasdasd123123123");
    });

    when("I click login", async () => {
      const button = await driver.findElement(By.css("#loginBtn"));
      await button.click();
    });
    
    then("I should see a message Invalid username or password", async () => {
      await driver.wait(async () => {
        return driver
          .findElements(By.id("loginError"))
          .then((found) => !!found.length);
      }, 5000);
    });
  });
});