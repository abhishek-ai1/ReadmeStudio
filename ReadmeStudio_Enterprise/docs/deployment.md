# Deployment Guide: ReadmeStudio

## Local Development

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `cd ReadmeStudio/backend && uvicorn main:app --reload`

## Docker

1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```
2. The app will be available at `http://localhost:8000`

## Cloud Deployment

- Use services like Heroku, AWS Elastic Beanstalk, Azure App Service, or DigitalOcean App Platform.
- Set environment variables as needed (see `.env.example`).
- For static files, ensure the `static/` and `uploads/` directories are writable.
- Use a production server (e.g., Gunicorn with Uvicorn workers) for deployment.

## Environment Variables

- See `.env.example` for required and optional variables. 