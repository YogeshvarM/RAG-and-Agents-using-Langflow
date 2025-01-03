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
