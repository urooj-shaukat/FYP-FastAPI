# Plagiarism Checker for Coding Files

## Overview
This repository contains a plagiarism checking tool designed to compare coding files written in different programming languages. The application utilizes the FastAPI framework along with the scikit-learn library for cosine similarity calculation and the TF-IDF vectorizer for text representation.

## Features
- Supports plagiarism checking between coding files in various programming languages.
- Utilizes the FastAPI framework for a fast and efficient web application.
- Employs the scikit-learn library for cosine similarity calculation.
- Implements the TF-IDF vectorizer for text representation and feature extraction.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/plagiarism-checker.git
   cd plagiarism-checker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command:

```bash
uvicorn app:app --reload
```

This will start the FastAPI application, and you can access it through your browser at `http://127.0.0.1:8000`.

## API Endpoints

- `/`: Home endpoint with information about the plagiarism checker.
- `/check`: Endpoint to submit coding files and get plagiarism results.

## Example Usage

1. Start the application:

   ```bash
   uvicorn app:app --reload
   ```

2. Open your browser and go to `http://127.0.0.1:8000` to access the home page.

3. Use the `/check` endpoint to submit coding files and receive plagiarism results.

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast, web framework for building APIs with Python 3.7+.
- [scikit-learn](https://scikit-learn.org/): Simple and efficient tools for data mining and data analysis.
- [TF-IDF Vectorizer](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting): Term Frequency-Inverse Document Frequency for text feature extraction.

## Contributing

Feel free to contribute by submitting bug reports, feature requests, or pull requests. Your input is highly valued!

## Author

[urooj-shaukat]

If you have any questions or issues, please contact [uroojshaukat20@gmail.com].
