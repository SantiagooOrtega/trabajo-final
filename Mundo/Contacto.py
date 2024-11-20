class Contacto:

    def __init__(self, nombre, apellido, direccion, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__correo = correo

        self.__telefonos = [] 
        self.__palabras = []


    def darNombre(self):
        return self.__nombre

    def darApellido(self):
        return self.__apellido

    def darDireccion(self):
        return self.__direccion

    def darCorreo(self):
        return self.__correo

    def darTelefonos(self):
        return self.__telefonos

    def darPalabras(self):
        return self.__palabras

    def cambiarDireccion(self, direccion):
        self.__direccion = direccion

    def cambiarCorreo(self, correo):
        self.__correo = correo

    def agregarTelefono(self, telefono):
        self.__telefonos += [telefono]

    def eliminarTelefono(self, telefonoEliminar):
        self.__telefonos.remove(telefonoEliminar)

    def agregarPalabra(self, palabra):
        self.__palabras += [palabra]

    def eliminarPalabra(self, palabraEliminar):
        self.__palabras.remove(palabraEliminar)

    def contienePalabraClave(self, palabra):
        if palabra in self.__palabras:
            return True
        else:
            return False