from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse

from .models import Fornecedor

class EscolherFornecedorTestCase(TestCase):
    def test_escolher_fornecedor_post(self):
        # Crie um fornecedor para testar
        fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            logo='caminho/para/logo.png',
            estado='SP',
            custo_por_kwh=0.5,
            limite_minimo_kwh=100,
            num_total_clientes=10,
            avaliacao_media=4.5
        )

        # URL reversa para a view
        url = reverse('escolher-fornecedor/')

        # Simule uma solicitação POST com um valor de consumo_mensal
        response = self.client.post(url, {'consumo_mensal': 150})

        # Verifique se a resposta é um JSON com os detalhes do fornecedor
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf-8'),
            {'fornecedores': [{'nome': 'Fornecedor Teste',
                               'logo': 'caminho/para/logo.png',
                               'estado': 'SP',
                               'custo_por_kwh': 0.5,
                               'limite_minimo_kwh': 100,
                               'num_total_clientes': 10,
                               'avaliacao_media': 4.5}]}
        )

    def test_escolher_fornecedor_post_sem_consumo_mensal(self):
        # URL reversa para a view
        url = reverse('escolher-fornecedor/')

        # Simule uma solicitação POST sem um valor de consumo_mensal
        response = self.client.post(url, {})

        # Verifique se a resposta contém um erro e tem o status 400
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(
            str(response.content, encoding='utf-8'),
            {'error': 'Algo deu errado. Verifique os dados da solicitação.'}
        )

    def test_escolher_fornecedor_metodo_nao_permitido(self):
        # URL reversa para a view
        url = reverse('escolher-fornecedor/')

        # Simule uma solicitação GET
        response = self.client.get(url)

        # Verifique se a resposta contém um erro e tem o status 405
        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(
            str(response.content, encoding='utf-8'),
            {'error': 'Método não permitido.'}
        )
