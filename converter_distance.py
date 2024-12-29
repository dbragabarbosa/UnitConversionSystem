def metros_para_quilometros(metros):
    result = metros / 1000
    return result

def quilometros_para_metros(quilometros):
    result = quilometros * 1000
    return result

def quilometros_para_milhas(quilometros):
    result = quilometros * 0.621371
    return result

def milhas_para_quilometros(milhas):
    result = milhas / 0.621371
    return result

def jardas_para_metros(jardas):
    result = jardas * 0.9144
    return result

def metros_para_jardas(metros):
    result = metros / 0.9144
    return result

def jardas_para_quilometros(jardas):
    metros = jardas_para_metros(jardas)
    quilometros = metros_para_quilometros(metros)
    return quilometros

def quilometros_para_jardas(quilometros):
    metros = quilometros_para_metros(quilometros)
    jardas = metros_para_jardas(metros)
    return jardas

def milhas_para_metros(milhas):
    result = milhas * 1609.34
    return result

def metros_para_milhas(metros):
    result = metros / 1609.34
    return result

def polegadas_para_centimetros(polegadas):
    result = polegadas * 2.54
    return result

def centimetros_para_polegadas(centimetros):
    result = centimetros / 2.54
    return result

def metros_para_polegadas(metros):
    result = metros * 39.3701
    return result

def polegadas_para_metros(polegadas):
    result = polegadas / 39.3701
    return result

def polegadas_para_jardas(polegadas):
    metros = polegadas_para_metros(polegadas)
    jardas = metros_para_jardas(metros)
    return jardas

def jardas_para_polegadas(jardas):
    metros = jardas_para_metros(jardas)
    polegadas = metros_para_polegadas(metros)
    return polegadas

def centimetros_para_metros(centimetros):
    result = centimetros / 100
    return result

def metros_para_centimetros(metros):
    result = metros * 100
    return result

def milhas_para_polegadas(milhas):
    metros = milhas_para_metros(milhas)
    polegadas = metros_para_polegadas(metros)
    return polegadas

def polegadas_para_milhas(polegadas):
    metros = polegadas_para_metros(polegadas)
    milhas = metros_para_milhas(metros)
    return milhas

def quilometros_para_centimetros(quilometros):
    metros = quilometros_para_metros(quilometros)
    centimetros = metros_para_centimetros(metros)
    return centimetros

def centimetros_para_quilometros(centimetros):
    metros = centimetros_para_metros(centimetros)
    quilometros = metros_para_quilometros(metros)
    return quilometros

def milhas_para_jardas(milhas):
    metros = milhas_para_metros(milhas)
    jardas = metros_para_jardas(metros)
    return jardas

def jardas_para_milhas(jardas):
    metros = jardas_para_metros(jardas)
    milhas = metros_para_milhas(metros)
    return milhas
