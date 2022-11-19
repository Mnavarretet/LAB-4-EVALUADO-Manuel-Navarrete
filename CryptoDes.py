from Crypto.Cipher import DES

llave = token_bytes(12)
iniciar = token_bytes(12)

def encriptacion(mensaje):
    Crypto = DES.new(llave,DES.MODE_CFD,iniciar)
    mensaje = mensaje.encode()
    codificacion = Crypto.encrypt(mensaje)
    return codificacion

def desencriptacion(codificacion):
    CryptoC = DES.new(llave,DES.MODE_CFD,iniciar)
    codificado = CryptoC.encrypt(codificacion).decode()
    return codificado
