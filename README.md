🌿 UnruffledAI — Burnout Prediction & Wellness Platform

Status: Actively In Development | Core ML pipeline and backend architecture complete | Biometric integrations and cloud deployment in progress


What Is UnruffledAI?
UnruffledAI is an AI-powered wellness platform built to predict and prevent burnout in remote and distributed teams — before it becomes a crisis.
Most burnout solutions are reactive. UnruffledAI is proactive. By analyzing behavioral patterns and biometric signals, the platform flags risk early and delivers personalized recommendations to help individuals and teams course-correct before performance and well-being deteriorate.
Built for the modern remote-first workforce, UnruffledAI is designed as a natural partner platform for wellness tools like Calm and wearable ecosystems like Fitbit and Apple Health.

✅ What's Working Now

Django Web Application — Full backend with user authentication, dashboard views, and data input handling
TensorFlow ML Pipeline — Trained predictive model that analyzes structured behavioral data to generate burnout risk scores
Real-Time Predictions — ML model integrated into backend services; generates live risk output from user inputs
PostgreSQL Database — Relational schema designed to store prediction results, user profiles, and activity history
Manual Biometric Input — Users can manually log stress indicators, sleep patterns, workload, and wellness data
Wellness Recommendations Engine — Platform surfaces actionable recommendations based on risk score output
Docker & Docker Compose — Fully containerized application for consistent, reproducible development environments
CI/CD Pipeline Setup — GitHub Actions and Jenkins configured for automation practices


🛠️ Tech Stack
LayerTechnologyBackendPython · Django · REST APIsMachine LearningTensorFlow · Scikit-learn · Data Preprocessing PipelinesDatabasePostgreSQLContainerizationDocker · Docker ComposeCI/CDGitHub Actions · JenkinsCloud (In Progress)AWS EC2FrontendHTML5 · CSS3 · JavaScript

🔬 In Progress & Next Steps
🔗 Fitbit API Integration

Automated ingestion of real-time biometric data including heart rate variability, sleep quality, activity levels, and stress scores
OAuth 2.0 authentication flow for secure user authorization
Webhook setup for continuous data streaming into the ML pipeline

🍎 Apple Health Integration

HealthKit data pipeline to pull recovery metrics, activity rings, and sleep analysis
Mapping Apple Health data schema to UnruffledAI's prediction input format
Testing cross-platform data normalization between Fitbit and Apple Health inputs

☁️ AWS EC2 Cloud Deployment

Containerized deployment on AWS EC2 using Docker
Environment configuration and security group setup in progress
Load balancer and auto-scaling architecture planned for production

🤝 Calm App Partnership Architecture

Designing API hooks to surface UnruffledAI risk scores directly inside Calm
Recommendation engine to trigger Calm content (meditations, sleep stories, breathing exercises) based on predicted burnout level

📊 Dashboard Enhancements

Team-level burnout risk visualization for managers
Historical trend tracking and burnout risk timeline
Exportable wellness reports for HR and People Operations teams


🏗️ Project Structure
unruffledai/
├── core/                  # Django app — views, models, URLs
├── ml_pipeline/           # TensorFlow model training & inference
├── predictions/           # Prediction results & recommendation engine
├── users/                 # Authentication & user profiles
├── biometrics/            # Biometric data ingestion & normalization
├── templates/             # Frontend HTML templates
├── static/                # CSS, JS, assets
├── docker-compose.yml     # Multi-container orchestration
├── Dockerfile             # Container configuration
├── requirements.txt       # Python dependencies
└── .env.example           # Environment variable template

🚀 Running Locally
Prerequisites

Docker & Docker Compose installed
Python 3.10+
PostgreSQL (handled via Docker)

Setup
bash# Clone the repository
git clone https://github.com/spauleyinthecloud/unruffledai.git
cd unruffledai

# Copy environment variables
cp .env.example .env

# Build and start containers
docker-compose up --build

# Run database migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Access the app
open http://localhost:8000

💡 The Problem This Solves
Remote work burnout costs companies an estimated $125–$190 billion annually in healthcare spending alone, according to Harvard Business Review. For distributed teams at companies like Atlassian, Airbnb, and GitHub, where async collaboration is the norm, the warning signs are even harder to detect through traditional management.
UnruffledAI gives teams an early warning system built on real data, not gut feelings.

👩🏽‍💻 About The Developer
Built by SPauley — DevOps & AI Engineer, BS Information Technology (Web Applications), Middle Georgia State University.

🐙 GitHub: github.com/spauleyinthecloud
💼 LinkedIn: linkedin.com/in/Shateriapauley


📄 License
MIT License — open for collaboration and feedback. If you're working on adjacent problems in the wellness tech or remote work space, let's connect.

UnruffledAI is actively being developed. Stars, forks, and feedback are welcome. 🌿
