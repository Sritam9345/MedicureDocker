# MediCure

MediCure is a healthcare recommendation web application designed to intelligently map patient symptoms to appropriate medicines. It leverages advanced Machine Learning and Natural Language Processing (NLP) techniques to provide accurate recommendations and is deployed for scalability using modern DevOps practices.

## 🚀 Key Features

* **Symptom-to-Medicine Mapping:** Utilizes a robust **XGBoost classifier** to analyze symptoms and predict suitable medications.
* **NLP Pipeline:** Incorporates a pre-trained **all-MiniLM-L6-v2** model to generate text embeddings, enabling high-quality **semantic search** capabilities.
* **Data Management:** Integrated with **MongoDB** to efficiently store user queries, medicine datasets, and recommendation history.
* **Scalable Deployment:** The application server is containerized using **Docker** and deployed on **AWS EC2** to ensure reliability and scalability.

## 🛠️ Tech Stack

* **Machine Learning:** XGBoost, Optuna (Hyperparameter Tuning)
* **Natural Language Processing:** all-MiniLM-L6-v2 (Hugging Face / Sentence Transformers)
* **Backend & Database:** Python, MongoDB
* **DevOps:** Docker, AWS EC2

## 📊 Model Performance

The machine learning models have been rigorously optimized and tested to ensure high reliability in a healthcare context:

* **Accuracy:** 94%
* **Precision:** 98%
* **Optimization Techniques:**
    * Hyperparameter tuning using **Optuna**
    * Data Normalization
    * **Five-fold Cross-Validation** for robust model assessment

## 🔧 Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/medicure.git](https://github.com/yourusername/medicure.git)
    cd medicure
    ```

2.  **Environment Variables**
    Create a `.env` file and configure your MongoDB connection string and other necessary API keys.

3.  **Run with Docker (Recommended)**
    ```bash
    docker build -t medicure-app .
    docker run -p 8000:8000 medicure-app
    ```

4.  **Run Locally (Manual)**
    ```bash
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```

## 📂 Database Structure

The project uses **MongoDB** to handle the following collections:
* `queries`: Stores raw user input and symptom descriptions.
* `medicines`: Contains the dataset of medicines and their attributes.
* `history`: Logs user recommendation history for future reference.

The server is deployed on AWS EC2 instance

copy and go -> http://13.62.231.55:8000/docs


## 🔗 Source

[Link to Source Code]
