# 📝 Serverless Cloud Notes Application (CloudKeep)

A single-file serverless document notes application built with Python and Streamlit. This project simulates a cloud-native CRUD application backed by a NoSQL document database (such as **Amazon DynamoDB**, **Firebase Firestore**, or **MongoDB Atlas**).

Built for engineering portfolio showcases, academic project presentations, and cloud architecture viva examinations.

---

## 🌟 Key Features

- **Full CRUD Functionality**: Create, Read, Update, and Delete documents seamlessly.
- **Instant Search & Querying**: Real-time filtering across titles, note bodies, and categories.
- **Categorization & Priority Tags**: Organize notes by tags (Cloud Architecture, DevOps, Security, AI & ML, General) and priorities (High, Medium, Low).
- **Automated Local Persistence**: Changes automatically commit to a local JSON document store (`cloud_notes_database.json`) and synchronize with session state.
- **Telemetry & Word Metrics**: Live tracking of total documents, total word counts, active category tags, and simulated replica health.
- **Database Backup & Export**: Download the entire document store as a JSON backup with one click.
- **College Viva Cheatsheet**: Built-in interactive guide explaining serverless compute, NoSQL schemas, and consistency models.

---

## 📐 Cloud Computing Concepts Demonstrated

1. **Serverless Architecture**: Understanding how stateless frontends interact with cloud microservices (e.g. AWS Lambda + API Gateway) without maintaining physical server infrastructure.
2. **NoSQL Document Storage**: Contrasting flexible schema-less JSON document models (DynamoDB/Firestore) against rigid relational schemas (SQL).
3. **Partition Keys & Indexing**: How NoSQL databases use unique IDs for $O(1)$ fast lookups across distributed storage nodes.
4. **Consistency Models**: Understanding Eventual Consistency vs Strong Consistency in multi-region cloud replication.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip package manager

### 1. Installation
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/cloud-notes-app.git
cd cloud-notes-app
pip install -r requirements.txt
```

### 2. Run the Application
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser.

---

## 📁 Repository Structure

```text
cloud-notes-app/
├── app.py                     # Single-file Streamlit application (UI + NoSQL CRUD logic)
├── requirements.txt           # Minimal dependencies (streamlit, pandas)
└── README.md                  # Comprehensive documentation & Viva guide
```

---

## 🎓 College Viva Preparation Guide

- **Q: What is the difference between SQL and NoSQL in cloud systems?**
  - **A:** SQL databases (e.g. Amazon RDS, PostgreSQL) use structured tables with ACID guarantees and scale vertically. NoSQL databases (e.g. Amazon DynamoDB, MongoDB) store flexible JSON documents, scale horizontally across partitions, and provide massive throughput at scale.
- **Q: What is a Serverless application?**
  - **A:** Serverless is an event-driven cloud computing model where cloud providers automatically manage machine provisioning, scaling, and maintenance. Developers write application code, paying only for the exact compute execution time.
- **Q: What is the CAP Theorem?**
  - **A:** In any distributed data store, you can only guarantee two out of three: **Consistency** (all nodes see same data at same time), **Availability** (every request gets a non-error response), and **Partition Tolerance** (system functions despite network drops).

---

## 🔮 Limitations & Future Improvements

- **Local Storage Engine**: Uses local JSON file storage rather than direct AWS DynamoDB API calls via Boto3.
- **Authentication**: Can be extended with Amazon Cognito or Firebase Auth for user-specific private note silos.
- **Rich Text / WYSIWYG**: Integrate an advanced visual markdown editor component.

---

## 📄 License
MIT License. Created for AI & Data Science Engineering Portfolio.
