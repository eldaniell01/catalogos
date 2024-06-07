import mysql.connector


class ConexionMysql:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123'
        self.data_base = 'catalogos'
        self.conexion = None
        self.cursor = None
        
    def connection(self):
        try:
            self.conexion = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.data_base
            )
            self.cursor = self.conexion.cursor()
            return f"conectado a {self.cursor}"
        except mysql.connector.Error as error:
            return error
    
    def execute_query(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            
            result = self.cursor.fetchall()
            self.conexion.commit()
            return result
        except mysql.connector.Error as e:
            print(f"error: {e}")
    
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
            
        if self.conexion:
            self.conexion.close()
            return f"{self.conexion} sea cerrado"