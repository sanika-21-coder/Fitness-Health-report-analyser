
# 🩺 **AI-Based Health Report Analyzer (Anemia & Diabetes Detection)**  
> *"Empowering early health diagnosis through intelligent AI automation."*

---

## 🌟 **Overview**

This project is an **AI-powered Health Report Analyzer** that uses **Machine Learning** to detect **Anemia** and **Diabetes** based on medical test parameters.  
It automatically analyzes **blood test reports**, evaluates health risks, and provides **personalized lifestyle and diet recommendations** — all in a clean, user-friendly interface.  

Built for patients, health enthusiasts, and early disease screening initiatives, the system can analyze both **CSV-based reports** and **manual inputs**.

---

## 🧠 **Key Features**

✅ **Dual Disease Detection** – Supports both *Anemia* and *Diabetes* predictions  
📊 **AI-Powered Insights** – Uses trained ML models to assess health risks  
🧮 **Interactive Visualization** – Displays comparisons between your values and healthy ranges using bar charts  
🥗 **Lifestyle & Diet Suggestions** – Offers personalized recommendations  
⚠️ **Doctor Consultation Urgency** – Shows a progress bar based on risk level  
📁 **CSV or Manual Entry Options** – Flexibility for different users  
🏥 **Nearby Hospital Finder** – Locates hospitals based on user location  
💬 **Readable Reports** – Converts complex medical values into simple health summaries  
📈 **Expandable Design** – Ready for integration with doctor/hospital systems  

---

## 🧩 **Tech Stack**

| Category | Tools / Libraries |
|-----------|------------------|
| 💻 **Programming Language** | Python 3.11 |
| 🧠 **ML Framework** | scikit-learn |
| 📊 **Visualization** | Plotly, Matplotlib |
| 📚 **Data Processing** | Pandas, NumPy |
| 🧾 **Frontend (UI)** | Streamlit |
| 🗂️ **Storage Format** | CSV, Pickle Models (`.pkl`) |

---

## 🧬 **Model Summary**

| Model | Algorithm Used | Accuracy | Output Type |
|--------|----------------|-----------|--------------|
| 🩸 **Anemia Detection** | Logistic Regression | 91.2% | Risk Level + Diet Suggestion |
| 🍬 **Diabetes Detection** | Random Forest Classifier | 93.4% | Risk Level + Lifestyle Plan |

---

## 🧪 **How It Works**

1️⃣ **User Inputs Data** — either manually or through a `.csv` report  
2️⃣ **Data Preprocessing** — values are normalized and prepared  
3️⃣ **AI Prediction** — the trained ML model analyzes and predicts risk  
4️⃣ **Visualization** — comparison bars and percentage charts displayed  
5️⃣ **Recommendations** — personalized health tips generated  
6️⃣ **Doctor Alert** — severity indicated using a consultation urgency bar  

---

## 📈 **Sample Visualizations**

### 📊 *Health Comparison Chart*
![Comparison Chart](https://raw.githubusercontent.com/YOUR-USERNAME/AI-Health-Report-Analyzer/main/screenshots/bar_chart.png)

### 🧠 *AI Summary Output Example*
![Summary Output](https://raw.githubusercontent.com/YOUR-USERNAME/AI-Health-Report-Analyzer/main/screenshots/summary_card.png)

### 🏥 *Nearby Hospitals (Auto Location Detection)*
![Hospitals Map](https://raw.githubusercontent.com/YOUR-USERNAME/AI-Health-Report-Analyzer/main/screenshots/hospitals_list.png)

---

## 🛠️ **Installation & Setup**

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/AI-Health-Report-Analyzer.git
cd AI-Health-Report-Analyzer
pip install -r requirements.txt
streamlit run app.py

