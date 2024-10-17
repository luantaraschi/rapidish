import os

def exibir_nome():
      print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
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

def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opcao: '))
            match opcao_escolhida:
                  case 1:
                        print('Adicionar restaurante')
                  case 2:
                        print('Listar restaurantes')
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