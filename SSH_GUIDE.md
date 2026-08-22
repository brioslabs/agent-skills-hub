# 🔑 Guía de Uso de SSH: `brioslabs/agent-skills-hub`

Esta guía contiene los comandos estándar para clonar, vincular y administrar el repositorio de skills utilizando **SSH**.

---

## 1. Clonar el Repositorio mediante SSH

Para clonar el repositorio completo en cualquier equipo con acceso SSH configurado:

```bash
git clone git@github.com:brioslabs/agent-skills-hub.git
```

---

## 2. Agregar como Submódulo Git (SSH)

Si deseas integrar este repositorio dentro de otro proyecto utilizando Git Submodules:

```bash
# 1. Navegar a la raíz de tu proyecto cliente
cd /ruta/a/tu-proyecto

# 2. Agregar el repositorio como submódulo SSH
git submodule add git@github.com:brioslabs/agent-skills-hub.git .agents/skills-hub

# 3. Crear la carpeta local de skills
mkdir -p .agents/skills

# 4. Vincular la skill deseada mediante un enlace simbólico (symlink)
ln -s ../skills-hub/skills/python-backend-expert .agents/skills/python-backend-expert
```

---

## 3. Configurar el Remoto SSH en el Repositorio Local

Para conectar el repositorio local (`agent-skills-hub`) con el origen en GitHub por SSH y publicar los cambios:

```bash
cd /home/bra/proyectos/agent-skills-hub

# Agregar el remoto SSH
git remote add origin git@github.com:brioslabs/agent-skills-hub.git

# Subir la rama main a GitHub
git push -u origin main
```

---

## 4. Verificar Autenticación SSH con GitHub

Para asegurarte de que tu clave SSH (`~/.ssh/id_ed25519` o `~/.ssh/id_rsa`) esté vinculada a tu cuenta de GitHub (`brioslabs`):

```bash
ssh -T git@github.com
```

> **Mensaje esperado de éxito:**
> `Hi brioslabs! You've successfully authenticated, but GitHub does not provide shell access.`
