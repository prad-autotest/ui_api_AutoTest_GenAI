# 🔍 QA Automation Framework — Python + Playwright + API + MySQL

This is a scalable and reusable **end-to-end automation framework** designed for testing web, API, and database layers with **CI/CD** using GitHub Actions and **Allure reporting**.

> ✅ Application Under Test: [Automation Exercise](https://www.automationexercise.com)

---

## 📦 Tech Stack

| Layer         | Tech                                   |
|---------------|----------------------------------------|
| Web UI        | [Playwright (Python)](https://playwright.dev/python/) |
| API           | [Requests](https://docs.python-requests.org/) |
| Database      | MySQL (via `mysql-connector-python`)   |
| Test Runner   | [Pytest](https://docs.pytest.org/)     |
| Reports       | [Allure](https://docs.qameta.io/allure/) |
| CI/CD         | [GitHub Actions](https://github.com/features/actions) |
| Logs          | Built-in logging with custom formatter |
| Config        | `config.yaml` (per environment)        |

---

## 📁 Folder Structure

```bash
.
├── config/
│   └── config.yaml            # Environment configs (e.g. base URL)
├── data/
│   └── test_data.json         # Input test data
├── pages/
│   └── base_page.py           # Common Playwright methods
│   └── login_page.py          # Login/Signup POM
│   └── products_page.py       # Products POM
│   └── ...
├── tests/
│   ├── web/                   # UI Tests
│   ├── api/                   # API Tests
│   ├── db/                    # DB Validation Tests
│   └── ...
├── utils/
│   ├── db_utils.py            # DB query/connection helper
│   ├── logger.py              # Central logging config
│   └── common.py              # Generic utilities
├── .github/
│   └── workflows/
│       └── pr-test.yml        # GitHub Actions for PR testing
├── requirements.txt
├── README.md
└── pytest.ini                 # Pytest config
