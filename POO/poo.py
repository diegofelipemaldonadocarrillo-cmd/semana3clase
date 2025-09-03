class carro:
    def __init__(self , marca, modelo, color):
        self.dato_marca = marca
        self.dato_modelo = modelo
        self.dato_color = color
        
        
        def set_marca(self, nueva_marca):
        #todos los metodos set tienen como obliagacion tener parametro
            self.dato_marca= nueva_marca 
            
        def get_marca(self, nueva_marca):
        #todos los metodos get tienen como obliagacion tener retorno
            return self.dato_marca
        
        
        def imprimir_carro(self):
            print(self.dato_marca,  self.dato_modelo,  self.dato_color)
            
        
        def mover_carro(self, obj_motor):
            #un metodo que depende de un obj
            obj_motor.arrancar_motor()
        
        
        def apagar_carro(self, obj_motor):
            #un metodo que depende de un obj
            obj_motor.apagar_motor()
            
class Motor:
    def __init__(self):
        self.estado_motor = "apagado"
    
    def prender_motor(self):
        self.estado_motor = "prendido"
    
    def apagar_motor(self):
        self.estado_motor = "apagado"
    
    
    
        
            
            
##zona de codigo principal###
obj_carro = carro("mazda","2021","negro")
#todos los metodos que tienen return deben tener almacenamiento
dato_marca = obj_carro.get_marca()
print(" marca carro: " + dato_marca)
obj_carro.imprimir_carro()
        
       
            
        
        
            
            
            