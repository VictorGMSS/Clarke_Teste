import React, { useState } from 'react';
import logoClarke from '../assets/Logo_ClarkeEneriga.jpg'

const ConsumoInput = ({ onConsumoChange }) => {
  const [consumoMensal, setConsumoMensal] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onConsumoChange(consumoMensal);
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto my-8 p-6 bg-white rounded shadow-md">
      <div className="mb-4">
        
        <img
          src={logoClarke}
          alt={`${logoClarke} Logo`}
          className="mx-auto rounded-full object-center object-cover w-24 h-24 filter-none"
        />
        <label htmlFor="Clarke" className="block white text-xl font-bold mb-6">
          <p className="text-center">Clarke Energia Desafio</p>
        </label>
        
        <label htmlFor="consumoMensal" className="block text-gray-700 text-sm font-bold mb-2">
          Consumo Mensal (kWh):
        </label>
        <input
          id="consumoMensal"
          type="number"
          className="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500"
          value={consumoMensal}
          onChange={(e) => setConsumoMensal(e.target.value)}
        />
      </div>
      <button
        type="submit"
        className="w-full bg-blue-500 text-white p-3 rounded hover:bg-blue-600 focus:outline-none"
      >
        Buscar Fornecedores
      </button>
    </form>
  );
};

export default ConsumoInput;
