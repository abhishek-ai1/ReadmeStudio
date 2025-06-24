# ReadmeStudio

[![CI](https://github.com/abhishek-ai1/ReadmeStudio/actions/workflows/ci.yml/badge.svg)](https://github.com/abhishek-ai1/ReadmeStudio/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A modern, block-based Markdown editor inspired by [readme.so](https://readme.so), built with FastAPI, Jinja2, and modern JavaScript/CSS.  
**Create, preview, and export beautiful README files with ease.**

---

## 🚀 Features

- Block-based markdown editing (add, remove, reorder, collapse)
- Live GitHub-style markdown preview
- Emoji support
- Sidebar block template search and quick add
- Markdown file upload, preview, and PDF/HTML/Markdown export
- Pixel-perfect, responsive UI (dark mode included)
- Block-specific settings (Badges, Author, License, Socials, etc.)
- Modern, enterprise-ready codebase and structure

---

## 📂 Project Structure

```
your-project-root/
├── .github/                # GitHub workflows, issue templates
├── docs/                   # Documentation
├── ReadmeStudio/           # Main app package
│   └── backend/
│       ├── main.py
│       ├── static/
│       ├── templates/
│       ├── uploads/
│       └── ...
├── tests/                  # Test scripts
├── .env.example            # Example environment variables
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
├── LICENSE
└── CHANGELOG.md
```

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+
- Node.js (for advanced frontend development, optional)
- Docker (optional, for containerized deployment)

### Installation

```bash
# Clone the repository
git clone https://github.com/abhishek-ai1/ReadmeStudio.git
cd ReadmeStudio

# (Recommended) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Copy and edit environment variables
cp .env.example .env
```

### Running the App

```bash
cd ReadmeStudio/backend
uvicorn main:app --reload
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 🐳 Docker

```bash
docker-compose up --build
```

---

## 📄 Documentation

- [API Reference](docs/api.md)
- [Deployment Guide](docs/deployment.md)
- [Contributing](docs/contributing.md)

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](docs/contributing.md) for guidelines.

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [readme.so](https://readme.so) for inspiration
- [FastAPI](https://fastapi.tiangolo.com/)
- [Jinja2](https://jinja.palletsprojects.com/)
- [Marked.js](https://marked.js.org/) 