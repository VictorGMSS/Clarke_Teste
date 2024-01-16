import React, { useState } from 'react';
import axios from 'axios';
import ConsumoInput from './components/ConsumoInput';
import FornecedoresList from './components/FornecedorList';
import getCsrfToken from './utilis/CsrfToken';

const App = () => {
  const [fornecedores, setFornecedores] = useState([]);

  const handleConsumoChange = (consumoMensal) => {
    const csrfToken = getCsrfToken();
  
    // Construa os dados do formulário
    const formData = new URLSearchParams();
    formData.append('consumo_mensal', consumoMensal);
  
    axios
      .post(
        'http://127.0.0.1:8000/fornecedores/escolher-fornecedor/',
        formData,
        {
          headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        }
      )
      .then((response) => {
        // Lógica para manipular a resposta
        if (response.data && response.data.fornecedores) {
          setFornecedores(response.data.fornecedores);
        } else {
          console.error('Resposta inválida do servidor:', response.data);
        }
      })
      .catch((error) => {
        // Lógica para lidar com erros
        console.error('Erro ao buscar fornecedores:', error);
      });
  };

  return (
    <div className="bg-gray-200 p-8">
      <ConsumoInput onConsumoChange={handleConsumoChange} />
      <FornecedoresList fornecedores={fornecedores} />
    </div>
  );
};

export default App;





