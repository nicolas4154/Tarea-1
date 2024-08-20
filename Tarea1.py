class Paciente:

    def __init__(self):
        self.__nombre= ""
        self.__cedula= ""
        self.__genero= ""
        self.__servicio= ""

    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarServicio(self, s):
        self.__servicio = s
    def asignarGenero(self, g):
        self.__genero = g
    def asignarCedula(self, c):
        self.__cedula = c

class Sistema:

    def __init__(self):
        self.__lista_pacientes = [ ]
        self.__numero_pacientes = len(self.__lista_pacientes)

    def ingresarPaciente(self,pac):
        
        self.__lista_pacientes.append(pac)
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPacientes(self,c):
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                 return p

def main():
     
    sistema = Sistema()
    
    while True:
        opcion = int(input("1. Nuevo Paciente -2. Numero de Pacientes -3. Datos Paciente -4.Salir"))
        if opcion == 1:
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            pac= Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            sistema.ingresarPaciente()

        elif opcion == 2:
            print("Ahora hay: " + str(sistema.verNumeroPacientes()))

        elif opcion == 3:

            cedula = int(input("Ingrese la cedula a buscar: "))
            pac=sistema.verDatosPacientes
            print("Nombre: " + pac.verNombre())
            print("Cedula" + str(pac.verNombre()))
            print("Gener: " + pac.verGenero())
            print("Servicio: " + pac.verServicio())

        elif opcion !=0:
            continue
        else:
            print("Opcion invalida")
            break
            
    
    if __name__=="__main__":
        main()