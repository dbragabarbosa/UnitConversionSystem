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

if __name__ == "__main__":
    unittest.main()
