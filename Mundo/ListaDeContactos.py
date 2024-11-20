from Mundo.Contacto import Contacto

class ListaDeContactos:
    def __init__(self):
        self.__contactos = []

    def darTodosLosContactos(self):
        return self.__contactos

    def buscarContactosPalabraClave(self, palabra):
        contactosConLaPalabra = []
        for contacto in self.__contactos:
            if contacto.contienePalabraClave(palabra):
                contactosConLaPalabra += [contacto.darNombre()+" "+contacto.darApellido()]
        return contactosConLaPalabra
                
    
    def buscarContacto(self, nombre, apellido):
        for contacto in self.__contactos:
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido:
                return contacto
        return None

    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        if self.buscarContacto(nombre, apellido) == None:
            ContactoNuevo = Contacto(nombre, apellido, direccion, correo)
            for telefono in telefonos:
                ContactoNuevo.agregarTelefono(telefono)
            for palabra in palabras:
                ContactoNuevo.agregarPalabra(palabra)   
            self.__contactos += [ContactoNuevo]
            return True
        else:
            return False

    def eliminarContacto(self, nombre, apellido):

    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):

    def actualizarTelefonos(self, telefonos, contacto):

    def actualizarPalabras(self, palabras, contacto):

    def metodo1(self):

    def metodo2(self):
    
    
