#  Multi-Agent RAG System for Natural Language Querying of a Relational Database

###  Objective
This project implements a **Multi-Agent Retrieval-Augmented Generation (RAG)** system that allows users to ask **natural language questions**, translates them to **PostgreSQL SQL queries**, and returns human-readable answers via a web interface and API.

---

##  Features
-  Natural language query interface
-  Modular multi-agent architecture:
  - **Schema Agent**: Finds relevant tables
  - **SQL Generator Agent**: Creates SQL query
  - **Retriever Agent**: Executes query on PostgreSQL
  - **Synthesizer Agent**: Converts results to human-like answer
-  `/ask` API endpoint (FastAPI)
-  Web frontend (HTML+JS)
-  Error handling for schema, SQL, empty results

---

##  System Architecture
User → Web/API → Schema Agent → SQL Agent → Retriever → Synthesizer → Final Answer


---

##  Database Schema

PostgreSQL schema includes 5 interrelated tables:
- `customers(id, name, email, created_at)`
- `products(id, name, category, price)`
- `employees(id, name, role, department, hire_date)`
- `projects(id, name, description, start_date, end_date)`
- `sales(id, customer_id, product_id, employee_id, amount, sale_date)`

---

##  Setup Instructions

### Clone the repository
```bash
git clone https://github.com/yourusername/multi-agent-rag.git
cd multi-agent-rag

### 1. Create the PostgreSQL database
Run the schema file: 
-- In pgAdmin or psql
- \i init_db.sql

### 2. Populate with fake data
- pip install -r requirements.txt
- python populate_mock_data.py

### 3. Start the FastAPI server
uvicorn app.main:app --reload

### 4. Visit the web interface
Go to: http://localhost:8000

### 5. API Endpoint
POST /ask
Input: {
  "question": "Who spent the most last year?"
}

Output: {
  "answer": "Answer: Alice Smith, 15000.50",
  "intermediate_steps": {
    "schema": ["customers", "sales"],
    "sql_query": "...",
    "result": {
      "columns": ["name", "total"],
      "rows": [["Alice Smith", 15000.50]]
    }
  }
}

## Error Handling
- Unknown schema → Schema agent returns empty
- Invalid SQL → Catch and display message
- No results → “No data found.”
