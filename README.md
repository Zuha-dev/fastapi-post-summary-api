# Post Summary API

## Overview

A backend API built with FastAPI that fetches post data from an external source, applies conditional filtering, and returns summarized insights.

This project demonstrates structured backend design, data processing, and API development.

---

## Features

- Fetches data from an external API  
- Filters posts based on:
  - keyword (optional)
  - minimum length (optional)  
- Computes:
  - total results
  - average post length
  - longest post  
- Exposes a REST API endpoint  

---

## How It Works

Client → FastAPI → Data Layer → Processing Layer → Response  

1. FastAPI receives query parameters  
2. `data_layer.py` fetches raw post data  
3. `processing.py` filters and analyzes the data  
4. API returns structured JSON response  

---

## API Endpoint

`GET /posts/summary`

---

## Query Parameters

- `keyword` (optional): filters posts containing the word  
- `min_length` (optional): filters posts by minimum body length  

---

## Example Request

```
/posts/summary?keyword=qui&min_length=100
```

---

## Example Response

```json
{
  "status": "success",
  "data": {
    "total_results": 48,
    "average_length": 165.45,
    "longest_post": {
      "id": 69,
      "userId": 7,
      "title": "example",
      "body": "..."
    }
  }
}
```

---

## Project Structure

- `data_layer.py` → handles data fetching  
- `processing.py` → filtering and summarization logic  
- `api.py` → API layer  

---

## Design Decisions

- Separation of concerns (data / logic / API)  
- Optional query parameters for flexible filtering  
- AND logic used when multiple filters are provided  
- Clean JSON response structure  

---

## Future Improvements

- Add database (SQLite/PostgreSQL)  
- Add user-based analytics  
- Implement authentication  
- Add pagination  

---

## Tech Stack

- Python  
- FastAPI  
- Requests  

---

## Run Locally

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

Open:
```
http://127.0.0.1:8000/docs
```

---

## Author

Zuha