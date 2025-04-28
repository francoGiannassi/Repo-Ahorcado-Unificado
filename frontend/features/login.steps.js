import { defineFeature, loadFeature } from "jest-cucumber";
const feature = loadFeature("./features/login.feature");
const { getWebdriver, By } = require("./webdriver");
jest.setTimeout(10000);

defineFeature(feature, async (test) => {
  test("Login successful", ({ given, when, then }) => {
    const driver = getWebdriver();
    given("I set franco as username", async () => {
      await driver.wait(function () {
        return driver
          .findElements(By.id("username"))
          .then((found) => !!found.length);
      }, 5000);
      const input = await driver.findElement(By.css("#username input"));
      input.sendKeys("franco");
    });
    given("12345 as password", async () => {
      const input = await driver.findElement(By.css("#password input"));
      input.sendKeys("12345");
    });
    when("I click login", async () => {
      const button = await driver.findElement(By.css("#loginBtn"));
      button.click();
    });
    then("I should see Difficulty Selection Page", async () => {
      await driver.wait(function () {
        return driver
          .findElements(By.id("difSelector"))
          .then((found) => !!found.length);
      }, 5000);
      await new Promise((r) => setTimeout(r, 2000));
      await driver.close();
    });
  });

  test("Login unsuccessful", async ({ given, when, then }) => {
    const driver = await getWebdriver();
    given("I set franco as username", async () => {
      await driver.wait(function () {
        return driver
          .findElements(By.id("username"))
          .then((found) => !!found.length);
      }, 5000);
      const input = await driver.findElement(By.css("#username input"));
      input.sendKeys("franco");
    });
    given("asdasdasd123123123 as password", async () => {
      const input = await driver.findElement(By.css("#password input"));
      input.sendKeys("asdasdasd123123123");
    });
    when("I click login", async () => {
      const button = await driver.findElement(By.css("#loginBtn"));
      button.click();
    });
    then("I should see a message Invalid username or password", async () => {
      await driver.wait(function () {
        return driver
          .findElements(By.id("loginError"))
          .then((found) => !!found.length);
      }, 5000);
      await new Promise((r) => setTimeout(r, 2000));
      await driver.close();
    });
  });
});
