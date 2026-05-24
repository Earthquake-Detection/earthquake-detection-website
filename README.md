# SeismoAI — Earthquake Detection Website

A full-stack earthquake detection and early warning prototype with live seismic data ingestion, AI prediction, visualization, and alerting.

## Project Overview

`SeismoAI` is a proof-of-concept web application designed to collect realtime seismic readings from ESP32 sensor devices, store them in MongoDB, predict earthquake severity with an AI model, and display live dashboards in a React frontend.

## Key Features

- Live sensor data ingestion via `POST /api/ingest`
- Batch sensor upload support via `POST /api/ingest/batch`
- Live readings and event history endpoints
- AI prediction support via `POST /api/predict`
- WebSocket feed at `/ws` for realtime updates
- Telegram alert integration for critical events
- Responsive React dashboard and mapping UI

## Tech Stack

- Backend: Node.js, Express, MongoDB, Mongoose
- Frontend: React, React Scripts, Recharts
- AI/ML: Python, Flask, TensorFlow, pandas, joblib
- Real-time: WebSocket (`ws`)
- Alerts: Telegram Bot API

## 📁 Repository Structure

- `backend/`
  - `server.js` — Express API server
  - `config/db.js` — MongoDB connection
  - `routes/` — API route handlers
  - `services/` — WebSocket and Telegram support
  - `middleware/` — logging and error handling
  - `ai/` — Python model server and TensorFlow model
- `frontend/`
  - `src/` — React app source files
  - `public/` — static HTML and assets
- `requirements.txt` — Python dependencies for AI model service

## ⚙️ Setup Instructions

### 1. Clone repository

```bash
git clone https://github.com/<your-username>/earthquake-detection-website.git
cd earthquake-detection-website
```

### 2. Backend setup

```bash
cd backend
npm install
```

Create a `.env` file in `backend/` with values like:

```env
PORT=5000
MONGO_URI=mongodb://localhost:27017/seismoai
FRONTEND_URL=http://localhost:3000
TELEGRAM_TOKEN=<your-telegram-bot-token>
TELEGRAM_CHAT_ID=<your-chat-id>
```

Start the backend:

```bash
npm run dev
```

or for production:

```bash
npm start
```

### 3. Frontend setup

```bash
cd ../frontend
npm install
npm start
```

The React app should open at `http://localhost:3000`.

### 4. AI model service (optional)

The AI model service is implemented in `backend/ai/app.py`.

```bash
cd backend/ai
python -m venv venv
venv\Scripts\activate
pip install -r ../../requirements.txt
python app.py
```

> If you do not need the separate Python model server, the backend may already provide prediction logic through its existing routes.

## API Endpoints

- `GET /health` — health check
- `GET /api` — API index
- `POST /api/ingest` — single sensor reading
- `POST /api/ingest/batch` — batch sensor readings
- `GET /api/sensor/latest` — latest sensor readings
- `GET /api/events/recent` — recent seismic events
- `POST /api/predict` — request earthquake prediction
- `GET /ws` — WebSocket realtime feed

## Notes

- The backend includes rate limiting tuned for high-frequency sensor ingestion.
- Frontend visualization components are under `frontend/src/components/`.
- AI model and scaler files are stored in `backend/ai/`.

## Contributing

Feel free to open issues, submit pull requests, or extend this project with more advanced analytics, notifications, and mapping capabilities.

## License

Specify your license here, or add one if needed.
