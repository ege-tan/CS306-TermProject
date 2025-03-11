# 🎓 CS 306 - University Student Management System

This repository contains the **University Student Management System**, developed as part of **CS 306: Database Systems**. The project spans multiple phases, integrating **relational (SQL) and NoSQL (MongoDB) databases** to manage **students, courses, faculty, departments, attendance, and evaluations**.

---

## 📌 Project Overview
The **University Student Management System** ensures efficient data management within an educational institution, focusing on:
- **Data Integrity**
- **Normalization & Query Optimization**
- **SQL & NoSQL Hybrid Database Architecture**
- **Scalable and Flexible Data Operations**

---

## 🔹 Phase I: Database Schema Design
- **Designed 8 entities**:  
  - `Student`, `Course`, `Professor`, `Department`, `Attendance`, `Building`, `Room`, `Project`
- **Defined relationships** to enforce referential integrity:
  - **Many-to-Many**: Student-Course Enrollment, Professor-Course Teaching
  - **One-to-Many**: Department-Professor, Course-Attendance, Building-Room, Student-Project
- **Implemented participation constraints** ensuring:
  - Every course must have at least one student and professor.
  - Buildings must have at least one room.
  - Attendance is optional for some courses.

---

## 🔹 Phase II: Database Normalization & Query Optimization
- **Ensured Boyce-Codd Normal Form (BCNF)**:
  - Removed redundancies while preserving dependencies.
  - Optimized query performance.
- **Implemented SQL Queries**:
  - **Filter students with project deadlines beyond a specific date**.
  - **Calculate the average GPA of students based on project deadlines**.
- **Applied Constraints**:
  - **Foreign keys** for referential integrity.
  - **Check constraints** to prevent invalid entries (e.g., negative student IDs).
- **Populated Database with Sample Data**.

---

## 🔹 Phase III: Python & MySQL Integration (CRUD Operations)
In **Phase III**, we extended the system with a **Python-based MySQL application**, allowing **interactive CRUD (Create, Read, Update, Delete) operations**.

### **🚀 Features Implemented in Python**
1️⃣ **Database Connection Handling**  
   - Established a secure connection with **MySQL Connector**.  
   - Included error handling for **invalid credentials & non-existent databases**.  

2️⃣ **Create Operations**  
   - Inserted new **student records** and **project assignments**.  

3️⃣ **Read Operations**  
   - Queried **all student records** and **project assignments**.  

4️⃣ **Update Operations**  
   - Modified student GPAs and project deadlines dynamically.  

5️⃣ **Delete Operations**  
   - Removed **students & projects** while preserving database integrity.  

6️⃣ **Secure & Structured Queries**  
   - Used **parameterized queries** to prevent **SQL injection**.  

---

## 🔹 Phase IV: MongoDB Integration & NoSQL Expansion (Most Critical Phase)
In **Phase IV**, we extended our system by implementing a **NoSQL database** using **MongoDB**, enabling **scalable and flexible data management**.

### **🚀 Features of the MongoDB-Based System**
1️⃣ **Create Collections**  
   - Supports dynamic collection creation (e.g., `student_evaluation`, `teacher_evaluation`).  
   - Prevents duplicate collections, maintaining **data integrity**.

2️⃣ **Insert Data**  
   - Adds new documents to collections.  
   - Ensures **unique document IDs** to prevent conflicts.  

3️⃣ **Read All Data**  
   - Displays all records from a selected collection.  
   - Helps review datasets efficiently.  

4️⃣ **Read Filtered Data**  
   - Retrieves documents based on filtering criteria (e.g., `given_star > X`).  
   - Enables targeted analysis.  

5️⃣ **Update Data**  
   - Updates documents based on their **ID**.  
   - Ensures updates apply only to **existing records**.  

6️⃣ **Delete Data**  
   - Removes documents safely.  

7️⃣ **List Collections**  
   - Displays available collections, allowing users to navigate the database easily.  

### **🔧 Technical Aspects**
- **Built with Python & PyMongo** for MongoDB interaction.  
- **Command-Line Interface (CLI)** for user-driven CRUD operations.  
- **Data Integrity Enforcement** through constraints.  
- **Hybrid Approach** combining **SQL (Relational) and NoSQL (Document-Based) storage models**.  

---

## 📌 Key Takeaways
- **Database Design Principles**: Understanding entity relationships and referential integrity.
- **Normalization & Integrity**: Adhering to **BCNF for structured databases**.
- **Query Optimization**: Efficient **indexing, filtering, and aggregation**.
- **NoSQL Flexibility**: Implemented **MongoDB-based evaluations** for student & teacher feedback.
- **Real-World Application**: Demonstrated **scalability & usability** in data management.
