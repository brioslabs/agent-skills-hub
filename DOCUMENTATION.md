# 📄 Documentación Técnica: Central Agent Skills Hub (`brioslabs`)

---

## 📌 1. Resumen Ejecutivo

El **Central Agent Skills Hub** de **`brioslabs`** es un repositorio centralizado diseñado para alojar, versionar y distribuir **Skills (habilidades organizadas)** para agentes de inteligencia artificial (Antigravity CLI, Cursor, Claude Code, Copilot, custom LLM pipelines, etc.).

Cada skill encapsula el conocimiento experto, reglas críticas, plantillas de código y listas de verificación para que cualquier agente en cualquier proyecto pueda ejecutar tareas con los estándares de calidad definidos por `brioslabs`.

---

## 📂 2. Estructura del Repositorio

```text
agent-skills-hub/
├── .github/
│   └── workflows/
│       ├── validate-skills.yml     # CI: Valida la sintaxis del YAML Frontmatter
│       └── generate-index.yml      # CI: Genera y actualiza index.json automáticamente
├── skills/
│   ├── python-backend-expert/      # Skill experta en Backend con Python & FastAPI
│   │   ├── SKILL.md
│   │   ├── assets/
│   │   │   └── fastapi_template.py # Plantilla base de aplicación FastAPI
│   │   └── references/
│   │       └── security_checklist.md # Lista de comprobación de seguridad
│   ├── frontend-expert/            # Skill experta en Frontend Web Moderno
│   │   └── SKILL.md
│   └── skill-creator/              # Skill meta para crear nuevas habilidades
│       └── SKILL.md
├── scripts/
│   ├── sync-skills.py              # Script multiplataforma en Python para descargar skills
│   └── sync-skills.sh              # Script cliente en Bash
├── index.json                      # Registro central autogenerado con el catálogo de skills
├── README.md                       # Guía rápida para desarrolladores y agentes
├── DOCUMENTATION.md                # Esta documentación técnica
└── .git/                           # Repositorio Git local (rama 'main')
```

---

## 🛠️ 3. Componentes Creados

### A. Catálogo Central (`index.json`)
Consolida el registro de todas las skills disponibles para permitir el descubrimiento dinámico mediante APIs o agentes de IA.

```json
{
  "author": "brioslabs",
  "repository": "https://github.com/brioslabs/agent-skills-hub",
  "updated_at": "2026-08-17T00:00:00Z",
  "skills": [
    {
      "name": "python-backend-expert",
      "description": "Guía y buenas prácticas para construir APIs robustas y escalables con Python y FastAPI.",
      "version": "1.0.0",
      "path": "skills/python-backend-expert/SKILL.md",
      "raw_url": "https://raw.githubusercontent.com/brioslabs/agent-skills-hub/main/skills/python-backend-expert/SKILL.md"
    },
    ...
  ]
}
```

### B. Herramientas de Sincronización (`scripts/sync-skills.py` y `scripts/sync-skills.sh`)
Permite instalar o actualizar skills en cualquier proyecto local hacia la carpeta `.agents/skills/`. Cuenta con un mecanismo de *fallback* automático que permite probar skills de forma local antes de hacer `push` a GitHub.

### C. Integración Continua (GitHub Actions)
- **`validate-skills.yml`**: Inspecciona cada commit para asegurar que los archivos `SKILL.md` cumplan con el encabezado YAML `---`.
- **`generate-index.yml`**: Genera automáticamente `index.json` en cada `push` que modifique la carpeta `skills/`.

---

## 🚀 4. Guía para Crear el Repositorio en GitHub (`brioslabs`)

Ejecuta los siguientes comandos desde tu terminal para subir este repositorio a tu cuenta de GitHub:

### Opción A: Usando GitHub CLI (`gh`)

```bash
cd /home/bra/proyectos/agent-skills-hub

# Crear el repositorio público en GitHub e impulsar el código
gh repo create brioslabs/agent-skills-hub --public --source=. --remote=origin --push
```

---

### Opción B: Usando Git Tradicional

1. Ve a [GitHub - New Repository](https://github.com/new).
2. Nombra el repositorio como **`agent-skills-hub`** bajo la cuenta **`brioslabs`**.
3. Deja el repositorio como **Público** y NO inicialices con README (ya lo creamos).
4. Corre los siguientes comandos en tu consola:

```bash
cd /home/bra/proyectos/agent-skills-hub

# Conectar con el repositorio remoto
git remote add origin https://github.com/brioslabs/agent-skills-hub.git

# Subir la rama main
git push -u origin main
```

---

## 💻 5. Uso en Otros Proyectos

Cualquier proyecto puede obtener las skills ejecutando:

```bash
# Descargar skill específica de Python Backend
python3 scripts/sync-skills.py python-backend-expert

# Descargar TODAS las skills disponibles
python3 scripts/sync-skills.py --all
```
