#ZeroDivisonError  -> Acontece quando tentamos realizar uma divisão por zero
#ValueError        -> Acontece quando tentamos converter uma variável da forma errada
#IndexError        -> Quando tentamos acessar uma lista que não contém aquele índice
#FileNotFoundError -> Quando tentamos acessar um arquivo que não existe
#NameError         -> Quando uma variável não existe

def escreve_log(nome_opcao : str, nome_erro : str):
    with open("log.txt", "a+") as arquivo:
        arquivo.write("Erro na funcao: " + nome_opcao + " Descricao do erro: " + 
                      str(nome_erro) + "\n")
    print("Arquivo de log gerado com sucesso")

def simula_erro(opcao : int):
    deu_erro = False
    if opcao == 1:
        print("Simulação de divisão por Zero")
        #Tenta executar uma linha
        #Caso alguma linha dê erro, ele para a execução e pula direto para o except
        try:
            resultado = 10 / int(input("Digite um número inteiro: "))
            print(resultado)
            deu_erro = False
        #Será executado somente se as linhas dentro do Try derem erro
        except Exception as nome_erro: #Jogamos o erro para dentro de uma variável
            deu_erro = True
            print(f"O erro foi: {nome_erro}")
            escreve_log("Opcao 1, divisao por zero", nome_erro)
        #Sempre será executado, independente se deu certo ou não
        finally:
            return deu_erro
    if opcao == 2:
        print("Simulação de conversão")
        try:
            variavel = float(input("Digite um valor que pode ser convertido para float"))
            print(f"{variavel:.1f}")
            deu_erro = False
        except Exception as nome_erro:
            deu_erro = True
            escreve_log("Opcao 2, erro de conversao", nome_erro)
        finally:
            return deu_erro
#IndexError        -> Quando tentamos acessar uma lista que não contém aquele índice
#FileNotFoundError -> Quando tentamos acessar um arquivo que não existe

                            #r -> leitura , a+ append, w -> escrita
#with open("nome_arquivo", "modo_do_arquivo")

if simula_erro(int(input("Digite qual opção você quer tentar: "))):
    print("Deu erro")
else:
    print("Não deu erro")