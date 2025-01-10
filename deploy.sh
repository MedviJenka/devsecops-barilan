#!/bin/bash
minikube start
minikube addons enable ingress

MINIKUBE_IP=$(minikube ip)
ENTRY="$MINIKUBE_IP app.local.com"

if ! grep -qxF "$ENTRY" /etc/hosts; then
  echo "$ENTRY" | sudo tee -a /etc/hosts
  echo "Entry added: $ENTRY"
else
  echo "Entry already exists: $ENTRY"
fi
grep -qxF "$(minikube ip) ai-bot.local.com" /etc/hosts || echo "$(minikube ip) ai-bot.local.com" | sudo tee -a /etc/hosts
kubectl /k8s/apply -f .
curl http://app.local.com/health