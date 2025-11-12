# Metoffice_Climate_Dashboard

A modern Django application that ingests, stores, exposes, and visualizes UK MetOffice open climate datasets. This project demonstrates end-to-end skills in backend API development, data parsing, RESTful service design, and frontend data visualization.

---

## Features

- **Automated data ingestion:** Parses MetOffice published datasets (e.g. historic monthly Tmax series).
- **Database-backed storage:** Efficiently stores weather/climate metrics.
- **RESTful API:** Dynamic filtering for region, parameter, and date range (`/api/weather/`).
- **Interactive dashboard:** Visual analytics for UK temperature trends via HTML, CSS, Chart.js.
- **Cloud-ready:** Easily deployable on Render, Heroku, Railway; supports Docker.
- **Responsive design:** Usable on desktop and mobile.

---

## Live Demo

*(Add your Render deployment link here once live)*

---

## Data Source

Official UK MetOffice time-series data:  
[UK & Regional Series](https://www.metoffice.gov.uk/research/climate/maps-and-data/uk-and-regional-series#yearOr)  
Primary dataset:  
[UK Monthly Max Temps](https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt)

---

## Tech Stack

- Python 3.9 + Django 4.x
- Django REST Framework
- HTML/CSS/JS (Chart.js for data visualization)
- SQLite (local dev) / PostgreSQL (production)
- Render/Heroku for deployment

---

## Quickstart (Local)

1. **Clone repo**
    ```
    git clone https://github.com/yourusername/Metoffice_Climate_Dashboard.git
    cd Metoffice_Climate_Dashboard
    ```

2. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```

3. **Apply migrations / ingest data**
    ```
    python manage.py migrate
    python manage.py fetch_weather
    ```

4. **Run server**
    ```
    python manage.py runserver
    # Visit http://localhost:8000/dashboard/
    ```

---

## Deployment (Render Example)

1. Push repo to GitHub.
2. Create a Render "Web Service", select your repo.
3. Add env vars: `DJANGO_SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=*`
4. Build command:  
   `pip install -r requirements.txt && python manage.py collectstatic --noinput`
5. Start command:  
   `gunicorn farmsetu_weather.wsgi:application`
6. (Optional) Add Render PostgreSQL; update `settings.py`.
7. Use Shell tab to run initial migrations and data fetch:
    ```
    python manage.py migrate
    python manage.py fetch_weather
    ```

---

## API Usage

- `/api/weather/?region=UK&parameter=Tmax&start_date=2020-01-01`
- `/api/weather/regions/` — returns available regions
- `/api/weather/parameters/` — returns available parameters

---

## Screenshots

*(Include dashboard images to highlight data visualization)*

---

## License & Attribution

- For educational and research use.
- Weather data © UK MetOffice (open data license).
- Project by Gaurav Khandelwal.

---

*Questions or feedback? Contact via gauravkhandelwal327@gmail.com.*
