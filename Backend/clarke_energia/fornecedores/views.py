from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Fornecedor
import logging
logger = logging.getLogger(__name__)

def escolher_fornecedor(request):
    if request.method == 'POST':
        consumo_mensal = request.POST.get('consumo_mensal')
        logger.debug(f'Valor de consumo_mensal: {consumo_mensal}')

        if consumo_mensal:
            fornecedores_disponiveis = Fornecedor.objects.filter(limite_minimo_kwh__lte=consumo_mensal)
            data = [{'nome': fornecedor.nome,
                     'logo': fornecedor.logo.url,
                     'estado': fornecedor.estado,
                     'custo_por_kwh': fornecedor.custo_por_kwh,
                     'limite_minimo_kwh': fornecedor.limite_minimo_kwh,
                     'num_total_clientes': fornecedor.num_total_clientes,
                     'avaliacao_media': fornecedor.avaliacao_media}
                    for fornecedor in fornecedores_disponiveis]
            return JsonResponse({'fornecedores': data})
        else:
           return JsonResponse({'error': 'Algo deu errado. Verifique os dados da solicitação.'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido.'}, status=405)
