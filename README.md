# Cookie Clicker Bot 🍪🤖

This Python script uses **Selenium** to automate playing the **Cookie Clicker** game on the [Cookie Clicker Experiment](http://orteil.dashnet.org/experiments/cookie/). The bot repeatedly clicks the cookie for 5 minutes and purchases upgrades when it has enough money. It prioritizes purchasing the most expensive upgrade that can be afforded.

## Requirements 📦

- **Python 3.x**
- **Selenium** library
- **ChromeDriver** for Chrome browser (ensure it is installed and in your PATH)

## Installation 🛠️

1. **Install Selenium**:  
   Use pip to install the Selenium library:
   ```bash
   pip install selenium

## Usage 🚀

1. **Run the script**:  
   Simply run the Python script:
   ```bash
   python cookie_clicker_bot.py

   This will:
   - Open the game in Chrome.
   - Click the cookie endlessly for 5 minutes.
   - Track the in-game money and purchase the most expensive affordable upgrade.

2. **The bot's behavior**:
   - It starts by endlessly clicking the cookie.
   - Every second, it checks the amount of money available and attempts to purchase the most expensive upgrade it can afford.
   - The process runs for 5 minutes and then stops automatically.


