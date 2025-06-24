# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-06-24

### Added

- **Block-based Markdown Editor:**  
  - Add, remove, reorder, and collapse blocks for modular README creation.
  - Sidebar with searchable block templates and click-to-add functionality.
  - Block-specific settings (Badges, Author, License, Socials, etc.).
  - Emoji support in blocks and section headers.

- **Live GitHub-style Markdown Preview:**  
  - Real-time preview pane styled to match GitHub markdown rendering.
  - GitHub-flavored markdown support (tables, checklists, code, etc.).

- **Export & Import Features:**  
  - Export README as Markdown (`.md`), HTML, or PDF (with styled output).
  - Upload and parse existing markdown files for editing.

- **Modern, Responsive UI:**  
  - Pixel-perfect, professional design inspired by readme.so.
  - Fully responsive layout with dark mode support.
  - Sidebar with smooth fold/unfold animation and improved visual appeal.
  - Consistent, accessible header with all actions visible on all screen sizes.

- **Project Structure & Documentation:**  
  - Enterprise-level folder structure for easy GitHub publishing.
  - Clean, project-specific `README.md`, `.gitignore`, `LICENSE`, and `CHANGELOG.md`.
  - Professional documentation: API reference, deployment guide, and contributing guide.
  - Code of Conduct for open source collaboration.

- **Robust Backend:**  
  - FastAPI backend with Jinja2 templates.
  - Absolute path handling for static and template directories.
  - Secure file upload and PDF export logic.
  - CORS enabled for local development.

- **Clean-up & Refactoring:**  
  - Removed all unrelated files and references from other projects (e.g., VaultView).
  - Replaced all placeholder URLs with the actual GitHub repository link.
  - Ensured all documentation and code is specific to ReadmeStudio. 