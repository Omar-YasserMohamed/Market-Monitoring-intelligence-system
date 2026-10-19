# ==============================================================================
# Git Branching Strategy & Workflow Guide
# Project: Real-Time Food Delivery Monitoring & Historical Analytics Platform
# ==============================================================================

## 1. Branch Structure
- `main`: Production-ready code ONLY. Protected branch. No one pushes directly to main.
- `feature/<name>`: Dedicated branch for each team member's specific component.

### Official Team Branches:
- `feature/streaming-kafka`   -> Person 1 (Live Simulator, Kafka, MinIO Bronze)
- `feature/spark-etl`         -> Person 2 (Historical Data, Spark Bronze->Silver->Gold)
- `feature/dwh-postgres`      -> Person 3 (PostgreSQL Star Schema, DDL, Idempotent Loader)
- `feature/airflow-bi`        -> Person 4 (Airflow DAGs, Data Quality Tests, Metabase)

---

## 2. Daily Workflow for Each Team Member (3 Simple Steps)

### Step 1: Switch to your branch before writing code
```bash
# Example for Person 1:
git checkout -b feature/streaming-kafka
```

### Step 2: Save your work locally and push to your branch
```bash
git add .
git commit -m "feat: describe what you added in one sentence"
git push -u origin feature/streaming-kafka
```

### Step 3: Merging into `main` (Pull Request)
1. Go to GitHub in your browser.
2. Click **Compare & pull request**.
3. Have at least one teammate review and click **Merge**.
4. Everyone updates their local `main`:
```bash
git checkout main
git pull origin main
```

---

## 3. Golden Commit Rules
1. Never commit `.env` files, passwords, or personal credentials.
2. Never commit large data dumps (`.json` or `.parquet` files). They belong in MinIO.
3. Keep commit messages concise and informative (e.g., `feat: add kafka producer`, `fix: handle null order timestamps`).
