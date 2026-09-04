class Nodo_Archivo:
    def __init__(self, nombre, extension):
        self.nombre = nombre
        self.extension = extension
        self.siguiente = None

class Nodo_Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente_carpeta = None
        self.primer_archivo = None

class ExploradorArchivos:
    def __init__(self):
        self.primera_carpeta = None

    def agregar_carpeta(self, nombre):
        nueva = Nodo_Carpeta(nombre)
        if self.primera_carpeta == None:
            self.primera_carpeta = nueva
        else:
            aux = self.primera_carpeta
            while aux.siguiente_carpeta != None:
                aux = aux.siguiente_carpeta
            aux.siguiente_carpeta = nueva

    def agregar_archivo(self, nombre_carpeta, nombre_archivo, extension):
        aux = self.primera_carpeta
        
        while aux != None:
            if aux.nombre == nombre_carpeta:
                nuevo_archivo = Nodo_Archivo(nombre_archivo, extension)
                if aux.primer_archivo == None:
                    aux.primer_archivo = nuevo_archivo
                else:
                    aux_arch = aux.primer_archivo
                    while aux_arch.siguiente != None:
                        aux_arch = aux_arch.siguiente
                    aux_arch.siguiente = nuevo_archivo
                print("Archivo agregado con exito a la carpeta", nombre_carpeta)
                return
            aux = aux.siguiente_carpeta
        print("La carpeta no existe.")

    def mostrar_todo(self):
        aux = self.primera_carpeta
        while aux != None:
            print("\nCarpeta:", aux.nombre)
            aux_arch = aux.primer_archivo
            if aux_arch == None:
                print("  (Carpeta vacia)")
            while aux_arch != None:
                print("  -> Archivo:", aux_arch.nombre + "." + aux_arch.extension)
                aux_arch = aux_arch.siguiente
            aux = aux.siguiente_carpeta

pc = ExploradorArchivos()
pc.agregar_carpeta("Documentos")
pc.agregar_carpeta("Imagenes")
pc.agregar_carpeta("Proyectos")

pc.agregar_archivo("Documentos", "tesis", "docx")
pc.agregar_archivo("Documentos", "reporte", "pdf")
pc.agregar_archivo("Imagenes", "logo", "png")
pc.agregar_archivo("Imagenes", "foto", "jpg")
pc.agregar_archivo("Proyectos", "main", "py")

pc.mostrar_todo()