# Text Summarizer

## Overview
The Text Summarizer is a FastAPI application that provides a simple and efficient way to summarize text using a pre-trained summarization model (_With finetune option_). This application is designed to handle multiple user requests simultaneously, making it suitable for production use.

## Features
- Summarizes input text using `google/pegasus-cnn_dailymail` model from huggingface.
- Supports CORS for cross-origin requests.
- Asynchronous processing for improved performance.

## Installation

### Prerequisites
- Python `3.10` or `3.11`

### Clone the Repository
```bash
git https://github.com/sadhiin/text-summarizer.git
cd text-summarizer
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
To run the application, use the following command:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
or
```bash
python app.py
```


Once the server is running, you can access the API at `http://localhost:8000`.

## API Endpoints

### 1. Root Endpoint
- **GET** `/`
  - Redirects to the API documentation.

### 2. Health Check
- **GET** `/health`
  - Returns the status of the application.
  - **Response**: `{"status": "ok"}`

### 3. Get Summary
- **POST** `/get_summary`
  - Summarizes the provided text.
  - **Request Body**:
    ```json
    {
      "text": "Your text to summarize."
    }
    ```
  - **Response**:
    ```json
    {
      "prediction": "Summarized text."
    }
    ```
  - **Error Responses**:
    - `400 Bad Request`: If the input text is invalid.
    - `500 Internal Server Error`: If an error occurs during processing.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the FastAPI framework for providing a robust and easy-to-use web framework.
- Thanks to the contributors and the community for their support.
```