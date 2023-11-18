import os
# Define a função de pesquisa binária
def pesquisaBinaria(codigoCadastrados, minimo, maximo, buscar):
    if minimo > maximo:
        return -1  # Se o valor mínimo for maior que o máximo, retorna -1 indicando que o item não foi encontrado

    meio = (minimo + maximo) // 2  # Calcula o índice do meio
    if codigoCadastrados[meio] == buscar:  # Se o item do meio for o item procurado, retorna o índice do meio
        return meio
      
    elif codigoCadastrados[meio] > buscar:  # Se o item do meio for maior que o item procurado, faz a pesquisa na metade da esquerda
        return pesquisaBinaria(codigoCadastrados, minimo, meio - 1, buscar)
      
    else:  # Se o item do meio for menor que o item procurado, faz a pesquisa na metade da direita
        return pesquisaBinaria(codigoCadastrados, meio + 1, maximo, buscar)

# Define as listas de códigos e pessoas cadastradas
codigoCadastrados = [0,10,20,30,40,50,60,70,80,90]
pessoasCadastradas = ['Ana Silva',
                      'João Costa',
                      'Maria Santo',
                      'Pedro Oliveira',
                      'Beatriz Souza',
                      'Lucas Pereira',
                      'Fernanda Lima',
                      'Gabriel Almeida',
                      'Juliana Rocha',
                      'Rafael Gomes',]

# Inicia um loop 
while True:
    try:
        print('-' * 50)
        codigo = input('Digite o código para pesquisar o usuário desejado: ')  # Solicita ao usuário que insira um código  
        numeroProcurado = int(codigo)  # Converte o código para um número inteiro 
        print(' ')
        os.system('clear') #limpar terminal
    except ValueError:  
        print(' ')# Se o usuário inserir algo que não seja um número, exibe uma mensagem de erro e continua o loop
        print("Por favor, insira um número válido.")
        continue
    
    # Chama a função de pesquisa binária para encontrar o índice do código na lista de códigos cadastrados
    paraTeste = pesquisaBinaria(codigoCadastrados, 0, len(codigoCadastrados) - 1, numeroProcurado)
    if paraTeste != -1:  # Se o código foi encontrado, exibe o nome da pessoa correspondente
        print(' ')
        print(f'O usuário com o código {numeroProcurado} é {pessoasCadastradas[paraTeste]}')
         
    else:  # Se o código não foi encontrado, pergunta ao usuário se ele deseja cadastrar uma nova pessoa com esse código
        print(' ')
        print('Este usuário não está cadastrado.')
        resposta = input('Deseja cadastrá-lo? (S/N): ').upper()
      
        if resposta == 'S': 
            print(' ')
            nome = input('Digite o nome do novo usuário: ')
            codigoCadastrados.append(numeroProcurado)
            codigoCadastrados.sort()
            pessoasCadastradas.append(nome)
            print(' ')
            print(f'O usuário {nome} foi cadastrado com o código {numeroProcurado}.')
          
        else:  
            print(' ')
          # Pergunta ao usuário se ele deseja continuar com o programa após o cadastro
        continuarPrograma = input('Deseja continuar com o programa? (S/N): ').upper()
        if continuarPrograma == 'S':
          continue
        else:
          print('Programa encerrado!!')# Se o usuário responder não, encerra o loop e, portanto, o programa.
        print(' ')
        break
      
# Após o término do loop, exibe a lista de pessoas cadastradas e a primeira e a última pessoa a serem adicionadas
print('Lista de pessoas cadastradas:', pessoasCadastradas)
print(' ')
print('Primeira pessoa cadastrada:', pessoasCadastradas[0])
print(' ')
print('Última pessoa cadastrada:', pessoasCadastradas[-1])
