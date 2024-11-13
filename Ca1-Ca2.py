from colorama import Fore

def convertir_a_binario(numero, base):
    # Convertimos el número a binario, considerando el signo si es negativo
    if numero.startswith('-'):
        numero = numero[1:]  # Elimina el signo para convertir el valor absoluto
        es_negativo = True
    else:
        es_negativo = False

    if base == 10:
        binario = bin(int(numero))[2:].zfill(8)  # Convierte decimal a binario y completa a 8 bits
    elif base == 2:
        binario = numero.zfill(8)  # Completa a 8 bits si ya es binario
    elif base == 8:
        binario = bin(int(numero, 8))[2:].zfill(8)  # Convierte octal a binario y completa a 8 bits
    elif base == 16:
        binario = bin(int(numero, 16))[2:].zfill(8)  # Convierte hexadecimal a binario y completa a 8 bits
    else:
        raise ValueError("Base no soportada. Usa 2, 8, 10 o 16.")

    # Si el número era negativo, convertimos a complemento a dos
    if es_negativo:
        ca1 = binario_a_ca1(binario)
        ca2 = bin(int(ca1, 2) + 1)[2:].zfill(len(binario))  # Suma 1 para obtener Ca2
        return ca2  # Retorna el número en complemento a dos
    else:
        return binario

def binario_a_ca1(binario):
    # Convierte el binario a su complemento a uno
    return ''.join('1' if bit == '0' else '0' for bit in binario)

def binario_a_ca2(binario):
    # Convierte el binario a Ca2 sumando 1 al Ca1
    ca1 = binario_a_ca1(binario)
    ca2 = bin(int(ca1, 2) + 1)[2:].zfill(len(binario))
    return ca1, ca2

def binario_a_decimal(binario):
    # Convierte binario a decimal considerando el primer bit como signo
    if binario[0] == '1':  # Si es un número negativo
        return -((1 << len(binario)) - int(binario, 2))
    else:  # Si es positivo
        return int(binario, 2)


def bucle():

    # Entrada del usuario
    print(Fore.YELLOW + "Conversor de números a binario y complementos a uno y dos")
    numero = input("Introduce un número (puede ser negativo): ")
    base = int(input("Introduce la base del número (2, 8, 10, 16): "))

    # Conversión a binario
    numero_binario = convertir_a_binario(numero, base)

    # Cálculo de Ca1 y Ca2
    ca1, ca2 = binario_a_ca2(numero_binario)

    # Conversión a decimal de cada uno
    decimal_original = binario_a_decimal(numero_binario)
    decimal_ca1 = binario_a_decimal(ca1)
    decimal_ca2 = binario_a_decimal(ca2)

    # Mostrando los resultados
    print(Fore.RED + f"\nNúmero original: {numero} en base {base} (Binario: {numero_binario}, Decimal: {decimal_original})")
    print(Fore.LIGHTGREEN_EX + f"Complemento a uno (Ca1): {ca1} (Decimal: {decimal_ca1})")
    print(f"Complemento a dos (Ca2): {ca2} (Decimal: {decimal_ca2})")
    print(f"Bit del Ca2 (bit de signo): {ca2[0]}")

    # Preguntar si desea hacer otra conversión
    respuesta = input(Fore.LIGHTBLACK_EX + "¿Deseas hacer otra conversión? (s/n): ")
    if respuesta.lower() == 's':
        bucle()
    else:
        print(Fore.CYAN + "¡Hasta luego!")

bucle()