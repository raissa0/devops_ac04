from unittest import TestCase
from com.kuma.cabecalho import NOMES

class TestCabecalho(TestCase):
	
		def setUp(self):
			self.cabecalho = NOMES()
		
		def test_nome(self):
			self.assertEqual(self.cabecalho.nome(), 'DEVOPS')
