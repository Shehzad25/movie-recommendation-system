🎬 Movie Recommendation System (FastAPI + Docker + AWS)
📌 Overview

This Movie Recommendation System is a content-based recommender that suggests movies similar to a given movie using Natural Language Processing (NLP) and cosine similarity.

The system analyzes movie metadata such as genres, keywords, cast, crew, and overview, converts them into numerical vectors, and computes similarity scores to recommend the top 5 most similar movies.

The backend is built using FastAPI, containerized with Docker, and designed for deployment on AWS EC2.

🚀 Features

Content-based movie recommendations

NLP preprocessing with stemming

Vectorization using CountVectorizer

Similarity computation using cosine similarity

Fast and scalable FastAPI backend

Separate frontend and backend architecture

Dockerized for consistent deployment

Cloud-ready (AWS EC2)

Efficient handling of large model files

🛠️ Tech Stack

Language: Python

Data Processing: Pandas, NumPy

NLP: NLTK (Stemming)

Vectorization & Similarity: Scikit-learn

Backend API: FastAPI

Frontend: Streamlit

Containerization: Docker

Deployment: AWS EC2

📂 Project Structure
Movie-Recommendor-System/
│
├── __pycache__/                 # Python cache (ignored)
│
├── models/
│   ├── movies_dict.pkl          # Processed movie metadata
│   └── similarity.pkl           # Cosine similarity matrix (generated locally)
│
├── app.py                       # FastAPI backend
├── frontend.py                  # Streamlit frontend
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
├── README.md

⚠️ Important Note About similarity.pkl

similarity.pkl is NOT pushed to GitHub

Why?

The similarity matrix file size is greater than 25 MB

GitHub has strict file size limits

Pushing it would make the repository heavy and inefficient

Correct Approach (Industry Standard)

Generate similarity.pkl locally or on AWS EC2

Store it inside the models/ directory

Load it at runtime inside the FastAPI app

This keeps the repository clean, lightweight, and professional.

⚙️ Installation & Usage (Local)
1️⃣ Clone the repository
git clone https://github.com/Shehzad25/movie-recommendor-system.git
cd Movie-Recommendor-System

2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

🧠 Generate Model Files

Run the notebook used for preprocessing and training:

Movie_recommender_system.ipynb


This will generate:

movies_dict.pkl

similarity.pkl

Place both files inside the models/ directory.

▶️ Run FastAPI Backend
uvicorn app:app --reload


API will be available at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

🖥️ Run Frontend (Streamlit)
streamlit run frontend.py

🐳 Run Using Docker
1️⃣ Build Docker image
docker build -t movie-recommender-api .

2️⃣ Run Docker container
docker run -p 8000:8000 movie-recommender-api


Application will be accessible at:

http://localhost:8000

☁️ Deploy on AWS EC2 (High-Level Steps)

Launch an Ubuntu EC2 instance

Install Docker on EC2

Clone this repository

Generate or upload similarity.pkl into models/

Build Docker image on EC2

Run the container

Open port 8000 in EC2 Security Group

Access API using:

http://<EC2-PUBLIC-IP>:8000

🔍 How It Works

Movie and credits datasets are merged

Important textual features are extracted

Text is cleaned and stemmed using NLP

CountVectorizer converts text into vectors

Cosine similarity computes similarity between movies

Given a movie title, the system returns top 5 similar movies

🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

📜 License

This project is licensed under the MIT License.

⭐ If You Like This Project

Give it a ⭐ on GitHub — it really helps!
