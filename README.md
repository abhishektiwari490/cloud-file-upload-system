# Cloud File Upload System (AWS S3 + Lambda)

## 📌 Overview
This project demonstrates a cloud-based file upload system using AWS services. It uses pre-signed URLs to securely upload files to S3 without exposing credentials.

## 🏗 Architecture
User → API Gateway → Lambda → S3

## ⚙️ Technologies Used
- AWS S3
- AWS Lambda (Python)
- API Gateway
- IAM

## 🔐 Features
- Secure file upload using pre-signed URLs
- Serverless architecture
- Scalable cloud storage

## 🚀 How It Works
1. User sends request to API Gateway
2. Lambda generates pre-signed URL
3. User uploads file directly to S3
4. File stored securely in cloud

## 📷 Architecture Diagram
(Add your image here)

## 📌 Future Improvements
- Add authentication
- Connect with Android app
- Add file download API
