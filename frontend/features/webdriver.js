const { Builder, By } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
//const url = process.env.VUE_APP_AT_URL;
//const getDriver = async () => await new Builder().forBrowser("chrome").build();
const url = 'http://localhost:8080/';

const getDriver = async () => {
  const options = new chrome.Options();
  options.addArguments("--headless");
  options.addArguments("--no-sandbox");
  options.addArguments("--disable-dev-shm-usage");
  options.addArguments("--disable-gpu");
  options.addArguments("--window-size=1920,1080");
  options.setChromeBinaryPath("/usr/bin/google-chrome"); 
  
  const service = new chrome.ServiceBuilder("/usr/bin/chromedriver");
  return await new Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .setChromeService(service)
    .build();
};

const getWebdriver = async () => {
  const driver = await getDriver();
  try {
    await driver.get(url);
  } catch (error) {
    console.error("Error accessing URL:", error);
    throw error;
  }
};
module.exports = { getWebdriver, By };
