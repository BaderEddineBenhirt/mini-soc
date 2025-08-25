# Mini SOC on Docker Swarm (Wazuh + Traefik + Ansible + CI/CD)

A production-ready, reproducible Mini SOC implementing **Wazuh** (Indexer, Manager, Dashboard) on **Docker Swarm** with **Traefik** (TLS/ACME), **Ansible** automation, **Trivy** scanning, and **Selenium** UI tests, delivered with a **GitHub Actions** pipeline and self-hosted runner. Designed to satisfy the challenge deliverables for correctness, security, reliability, and clarity. Requirements and scoring criteria are derived from the challenge PDF. :contentReference[oaicite:1]{index=1}

---

## Architecture Overview

```mermaid
flowchart LR
  Dev[Developer / PR] -->|push/PR| GH[GitHub Actions]
  GH -->|lint, build, Trivy, Selenium| Gates[Quality Gates]
  Gates -->|main only| SH[Self-Hosted Runner]
  SH -->|Ansible| Swarm[Docker Swarm Manager]
  Swarm --> Traefik
  Swarm --> Indexer[Wazuh Indexer (OpenSearch)]
  Swarm --> Manager[Wazuh Manager (API 55000)]
  Swarm --> Dashboard[Wazuh Dashboard]
  Traefik -->|HTTPS 443| Dashboard
  Manager --> Indexer
  Agents[(Wazuh Agents)] --> Manager
