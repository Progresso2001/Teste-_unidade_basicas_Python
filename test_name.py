import unittest
from name_function import formatar_nome

class NomeTesteCasos(unittest.TestCase): #criamos uma classe que herda do unittest.Testcase 
    
    def test_nome_sobrenome(self): #defimos um metodo para a classe e contera uma serie de teste de unidade. para formatar_nome()
        nome_formatado=formatar_nome('manuel', 'elias')
        self.assertEqual(nome_formatado, 'Manuel Elias')
        
    def test_nome_sobrenome_apelido(self):
        nome_formatado=formatar_nome("carla", "manuel", "costa")
        self.assertEqual(nome_formatado, "Carla Manuel Costa")# usamos o metodo assertEqual que verifica a igualidade dos nomes 
unittest.main()