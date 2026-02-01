#!/bin/bash
set -e

ENVIRONMENT=$1

if [ -z "$ENVIRONMENT" ]; then
  echo "Uso: $0 <environment>"
  exit 1
fi

echo "🚀 Deploying to $ENVIRONMENT"

echo "📋 Running tests..."
python -m pytest airflow_project/tests -v

GIT_SHA=${GITHUB_SHA:-local}

if [ "$ENVIRONMENT" = "prod" ]; then
  docker build -t airflow-prod:$GIT_SHA .
fi

echo "✅ Deployment terminado"
