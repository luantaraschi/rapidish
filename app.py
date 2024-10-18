import os

restaurantes = [{'nome':'Tropicália', 'categoria':'Brasileira', 'ativo':False},
                {'nome':'Baião Bistrô', 'categoria':'Regional', 'ativo':True},
                {'nome':'Yaki Station', 'categoria':'Japonesa', 'ativo':True}]

def exibir_nome():
      '''Funcao responsavel por exibir o nome do sistema'''
      print('''
█▀█ ▄▀█ █▀█ █ █▀▄ █ █▀ █░█
█▀▄ █▀█ █▀▀ █ █▄▀ █ ▄█ █▀█
      ''')

def exibir_opcoes():
      '''Funcao responsavel por exibir as opcoes do sistema'''
      print('1. Cadastrar restauras')
      print('2. Listar restaurantes')
      print('3. Alternar estado do restaurantes')
      print('4. Sair\n')

def finalizar_app():
      '''Funcao responsavel por finalizar o sistema'''
      exibir_subtitulos('Encerrando...')

def voltar_ao_menu():
      '''Funcao responsavel por voltar ao menu principal'''
      input('\nPressione enter para voltar ao menu')
      main()      

def alternar_estado():
      '''Funcao responsavel por alternar o estado do restaurante'''
      exibir_subtitulos('Vamos alterar o estado do seu restaurante')
      nome_restaurante =  input('Qual é o nome do seu restaurante? ')
      restaurante_encontrado = True
      for restaurante in restaurantes:
            if restaurante['nome'] == nome_restaurante:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem  = f'Restaurante {nome_restaurante} ativado com sucesso' if restaurante['ativo'] else f'Restaurante {nome_restaurante} desativado com sucesso'
                  print(mensagem)
      if not restaurante_encontrado:
            print('Restaurante não encontrado')
      voltar_ao_menu()

def opcao_invalida():
      '''Funcao responsavel por exibir mensagem de opcao invalida'''
      print('Opcao invalida!\n')
      voltar_ao_menu()

def exibir_subtitulos(texto):
      '''Funcao responsavel por exibir subtitulos'''
      os.system('cls')
      linha = '-' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_restaurante():
      '''Funcao responsavel por cadastrar um novo restaurante
            
      Inputs:
      - nome do restaurante
      - categoria

      Outputs:
      - adiciona um novo restaurante ao sistema

      '''
      exibir_subtitulos('Cadastrar novo restaurante')
      nome_do_restaurante = input('Digite o nome do restautante a ser cadastrado: ')
      categoria_do_restaurante = input(f'Digite a categoria do restautante {nome_do_restaurante}: ')
      dados_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
      restaurantes.append(dados_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      voltar_ao_menu()

def listar_restaurantes():
      '''Funcao responsavel por listar os restaurantes'''
      exibir_subtitulos('Lista dos restaurantes cadastrados')
      print(f'{'Restaurante:'.ljust(22)} | {'Categoria:'.ljust(20)} | Status:  |')
      print(f'{"-" * 22} | {"-" * 20} | {"-" * 8} |')
      for restaurante in restaurantes:
            estado = 'Ativo    |' if restaurante['ativo'] else 'Inativo  |'
            print(f'{restaurante["nome"].ljust(22)} | {restaurante["categoria"].ljust(20)} | {estado}')
      voltar_ao_menu()

def escolher_opcao():
      '''Funcao responsavel por exibir as opcoes e escolher a opcao'''
      try:
            opcao_escolhida = int(input('Escolha uma opcao: '))
            match opcao_escolhida:
                  case 1:
                        cadastrar_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        alternar_estado()
                  case 4:
                        finalizar_app()
                  case _:
                        opcao_invalida()
      except:
            opcao_invalida()

def main():
      '''Funcao responsavel por iniciar o programa'''
      os.system('cls')
      exibir_nome()
      exibir_opcoes()
      escolher_opcao()

if __name__ == '__main__':
      main()