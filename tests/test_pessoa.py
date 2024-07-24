"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool inicia false

    API:
    obter_todos_os_dados -> methed
        OK
        404

        (dados_obtidos se torna True se dados obtidos com sucesso)
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from src.Pessoa import Pessoa
from unittest.mock import patch

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Artur', 'Pedro')
        self.p2 = Pessoa('Maria', 'Lima')

    def test_pessoa_attr_nome_valor_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Artur')
        self.assertEqual(self.p2.nome, 'Maria')

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_attr_sobrenome_valor_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Pedro')
        self.assertEqual(self.p2.sobrenome, 'Lima')

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'Error 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'Error 404')
            self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequecial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'Error 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'Error 404')
            self.assertFalse(self.p2.dados_obtidos)

if __name__ == '__main__':
    unittest.main(verbosity=2)