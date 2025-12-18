# dev_team.py (Actualizado para 3 Agentes)
from enum import Enum

# Define los Roles de Usuario/Agente para la Validación
class AgentRole(Enum):
    """Roles de Agentes utilizados para validar la arquitectura y el código."""
    ARQUITECTO_SEGURIDAD = "Arquitecto Senior y Especialista en Seguridad"
    BACKEND_ESPECIALISTA = "Ingeniero Backend Senior (Django y DB)"
    PRODUCT_OWNER = "Dueño de Producto y Especialista en KPIs"

# Define las Tools (Funciones) a las que cada Agente tiene acceso.
# Estas herramientas representan la capacidad de acceso a datos para la validación.
TOOL_ACCESS = {
    AgentRole.ARQUITECTO_SEGURIDAD: [
        "check_permissions_segregation",
        "validate_access_control_flow",
        "audit_sensitive_data_storage",
    ],
    AgentRole.BACKEND_ESPECIALISTA: [
        "query_db_model_relationships",
        "check_api_endpoint_design",
        "validate_migration_logic",
    ],
    AgentRole.PRODUCT_OWNER: [
        "evaluate_kpi_feasibility",
        "check_user_story_coverage",
        "validate_multi_sede_logic",
    ]
}

def get_agent_tools(role: AgentRole) -> list[str]:
    """Devuelve la lista de tools a las que un rol de agente tiene acceso."""
    return TOOL_ACCESS.get(role, [])

if __name__ == "__main__":
    print("--- Configuración de Agentes de Validación AXIOM ---")
    # ... (El código de prueba permanece igual)