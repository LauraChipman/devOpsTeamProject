**Flask Weather Application**
=============================

**Project Overview**
--------------------

This project is a **Flask-based Weather Application** that retrieves and displays real-time weather data for any city using the OpenWeatherMap API. It is designed to be simple, interactive, and demonstrate key DevOps concepts, such as CI/CD pipeline implementation and deployment to AWS EC2.

* * * * *

**Table of Contents**
---------------------

1.  [Project Purpose](#project-purpose)
2.  [Features](#features)
3.  [Technologies Used](#technologies-used)
4.  [Repository Organization](#repository-organization)
5.  [Setup Instructions](#setup-instructions)
6.  [Usage](#usage)
7.  [CI/CD Pipeline](#cicd-pipeline)
8.  [Deployment](#deployment)


* * * * *

**Project Purpose**
-------------------

The purpose of this project is to:

-   Provide users with real-time weather updates in a user-friendly interface.
-   Demonstrate practical implementation of DevOps concepts, including:
    -   Version control using GitHub.
    -   CI/CD pipelines with GitHub Actions.
    -   Deployment of a Flask application to AWS EC2.

* * * * *

**Features**
------------

-   Search for any city to view its weather conditions.
-   Displays:
    -   Temperature (in Celsius).
    -   Humidity percentage.
    -   Wind speed.
    -   Weather description and icon.
-   Dynamic background updates for a visually engaging experience.

* * * * *

**Technologies Used**
---------------------

-   **Backend**: Flask (Python)
-   **Frontend**: HTML, CSS, JavaScript
-   **Weather API**: [OpenWeatherMap API](https://openweathermap.org/)
-   **DevOps Tools**:
    -   GitHub for version control.
    -   GitHub Actions for CI/CD pipeline.
    -   AWS EC2 for application deployment.
-   **Virtual Environment**: Python venv

* * * * *

**Repository Organization**
---------------------------

The repository is structured as follows:


weather-app/

├── .github/workflows/     # GitHub Actions CI/CD pipeline configuration

│   └── ci-cd-pipeline.yml # Pipeline script

├── app.py                 # Main Flask application

├── templates/             # HTML templates (frontend UI)

│   └── index.html

├── static/                # Static assets

│   ├── style.css          # Stylesheet

│   └── script.js          # JavaScript logic for interactivity

├── requirements.txt       # Project dependencies

├── README.md              # Documentation (you are here!)

└── .gitignore             # Ignored files (e.g., .venv)

* * * * *

**Setup Instructions**
----------------------

### 1\. **Clone the Repository**


`git clone https://github.com/your-username/weather-app.git
cd weather-app`

### 2\. **Set Up the Virtual Environment**

If a `.venv` folder doesn't already exist:

bash

Copy code

`python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
.venv\Scripts\activate     # For Windows`

### 3\. **Install Dependencies**



`pip install -r requirements.txt`

### 4\. **Add Your API Key**

-   Replace the placeholder API key in `app.py`:


    `API_KEY = "your_openweathermap_api_key"`

### 5\. **Run the Application**


`python app.py`

-   Visit `http://127.0.0.1:5000` in your browser.

* * * * *

**Usage**
---------

1.  Enter the name of a city in the search bar.
2.  Press the search button to fetch weather details.
3.  View:
    -   Temperature
    -   Humidity
    -   Wind speed
    -   Weather description and icon.

* * * * *

**CI/CD Pipeline**
------------------

-   **Build**: The application dependencies are installed and validated.
-   **Test**: Basic automated tests ensure functionality.
-   **Deploy**: On success, the application is deployed to the configured AWS EC2 instance.

The pipeline is configured using GitHub Actions and is located in `.github/workflows/ci-cd-pipeline.yml`.

* * * * *

**Deployment**
--------------

The application is deployed to an **AWS EC2 instance**:

-   Flask serves the backend.
-   Nginx (or Gunicorn) acts as the web server for deployment.
-   Automated deployment using SSH from GitHub Actions.

* * * * *


**Future Enhancements**
-----------------------

-   Add user authentication to save favorite cities.
-   Integrate a 7-day forecast feature.
-   Improve UI with additional animations and themes.

* * * * *

**Contributors**
----------------

-   **Laura Chipman**: Initial App and Repository Organization
-   **Liam Bone**: CI/CD Pipeline
-   **William Webster**: EC2 Deployment


* * * * *

**License**
-----------

This project is licensed under the MIT License.
