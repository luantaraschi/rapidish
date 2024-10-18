import os

restaurantes = ['Tropicália', 'Baião Bistro', 'Yaki Station']

def exibir_nome():
      print('''
█▀█ ▄▀█ █▀█ █ █▀▄ █ █▀ █░█
█▀▄ █▀█ █▀▀ █ █▄▀ █ ▄█ █▀█
      ''')

def exibir_opcoes():
      print('1. Cadastrar restauras')
      print('2. Listar restaurantes')
      print('3. Ativar restaurantes')
      print('4. Sair\n')

def finalizar_app():
      os.system('cls')
      print('Encerrando!\n')

def opcao_invalida():
      print('Opcao invalida!\n')
      input('Pressione enter para voltar ao menu')
      main()

def cadastrar_restaurante():
      os.system('cls')
      print('Cadastro de novos restaurantes\n')
      nome_do_restaurante = input('Digite o nome do restautante a ser cadastrado: ')
      restaurantes.append(nome_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      input('\nPressione enter para voltar ao menu')
      main()

def listar_restaurantes():
      os.system('cls')
      print('Lista dos restaurantes cadastrados\n')
      for restaurante in restaurantes:
            print(f'.{restaurante}')
      input('\nPressione enter para voltar ao menu')
      main()

def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opcao: '))
            match opcao_escolhida:
                  case 1:
                        cadastrar_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        print('Ativar restaurante')
                  case 4:
                        finalizar_app()
                  case _:
                        opcao_invalida()
      except:
            opcao_invalida()

def main():
      os.system('cls')
      exibir_nome()
      exibir_opcoes()
      escolher_opcao()

if __name__ == '__main__':
      main()