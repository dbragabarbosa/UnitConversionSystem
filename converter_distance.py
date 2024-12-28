def metros_para_quilometros(metros):
    result = metros / 1000
    return result

def quilometros_para_milhas(quilometros):
    result = quilometros * 0.621371
    return result

def jardas_para_metros(jardas):
    result = jardas * 0.9144
    return result

def milhas_para_metros(milhas):
    result = milhas * 1609.34
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

def milhas_para_quilometros(milhas):
    metros = milhas_para_metros(milhas)
    quilometros = metros_para_quilometros(metros)
    return quilometros
