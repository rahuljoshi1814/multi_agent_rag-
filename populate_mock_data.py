import psycopg2
from faker import Faker
import random
from app.db import get_connection

fake = Faker()

conn = get_connection()
cur = conn.cursor()

# Insert Customers
for _ in range(200):
    cur.execute("INSERT INTO customers (name, email, created_at) VALUES (%s, %s, %s)",
                (fake.name(), fake.email(), fake.date_between(start_date='-3y', end_date='today')))

# Insert Products
product_ids = []
for _ in range(20):
    cur.execute("INSERT INTO products (name, category, price) VALUES (%s, %s, %s) RETURNING id",
                (fake.word().capitalize(), random.choice(["Electronics", "Books", "Clothing"]), round(random.uniform(10, 500), 2)))
    product_ids.append(cur.fetchone()[0])

# Insert Employees
employee_ids = []
for _ in range(50):
    cur.execute("INSERT INTO employees (name, role, department, hire_date) VALUES (%s, %s, %s, %s) RETURNING id",
                (fake.name(), random.choice(["Sales Rep", "Manager"]), random.choice(["Sales", "HR", "IT"]), fake.date_between(start_date='-5y', end_date='today')))
    employee_ids.append(cur.fetchone()[0])

# Insert Projects
for _ in range(30):
    cur.execute("INSERT INTO projects (name, description, start_date, end_date) VALUES (%s, %s, %s, %s)",
                (fake.bs().title(), fake.text(), fake.date_between('-2y', '-1y'), fake.date_between('-1y', 'today')))

# Insert Sales
for _ in range(500):
    cur.execute("INSERT INTO sales (customer_id, product_id, employee_id, amount, sale_date) VALUES (%s, %s, %s, %s, %s)",
                (random.randint(1, 200), random.choice(product_ids), random.choice(employee_ids), round(random.uniform(50, 1000), 2), fake.date_between(start_date='-2y', end_date='today')))

conn.commit()
cur.close()
conn.close()
print(" Mock data inserted successfully!")
