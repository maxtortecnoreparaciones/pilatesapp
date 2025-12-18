import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# --- Cargar variables de entorno ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("⚠️ Falta la clave GEMINI_API_KEY en tu archivo .env")

client = genai.Client(api_key=api_key)

# --- Configuración del Proyecto ---
PROYECTO_PATH = Path(__file__).resolve().parent
MODEL = "gemini-2.0-flash"  # puedes usar "gemini-1.5-flash" o "gemini-2.5-flash"

# --- Definición de los Agentes Técnicos ---
AGENTES = {
    "arquitecto": "Diseña la estructura modular del proyecto, define buenas prácticas y recomienda estándares de arquitectura limpia.",
    "backend": "Crea y valida la base de datos, API, modelos y lógica de negocio. Propone migraciones y relaciones óptimas.",
    "frontend": "Diseña la capa visual (UI/UX) y define componentes reutilizables. Sugiere frameworks y estructura de carpetas.",
    "tester": "Evalúa cobertura, casos de prueba, y propone pruebas automatizadas (unitarias e integradas).",
    "seguridad": "Evalúa vulnerabilidades, manejo de variables sensibles, permisos y cifrado.",
}

# --- Función para analizar el proyecto ---
def analizar_proyecto():
    """
    Lee la estructura y el contenido de los archivos del proyecto
    para que Gemini los evalúe y genere un plan de desarrollo coordinado.
    """
    estructura = []
    for ruta in PROYECTO_PATH.rglob("*"):
        if ruta.is_file() and ruta.suffix in [".py", ".sql", ".env", ".txt"]:
            try:
                with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
                    contenido = f.read()[:1500]  # límite por archivo
                estructura.append(f"📄 {ruta.name}\n{contenido}\n---")
            except Exception as e:
                print(f"Error leyendo {ruta}: {e}")

    prompt = f"""
Eres el **equipo de desarrollo AXIOM-PILATES**, compuesto por estos agentes:

{chr(10).join([f"- {rol.upper()}: {desc}" for rol, desc in AGENTES.items()])}

Tu tarea es analizar el proyecto actual de una **aplicación de pilates con sistema multiagente**.
Evalúa los archivos existentes, detecta qué falta, y genera un plan colaborativo de desarrollo.

Archivos actuales del proyecto:
{chr(10).join(estructura)}

Responde con:
1️⃣ Estado actual (madurez técnica, estructura, modularidad).  
2️⃣ Riesgos o incoherencias.  
3️⃣ Qué archivos o módulos deben crearse a continuación (con prioridad).  
4️⃣ Cómo deberían coordinarse los agentes para avanzar en el desarrollo.  
5️⃣ Sugerencias técnicas (nombres de archivos, frameworks, herramientas o scripts base).
    """

    try:
        respuesta = client.models.generate_content(
            model=MODEL,
            contents=prompt,
        )
        print("\n📊 INFORME DE ANÁLISIS TÉCNICO MULTIAGENTE:\n")
        print(respuesta.text)

    except Exception as e:
        print(f"\n❌ ERROR al conectar con la API de Gemini: {e}")
        print("Verifica que tu GEMINI_API_KEY es válida y que el modelo está disponible.")


if __name__ == "__main__":
    analizar_proyecto()
