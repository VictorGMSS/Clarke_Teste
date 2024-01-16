import React, { useState } from 'react';

const FornecedorList = ({ fornecedores }) => {
  const [fornecedorSelecionado, setFornecedorSelecionado] = useState(null);

  const handleFornecedorClick = (nome) => {
    // Verifica se o fornecedor clicado já está selecionado
    // Se estiver, desseleciona, caso contrário, define como selecionado
    setFornecedorSelecionado((prev) => (prev === nome ? null : nome));
  };

  return (
    <div className='py-0 px-[10%]'>
      <h2 className="text-2xl font-bold mb-4">Fornecedores Disponíveis</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {fornecedores.map((fornecedor) => (
          <div
            key={fornecedor.nome}
            className={`p-4 rounded-md cursor-pointer transition-transform transform ${
              fornecedorSelecionado === fornecedor.nome ? 'bg-green-500 hover:scale-105' : 'bg-blue-500 hover:scale-105'
            }`}
            onClick={() => handleFornecedorClick(fornecedor.nome)}
          >
            <img src={fornecedor.logo_url}></img>
            <h2 className="text-xl font-semibold text-white">{fornecedor.nome}</h2>
            <p className="text-white">Estado: {fornecedor.estado}</p>
            <p className="text-white">Custo por kWh: {fornecedor.custo_por_kwh}</p>
            <p className="text-white">Limite mínimo de kWh: {fornecedor.limite_minimo_kwh}</p>
            <p className="text-white">Total de clientes: {fornecedor.num_total_clientes}</p>
            <p className="text-white">Avaliação média dos clientes: {fornecedor.avaliacao_media}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FornecedorList;
