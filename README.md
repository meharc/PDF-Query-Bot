# PDF-Query-Bot
Sure, here's a description you can use for your GitHub repository:

### Description

This repository contains a demo application that uses Langchain and Streamlit to create an interactive chatbot capable of answering questions based on the content of uploaded PDF files. The application integrates with a Language Learning Model (LLM) API, utilizes vector stores for efficient searching, and leverages word embeddings and FAISS for advanced querying.

### Features

- **LLM Integration:** Connects with various LLM providers (OpenAI, Anthropic, or Ollama).
- **PDF Interaction:** Allows users to upload PDF files and interact with the content via natural language questions.
- **Vector Stores:** Utilizes FAISS for efficient text searching and retrieval.
- **Embeddings:** Employs word embeddings to enhance the search accuracy and relevance.

### Aim

1. Integrate code with an LLM API (e.g., OpenAI, Anthropic, or local Ollama).
2. Use LLM to search PDF content using a vector store solution.
3. Implement word embedding, FAISS, and a question-answering chain.

### Getting Started

Follow the steps below to set up and run the application on your local machine.

### Prerequisites

- Python 3.6 or higher.
- API key for your LLM provider (e.g., OpenAI).

### Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the following command to start the Streamlit application:

```bash
streamlit run script_name.py
```

Replace `script_name.py` with the name of your script.

### Project Structure

- **main.py**: The main script to run the Streamlit app.
- **requirements.txt**: List of dependencies.
- **.env**: Environment file to store API keys (not included in the repository, to be created by the user).

### How It Works

1. **Load Packages**: Imports necessary libraries including Streamlit, PyPDF2, and various langchain components.
2. **Streamlit Setup**: Sets up the Streamlit interface with a file uploader for PDFs and a text input for user queries.
3. **Main Function**:
    - Loads and extracts text from the uploaded PDF.
    - Splits the extracted text into manageable chunks.
    - Creates word embeddings and stores them in a FAISS vector database.
    - Sets up the LLM and the question-answering chain.
    - Processes user queries and displays answers based on the PDF content.

### Example Workflow

1. **Upload PDF**: User uploads a PDF file.
2. **Ask a Question**: User inputs a question related to the PDF content.
3. **Get Response**: The application processes the query using the LLM and returns the relevant answer.

