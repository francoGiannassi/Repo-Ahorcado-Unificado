import { defineFeature, loadFeature } from "jest-cucumber";
const feature = loadFeature("./features/login.feature");
const { getWebdriver, By } = require("./webdriver");

jest.setTimeout(30000); // Aumenta el tiempo de espera global

defineFeature(feature, (test) => {
  let driver;

  beforeEach(async () => {
    driver = await getWebdriver();
    await driver.get("http://localhost:8080");
  });

  afterEach(async () => {
    if (driver) {
      try {
        const pageSource = await driver.getPageSource();
        require("fs").writeFileSync("pageSource.html", pageSource);
      } catch (e) {
        console.error("Error capturing page source:", e);
      }
      await driver.quit();
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
});