# SYSAD_TASK3

## Overview 
This repository is divided two sections into `task3a` and `task3b` 
1. `task3a` : Focuses on containerizing the deltaplay server application and deploying on Cloud
2. `task3b` : Built 5 CTF challenges and solved them

# Task 3A

## Overview 
> Containerized a Python-based music streaming server using Docker and orchestrated the complete application with Docker Compose, including the backend, PostgreSQL database, and nginx. Deployed an Nginx reverse proxy in front of the DeltaPlay server to securely forward client requests. Configured health checks, persistent Docker volumes, environment variables configuration, and isolated internal networking to improve reliability, maintainability, and deployment consistency in a production-like environment.

## Features

- **Database Health Monitoring**
  - Implemented Docker health checks for the PostgreSQL service, ensuring dependent services start only after the database is fully initialized.

- **Persistent Database Storage**
  - Configured Docker named volumes to persist PostgreSQL data across container restarts, recreations, and image updates, preventing data loss during deployments.

- **Environment-Based Configuration**
  - Managed application configuration using a `.env` file, securely injecting database credentials, secrets, and runtime configuration into containers without hardcoding sensitive information.

- **Bridge Network Isolation**
  - Configured a dedicated Docker bridge network to enable secure inter-container communication while isolating internal services from the host network.

- **Containerized Multi-Service Architecture**
  - Orchestrated backend and PostgreSQL services using Docker Compose with isolated networking, and inter-container communication.
    
- **Network Security**

  - Configured the VM firewall to allow only SSH (22) and HTTPS (443) traffic while blocking all other inbound ports, reducing the attack surface.

- **Domain Configuration**

  - Configured **DuckDNS** to map the `deltaplay.duckdns.org` domain to the Azure VM's public IP.

##  Infrastructure Diagram

```mermaid
flowchart LR
    Client(["🖥️ Client"])

    subgraph Azure["☁️ Azure VM — 20.XX.XX.XX (deltaplay.duckdns.org)"]
        direction LR

        Nginx["🔀 Nginx Reverse Proxy
20.XX.XX.XX:443"]
        Server["🎵 DeltaPlay TCP Server
20.XX.XX.XX:8080"]

        subgraph DataLayer["Data Layer"]
            direction TB
            DB[("🗄️ PostgreSQL
db:5432")]
            Music[("📁 Music Library
/music")]
        end

        Nginx <-->|"Proxy TCP"| Server
        Server <-->|"Metadata Queries"| DB
        Server <-->|"Read Audio File"| Music
    end

    Client <-->|"SSL/TLS TCP :443"| Nginx

    classDef client fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f1f5f9
    classDef proxy fill:#0c4a6e,stroke:#38bdf8,stroke-width:2px,color:#f0f9ff
    classDef server fill:#164e3f,stroke:#34d399,stroke-width:2px,color:#ecfdf5
    classDef db fill:#7c2d12,stroke:#fb923c,stroke-width:2px,color:#fff7ed
    classDef store fill:#581c87,stroke:#c084fc,stroke-width:2px,color:#faf5ff
    classDef azureBox fill:#0f172a,stroke:#64748b,stroke-width:1.5px,color:#e2e8f0
    classDef dataBox fill:#1e1b4b,stroke:#818cf8,stroke-width:1px,color:#e0e7ff

    class Client client
    class Nginx proxy
    class Server server
    class DB db
    class Music store
    class Azure azureBox
    class DataLayer dataBox
```
## Tech Stack

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)


# Task 3B

## Overview
> Designed and solved five Capture The Flag (CTF) challenges - Web Exploitation, Cryptography, Reverse Engineering, Binary Exploitation (Pwn), and Digital Forensics, using a range of cybersecurity tools and techniques to identify, analyze, and exploit vulnerabilities.

## Tools Used 
![ExifTool](https://img.shields.io/badge/ExifTool-006699?style=for-the-badge)
![zsteg](https://img.shields.io/badge/zsteg-CC0000?style=for-the-badge)
![pwntools](https://img.shields.io/badge/pwntools-FF6F00?style=for-the-badge)
![hashlib](https://img.shields.io/badge/hashlib-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Z3 Solver](https://img.shields.io/badge/Z3_Solver-00599C?style=for-the-badge)
![secrets](https://img.shields.io/badge/secrets-3776AB?style=for-the-badge&logo=python&logoColor=white)



