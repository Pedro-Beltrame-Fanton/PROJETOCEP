# -*- coding: utf-8 -*-
"""Projeto CEP

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-_bHQfSem1uguNwdWIMEZn7Lnl-iFDXD
"""

import streamlit as st
from scipy.stats import binom

def calcular_probabilidade_aceitacao(tamanho_amostra, itens_aceitaveis, taxa_defeitos):
    return binom.cdf(itens_aceitaveis, tamanho_amostra, taxa_defeitos)

def calcular_ITM(tamanho_lote, tamanho_amostra, taxa_aceitacao):
    return (1 - taxa_aceitacao) * (tamanho_lote - tamanho_amostra) + tamanho_amostra

def calcular_risco_fornecedor(tamanho_amostra, itens_aceitaveis, taxa_defeitos_aceitaveis):
    return 1 - binom.cdf(itens_aceitaveis, tamanho_amostra, taxa_defeitos_aceitaveis)

def calcular_risco_consumidor(tamanho_amostra, itens_aceitaveis, taxa_defeitos_inaceitaveis):
    return binom.cdf(itens_aceitaveis, tamanho_amostra, taxa_defeitos_inaceitaveis)

def main():
    st.title("Cálculo de Inspeção e Aceitação de Lotes")

    tamanho_lote = st.number_input("Informe o tamanho do lote:", min_value=1, value=100)
    tamanho_amostra = st.number_input("Informe o tamanho da amostra:", min_value=1, value=10)
    itens_aceitaveis = st.number_input("Informe o número de itens aceitáveis:", min_value=0, value=2)
    taxa_defeitos = st.number_input("Informe a taxa de defeitos esperada (0 a 1):", min_value=0.0, max_value=1.0, value=0.05)
    numero_lotes = st.number_input("Informe o número de lotes:", min_value=1, value=10)
    custo_unitario = st.number_input("Informe o custo unitário:", min_value=0.0, value=10.0)
    custo_lote_rejeitado = st.number_input("Informe o custo de deslocamento por lote rejeitado:", min_value=0.0, value=100.0)
    taxa_defeitos_aceitaveis = st.number_input("Informe a taxa de defeitos aceitável (NQA) (0 a 1):", min_value=0.0, max_value=1.0, value=0.05)
    taxa_defeitos_inaceitaveis = st.number_input("Informe a taxa de defeitos inaceitável (PTDL) (0 a 1):", min_value=0.0, max_value=1.0, value=0.1)

    if st.button("Calcular"):
        taxa_aceitacao = calcular_probabilidade_aceitacao(tamanho_amostra, itens_aceitaveis, taxa_defeitos)
        ITM = calcular_ITM(tamanho_lote, tamanho_amostra, taxa_aceitacao)
        custo_inspecao = numero_lotes * ITM * custo_unitario
        custo_deslocamento = numero_lotes * custo_lote_rejeitado * (1 - taxa_aceitacao)
        custo_total = custo_inspecao + custo_deslocamento
        risco_fornecedor = calcular_risco_fornecedor(tamanho_amostra, itens_aceitaveis, taxa_defeitos_aceitaveis)
        risco_consumidor = calcular_risco_consumidor(tamanho_amostra, itens_aceitaveis, taxa_defeitos_inaceitaveis)

        st.write(f"A probabilidade de aceitação do lote é: {taxa_aceitacao:.4f}")
        st.write(f"O ITM (Índice de Tamanho do Lote) é: {ITM:.2f}")
        st.write(f"O custo de inspeção é: R${custo_inspecao:.2f}")
        st.write(f"O custo de deslocamento é: R${custo_deslocamento:.2f}")
        st.write(f"O custo total é: R${custo_total:.2f}")
        st.write(f"O risco do fornecedor (rejeição injusta) é: {risco_fornecedor:.4f}")
        st.write(f"O risco do consumidor (aceitação injusta) é: {risco_consumidor:.4f}")

if __name__ == "__main__":
    main()
