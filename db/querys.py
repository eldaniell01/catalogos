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