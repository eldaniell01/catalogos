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
        
    def selectRepuestos(self, codigo):
        query = """
                    SELECT codigo, GROUP_CONCAT(descripcion SEPARATOR ", ") as descrip FROM repuestos WHERE codigo = %s GROUP BY codigo
                """
        values = (codigo,)
        result = self.db.execute_query(query, values)
        self.db.close_connection()
        return result