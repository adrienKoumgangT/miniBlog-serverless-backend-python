# Mini Blog Using Serverless Philosophy, Flask Framework, and DynamoDB

This project aims to create a mini blog application following the serverless philosophy. 
It utilizes Flask, a lightweight web application framework in Python, for handling HTTP requests and DynamoDB, 
a NoSQL database service provided by AWS, for data storage.

## Features

- **Serverless Architecture:** The application is built following serverless principles, leveraging AWS services like Lambda and API Gateway for server-side operations.
- **Flask Framework:** Flask is used for creating routes, handling requests, and rendering HTML templates to build the web application.
- **DynamoDB:** The NoSQL database is used for storing blog posts, user data, and other necessary information in a scalable and flexible manner.
- **CRUD Operations:** Users can create, read, update, and delete blog posts.
- **Authentication and Authorization:** Implement authentication mechanisms for user access control to manage their blog posts.

## Requirements

- Python 3.11
- Flask
- AWS account with DynamoDB, S3 access

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/adrienKoumgangT/miniBlog-serverless-backend-python.git
   cd miniBlog-serverless-backend-python
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **AWS Configuration:**

   - Create an AWS account if you don't have one.
   - Set up AWS credentials and configure them locally using AWS CLI or environment variables.
   - Create a DynamoDB table to store blog post data.

4. **Configuration:**

   - Configure Flask application settings, AWS credentials, and DynamoDB connection details in the `config.py` file.

5. **Run the Application:**

   ```bash
   python app.py
   ```

   The application should start running locally on `http://localhost:5000`.

## Usage

- Access the application through a web browser by visiting `http://localhost:5000`.
- Users can create an account, log in, create, edit, delete blog posts, and view existing posts.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or new features.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [DynamoDB](https://aws.amazon.com/dynamodb/) (For local dev: [NoSQL Workbench For DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html))
- [S3](https://aws.amazon.com/s3/) (For local dev: [MINIO](https://min.io))

---

Feel free to customize this README to fit your project's specific details, add more information, or modify the sections as needed.
