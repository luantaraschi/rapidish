import os


print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      ''')

print('1. Cadastrar restauras')
print('2. Listar restaurantes')
print('3. Ativar restaurantes')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opcao: '))
# opcao_escolhida = int(opcao_escolhida)

def finalizar_app():
      os.system('cls')
      print('Encerrando!\n')

if opcao_escolhida == 1:
      print('Cadastrar restaurantes')
elif opcao_escolhida == 2:
      print('Listar restaurantes')
elif opcao_escolhida == 3:
      print('Ativar restaurante')
else:
      finalizar_app()


    
