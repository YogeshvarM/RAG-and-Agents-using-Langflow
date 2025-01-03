Customer Service AI Assistant
A sophisticated AI-powered customer service system that combines RAG (Retrieval Augmented Generation) with specialized agents to handle customer inquiries, order lookups, and product information requests.
System Overview
This system consists of three main components:

FAQ Knowledge Base

Processes and indexes FAQ documents for quick retrieval
Uses vector storage for semantic search capabilities
Helps answer general customer queries


Order Management System

Direct access to order database
Ability to look up order details
Links orders with product information


Manager Agent

Orchestrates between different specialized agents
Routes queries to appropriate subsystems
Provides unified responses to users



Architecture
Document Processing Pipeline

Input files are processed and split into manageable chunks
Text chunks are embedded and stored in vector database (Astra DB)
Enables semantic search capabilities

Query Processing Flow

User submits a question
System performs vector search to find relevant FAQ content
Retrieved content is parsed and structured
Augmented prompt is created combining user question and relevant information
Specialized agents process the request:

FAQ Agent handles general inquiries
Order Analysis Agent processes order-related queries
Manager Agent coordinates responses



Technical Components
Vector Storage (Astra DB)

Collection for FAQ documents: faq_document
Collection for orders: orders
Collection for products: product

Agents

FAQ Agent

Handles general customer service inquiries
Uses RAG for accurate responses
Access to company documentation


Order Analysis Agent

Specialized in order lookup and analysis
Can access order and product databases
Provides detailed order information


Manager Agent

Main orchestrator
Routes requests to appropriate agents
Ensures coherent responses

Deployment Guide: Langflow with DataStax Integration
Overview of app.py
The app.py file serves as a Streamlit-based web interface that connects to a deployed Langflow instance through DataStax. Here's how it works:
pythonCopyimport streamlit as st 
import requests
import os
from dotenv import load_dotenv
Key Components

Environment Configuration

pythonCopyload_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "10e7b18a-333b-434c-8ad5-aecb61d2817e"
FLOW_ID = "9c5dfd71-adf9-4a6c-96ab-5b8f98b9571f"
APPLICATION_TOKEN = os.environ.get("APPLICATION_TOKEN")
ENDPOINT = "Customer"

BASE_API_URL: DataStax Astra API endpoint
LANGFLOW_ID: Unique identifier for your Langflow instance
FLOW_ID: Identifier for the specific flow (Customer Service flow)
APPLICATION_TOKEN: Authentication token stored in environment variables
ENDPOINT: The name of the endpoint configured in flow settings

API Integration
The run_flow function handles communication with the Langflow API:
pythonCopydef run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {
        "Authorization": "Bearer " + APPLICATION_TOKEN,
        "Content-Type": "application/json"
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()
Streamlit Interface
The application uses Streamlit's chat interface for a user-friendly experience:
pythonCopydef main():
    st.title("Chat Interface")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "How can I help you?"}
        ]
    
    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    # Chat input
    if message := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": message})
        st.chat_message("user").write(message)
        try:
            response = run_flow(message)
            response_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            st.chat_message("assistant").write(response_text)
        except Exception as e:
            st.error(str(e))
DataStax Deployment Process

Flow Export and Import

Export the Langflow JSON configuration
Upload to DataStax Astra platform
Configure environment variables and API tokens


Environment Setup
Create a .env file with the necessary credentials:
plaintextCopyAPPLICATION_TOKEN=your_astra_token

API Configuration

Get the Langflow ID from DataStax dashboard
Configure the Flow ID and endpoint name
Set up authentication tokens



Running the Application

Install Dependencies
bashCopypip install streamlit requests python-dotenv

Start the Application
bashCopystreamlit run app.py


Security Considerations

Token Management

Store tokens in environment variables
Never commit tokens to version control
Use proper secret management in production


API Security

All requests are authenticated using Bearer tokens
HTTPS endpoints ensure encrypted communication
Rate limiting and monitoring through DataStax
