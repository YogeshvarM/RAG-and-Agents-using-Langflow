# Customer Service AI Assistant

A sophisticated AI-powered customer service system that combines RAG (Retrieval Augmented Generation) with specialized agents to handle customer inquiries, order lookups, and product information requests.

---

## System Overview

This system is designed to enhance customer service through efficient query resolution and seamless integration of multiple subsystems. It consists of three main components:
![Customer Service AI Architecture](Overview_Architecture.png")

### 1. FAQ Knowledge Base
- **Purpose**: Answers general customer queries.
- **Features**:
  - Processes and indexes FAQ documents for quick retrieval.
  - Employs vector storage for semantic search capabilities.

### 2. Order Management System
- **Purpose**: Handles order-related inquiries.
- **Features**:
  - Direct access to the order database.
  - Ability to look up order details and link orders with product information.

### 3. Manager Agent
- **Purpose**: Orchestrates between specialized agents.
- **Features**:
  - Routes queries to appropriate subsystems.
  - Provides unified responses to users.

---

## Architecture

### Document Processing Pipeline
1. Input files are split into manageable chunks.
2. Text chunks are embedded and stored in a vector database (Astra DB).
3. Enables efficient semantic search capabilities.

### Query Processing Flow
1. **User Interaction**: User submits a question.
2. **Vector Search**: Relevant FAQ content is retrieved through semantic search.
3. **Response Augmentation**:
   - Relevant information is structured.
   - Augmented prompts are created combining user input and retrieved data.
4. **Agent Handling**:
   - **FAQ Agent**: Handles general inquiries.
   - **Order Analysis Agent**: Processes order-related queries.
   - **Manager Agent**: Coordinates responses.

---

## Technical Components

### Vector Storage (Astra DB)
- **Collections**:
  - `faq_document`: Stores FAQ documents.
  - `orders`: Stores order details.
  - `product`: Stores product information.

### Agents
1. **FAQ Agent**
   - Handles general inquiries.
   - Utilizes RAG for accurate responses.
   - Accesses company documentation.

2. **Order Analysis Agent**
   - Specializes in order lookups.
   - Accesses order and product databases.
   - Provides detailed order insights.

3. **Manager Agent**
   - Coordinates between agents.
   - Ensures coherent and unified responses.

---

## Deployment Guide: Langflow with DataStax Integration

### Overview of `app.py`
- A Streamlit-based web interface connecting to Langflow via DataStax.

### Key Components

#### Environment Configuration
```python
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "10e7b18a-333b-434c-8ad5-aecb61d2817e"
FLOW_ID = "9c5dfd71-adf9-4a6c-96ab-5b8f98b9571f"
APPLICATION_TOKEN = os.environ.get("APPLICATION_TOKEN")
ENDPOINT = "Customer"
