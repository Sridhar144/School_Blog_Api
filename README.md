# School Blog API

Welcome to the **School Blog API**! This project is a RESTful API designed to facilitate the management of blog posts in a school environment. Built using **FastAPI** and **MongoDB**, this API is designed for both efficiency and ease of use, allowing users to perform CRUD operations on blog posts seamlessly.

## Overview

This API provides functionality to:

- Create new blog posts
- Retrieve all existing blog posts
- Fetch a specific blog post by its unique ID
- Update details of existing blog posts
- Permanently delete blog posts from the database

## Technologies Employed

This API is powered by the following technologies:

- **[FastAPI](https://fastapi.tiangolo.com/)**: A fast web framework for Python that enables easy development of APIs.
- **[MongoDB](https://www.mongodb.com/)**: A NoSQL database system used for storing the blog posts efficiently.
- **[Motor](https://motor.readthedocs.io/en/stable/)**: An asynchronous MongoDB driver for Python, ensuring smooth and non-blocking operations.
- **[Pydantic](https://pydantic-docs.helpmanual.io/)**: A data validation library that helps maintain data integrity and structure.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11 or higher**
- **MongoDB**: You can either set up a local instance or use MongoDB Atlas.
- **pip**: Python's package installer.

### Installation Steps

1. **Clone the Repository**:
Install Required Packages: It's recommended to create a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Then, install the dependencies:

Set Up Environment Variables: Create a .env file in the root directory of the project and add your MongoDB connection URI:

env
Copy code
MONGODB_CONNECTION_URI="your_mongodb_connection_string"
Run the Application: Start the FastAPI application with:

bash
Copy code
uvicorn main:app --reload
You can access the API documentation at http://localhost:8000/docs.

Usage Instructions
Once the application is up and running, you can interact with the API using tools like Postman or through the integrated Swagger UI available at the documentation link.

API Endpoints
Below is a quick reference for the available API endpoints:

POST /api/v1/posts/: Create a new blog post.
GET /api/v1/posts/: Retrieve a list of all blog posts.
GET /api/v1/posts/{post_id}: Fetch a specific blog post by its ID.
PUT /api/v1/posts/{post_id}: Update an existing blog post.
DELETE /api/v1/posts/{post_id}: Delete a blog post from the database.
