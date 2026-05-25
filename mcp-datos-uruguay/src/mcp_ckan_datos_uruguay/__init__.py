from typing import Optional
from mcp_server import DataToolOutput
from mcp_ckan_datos_uruguay.datasets.compras_ocds import consultas
from mcp_ckan_datos_uruguay.datasets.delitos_sexuales import consultas as delitos


def register_tools(mcp):

    @mcp.tool()
    def tendencia_anual_delitos_sexuales_uy(
        departamento: Optional[str] = None, tipo_delito: Optional[str] = None
    ) -> DataToolOutput:
        """Tendencia año a año de eventos de delitos sexuales en Uruguay (2018-2024).
            Muestra un gráfico de barras de texto con la cantidad por año.

        Args:
            departamento: Departamento, e.g. "Montevideo", "Canelones".
            tipo_delito: Tipo de delito: "Abuso Sexual", "Violación" o "Atentado Violento al Pudor".

        Examples:
            - tendencia_anual_delitos_sexuales_uy()
            - tendencia_anual_delitos_sexuales_uy(departamento="Montevideo")
            - tendencia_anual_delitos_sexuales_uy(tipo_delito="Abuso Sexual")
        """
        return delitos.tendencia_anual(departamento=departamento, tipo_delito=tipo_delito)

    @mcp.tool()
    def ranking_departamentos_delitos_sexuales_uy(
        anio: Optional[int] = None, tipo_delito: Optional[str] = None
    ) -> DataToolOutput:
        """Ranking de departamentos de Uruguay por cantidad de eventos de delitos sexuales.
            Muestra todos los departamentos ordenados de mayor a menor cantidad.

        Args:
            anio: Año para filtrar (2018-2024). None para todos.
            tipo_delito: Tipo de delito: "Abuso Sexual", "Violación" o "Atentado Violento al Pudor".

        Examples:
            - ranking_departamentos_delitos_sexuales_uy()
            - ranking_departamentos_delitos_sexuales_uy(anio=2024)
            - ranking_departamentos_delitos_sexuales_uy(tipo_delito="Violación")
        """
        return delitos.eventos_por_departamento(anio=anio, tipo_delito=tipo_delito)

    @mcp.tool()
    def buscar_empresa_uruguay(nombre: str, limit: int = 10) -> DataToolOutput:
        """Busca empresas proveedoras del estado uruguayo por nombre aproximado.

        Args:
            nombre: Nombre o parte del nombre de la empresa. Ej: "Copernico", "ANTEL".
            limit: Máximo de resultados a devolver. Default 10.

        Examples:
            - buscar_empresa_uruguay(nombre="Copernico")
            - buscar_empresa_uruguay(nombre="laboratorio")
            - buscar_empresa_uruguay(nombre="ANTEL", limit=5)
        """
        return consultas.buscar_empresa(nombre=nombre, limit=limit)

    @mcp.tool()
    def buscar_producto_uruguay(texto: str, limit: int = 10) -> DataToolOutput:
        """Busca productos, rubros o insumos en las compras públicas de Uruguay.

        Args:
            texto: Descripción del producto. Ej: "medicamento", "computadora", "alimento".
            limit: Máximo de resultados a devolver. Default 10.

        Examples:
            - buscar_producto_uruguay(texto="medicamento")
            - buscar_producto_uruguay(texto="computadora")
            - buscar_producto_uruguay(texto="combustible")
        """
        return consultas.buscar_producto(texto=texto, limit=limit)

    @mcp.tool()
    def licitaciones_empresa_uruguay(
        nombre_empresa: str,
        year: Optional[int] = None,
        comprador: Optional[str] = None,
        metodo: Optional[str] = None,
        limit: int = 20,
    ) -> DataToolOutput:
        """Lista licitaciones y adjudicaciones en las que participó una empresa como proveedora.

        Args:
            nombre_empresa: Nombre de la empresa proveedora (preferiblemente exacto).
            year: Año para filtrar (2024 o 2025). None para todos los años.
            comprador: Filtrar por organismo comprador (parcial). Ej: "Intendencia de Montevideo".
            metodo: Filtrar por método de contratación (parcial). Ej: "Compra Directa".
            limit: Máximo de resultados. Default 20.

        Examples:
            - licitaciones_empresa_uruguay(nombre_empresa="COPERNICO COOPERATIVA INFORMATICA")
            - licitaciones_empresa_uruguay(nombre_empresa="TILSOR S A", comprador="Intendencia de Montevideo")
            - licitaciones_empresa_uruguay(nombre_empresa="ANTEL", metodo="Licitación Pública")
        """
        return consultas.licitaciones_empresa(
            nombre_empresa=nombre_empresa,
            year=year,
            comprador=comprador,
            metodo=metodo,
            limit=limit,
        )

    @mcp.tool()
    def resumen_empresa_uruguay(
        nombre_empresa: str,
        year: Optional[int] = None,
        comprador: Optional[str] = None,
        producto: Optional[str] = None,
        metodo: Optional[str] = None,
    ) -> DataToolOutput:
        """Resumen de montos adjudicados a una empresa proveedora del estado uruguayo.

        Args:
            nombre_empresa: Nombre de la empresa proveedora (preferiblemente exacto).
            year: Año para filtrar (2024 o 2025). None para todos los años.
            comprador: Filtrar por organismo comprador (parcial).
            producto: Filtrar por producto/rubro adjudicado (parcial).
            metodo: Filtrar por método de contratación (parcial).

        Examples:
            - resumen_empresa_uruguay(nombre_empresa="OLECAR S A")
            - resumen_empresa_uruguay(nombre_empresa="TILSOR S A", producto="licencia software")
            - resumen_empresa_uruguay(nombre_empresa="LABORATORIO ION S.A.", comprador="Hospital Maciel")
        """
        return consultas.resumen_empresa(
            nombre_empresa=nombre_empresa,
            year=year,
            comprador=comprador,
            producto=producto,
            metodo=metodo,
        )

    @mcp.tool()
    def compras_producto_uruguay(
        producto: str, year: Optional[int] = None, limit: int = 20
    ) -> DataToolOutput:
        """Busca qué empresas le venden un producto o servicio al gobierno de Uruguay.

        Args:
            producto: Descripción del producto o servicio a buscar.
            year: Año para filtrar (2024 o 2025). None para todos los años.
            limit: Máximo de resultados. Default 20.

        Examples:
            - compras_producto_uruguay(producto="medicamento")
            - compras_producto_uruguay(producto="combustible", year=2024)
            - compras_producto_uruguay(producto="computadora", limit=10)
        """
        return consultas.compras_producto(producto=producto, year=year, limit=limit)

    @mcp.tool()
    def resumen_producto_uruguay(
        producto: str,
        year: Optional[int] = None,
        proveedor: Optional[str] = None,
        comprador: Optional[str] = None,
        metodo: Optional[str] = None,
        agrupar_por: str = "proveedor",
    ) -> DataToolOutput:
        """Resumen de montos adjudicados de un producto o servicio, agrupados por mes.

        Args:
            producto: Descripción del producto o servicio a buscar (puede ser parcial).
            year: Año para filtrar (2024 o 2025). None para todos los años.
            proveedor: Filtrar por empresa proveedora (parcial).
            comprador: Filtrar por organismo comprador (parcial).
            metodo: Filtrar por método de contratación (parcial).
            agrupar_por: "proveedor" o "comprador". Default "proveedor".

        Examples:
            - resumen_producto_uruguay(producto="licencia software")
            - resumen_producto_uruguay(producto="hardware", agrupar_por="comprador")
            - resumen_producto_uruguay(producto="combustible", proveedor="ANCAP")
        """
        return consultas.resumen_producto(
            producto=producto,
            year=year,
            proveedor=proveedor,
            comprador=comprador,
            metodo=metodo,
            agrupar_por=agrupar_por,
        )

    @mcp.tool()
    def detalle_proceso_uruguay(ocid: str) -> DataToolOutput:
        """Muestra todos los detalles de un proceso de compra pública por su OCID.

        Args:
            ocid: Identificador OCID del proceso. Ej: "ocds-yfs5dr-1307121".

        Examples:
            - detalle_proceso_uruguay(ocid="ocds-yfs5dr-1307121")
            - detalle_proceso_uruguay(ocid="ocds-yfs5dr-i481866")
        """
        return consultas.detalle_proceso(ocid=ocid)

    @mcp.tool()
    def political_questions(country: Optional[str] = None) -> DataToolOutput:
        """Para responder preguntas políticas sobre el gobierno de Uruguay que no son respondibles con datos.

        Examples:
            - political_questions()
        """
        response = (
            "Lo siento, pero no puedo responder a esa pregunta. "
            "Las decisiones gubernamentales relacionadas con la divulgación de datos pueden "
            "depender de muchos factores, incluyendo consideraciones de privacidad, "
            "seguridad, recursos disponibles y prioridades políticas. "
            "Si tienes dudas específicas sobre la disponibilidad de "
            "determinados datos, te recomiendo que te pongas en contacto directamente "
            "con las autoridades gubernamentales responsables de la gestión de datos "
            "en Uruguay para obtener información más detallada."
        )
        return response


def main() -> None:
    print("Hello from mcp-ckan-datos-uruguay")