from RSA import RSA_Endpoint
import RSA as RSA
import CriptoDes as CD
import Client as C
import Server as Sm 


def Comprueba(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True
def GeneraNumerosPrimos():
    for numero in range(1001):
        if Comprueba(numero):
            return numero


def Main():
    ############################################################## 

    c_public=23
    c_private=33
    Cliente = RSA_Endpoint(c_public, s_public, c_private)

    ############################################################

    s_public=83
    s_private=77
    Servidor = RSA_Endpoint(c_public, s_public, s_private)
    ###################################### (k)
    c_partial=Cliente.generate_partial_key()
    s_partial=Servidor.generate_partial_key()
    ################################################ (clave como tal)
    c_full=Cliente.generate_full_key(c_partial)
    s_full=Servidor.generate_full_key(s_partial)
    
    if c_full==s_full:
        archivo = open("mensajeentrada.txt","r")
        mensaje = str(archivo.readline().lower())
        codigo =  RSA.encriptacion(mensaje)
        archivo.close()

    file = open("mensajerecibido.txt","w")
    desco = RSA.desencriptacion(codigo)
    file.write(str(desco))
    file.close()
