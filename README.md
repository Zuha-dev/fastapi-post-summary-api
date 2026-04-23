# Post Summary API

## Overview

A FastAPI backend project that fetches post data from an external API, filters it based on user input, and returns structured analytical summaries.

This project demonstrates backend development fundamentals including API design, data filtering pipelines, and basic analytics.

---

## Features

- Fetches posts from an external API
- Filters posts using:
  - user_id (required)
  - keyword (optional)
  - minimum length (optional)
- Computes analytics:
  - total posts
  - average post length
  - longest post
- Returns structured JSON response
- Clean separation of data fetching, processing, and API layers

---

## How It Works

Client → FastAPI → Data Layer → Processing Layer → Response

1. API receives request with parameters
2. Data layer fetches raw posts
3. Processing layer filters and analyzes data
4. API returns structured JSON response

---

## API Endpoint

GET /users/summary/{user_id}

---

## Query Parameters

- user_id (required): ID of the user
- keyword (optional): filter posts containing a specific word
- min_length (optional): filter posts by minimum body length

---

## Example Request

/users/summary/1?keyword=qui&min_length=100

---

## Example Response

{
  "user_id": 1,
  "total_posts": 10,
  "average_length": 145.32,
  "longest_post": {
    "id": 69,
    "length": 250
  }
}

---

## Project Structure

- api.py → FastAPI routes and endpoints
- data_layer.py → Fetches external API data
- processing.py → Filtering and analytics logic

---

## Design Decisions

- Separation of concerns (API / logic / data)
- Required vs optional parameter handling
- Early filtering pipeline (user → keyword → length)
- Early return for empty results
- Clean and minimal JSON response structure

---

## Key Concepts Learned

- FastAPI basics
- REST API design
- Query parameter handling
- Data filtering pipelines
- Functional decomposition
- Backend architecture fundamentals

---

## Future Improvements

- Add database (SQLite/PostgreSQL)
- Add authentication (JWT)
- Add pagination
- Improve schema validation using Pydantic models
- Deploy API (Render / Railway / AWS)

---

## Tech Stack

- Python
- FastAPI
- Requests
- Regex

---

## Run Locally

pip install -r requirements.txt
uvicorn api:app --reload

Then open:
http://127.0.0.1:8000/docs

---

## Author

Zuha