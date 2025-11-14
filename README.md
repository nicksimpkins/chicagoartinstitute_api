# Art Institute of Chicago API Browser

A Django web application that allows users to search and explore artworks from the Art Institute of Chicago's public API.

## Features

- 🔍 **Search artworks** by title, artist, or keywords
- 🎨 **Browse artwork collection** with image thumbnails
- 📱 **Detailed artwork views** with full metadata
- ⚡ **Real-time search** with debouncing
- 🖼️ **High-quality images** via IIIF image service

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nicksimpkins/chicagoartinstitute_api
cd chicagoartinstitute_api
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django djangorestframework django-cors-headers requests
```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

### 6. Access the Application

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

## Usage

1. **Search for Artworks**: Type in the search box on the homepage to find artworks by title, artist, or keywords
2. **Browse Results**: View artwork thumbnails with basic information in a grid layout
3. **View Details**: Click on any artwork to see detailed information including:
   - High-resolution image
   - Artist information
   - Date created
   - Medium/materials
   - Dimensions
   - Credit line
   - Department
   - Description (when available)

## Project Structure

```
chicagoartinstitute_api/
├── art_project/              # Main project directory
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI configuration
├── artworks/                 # Main application
│   ├── templates/           # HTML templates
│   │   ├── base.html       # Base template
│   │   ├── home.html       # Search/browse page
│   │   └── detail.html     # Artwork detail page
│   ├── services.py          # API integration logic
│   ├── views.py             # View functions
│   └── urls.py              # App URL configuration
├── manage.py                 # Django management script
└── db.sqlite3               # SQLite database (generated)
```

## API Integration

This project uses the [Art Institute of Chicago API](https://api.artic.edu/docs/), which provides:
- **No authentication required** - completely open API
- **Comprehensive artwork data** - over 120,000 artworks
- **High-resolution images** via IIIF standard
- **Rich metadata** including artist info, dates, departments, and more

### Key Endpoints Used

- `GET /api/v1/artworks/search` - Search for artworks
- `GET /api/v1/artworks/{id}` - Get specific artwork details

## Technology Stack

- **Backend**: Django 5.2.8
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **API Client**: Python Requests library
- **Additional Packages**:
  - Django REST Framework (API views)
  - django-cors-headers (CORS support)