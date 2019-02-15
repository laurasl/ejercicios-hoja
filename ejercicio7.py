class Empleado():
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
    def get_nombre(self):
        return self.nombre
    
    def get_salario(self):
        return self.salario

emp1 = Empleado(nombre = "Alejandro", salario = 1200)
emp2 = Empleado(nombre = "Sofia", salario = 1600)

print("Alejandro gana %i euros al mes" % emp1.get_salario())
print("Sofia gana %i euros al mes" % emp2.get_salario())
