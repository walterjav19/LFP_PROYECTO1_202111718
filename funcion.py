
from expression import Expression
class Funcion(Expression):

    def __init__(self, titulo, descripcion, contenido, line, column):
        self.titulo = titulo
        self.descripcion = descripcion
        self.contenido = contenido
        self.line = line
        self.column = column
    
    def ejecutar(self, getER):
        return None
        return [self.titulo, self.descripcion, self.contenido]