# API Reference: ReadmeStudio Backend

## Endpoints

### `GET /`
- **Description:** Main editor UI (HTML)

### `POST /preview`
- **Description:** Render markdown preview
- **Body:** `markdown_text` (str)
- **Returns:** HTML preview

### `POST /upload`
- **Description:** Upload a markdown file and render preview
- **Body:** `file` (UploadFile)
- **Returns:** HTML preview

### `POST /export/md`
- **Description:** Export markdown as .md file
- **Body:** `markdown_text` (str)
- **Returns:** Markdown file

### `POST /export/html`
- **Description:** Export markdown as HTML file
- **Body:** `markdown_text` (str)
- **Returns:** HTML file

### `POST /export/pdf`
- **Description:** Export markdown as PDF file
- **Body:** `markdown_text` (str)
- **Returns:** PDF file 