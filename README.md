# 🔗 LinkAutoPostAI

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/gvatsal60/LinkAutoPostAI/master.svg)](https://results.pre-commit.ci/latest/github/gvatsal60/LinkAutoPostAI/HEAD)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/90a56eff45db425b98f356d5e7e710be)](https://app.codacy.com/gh/gvatsal60/LinkAutoPostAI/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=gvatsal60_LinkAutoPostAI&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=gvatsal60_LinkAutoPostAI)
[![CodeFactor](https://www.codefactor.io/repository/github/gvatsal60/linkautopostai/badge)](https://www.codefactor.io/repository/github/gvatsal60/linkautopostai)
![GitHub pull-requests](https://img.shields.io/github/issues-pr/gvatsal60/LinkAutoPostAI)
![GitHub Issues](https://img.shields.io/github/issues/gvatsal60/LinkAutoPostAI)
![GitHub forks](https://img.shields.io/github/forks/gvatsal60/LinkAutoPostAI)
![GitHub stars](https://img.shields.io/github/stars/gvatsal60/LinkAutoPostAI)

A Python automation project that generates LinkedIn post content with Google GenAI via LangChain and publishes it using the LinkedIn API.

## 🚀 Features

- AI-generated LinkedIn post content
- Automated publishing to LinkedIn
- Environment-variable based configuration
- Pre-configured for best practices (linting, formatting, CI)
- Example documentation and contribution guidelines

## 🛠️ Quick Start

1. **Clone the repository:**

   ```sh
   git clone https://github.com/gvatsal60/LinkAutoPostAI.git
   cd LinkAutoPostAI
   ```

2. **Set up your environment:**

   ```sh
   uv sync
   ```

3. **Create your environment file:**

   ```sh
   cp src/.env.dev src/.env
   ```

4. **Update `src/.env` with required values:**

   ```env
   MODEL_API_KEY=your_model_api_key
   MODEL_NAME=gemini-2.5-flash
   LINKEDIN_ACCESS_TOKEN=your_linkedin_access_token
   ```

5. **Run the app:**

   ```sh
   make run
   ```

## 📦 Project Structure

```tree
LinkAutoPostAI/
├── src/                  # Application source code
│   ├── app.py            # Main entrypoint
│   ├── linkedin.py       # LinkedIn API integration
│   ├── config.py         # Environment variable loading
│   └── .env.dev          # Environment variable template
├── snippets/             # Sample snippets/assets
├── README.md
├── Makefile
├── pyproject.toml
├── LICENSE
└── ...
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 🛡️ License

This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE) for details.
