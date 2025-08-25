# Architecture

```mermaid
graph LR
  Dev["Developer / PR"] -->|push/PR| GH["GitHub Actions"]
  GH -->|lint, build, Trivy, Selenium| Gates["Quality Gates"]
  Gates -->|main only| Runner["Self-Hosted Runner (your PC)"]
  Runner -->|Ansible (local)| Host["Local Host (127.0.0.1)"]
  Host --> Swarm["Docker (single-node Swarm)"]
  Swarm --> Traefik["Traefik (HTTP in lab mode)"]
  Swarm --> Indexer["Wazuh Indexer (OpenSearch)"]
  Swarm --> Manager["Wazuh Manager (API 55000)"]
  Swarm --> Dashboard["Wazuh Dashboard"]
  Traefik -->|HTTP 80| Dashboard
  Manager --> Indexer
  Agents[("Wazuh Agents")] --> Manager
