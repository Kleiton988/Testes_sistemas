import unittest

from calculadora import Calculadora
from sistema import SistemaLogin, RegrasNegocio
from carrinho import Carrinho

# TESTES DA CALCULADORA

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_soma(self):

        # CENÁRIO
        # Definimos os números que serão usados
        a = 2
        b = 3

        # EXECUÇÃO
        resultado = self.calc.somar(a, b)

        # VERIFICAÇÃO
        self.assertEqual(resultado, 5)


    def test_soma_negativo(self):

        # CENÁRIO
        a = 5
        b = -2

        # EXECUÇÃO
        resultado = self.calc.somar(a, b)

        # VERIFICAÇÃO
        self.assertEqual(resultado, 3)


    def test_subtracao(self):

        # CENÁRIO
        a = 7
        b = 3

        # EXECUÇÃO
        resultado = self.calc.subtrair(a, b)

        # VERIFICAÇÃO
        self.assertEqual(resultado, 4)


    def test_multiplicacao(self):

        # CENÁRIO
        a = 4
        b = 3

        # EXECUÇÃO
        resultado = self.calc.multiplicar(a, b)

        # VERIFICAÇÃO
        self.assertEqual(resultado, 12)


    def test_divisao(self):

        # CENÁRIO
        a = 10
        b = 2

        # EXECUÇÃO
        resultado = self.calc.dividir(a, b)

        # VERIFICAÇÃO
        self.assertEqual(resultado, 5)


    def test_divisao_zero(self):

        # CENÁRIO
        a = 10
        b = 0

        # EXECUÇÃO + VERIFICAÇÃO
        with self.assertRaises(ValueError):
            self.calc.dividir(a, b)

# TESTES DO SISTEMA DE LOGIN


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login = SistemaLogin()

    def test_login_valido(self):

        # CENÁRIO
        usuario = "admin"
        senha = "123"

        # EXECUÇÃO
        resultado = self.login.login(usuario, senha)

        # VERIFICAÇÃO
        self.assertTrue(resultado)


    def test_login_invalido(self):

        # CENÁRIO
        usuario = "admin"
        senha = "999"

        # EXECUÇÃO
        resultado = self.login.login(usuario, senha)

        # VERIFICAÇÃO
        self.assertFalse(resultado)


    def test_usuario_vazio(self):

        # CENÁRIO
        usuario = ""
        senha = "123"

        # EXECUÇÃO
        resultado = self.login.login(usuario, senha)

        # VERIFICAÇÃO
        self.assertFalse(resultado)


    def test_senha_vazia(self):

        # CENÁRIO
        usuario = "admin"
        senha = ""

        # EXECUÇÃO
        resultado = self.login.login(usuario, senha)

        # VERIFICAÇÃO
        self.assertFalse(resultado)

# TESTES DAS REGRAS DE NEGÓCIO

class TestRegras(unittest.TestCase):

    # Cria o objeto de regras antes de cada teste
    def setUp(self):
        self.regra = RegrasNegocio()

    def test_desconto(self):

        # CENÁRIO
        valor = 100

        # EXECUÇÃO
        resultado = self.regra.desconto(valor)

        # VERIFICAÇÃO
        self.assertEqual(resultado, 90)


    def test_desconto_vip(self):

        # CENÁRIO
        valor = 100

        # EXECUÇÃO
        resultado = self.regra.desconto_vip(valor)

        # VERIFICAÇÃO
        self.assertEqual(resultado, 80)


    def test_media(self):

        # CENÁRIO
        notas = [7, 8, 9]

        # EXECUÇÃO
        resultado = self.regra.media(notas)

        # VERIFICAÇÃO
        self.assertEqual(resultado, 8)


    def test_aprovado(self):

        # CENÁRIO
        media = 7

        # EXECUÇÃO
        resultado = self.regra.aprovado(media)

        # VERIFICAÇÃO
        self.assertTrue(resultado)


    def test_reprovado(self):

        # CENÁRIO
        media = 5

        # EXECUÇÃO
        resultado = self.regra.aprovado(media)

        # VERIFICAÇÃO
        self.assertFalse(resultado)

# TESTES DO CARRINHO DE COMPRAS

class TestCarrinho(unittest.TestCase):

    # Cria um carrinho vazio antes de cada teste
    def setUp(self):
        self.carrinho = Carrinho()

    def test_adicionar(self):

        # CENÁRIO
        valor = 50

        # EXECUÇÃO
        self.carrinho.adicionar(valor)

        # VERIFICAÇÃO
        self.assertIn(valor, self.carrinho.itens)


    def test_remover(self):

        # CENÁRIO
        valor = 50
        self.carrinho.adicionar(valor)

        # EXECUÇÃO
        self.carrinho.remover(valor)

        # VERIFICAÇÃO
        self.assertNotIn(valor, self.carrinho.itens)


    def test_total(self):

        # CENÁRIO
        self.carrinho.adicionar(50)
        self.carrinho.adicionar(30)

        # EXECUÇÃO
        total = self.carrinho.total()

        # VERIFICAÇÃO
        self.assertEqual(total, 80)


# Executa todos os testes
if __name__ == "__main__":
    unittest.main()