# Backend

The UrjaSahayak AI backend is built with FastAPI.

## Setup

From the project root folder:

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpoints

| Endpoint | Description |
|---|---|
| `/` | API health/status response |
| `/api/suppliers` | Returns crude-oil supplier sample data |
| `/api/routes` | Returns shipping route sample data |
| `/api/events` | Returns simulated geopolitical risk events |

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

FastAPI will display interactive API documentation.
