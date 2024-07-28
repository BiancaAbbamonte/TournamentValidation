def validar_torneio(participantes):
  print(participantes)

  if len(participantes) % 2 != 0:
    return False  # Deve haver um número par de participantes em cada rodada
    # Ordenar os participantes para facilitar a formação de pares
    #participantes_ordenados = sorted(participantes)
  for i in range(0, len(participantes), 2):
    par = participantes[i:i + 2]
    # Verifica se o par é formado corretamente
    if not (
      par[0] < par[1] and
      participantes.index(par[0]) < participantes.index(par[1])):
        return False

    n_rodada = 0

  while len(participantes) > 1:
      # Formar pares
      pairs = [participantes[i:i + 2] for i in range(0, len(participantes), 2)]
      vencedores = []
      print(f"Rodada {n_rodada + 1}:")
      print(pairs)

      for par in pairs:
        vencedor = min(par)
        print(f"Vencedor da partida {par}: {vencedor}")
        vencedores.append(vencedor)
        #print(f"Vencedores por agora: {vencedores}")
      
      participantes = vencedores
      n_rodada = n_rodada + 1
      print(f"Vencedores da rodada: {vencedores}")

  # Se restar apenas um participante, ele é o vencedor final
  return True


# Exemplo de uso

input_participantes = [1, 8, 4, 5, 2, 7, 3, 6]
resultado = validar_torneio(input_participantes)
print(f"O torneio é válido: {resultado}")
