# Deployment Guide

This document describes how to deploy the application on a Linux VPS using Docker, Docker Compose, Nginx, and the Docker image published to GitHub Container Registry (GHCR).

## Deployment Architecture

Client
  |
  v
Nginx :80
  |
  v
FastAPI Container :8000

Docker image:

ghcr.io/milad5108/devops-deployment-pipeline:latest

---

## 1. Server Requirements

Recommended environment:

- Ubuntu Linux VPS
- Docker installed
- Docker Compose installed
- Git installed
- Port 80 open

---

## 2. Clone Repository

```bash
git clone https://github.com/milad5108/devops-deployment-pipeline.git
cd devops-deployment-pipeline