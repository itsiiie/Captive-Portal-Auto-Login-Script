# Captive Portal Auto-Login Script

Automate your login process to a captive portal using Selenium WebDriver!

## 📋 Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver

## 🚀 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/captive-portal-login.git
    cd captive-portal-login
    ```

2. **Install required Python packages**:
    ```bash
    pip install selenium
    ```

3. **Download ChromeDriver**:
    - Download the version of ChromeDriver that matches your installed version of Google Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Place the `chromedriver` executable in a directory included in your system's PATH, or specify its location in the script.

## ⚙️ Usage

1. **Edit the script**:
    - Open the `login.py` script and update the `USERNAME` and `PASSWORD` variables with your login credentials.
    - Update the URL in the `driver.get()` function to match your captive portal login page URL.

2. **Run the script**:
    ```bash
    python login.py
    ```

## 📌 Notes

- Ensure that the URL provided in the script (`driver.get()`) is correct and accessible.
- Modify the WebDriver wait conditions and element locators as per your specific login page requirements.

## 🛡 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Made with ❤️ by [Your Name](https://github.com/yourusername)
