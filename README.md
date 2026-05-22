# Python Basics Quest

App educativa en Streamlit para aprender Python escribiendo código: lecciones guiadas, ejemplos para Maya y arena de práctica.

## Ejecutar en local

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app.py
```

Abre la URL que muestra la terminal (normalmente `http://localhost:8501`).

## Desplegar en Streamlit Community Cloud

### 1. Subir el repo a GitHub

El repositorio debe incluir al menos:

```
app.py              ← archivo principal (entry point)
requirements.txt
assets/theme.css
.streamlit/config.toml
```

Comprueba que todo esté commiteado:

```powershell
git add app.py requirements.txt assets/ .streamlit/ README.md .gitignore .python-version
git commit -m "Preparar deploy en Streamlit Cloud"
git push origin main
```

### 2. Crear la app en Streamlit Cloud

1. Entra en [share.streamlit.io](https://share.streamlit.io) e inicia sesión con GitHub.
2. Pulsa **Create app**.
3. Elige tu repositorio, rama `main` y archivo principal **`app.py`**.
4. En **Advanced settings** (opcional):
   - **Python version:** 3.11
5. Pulsa **Deploy**.

La primera build puede tardar uno o dos minutos. Cuando termine, tendrás una URL pública del tipo:

`https://TU-APP.streamlit.app`

### 3. Actualizar la app publicada

Cada `git push` a la rama conectada vuelve a desplegar la app automáticamente.

## Estructura del proyecto

| Archivo / carpeta | Uso |
|-------------------|-----|
| `app.py` | Lógica y UI de la aplicación |
| `requirements.txt` | Dependencias Python |
| `assets/theme.css` | Estilos personalizados |
| `.streamlit/config.toml` | Tema y ajustes de servidor |

## Secretos (opcional)

Esta app no requiere API keys ni variables de entorno. Si más adelante las necesitas:

1. Crea `.streamlit/secrets.toml` en local (está en `.gitignore`).
2. En Streamlit Cloud: **App settings → Secrets** y pega el mismo contenido TOML.

## Notas

- **Vercel** no es compatible con Streamlit (necesita un servidor Python persistente). Usa Streamlit Cloud, Render o similar.
- Si el deploy falla, revisa los **Logs** en el panel de Streamlit Cloud; casi siempre es un error en `requirements.txt` o en la ruta de `app.py`.
