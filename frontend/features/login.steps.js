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
      await driver.quit();
    }
  });

  test("Login successful", ({ given, and, when, then }) => {
    given("I set franco as username", async () => {
      //try {
        await driver.wait(async () => {
          return driver
            .findElements(By.id("username"))
            .then((found) => !!found.length);
        }, 10000);
        const input = await driver.findElement(By.css("#username input"));
        await input.sendKeys("franco");
      //} catch (error) {
      //  console.error("I set franco as username", error);
      //}
    });

    and("12345 as password", async () => {
      //try {
        const input = await driver.findElement(By.css("#password input"));
        await input.sendKeys("12345");
      //} catch (error) {
      //  console.error("12345 as password", error);
      //}
    });

    when("I click login", async () => {
      //try {
        const button = await driver.findElement(By.css("#loginBtn"));
        await button.click();
      //} catch (error) {
      //  console.error("I click login", error);
      //}
    });

    then("I should see Difficulty Selection Page", async () => {
      //try {
        await driver.wait(async () => {
          return driver
            .findElements(By.id("difSelector"))
            .then((found) => !!found.length);
        }, 10000);
      //} catch (error) {
      //  console.error("I should see Difficulty Selection Page", error);
      //}
    });
  });
});