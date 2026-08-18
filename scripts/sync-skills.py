#!/usr/bin/env python3
"""
Sync Skills Script for brioslabs/agent-skills-hub
Descarga y actualiza skills desde el repositorio central de brioslabs en GitHub.
"""

import sys
import os
import json
import urllib.request
from pathlib import Path
import argparse

REPO_AUTHOR = "brioslabs"
REPO_NAME = "agent-skills-hub"
RAW_BASE_URL = f"https://raw.githubusercontent.com/{REPO_AUTHOR}/{REPO_NAME}/main"
DEFAULT_TARGET_DIR = Path(".agents/skills")

def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "brioslabs-skill-sync"})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

def download_file(url: str, dest_path: Path, local_fallback: Path = None):
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "brioslabs-skill-sync"})
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            with open(dest_path, "wb") as f:
                f.write(content)
        print(f"  [✓] Descargado de GitHub: {dest_path}")
    except Exception as e:
        if local_fallback and local_fallback.exists():
            with open(local_fallback, "rb") as sf, open(dest_path, "wb") as df:
                df.write(sf.read())
            print(f"  [✓] Copiado localmente (fallback): {dest_path}")
        else:
            print(f"  [✗] Error descargando {url}: {e}")

def sync_skill(skill_name: str, target_dir: Path):
    print(f"\n📦 Sincronizando skill '{skill_name}'...")
    skill_dir = target_dir / skill_name
    
    # 1. Descargar SKILL.md
    skill_md_url = f"{RAW_BASE_URL}/skills/{skill_name}/SKILL.md"
    local_skill_md = Path("skills") / skill_name / "SKILL.md"
    download_file(skill_md_url, skill_dir / "SKILL.md", local_fallback=local_skill_md)

def main():
    parser = argparse.ArgumentParser(description="Sincronizador de Skills de brioslabs")
    parser.add_argument("skills", nargs="*", help="Nombres de las skills a sincronizar")
    parser.add_argument("--all", action="store_true", help="Sincronizar todas las skills disponibles")
    parser.add_argument("--target", type=str, default=".agents/skills", help="Directorio de destino (default: .agents/skills)")
    
    args = parser.parse_args()
    target_dir = Path(args.target)
    
    # Cargar índice
    index_url = f"{RAW_BASE_URL}/index.json"
    try:
        index_data = fetch_json(index_url)
        available_skills = {s["name"]: s for s in index_data.get("skills", [])}
    except Exception as e:
        print(f"⚠️ No se pudo obtener el índice remoto ({e}). Intentando descarga directa...")
        available_skills = {}

    if args.all or not args.skills:
        if available_skills:
            skills_to_sync = list(available_skills.keys())
        else:
            skills_to_sync = ["python-backend-expert", "frontend-expert", "skill-creator"]
    else:
        skills_to_sync = args.skills

    print(f"🚀 Iniciando sincronización de {len(skills_to_sync)} skill(s) desde @{REPO_AUTHOR}...")
    for skill_name in skills_to_sync:
        sync_skill(skill_name, target_dir)
        
    print(f"\n✨ Sincronización completada. Skills listas en '{target_dir}'.")

if __name__ == "__main__":
    main()
