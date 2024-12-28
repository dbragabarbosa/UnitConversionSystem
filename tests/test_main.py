import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_mostrar_menu(self):
        with patch('builtins.print') as mock_print:
            main.mostrar_menu()
            mock_print.assert_any_call("=== Sistema de Conversão de Unidades ===")

    def test_obter_escolha(self):
        with patch('builtins.input', return_value='2'):
            escolha = main.obter_escolha(2)
            self.assertEqual(escolha, 2)

    def test_entrada_valor(self):
        with patch('builtins.input', return_value='15.5'):
            valor = main.entrada_valor("Digite um valor:")
            self.assertEqual(valor, 15.5)

    @patch("main.input", side_effect=["1", "1", "1000", "0"])
    @patch("main.dist.metros_para_quilometros", return_value=1.0)
    @patch("main.print")
    def test_conversao_distancia_metros_para_quilometros(self, mock_print, mock_converter, mock_input):
        main.main()
        mock_print.assert_any_call("1000 metros = 1.0 quilômetros")

    @patch("main.input", side_effect=["1", "2", "10", "0"])
    @patch("main.dist.quilometros_para_milhas", return_value=6.21)
    @patch("main.print")
    def test_conversao_distancia_quilometros_para_milhas(self, mock_print, mock_converter, mock_input):
        main.main()
        mock_print.assert_any_call("10 quilômetros = 6.2 milhas")

    @patch("main.input", side_effect=["2", "1", "70", "0"])
    @patch("main.weight.quilogramas_para_libras", return_value=154.32)
    @patch("main.print")
    def test_conversao_peso_quilogramas_para_libras(self, mock_print, mock_converter, mock_input):
        main.main()
        mock_print.assert_any_call("70 quilogramas = 154.32 libras")

    @patch("main.input", side_effect=["2", "2", "100", "0"])
    @patch("main.weight.libras_para_quilogramas", return_value=45.36)
    @patch("main.print")
    def test_conversao_peso_libras_para_quilogramas(self, mock_print, mock_converter, mock_input):
        main.main()
        mock_print.assert_any_call("100 libras = 45.36 quilogramas")

    @patch("main.input", side_effect=["3", "1", "25", "0"])
    @patch("main.temp.celsius_para_fahrenheit", return_value=77.0)
    @patch("main.print")
    def test_conversao_temperatura_celsius_para_fahrenheit(self, mock_print, mock_converter, mock_input):
        main.main()
        mock_print.assert_any_call("25°C = 77.0°F")

    @patch("main.input", side_effect=["3", "2", "98", "0"])
    @patch("main.temp.fahrenheit_para_celsius", return_value=36.7)
    @patch("main.print")
    def test_conversao_temperatura_fahrenheit_para_celsius(self, mock_print, mock_converter, mock_input):
        main.main()
        mock_print.assert_any_call("98°F = 36.7°C")

    @patch("main.input", side_effect=["4", "1", "3600", "0"])
    @patch("main.time.segundos_para_minutos", return_value=60.0)
    @patch("main.print")
    def test_conversao_tempo_segundos_para_minutos(self, mock_print, mock_converter, mock_input):
        main.main()
        mock_print.assert_any_call("3600 segundos = 60.0 minutos")

    @patch("main.input", side_effect=["5", "3", "2", "0"])
    @patch("main.volume.litros_para_galoes", return_value=0.528)
    @patch("main.print")
    def test_conversao_volume_litros_para_galoes(self, mock_print, mock_converter, mock_input):
        main.main()
        mock_print.assert_any_call("2 litros = 0.528 galões")

    @patch("main.input", side_effect=["6", "1", "10000", "0"])
    @patch("main.space.metros_quadrados_para_hectares", return_value=1.0)
    @patch("main.print")
    def test_conversao_espaco_metros_quadrados_para_hectares(self, mock_print, mock_converter, mock_input):
        main.main()
        mock_print.assert_any_call("10000 m² = 1.00 hectares")

    @patch("main.dist.milhas_para_metros", return_value=3218.68)
    @patch("main.dist.metros_para_quilometros", return_value=3.22)
    @patch("main.print")
    def test_sistema_conversao_distancia_milhas_para_quilometros(self, mock_print, mock_milhas_para_metros, mock_metros_para_quilometros, mock_input):
        main.main()
        mock_print.assert_any_call("2 milhas = 3.22 quilômetros")

if __name__ == "__main__":
    unittest.main()
