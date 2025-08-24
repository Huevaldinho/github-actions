# github-actions

This project is a hands-on learning journey through modern DevOps and cloud-native practices. The goal is to build, test, and deploy a FastAPI application, progressively evolving from a simple CI/CD pipeline to a microservices architecture orchestrated by Kubernetes.

### Core Technologies
- **Application**: FastAPI, Python
- **Testing**: Pytest
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Infrastructure as Code**: Terraform
- **Orchestration**: Kubernetes (GKE)

---

### Project Roadmap

#### ✅ Phase 1: CI & Containerization
- [x] Initial FastAPI application setup
- [ ] Implement comprehensive tests with `pytest` and coverage reporting
- [ ] Create a multi-stage `Dockerfile` for lean, secure images
- [ ] Set up a CI workflow (`ci.yml`) to lint, test, and build on Pull Requests
- [ ] Post test results and coverage as a comment in Pull Requests

#### ⬜ Phase 2: IaC & Continuous Deployment
- [ ] Use Terraform to provision a cloud VM for a self-hosted GitHub Actions runner
- [ ] Install the runner and Docker daemon on the provisioned VM
- [ ] Create a CD workflow (`deploy.yml`) that triggers on merge to `main`
- [ ] Push tagged Docker images to a container registry (e.g., GHCR)
- [ ] Deploy the application container to the self-hosted runner

#### ⬜ Phase 3: Kubernetes Orchestration
- [ ] Evolve Terraform code to provision a GKE (Google Kubernetes Engine) cluster
- [ ] Write Kubernetes manifests (`Deployment`, `Service`, `Ingress`) for the application
- [ ] Update the CD workflow to deploy the application to GKE
- [ ] Begin refactoring the monolith into a 2-service microservices architecture

#### ⬜ Phase 4: Advanced Concepts & Observability
- [ ] Implement structured logging across services
- [ ] Introduce monitoring and metrics (e.g., Prometheus/Grafana)
- [ ] Set up email notifications for build and deployment status