#!/bin/bash

# Cambia al directorio del repositorio
cd /c/Python_WORLD/Python_Elementary

# Agrega todos los cambios
git add .

# Configura el mensaje del commit
COMMIT_MESSAGE="Automated commit: $(date +'%Y-%m-%d %H:%M:%S')"

# Hace el commit
git commit -m "$COMMIT_MESSAGE"

# Empuja los cambios a GitHub
git push origin master

echo "Changes have been pushed to GitHub!"




