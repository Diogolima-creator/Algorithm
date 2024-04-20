def imprimirResult(nome_arquivo, fc, solucao):

  nome_arquivo += '.txt'
  # Convertendo os valores para strings
  fc2_str = str(fc)
  solucao_str = ' '.join(map(str, solucao))  # Convertendo a lista em uma única string

  # Criando a lista de strings para escrever no arquivo
  arrayTxt = [fc2_str, solucao_str]

  # Abre o arquivo em modo de escrita ('w' significa write)
  with open(nome_arquivo, 'w') as arquivo:
      # Escreve os dados no arquivo
      arquivo.write('\n'.join(arrayTxt))

  print("Solução:", solucao)
  print("Custo da solução:", fc)
