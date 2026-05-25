## Sobre este servidor

Este servidor MCP consulta el clima de Estados Unidos usando la API del National Weather Service (NWS).

## Tools disponibles

- **`get_alerts`** → recibe un código de estado de EEUU (ej: `CA`, `NY`, `TX`) y devuelve las alertas meteorológicas activas
- **`get_forecast`** → recibe latitud y longitud y devuelve el pronóstico del tiempo

## Limitaciones

La API del NWS solo funciona para Estados Unidos, no para Uruguay ni otros países.

## Ejemplo de uso

| Tool | Parámetro | Ejemplo |
|---|---|---|
| `get_alerts` | state | `CA` (California) |
| `get_forecast` | latitude / longitude | `40.7128` / `-74.0060` (Nueva York) |