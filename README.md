# Tumor-Size-Detection-by-ML
# 🧬 Tumor Size Prediction from Gene Expression

This project predicts **tumor size (in cm)** based on **gene expression values**, using a **Linear Regression model**.  
It was developed in **Google Colab** and deployed via **Streamlit** for interactive predictions.

---

## 🚀 Features

- 📂 Upload your own **gene expression CSV file**
- 🔍 View dataset preview directly in the app
- 🧠 Train a **Linear Regression model** on your dataset
- 📊 Input new gene expression values to predict tumor size
- 💻 Runs interactively with **Streamlit**

---

## 📊 Dataset Format

The dataset should be in CSV format, where:

- **Columns**: Gene expression values for each gene (numeric)
- **Target column**: `Tumor_Size_cm` (numeric, tumor size in centimeters)


---

## 🛠️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/washma-sajjad/Tumor-Size-Detecction-by-ML.git
cd tumor-size-prediction
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
📈 Model Details
Algorithm: Linear Regression (from sklearn)

Inputs: Multiple gene expression values

Output: Predicted tumor size in cm



📦 Tech Stack
Python 3.x

Pandas – Data handling

NumPy – Numerical computation

Scikit-learn – Model building

Streamlit – Web app deployment

📌 Future Improvements
🔹 Add more advanced models (Random Forest, XGBoost)

🔹 Integrate real genomic datasets from TCGA or Kaggle

🔹 Deploy on Streamlit Cloud or Heroku

🔹 Add visualization dashboards with Power BI
