def nome_programa():
    print("""
        𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
      """)
    
def opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('cadastrado')
    elif opcao_escolhida == 2:
        print('listado')
    elif opcao_escolhida == 3:
        print('ativo')
    elif opcao_escolhida == 4:
        print('saindo')
    else:
        finalizar_app()

def finalizar_app():
    print('Programa encerrado...')


def main():
    nome_programa()
    opcoes()

if __name__ == '__main__':
    main()