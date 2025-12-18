import os
import requests
from dotenv import load_dotenv

load_dotenv()
LINEAR_API_KEY = os.getenv("LINEAR_API_KEY")

if not LINEAR_API_KEY:
    raise ValueError("⚠️ Falta la clave LINEAR_API_KEY en tu archivo .env")

LINEAR_API_URL = "https://api.linear.app/graphql"
HEADERS = {"Authorization": LINEAR_API_KEY, "Content-Type": "application/json"}


def crear_ticket(titulo, descripcion, team_id=None, prioridad="medium"):
    """
    Crea un nuevo ticket en Linear.
    """
    mutation = """
    mutation CrearTicket($input: IssueCreateInput!) {
      issueCreate(input: $input) {
        success
        issue {
          id
          title
          identifier
          url
        }
      }
    }
    """
    prioridad_map = {"low": 0, "medium": 1, "high": 2, "urgent": 3}
    variables = {
        "input": {
            "title": titulo,
            "description": descripcion,
            "priority": prioridad_map.get(prioridad, 1),
        }
    }
    if team_id:
        variables["input"]["teamId"] = team_id

    response = requests.post(LINEAR_API_URL, headers=HEADERS, json={"query": mutation, "variables": variables})
    data = response.json()
    if "errors" in data:
        print("❌ Error al crear ticket:", data["errors"])
        return None
    issue = data["data"]["issueCreate"]["issue"]
    print(f"✅ Ticket creado: {issue['identifier']} - {issue['url']}")
    return issue


def listar_tickets(limit=5):
    """
    Lista los últimos tickets creados.
    """
    query = """
    query ListarTickets($first: Int!) {
      issues(first: $first) {
        nodes {
          id
          identifier
          title
          state {
            name
          }
          url
        }
      }
    }
    """
    variables = {"first": limit}
    response = requests.post(LINEAR_API_URL, headers=HEADERS, json={"query": query, "variables": variables})
    data = response.json()
    if "errors" in data:
        print("❌ Error al listar tickets:", data["errors"])
        return []
    issues = data["data"]["issues"]["nodes"]
    print("\n📋 Últimos tickets:")
    for issue in issues:
        print(f"- [{issue['state']['name']}] {issue['identifier']}: {issue['title']} → {issue['url']}")
    return issues


if __name__ == "__main__":
    # Prueba rápida
    listar_tickets()
    # crear_ticket("Test de integración Gemini", "Probando creación automática desde agente.")
