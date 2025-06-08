# Local Chatbot Setup

The goal of this guide is to show how you can run a chatbot on your own machine without any paid services. We will use only free and open source tools.

## Requirements
- **Docker**: container runtime (free)
- **Ollama**: local language model runner
- **n8n**: workflow automation tool
- **PostgreSQL**: database engine
- **Evolution API**: minimal example of a REST API (implemented locally)
- **Python 3** with `requests` library

## Installation Steps

### 1. Install Docker
Docker is available for Windows, macOS and Linux. Download it from [docker.com](https://www.docker.com/get-started/) and follow the installation instructions for your platform.

### 2. Start PostgreSQL
Run PostgreSQL in a container so that it stays local and costs nothing:
```bash
docker run --name local-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:16
```
This exposes the database on port `5432`.

### 3. Launch n8n
n8n can also run in Docker:
```bash
docker run --name n8n -p 5678:5678 -d n8nio/n8n
```
Access the web interface at <http://localhost:5678>.

### 4. Install and Run Ollama
Ollama provides local language models. Install it from the [Ollama website](https://ollama.com). After installation, start the service:
```bash
ollama run llama3
```
This downloads the model the first time and exposes an API on <http://localhost:11434>.

### 5. Implement Evolution API
As an example of a simple local API, run the provided Python script:
```bash
python evolution_api.py
```
It listens on `http://localhost:5000` and simply echoes requests. You can replace it with your own logic.

### 6. Simple Chatbot Script
Use `chatbot.py` to send a question to the local Ollama model:
```bash
python chatbot.py "Olá, mundo"
```
The script prints the response returned by the model.

## Files
- `chatbot.py` – example client that calls the Ollama API
- `evolution_api.py` – minimal Flask API serving as an example

These scripts demonstrate how everything works together. Because all services are local, no external paid services are required.
