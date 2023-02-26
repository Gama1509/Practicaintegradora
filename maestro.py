class Maestro:

    def __init__(self, nombre,boleta,grupo):
        
        self.nombre=nombre
        self.boleta=boleta
        self.grupo=grupo


    def getNombre(self):
        return self.__nombre


    def getBoleta(self):
        return self.__boleta


    def getGrupo(self):
        return self.__grupo

    def setNombre(self,nombre):
        self.__nombre=nombre


    def setBoleta(self,boleta):
        self.__boleta=boleta


    def setGrupo(self,grupo):
        self.__grupo=grupo
    

    
