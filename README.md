# mcp-projects

Colección de servidores MCP (Model Context Protocol) de prueba.

## Proyectos

| Proyecto | Descripción |
|---|---|
| [weather](./weather/) | Servidor MCP para consulta del clima |
| [mcp-ckan](./mcp-ckan/) | Servidor MCP para datos abiertos CKAN |
| [mcp-datos-uruguay](./mcp-datos-uruguay/) | Servidor MCP con datasets de Uruguay (compras, delitos) |
| [mcp-chat-gateway](./mcp-chat-gateway/) | Gateway de chat para MCP |

## Clonar un proyecto individual

```bash
git clone --filter=blob:none --sparse https://github.com/Abare/mcp-projects
cd mcp-projects
git sparse-checkout set weather   # o el proyecto que quieras
```

## Setup de cada proyecto

Cada proyecto usa [uv](https://github.com/astral-sh/uv):

```bash
cd <proyecto>
uv sync
```
