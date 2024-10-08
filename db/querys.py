from .conexion import ConexionMysql

class Query:
    def __init__(self) -> None:
        self.db = ConexionMysql()
        self.db.connection()
    
    def insertMoto(self, moto, descripcion, modelo, marca):
        query = """
                    INSERT INTO motos(nombre, descripcion, modelo, marca) VALUES(%s, %s, %s, %s)
                """
        values = (moto, descripcion, modelo, marca)
        self.db.execute_query(query, values)
        self.db.close_connection()
        
    def selectCategory(self):
        query = """
                    SELECT * FROM categorias
                """
        result = self.db.execute_query(query)
        print("hola ", result)
        self.db.close_connection()
        return result
    
    def selectMoto(self):
        query = """
                    SELECT idmotos, CONCAT_WS(' ', nombre, descripcion, modelo, marca) AS nombre_moto FROM motos ORDER BY idmotos
                """
        result = self.db.execute_query(query)
        self.db.close_connection()
        print(result)
        return result
    
    def insertRepuesto(self, codigo, descripcion, imagen, categoria, motos):
        query = """
                    INSERT INTO repuestos(codigo, descripcion, imagen, categorias_idcategorias, motos_idmotos) VALUES(%s, %s, %s, %s, %s)
                """
        values = (codigo, descripcion, imagen, categoria, motos)
        self.db.execute_query(query, values)
        
    def selectRepuestos(self, codigo=None):
        query = """
                    SELECT r.codigo, r.descripcion, GROUP_CONCAT(CONCAT(m.nombre, ' ', m.modelo) SEPARATOR ", ") as descrip FROM repuestos r  
                    INNER JOIN motos m on r.motos_idmotos = m.idmotos
                    WHERE codigo = %s OR LOWER(r.descripcion) LIKE LOWER(CONCAT('%', %s, '%'))
                    GROUP BY codigo
                """
        values = (codigo, codigo)       
        
        result = self.db.execute_query(query, values)
        print(result)
        self.db.close_connection()
        return result
    
    def selectRepuestosMotos(self, nombre, year):
        query = """
                    SELECT r.codigo, r.descripcion, c.descripcion, m.nombre FROM repuestos r  
                    INNER JOIN motos m on r.motos_idmotos = m.idmotos
                    INNER JOIN categorias c on r.categorias_idcategorias = c.idcategorias
                    WHERE m.nombre = %s AND m.modelo =%s
                    GROUP BY codigo
                """
        values = (nombre, year,)
        result = self.db.execute_query(query, values)
        self.db.close_connection()
        return result
    
    def selectMotoSearch(self):
        query = """
                    SELECT idmotos, nombre FROM motos ORDER BY idmotos
                """
        result = self.db.execute_query(query)
        self.db.close_connection()
        print(result)
        return result