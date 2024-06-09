from .conexion import ConexionMysql

class Query:
    def __init__(self) -> None:
        self.db = ConexionMysql()
        self.db.connection()
    
    def insertMoto(self, moto, descripcion, modelo):
        query = """
                    INSERT INTO motos(nombre, descripcion, modelo) VALUES(%s, %s, %s)
                """
        values = (moto, descripcion, modelo)
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
                    SELECT * FROM motos
                """
        result = self.db.execute_query(query)
        self.db.close_connection()
        return result