const { Builder, By } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
//const url = 'http://localhost:8080/';

const getWebdriver = async () => {
  const options = new chrome.Options();
  options.addArguments("--headless");
  options.addArguments("--no-sandbox");
  options.addArguments("--disable-dev-shm-usage");
  options.addArguments("--disable-gpu");
  options.addArguments("--window-size=1920,1080");

  return await new Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .build();
};

module.exports = { getWebdriver, By };
