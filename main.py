import converter_distance as dist
import converter_weight as weight
import converter_temperature as temp
import converter_time as time
import converter_volume as volume
import converter_space as space
import converter_velocity as velocity

def mostrar_menu():
    print()
    print("=== Sistema de Conversão de Unidades ===")
    print("1. Conversão de Distância")
    print("2. Conversão de Peso")
    print("3. Conversão de Temperatura")
    print("4. Conversão de Tempo")
    print("5. Conversão de Volume")
    print("6. Conversão de Espaço")
    print("7. Conversão de Velocidade")
    print("0. Sair")
    print()

def sub_menu(opcoes):
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    print("0. Voltar")
    print()

def obter_escolha(numero_opcoes):
    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            if 0 <= escolha <= numero_opcoes:
                return escolha
            print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def entrada_valor(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")

def conversao_distancia():
    opcoes = ["Metros para Quilômetros", "Quilômetros para Milhas", "Milhas para Quilômetros"]
    sub_menu(opcoes)
    escolha = obter_escolha(len(opcoes))
    if escolha == 0:
        return
    valor = entrada_valor("Insira o valor para conversão: ")
    if escolha == 1:
        print(f"{int(valor)} metros = {dist.metros_para_quilometros(valor):.1f} quilômetros")
    elif escolha == 2:
        print(f"{int(valor)} quilômetros = {dist.quilometros_para_milhas(valor):.1f} milhas")
    elif escolha == 3:
        print(f"{int(valor)} milhas = {dist.milhas_para_quilometros(valor):.1f} quilômetros")

def conversao_peso():
    opcoes = ["Quilogramas para Libras", "Libras para Quilogramas"]
    sub_menu(opcoes)
    escolha = obter_escolha(len(opcoes))
    if escolha == 0:
        return
    valor = entrada_valor("Insira o valor para conversão: ")
    if escolha == 1:
        print(f"{int(valor)} quilogramas = {weight.quilogramas_para_libras(valor):.2f} libras")
    elif escolha == 2:
        print(f"{int(valor)} libras = {weight.libras_para_quilogramas(valor):.2f} quilogramas")

def conversao_temperatura():
    opcoes = ["Celsius para Fahrenheit", "Fahrenheit para Celsius"]
    sub_menu(opcoes)
    escolha = obter_escolha(len(opcoes))
    if escolha == 0:
        return
    valor = entrada_valor("Insira a temperatura para conversão: ")
    if escolha == 1:
        print(f"{int(valor)}°C = {temp.celsius_para_fahrenheit(valor):.1f}°F")
    elif escolha == 2:
        print(f"{int(valor)}°F = {temp.fahrenheit_para_celsius(valor):.1f}°C")

def conversao_tempo():
    opcoes = ["Segundos para Minutos", "Minutos para Horas", "Horas para Dias"]
    sub_menu(opcoes)
    escolha = obter_escolha(len(opcoes))
    if escolha == 0:
        return
    valor = entrada_valor("Insira o valor para conversão: ")
    if escolha == 1:
        print(f"{int(valor)} segundos = {time.segundos_para_minutos(valor):.1f} minutos")
    elif escolha == 2:
        print(f"{int(valor)} minutos = {time.minutos_para_horas(valor):.1f} horas")
    elif escolha == 3:
        print(f"{int(valor)} horas = {time.horas_para_dias(valor):.1f} dias")

def conversao_volume():
    opcoes = ["Litros para Mililitros", "Mililitros para Litros", "Litros para Galões", "Galões para Litros"]
    sub_menu(opcoes)
    escolha = obter_escolha(len(opcoes))
    if escolha == 0:
        return
    valor = entrada_valor("Insira o valor para conversão: ")
    if escolha == 1:
        print(f"{int(valor)} litros = {volume.litros_para_mililitros(valor):.0f} mililitros")
    elif escolha == 2:
        print(f"{int(valor)} mililitros = {volume.mililitros_para_litros(valor):.3f} litros")
    elif escolha == 3:
        print(f"{int(valor)} litros = {volume.litros_para_galoes(valor):.3f} galões")
    elif escolha == 4:
        print(f"{int(valor)} galões = {volume.galoes_para_litros(valor):.3f} litros")

def conversao_espaco():
    opcoes = ["Metros Quadrados para Hectares", "Hectares para Metros Quadrados"]
    sub_menu(opcoes)
    escolha = obter_escolha(len(opcoes))
    if escolha == 0:
        return
    valor = entrada_valor("Insira o valor para conversão: ")
    if escolha == 1:
        print(f"{int(valor)} m² = {space.metros_quadrados_para_hectares(valor):.2f} hectares")
    elif escolha == 2:
        print(f"{int(valor)} hectares = {space.hectares_para_metros_quadrados(valor):.0f} m²")

def conversao_velocidade():
    opcoes = [
        "Metros por segundo para Quilômetros por hora",
        "Quilômetros por hora para Metros por segundo",
        "Metros por segundo para Milhas por hora",
        "Milhas por hora para Metros por segundo",
        "Quilômetros por hora para Milhas por hora",
        "Milhas por hora para Quilômetros por hora"
    ]
    sub_menu(opcoes)
    escolha = obter_escolha(len(opcoes))
    if escolha == 0:
        return
    valor = entrada_valor("Insira o valor para conversão: ")
    if escolha == 1:
        print(f"{valor} m/s = {velocity.mps_para_kmh(valor):.6f} km/h")
    elif escolha == 2:
        print(f"{valor} km/h = {velocity.kmh_para_mps(valor):.6f} m/s")
    elif escolha == 3:
        print(f"{valor} m/s = {velocity.mps_para_mph(valor):.6f} mph")
    elif escolha == 4:
        print(f"{valor} mph = {velocity.mph_para_mps(valor):.6f} m/s")
    elif escolha == 5:
        print(f"{valor} km/h = {velocity.kmh_para_mph(valor):.6f} mph")
    elif escolha == 6:
        print(f"{valor} mph = {velocity.mph_para_kmh(valor):.6f} km/h")

def main():
    while True:
        mostrar_menu()
        escolha = obter_escolha(7)
        if escolha == 0:
            print("Encerrando o sistema. Até mais!")
            break
        elif escolha == 1:
            conversao_distancia()
        elif escolha == 2:
            conversao_peso()
        elif escolha == 3:
            conversao_temperatura()
        elif escolha == 4:
            conversao_tempo()
        elif escolha == 5:
            conversao_volume()
        elif escolha == 6:
            conversao_espaco()
        elif escolha == 7:
            conversao_velocidade()

if __name__ == "__main__":
    main()
