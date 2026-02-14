# ML Reliability Monitoring Microservice

A production-ready FastAPI-based microservice for ML-driven reliability scoring and health monitoring. The system is containerized using Docker and integrated with a CI/CD pipeline for automated image publishing.

## Overview

This project implements a deployable microservice that evaluates system reliability metrics and exposes RESTful APIs for scoring and monitoring.

- Modular architecture
- Containerized deployment
- CI/CD automation
- Production-oriented structure

## Architecture

Client → FastAPI API Layer → ML Service Layer → Docker Container → Docker Hub (CI/CD Automated)

The architecture follows microservice design principles with separation of concerns and stateless execution.

## Features

### REST Endpoints

| Method | Endpoint | Description                  |
| ------ | -------- | ---------------------------- |
| GET    | /        | Service status               |
| GET    | /health  | Health check endpoint        |
| POST   | /predict | ML-based reliability scoring |

The /health endpoint provides structured service health status for integration with container orchestrators and monitoring systems.

Example response:

{
"status": "healthy",
"timestamp": "UTC timestamp",
"service": "reliability-ml-api"
}

## Reliability Scoring

The /predict endpoint accepts system performance metrics such as:

- CPU usage
- Memory usage
- Latency
- Error rate
  The request is processed by a modular service layer that computes reliability scores.

## Project Structure

.
├── src/
│ ├── api.py
│ ├── model_service.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── LICENSE
├── .github/
│ └── workflows/
│ └── ci.yml

## Docker Usage

### Build Locally

docker build -t ml-reliability-monitoring-microservice .

## Run Container

docker run -p 8000:8000 ml-reliability-monitoring-microservice

Access API documentation:
http://localhost:8000/docs

## Docker Hub

Pull the latest published image:
docker pull durga1127/ml-reliability-monitoring-microservice:latest

## Run directly:

docker run -p 8000:8000 durga1127/ml-reliability-monitoring-microservice:latest

## CI/CD Pipeline

The GitHub Actions workflow performs:

- Dependency installation
- FastAPI validation
- Docker image build
- Secure Docker Hub authentication
- Automated image publishing

Triggered on:

- Push to main branch
- Pull request to main branch
  This ensures continuous validation and reproducible deployments.

## Technology Stack

- Python 3.11
- FastAPI
- Uvicorn
- Docker
- Docker Compose
- GitHub Actions
- Docker Hub

## Design Principles

- Separation of API and ML logic
- Stateless service design
- Containerized infrastructure
- Automated build and deployment
- Production-oriented architecture

## Future Enhancements

- Prometheus metrics integration
- Structured logging middleware
- Kubernetes deployment manifests
- Model persistence and versioning
- Performance benchmarking

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Durga Sri
Machine Learning Engineer
GitHub: https://github.com/durgasri-dotcom
