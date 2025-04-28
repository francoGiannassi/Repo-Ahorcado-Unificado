const { Builder, By } = require("selenium-webdriver");
const url = process.env.VUE_APP_AT_URL;
//const url = 'http://localhost:8080/';

const getDriver = async () => {
  const chrome = require("selenium-webdriver/chrome");
  const options = new chrome.Options();
  options.addArguments("--headless");
  options.addArguments("--no-sandbox");
  options.addArguments("--disable-dev-shm-usage");
  options.addArguments("--disable-gpu");
  options.addArguments("--window-size=1920,1080");
  
  const service = new chrome.ServiceBuilder("/usr/local/bin/chromedriver");
  return await new Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .setChromeService(service)
    .build();
};

const getWebdriver = async () => {
  const driver = await getDriver();
  await driver.get(url);
  return driver;
};
module.exports = { getWebdriver, By };
