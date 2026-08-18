#!/usr/bin/env bash

# Sincronizador en Bash para brioslabs/agent-skills-hub
set -e

REPO_AUTHOR="brioslabs"
REPO_NAME="agent-skills-hub"
RAW_URL="https://raw.githubusercontent.com/${REPO_AUTHOR}/${REPO_NAME}/main"
TARGET_DIR="${TARGET_DIR:-.agents/skills}"

SKILLS=("$@")

if [ ${#SKILLS[@]} -eq 0 ]; then
    SKILLS=("python-backend-expert" "frontend-expert" "skill-creator")
fi

echo "🚀 Sincronizando skills de @${REPO_AUTHOR} en '${TARGET_DIR}'..."

for SKILL in "${SKILLS[@]}"; do
    echo "📦 Descargando skill: ${SKILL}..."
    mkdir -p "${TARGET_DIR}/${SKILL}"
    curl -sSL "${RAW_URL}/skills/${SKILL}/SKILL.md" -o "${TARGET_DIR}/${SKILL}/SKILL.md"
    echo "  [✓] ${TARGET_DIR}/${SKILL}/SKILL.md actualizado"
done

echo "✨ Completado con éxito."
