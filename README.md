# 🚀 Agent Skills Hub (`brioslabs`)

Repositorio centralizado de **Skills para Agentes de IA** (Antigravity CLI, Cursor, Claude Code, Copilot, etc.) mantenido por **brioslabs**.

Este repositorio permite definir, perfeccionar y distribuir habilidades especializadas para agentes de desarrollo. Cualquier proyecto puede sincronizar estas skills localmente o consumirlas dinámicamente desde GitHub.

---

## 📂 Estructura del Repositorio

```text
agent-skills-hub/
├── .github/
│   └── workflows/
│       ├── validate-skills.yml     # Valida sintaxis YAML de cada SKILL.md
│       └── generate-index.yml      # Autogenera index.json en cada push
├── skills/
│   ├── python-backend-expert/      # Skill experta en Python & FastAPI
│   │   ├── SKILL.md
│   │   ├── assets/
│   │   │   └── fastapi_template.py
│   │   └── references/
│   │       └── security_checklist.md
│   ├── frontend-expert/            # Skill experta en Frontend moderno
│   │   └── SKILL.md
│   └── skill-creator/              # Skill meta para crear nuevas habilidades
│       └── SKILL.md
├── scripts/
│   ├── sync-skills.py              # Script cliente en Python (Multiplataforma)
│   └── sync-skills.sh              # Script cliente en Bash
├── index.json                      # Catálogo autogenerado de skills
└── README.md
```

---

## 🛠️ Cómo Usar las Skills en Cualquier Proyecto

### Opción 1: Descarga Directa con Python (`sync-skills.py`)

Copia el script `sync-skills.py` a tu proyecto o descárgalo directamente:

```bash
# Descargar el script en tu proyecto
curl -sSL https://raw.githubusercontent.com/brioslabs/agent-skills-hub/main/scripts/sync-skills.py -o sync-skills.py

# Descargar una o varias skills específicas (se guardan en .agents/skills/)
python3 sync-skills.py python-backend-expert frontend-expert

# Descargar TODAS las skills disponibles
python3 sync-skills.py --all
```

### Opción 2: Usar Script Bash (`sync-skills.sh`)

```bash
curl -sSL https://raw.githubusercontent.com/brioslabs/agent-skills-hub/main/scripts/sync-skills.sh | bash -s python-backend-expert
```

### Opción 3: Git Submodule

```bash
# Agregar como submódulo en la carpeta del agente
git submodule add https://github.com/brioslabs/agent-skills-hub.git .agents/skills-hub

# Crear enlace simbólico a la skill deseada
mkdir -p .agents/skills
ln -s ../skills-hub/skills/python-backend-expert .agents/skills/python-backend-expert
```

---

## ✍️ Cómo Crear una Nueva Skill

1. Revisa la guía en [`skills/skill-creator/SKILL.md`](skills/skill-creator/SKILL.md).
2. Crea una nueva carpeta en `skills/{nombre-de-tu-skill}/`.
3. Añade el archivo `SKILL.md` incluyendo el encabezado YAML obligatorio:

```yaml
---
name: tu-skill-name
description: >
  Descripción corta de la habilidad.
  Trigger: Cuándo el agente debe cargar esta skill.
license: Apache-2.0
metadata:
  author: brioslabs
  version: "1.0.0"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---
```

4. Haz `push` a `main`. GitHub Actions validará el archivo y actualizará `index.json` automáticamente.

---

## 📜 Licencia

Apache-2.0 © [brioslabs](https://github.com/brioslabs)
