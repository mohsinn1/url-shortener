# URL Shortening Service API

This is a RESTful API for a URL shortening service built using **FastAPI** and **MongoDB**. This project provides core functionalities to create, retrieve, update, and delete shortened URLs, while also tracking access statistics.

Project Idea from roadmap.sh: [URL Shortening Service](https://roadmap.sh/projects/url-shortening-service)

GitHub Repository: [mohsinn1/url-shortener-backend](https://github.com/mohsinn1/url-shortener-backend)

## Features

- **Shorten URL:** Convert a long URL into a random 6-character short code.
- **Retrieve URL:** Get the original URL information and increment its access count.
- **Update URL:** Update the target URL of an existing short code.
- **Delete URL:** Remove a short code from the database.
- **Statistics:** View detailed statistics, including creation time, last updated time, and the number of times the URL has been accessed.

## Tech Stack

- **Backend Framework:** FastAPI (Python)
- **Database:** MongoDB
- **Database Driver:** PyMongo

## Getting Started

### Prerequisites

- Python 3.7+
- MongoDB instance (Atlas or local)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohsinn1/url-shortener-backend.git
   cd url-shortener-backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install the dependencies:**
   Make sure you have the following packages installed:
   ```bash
   pip install fastapi uvicorn pymongo certifi pydantic python-dotenv
   ```


4. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your MongoDB URI:
   ```env
   MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/
   ```

5. **Run the Application:**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`. You can also visit `http://127.0.0.1:8000/docs` to explore the interactive API documentation provided automatically by FastAPI (Swagger UI).

## API Endpoints

### 1. Create Short URL
- **Endpoint:** `POST /shorten`
- **Body:**
  ```json
  {
    "url": "https://www.example.com"
  }
  ```
- **Response (201 Created):**
  ```json
  {
    "url": "https://www.example.com",
    "shortCode": "abc123",
    "createdAt": "2024-05-01T10:00:00Z",
    "updatedAt": "2024-05-01T10:00:00Z",
    "accessCount": 0,
    "id": "60a7c4f1..."
  }
  ```

### 2. Retrieve URL
- **Endpoint:** `GET /shorten/{shortCode}`
- **Description:** Retrieves the URL record and increments the `accessCount` by 1.
- **Response (200 OK):**
  ```json
  {
    "url": "https://www.example.com",
    "shortCode": "abc123",
    "createdAt": "...",
    "updatedAt": "...",
    "accessCount": 1,
    "id": "..."
  }
  ```

### 3. Update URL
- **Endpoint:** `PUT /shorten/{shortCode}`
- **Body:**
  ```json
  {
    "url": "https://www.new-example.com"
  }
  ```
- **Response (200 OK):**
  ```json
  {
    "url": "https://www.new-example.com",
    "shortCode": "abc123",
    "createdAt": "...",
    "updatedAt": "...",
    "accessCount": 1,
    "id": "..."
  }
  ```

### 4. Delete URL
- **Endpoint:** `DELETE /shorten/{shortCode}`
- **Description:** Deletes the specific short code and its target URL from the database.
- **Response (204 No Content):** `No Content`

### 5. Get URL Stats
- **Endpoint:** `GET /shorten/{shortCode}/stats`
- **Description:** Returns the URL information and stats without incrementing the access count.
- **Response (200 OK):**
  ```json
  {
    "url": "https://www.new-example.com",
    "shortCode": "abc123",
    "createdAt": "...",
    "updatedAt": "...",
    "accessCount": 1,
    "id": "..."
  }
  ```
