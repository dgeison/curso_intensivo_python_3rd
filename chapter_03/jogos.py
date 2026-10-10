import itertools
from typing import List, Set
import random

def gerar_fechamento_guloso(numeros_escolhidos: List[int], garantia: int = 14):
    """
    Gera um fechamento reduzido para a Lotofácil.
    
    Args:
        numeros_escolhidos: Lista com os números que você quer jogar (ex: 18 números).
        garantia: Mínimo de acertos desejado (ex: 14) caso as 15 sorteadas estejam no seu conjunto.
    """
    
    # 1. Validação básica
    if len(numeros_escolhidos) < 15:
        raise ValueError("Você precisa escolher pelo menos 15 números.")
        
    print(f"--- Iniciando Fechamento para {len(numeros_escolhidos)} números ---")
    print(f"Garantia buscada: {garantia} acertos (se as 15 sorteadas estiverem no grupo).")

    # 2. Gerar todas as combinações possíveis (Espaço Amostral)
    # Se você escolheu 18 números, isso gera C(18, 15) = 816 combinações
    todas_combinacoes = list(itertools.combinations(numeros_escolhidos, 15))
    total_combinacoes_originais = len(todas_combinacoes)
    
    # Conjunto para controle do que ainda precisa ser coberto
    # Usamos set para performance, convertendo as tuplas
    universo_a_cobrir = set(todas_combinacoes)
    
    jogos_finais = []

    # 3. Loop Guloso (Greedy)
    while universo_a_cobrir:
        # Pega uma combinação qualquer que ainda não foi coberta
        # (Neste algoritmo simples, pegamos a primeira disponível)
        jogo_base = next(iter(universo_a_cobrir))
        
        # Adiciona este jogo à nossa carteira final
        jogos_finais.append(jogo_base)
        
        # Agora precisamos remover do universo tudo que esse jogo "cobre"
        # Um jogo cobre uma combinação se tiver X ou mais números em comum com ela
        cobertos = set()
        
        base_set = set(jogo_base)
        
        for possibilidade in universo_a_cobrir:
            # Interseção entre o jogo escolhido e a possibilidade
            acertos = len(base_set.intersection(possibilidade))
            
            # Se a possibilidade teria 'garantia' de acertos com nosso jogo base,
            # então ela está coberta e pode ser removida da lista de pendências.
            if acertos >= garantia:
                cobertos.add(possibilidade)
        
        # Remove os cobertos do universo
        universo_a_cobrir -= cobertos

    # 4. Resultados
    custo_original = total_combinacoes_originais * 3.50
    custo_otimizado = len(jogos_finais) * 3.50
    economia = custo_original - custo_otimizado
    
    print(f"\n--- Resultado ---")
    print(f"Total de combinações possíveis (Desdobramento): {total_combinacoes_originais}")
    print(f"Total de jogos gerados (Fechamento): {len(jogos_finais)}")
    print(f"Redução de: {(1 - (len(jogos_finais)/total_combinacoes_originais)):.1%}")
    print(f"\nCusto Desdobramento: R$ {custo_original:,.2f}")
    print(f"Custo Fechamento:    R$ {custo_otimizado:,.2f}")
    print(f"Economia:            R$ {economia:,.2f}")
    
    return jogos_finais

# --- EXECUÇÃO ---

# Exemplo: Escolhendo 18 números aleatórios (ou seus preferidos)
def gerar_numeros_aleatorios(quantidade: int = 18, minimo: int = 1, maximo: int = 25) -> List[int]:
    """
    Gera uma lista de números aleatórios únicos dentro de um intervalo.
    
    Args:
        quantidade: Quantidade de números a gerar (padrão: 18)
        minimo: Número mínimo do intervalo (padrão: 1)
        maximo: Número máximo do intervalo (padrão: 25)
    
    Returns:
        Lista ordenada de números únicos
    """
    if quantidade > (maximo - minimo + 1):
        raise ValueError(f"Não é possível gerar {quantidade} números únicos entre {minimo} e {maximo}")
    
    numeros = random.sample(range(minimo, maximo + 1), quantidade)
    return sorted(numeros)

meus_numeros = gerar_numeros_aleatorios()
print(f"Números escolhidos: {meus_numeros}")

# Gerar cartelas
cartelas = gerar_fechamento_guloso(meus_numeros, garantia=14)

print(f"\n--- Jogos a preencher ({len(cartelas)}) ---")
for i, jogo in enumerate(cartelas):
    print(f"Jogo {i+1}: {jogo}")