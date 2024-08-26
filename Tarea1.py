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

    def verifpac(self,cedula):
        encontrado= False
        for p in self.__lista_pacientes:
            if cedula==p.verCedula():
                encontrado= True
                break
        return encontrado

    def ingresarPaciente(self,pac):
        
        if self.verifpac(pac.verCedula()):
            return False
        self.__lista_pacientes.append(pac)
        return True

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPacientes(self,c):

        resultados = []

        if self.verifpac(c)== False:
            return None
        
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                resultados.append(p)
                break

        for p in self.__lista_pacientes:
            if isinstance(c, str) and c.lower() in p.verNombre().lower():
                resultados.append(p)

        if len(resultados) == 0:
            return None
        return resultados
        


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
            resultado = sistema.ingresarPaciente(pac)

            if resultado == False:
                print("ya existe un paciente con esta cedula ")
            else:
                print("paciente ingresado")

        elif opcion == 2:
            print("Ahora hay: " + str(sistema.verNumeroPacientes()))

        elif opcion == 3:

            ced_o_nom = int(input("Ingrese la cedula o el nombre a buscar: "))
            pac=sistema.verDatosPacientes(ced_o_nom)
            
            if pac is None:
                print("No se encontraron datos con ese nombre o cedula del paciente ")
            else:
                for pac in resultado:
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