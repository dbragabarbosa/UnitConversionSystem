import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    # Testes de Unidade
    def test_mostrar_menu(self):
        with patch('builtins.print') as mock_print:
            main.mostrar_menu()
            mock_print.assert_any_call("=== Sistema de Conversão de Unidades ===")

    def test_sub_menu(self):
        with patch('builtins.print') as mock_print:
            opcoes = ["Opção 1", "Opção 2"]
            main.sub_menu(opcoes)
            self.assertEqual(mock_print.call_count, len(opcoes) + 1)  # Opções + "0. Voltar"
            mock_print.assert_any_call("0. Voltar")

    def test_obter_escolha(self):
        with patch('builtins.input', return_value='2'):
            escolha = main.obter_escolha(2)
            self.assertEqual(escolha, 2)

    def test_entrada_valor(self):
        with patch('builtins.input', return_value='15.5'):
            valor = main.entrada_valor("Digite um valor:")
            self.assertEqual(valor, 15.5)

    # Testes de Integração
    @patch('main.dist.metros_para_quilometros', return_value=0.1)
    def test_conversao_distancia_metros_para_quilometros(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '100']), patch('builtins.print') as mock_print:
            main.conversao_distancia()
            mock_conversion.assert_called_once_with(100)
            mock_print.assert_any_call("100 metros = 0.1 quilômetros")

    @patch('main.weight.quilogramas_para_libras', return_value=2.20462)
    def test_conversao_peso_quilogramas_para_libras(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '1']), patch('builtins.print') as mock_print:
            main.conversao_peso()
            mock_conversion.assert_called_once_with(1)
            mock_print.assert_any_call("1 quilogramas = 2.20462 libras")

    @patch('main.temp.celsius_para_fahrenheit', return_value=32.0)
    def test_conversao_temperatura_celsius_para_fahrenheit(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '0']), patch('builtins.print') as mock_print:
            main.conversao_temperatura()
            mock_conversion.assert_called_once_with(0)
            mock_print.assert_any_call("0°C = 32.0°F")

    @patch('main.time.segundos_para_minutos', return_value=1.0)
    def test_conversao_tempo_segundos_para_minutos(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '60']), patch('builtins.print') as mock_print:
            main.conversao_tempo()
            mock_conversion.assert_called_once_with(60)
            mock_print.assert_any_call("60 segundos = 1.0 minutos")

    @patch('main.volume.litros_para_mililitros', return_value=1000)
    def test_conversao_volume_litros_para_mililitros(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '1']), patch('builtins.print') as mock_print:
            main.conversao_volume()
            mock_conversion.assert_called_once_with(1)
            mock_print.assert_any_call("1 litros = 1000 mililitros")

    @patch('main.space.metros_quadrados_para_hectares', return_value=0.01)
    def test_conversao_espaco_metros_quadrados_para_hectares(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '100']), patch('builtins.print') as mock_print:
            main.conversao_espaco()
            mock_conversion.assert_called_once_with(100)
            mock_print.assert_any_call("100 m² = 0.01 hectares")

    # Teste de Sistema
    @patch('builtins.input', side_effect=['1', '1', '100', '0'])
    @patch('builtins.print')
    def test_sistema_fluxo_distancia(self, mock_print, mock_input):
        main.main()
        mock_print.assert_any_call("100 metros =")

if __name__ == "__main__":
    unittest.main()
