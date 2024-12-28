import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    # Testes de Unidade
    def test_mostrar_menu(self):
        with patch('builtins.print') as mock_print:
            main.mostrar_menu()
            self.assertIn("=== Sistema de Conversão de Unidades ===", mock_print.call_args_list[0][0][0])

    def test_sub_menu(self):
        with patch('builtins.print') as mock_print:
            opcoes = ["Opção 1", "Opção 2"]
            main.sub_menu(opcoes)
            self.assertEqual(mock_print.call_count, len(opcoes) + 1)  # Opções + "0. Voltar"

    def test_obter_escolha(self):
        with patch('builtins.input', side_effect=['2']):
            escolha = main.obter_escolha(2)
            self.assertEqual(escolha, 2)

    def test_entrada_valor(self):
        with patch('builtins.input', side_effect=['15.5']):
            valor = main.entrada_valor("Digite um valor:")
            self.assertEqual(valor, 15.5)

    # Testes de Integração
    @patch('main.dist.metros_para_quilometros', return_value=0.1)
    def test_conversao_distancia_metros_para_quilometros(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '100']), patch('builtins.print') as mock_print:
            main.conversao_distancia()
            mock_conversion.assert_called_with(100)
            self.assertIn("100 metros = 0.1 quilômetros", mock_print.call_args_list[-1][0][0])

    @patch('main.weight.quilogramas_para_libras', return_value=2.20462)
    def test_conversao_peso_quilogramas_para_libras(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '1']), patch('builtins.print') as mock_print:
            main.conversao_peso()
            mock_conversion.assert_called_with(1)
            self.assertIn("1 quilogramas = 2.20462 libras", mock_print.call_args_list[-1][0][0])

    @patch('main.temp.celsius_para_fahrenheit', return_value=32.0)
    def test_conversao_temperatura_celsius_para_fahrenheit(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '0']), patch('builtins.print') as mock_print:
            main.conversao_temperatura()
            mock_conversion.assert_called_with(0)
            self.assertIn("0°C = 32.0°F", mock_print.call_args_list[-1][0][0])

    @patch('main.time.segundos_para_minutos', return_value=1.0)
    def test_conversao_tempo_segundos_para_minutos(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '60']), patch('builtins.print') as mock_print:
            main.conversao_tempo()
            mock_conversion.assert_called_with(60)
            self.assertIn("60 segundos = 1.0 minutos", mock_print.call_args_list[-1][0][0])

    @patch('main.volume.litros_para_mililitros', return_value=1000)
    def test_conversao_volume_litros_para_mililitros(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '1']), patch('builtins.print') as mock_print:
            main.conversao_volume()
            mock_conversion.assert_called_with(1)
            self.assertIn("1 litros = 1000 mililitros", mock_print.call_args_list[-1][0][0])

    @patch('main.space.metros_quadrados_para_hectares', return_value=0.01)
    def test_conversao_espaco_metros_quadrados_para_hectares(self, mock_conversion):
        with patch('builtins.input', side_effect=['1', '100']), patch('builtins.print') as mock_print:
            main.conversao_espaco()
            mock_conversion.assert_called_with(100)
            self.assertIn("100 m² = 0.01 hectares", mock_print.call_args_list[-1][0][0])

    # Teste de Sistema
    @patch('builtins.input', side_effect=['1', '1', '100', '0'])
    @patch('builtins.print')
    def test_sistema_fluxo_distancia(self, mock_print, mock_input):
        main.main()
        self.assertIn("100 metros =", mock_print.call_args_list[-2][0][0])

if __name__ == "__main__":
    unittest.main()
