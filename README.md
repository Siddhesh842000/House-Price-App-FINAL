# 🏠 House Price Prediction App

**Production-ready Machine Learning web application with classic gray UI**

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A professional Flask web application that predicts house prices using Machine Learning. Features a clean, corporate gray UI and is ready for deployment on Render, Docker, and local environments.

## ✨ Features

- 🎨 **Classic Gray UI** - Professional corporate design
- 🤖 **Smart ML** - Auto-selects best model (Linear/Tree/Forest)
- 🚀 **Production Ready** - Configured for Render deployment
- 🐳 **Docker Support** - Full containerization
- 📱 **Responsive** - Works on all devices
- ⚡ **Fast** - Optimized for performance

## 📁 Project Structure

```
house-price-prediction/
├── app.py                  # Flask application
├── train_model.py          # ML model training
├── requirements.txt        # Dependencies
├── Dockerfile              # Docker config
├── docker-compose.yml      # Docker Compose
├── Procfile               # Render config
├── render.yaml            # Render blueprint
├── .gitignore             # Git ignore
├── templates/
│   ├── index.html         # Input form
│   └── result.html        # Results page
└── static/
    └── style.css          # Gray UI theme
```

## 🚀 Quick Start

### Local Setup

```bash
# 1. Clone/extract project
cd house-price-prediction

# 2. Create virtual environment
python -m venv venv

# 3. Activate
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Train model
python train_model.py

# 6. Run app
python app.py
```

Open: http://127.0.0.1:5000

### Docker

```bash
# Using Docker Compose
docker-compose up

# Or build manually
docker build -t house-price-app .
docker run -p 5000:5000 house-price-app
```

## 🌐 Deploy on Render

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/house-price-prediction.git
git push -u origin main
```

### Step 2: Deploy

1. Go to [render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Build Command:** `pip install -r requirements.txt && python train_model.py`
   - **Start Command:** `gunicorn app:app`
5. Click **"Create Web Service"**

Your app will be live at: `https://your-app.onrender.com`

## 🧪 Test the App

**Sample Input:**
- Area: 2500 sq ft
- Bedrooms: 3
- Bathrooms: 2
- Floors: 2
- Year Built: 2015
- Location Score: 8

**Expected Output:** ~₹12,87,000

## 📊 Model Details

The app trains and compares three models:

1. **Linear Regression** - Usually achieves 99%+ accuracy
2. **Decision Tree** - Good for non-linear patterns
3. **Random Forest** - Ensemble approach

The best model is automatically selected based on R² score.

## 🎨 UI Design

**Classic Gray Theme:**
- Primary Color: `#4a5568` (Slate Gray)
- Secondary: `#2d3748` (Dark Gray)
- Background: `#f7fafc` (Light Gray)
- Professional corporate aesthetic

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `5000` | Server port |
| `PYTHON_VERSION` | `3.11.0` | Python version |

### Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application |
| `train_model.py` | Trains & saves ML model |
| `requirements.txt` | Python dependencies |
| `Procfile` | Render/Heroku config |
| `render.yaml` | Render auto-deploy |
| `Dockerfile` | Container definition |

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with form |
| `/predict` | POST | Prediction endpoint |

## 🐛 Troubleshooting

**Model not found:**
```bash
python train_model.py
```

**Port already in use:**
```bash
# Windows
netstat -ano | findstr :5000
# Mac/Linux
lsof -ti:5000 | xargs kill -9
```

**Module not found:**
```bash
pip install -r requirements.txt
```

## 📚 Technologies

- **Backend:** Flask 3.0.0
- **ML:** Scikit-learn, Pandas, NumPy
- **Server:** Gunicorn
- **Container:** Docker
- **Frontend:** HTML5, CSS3

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ using Flask and Machine Learning

## 🔗 Links

- **Live Demo:** [https://house-price-app-final.onrender.com]
- **GitHub:** [https://github.com/Siddhesh842000/House-Price-App-FINAL]

---

**⭐ Star this repo if you find it useful!**
