"""
https://pythonguides.com/python-dictionary-search-by-value/
"""
class Vehiculo(object):
    def __init__(self,noRuedas,combustible):
        self.dicAtrib=dict()
        self.dicAtrib["noRuedas"]=noRuedas
        self.dicAtrib["combusible"]=combustible

class Coche(Vehiculo):
    """noRuedas<-integer
          combustible<-string
          transmision<-string """
    def __init__(self,noRuedas,combustible,transmision):
        super().__init__(noRuedas,combustible)
        self.dicAtrib=dict()
        self.dicAtrib["noRuedas"]=noRuedas
        self.dicAtrib["combustible"]=combustible
        self.dicAtrib["transmision"]=transmision
        
    def desplazamiento(Self):
        pass
        
  
class Camion():
        pass

class Bici(Vehiculo):
    """noRuedas<-integer :{2,3,4}
          combustible<-string :{sangre, hybrida,electrica}
          transmision<-string:{cadena, cadena-polea,cvt}
          tipo<-string:{urbana, triciclo-carga, gemela,montaña}
          """
    def __init__(self,noRuedas,combustible,transmision,tipo):
         super().__init__(noRuedas,combustible)
         self.dicAtrib=dict()
         self.dicAtrib["noRuedas"]=noRuedas
         self.dicAtrib["combustible"]=combustible
         self.dicAtrib["transmision"]=transmision
         self.dicAtrib["tipo"]=tipo
  
class VehiculoAtributos():
    """ """
    @staticmethod
    def imprimeAtributos(Obj):
        """tipo deobjeto{Bici,Camion,Coche} """
        for k,v in Obj.dicAtrib.items():
            print(k,":",v)

    def getIdAtributos(Obj):
        print("atributos:",Obj.dicAtrib)
        id=0
        for key,value in Obj.dicAtrib.items():
            
            #numero de ruedas
            if Obj.dicAtrib["noRuedas"]== 2:
                id+=2
            if Obj.dicAtrib["noRuedas"]== 3:
                id+=3
            if Obj.dicAtrib["noRuedas"]== 4:
                id+=4
##            # tipo de combustible    
            if  Obj.dicAtrib["combustible"]=="sangre":
                id+=10
            if  Obj.dicAtrib["combustible"]=="hybrida":
                id+=20
            if  Obj.dicAtrib["combustible"]=="electrica":
                id+=30
##                
##            # tipo de transmision    
            if Obj.dicAtrib["transmision"]== "cadena":
                id+=100
            if Obj.dicAtrib["transmision"]== "cadena-polea":
                id+=200
            if Obj.dicAtrib["transmision"]== "cvt":
                id+=300
            
##             # tipo 
            if  Obj.dicAtrib["tipo"]=="urbana" :
                id=id+1000
            if  Obj.dicAtrib["tipo"]=="triciclo-carga" :
                id=id+2000
            if  Obj.dicAtrib["tipo"]=="gemela" :
                id=id+3000
            if  Obj.dicAtrib["tipo"]=="montaña" :
                id=id+4000
            return id

        def load_image(file):
            """loads and prepares image from data directory"""
            file = os.path.join(main_dir, 'data', file)
            try:
                surface = pygame.image.load(file)
            except pygame.error:
                raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
            return surface.convert()




        def getImagen(iD):
            imagenDic=dict()
            imagenDic={1332:"electricaCvt.jpg"}
            if iD==1332:
                with open("electricaCvt.jpg","rb") as type1332:
                    pass
                    
                
              
            
            
    
miBici=Bici(2,"electrica","cvt","urbana")
print(VehiculoAtributos. getIdAtributos(miBici))
miBici_1=Bici(3,"hybrida","cadena-polea","triciclo-carga")
print(VehiculoAtributos. getIdAtributos(miBici_1))

        
        


