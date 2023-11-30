#encoding: latin-1

#Todas as quest�es feitas est�o neste arquivo

#Q1 Escreva uma fun��o que recebe dois n�meros como argumentos e retorna a divis�o do primeiro pelo segundo.
print("Quest�o n1")
def dividir_numeros(numero1, numero2):
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        raise ValueError("Divis�o por zero n�o permitida")

# Exemplo de uso
numero1 = 10
numero2 = 0

try:
    resultado_divisao = dividir_numeros(numero1, numero2)
    print(f"Resultado da divis�o: {resultado_divisao} \n")
except ValueError as e:
    print(f"Erro: {e} \n")

#Q2 Escreva um programa que solicita ao usu�rio uma data no formato "dd/mm/aaaa" e verifica se ela � v�lida.
print("Quest�o n2")
from datetime import datetime

def validar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        raise ValueError("Data inv�lida")

data_input = input("Digite uma data no formato 'dd/mm/aaaa': ")

try:
    if validar_data(data_input):
        print(f"A data {data_input} � v�lida.\n")
except ValueError as e:
    print(f"Erro: {e}\n")

#Q3 Escreva uma fun��o que recebe uma lista de n�meros como argumento e retorna a soma dos elementos da lista. Use um bloco `try/except` para tratar o caso em que a lista cont�m algum elemento que n�o � um n�mero e lance uma exce��o personalizada com a mensagem �Lista inv�lida�.
print("Quest�o n3")
def somar_elementos(lista):
    try:
        soma = sum(lista)
        return soma
    except TypeError:
        raise ValueError("Lista inv�lida. Certifique-se de que todos os elementos s�o n�meros.")

lista_numeros = [1, 2, 3, 4, 5]

try:
    resultado_soma = somar_elementos(lista_numeros)
    print(f"A soma dos elementos da lista �: {resultado_soma}\n")
except ValueError as e:
    print(f"Erro: {e}\n")

#Q4 Escreva um programa que solicita ao usu�rio um nome de arquivo e tenta abri-lo para leitura. Use um bloco `try/except` para tratar o caso em que o arquivo n�o existe ou n�o pode ser aberto e lance uma exce��o personalizada com a mensagem �Arquivo inv�lido�.
print("Quest�o n4")
nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    print(f"Conte�do do arquivo:\n{conteudo}")
except FileNotFoundError:
    print("Erro: Arquivo n�o encontrado. Certifique-se de que o nome do arquivo est� correto.\n")
except IOError:
    print("Erro: N�o foi poss�vel abrir o arquivo. Verifique se o arquivo est� acess�vel.\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")
 
#Q5 Escreva um c�digo que tente abrir um arquivo com o modo de escrita, por�m o arquivo j� existe. Se ocorrer uma exce��o, imprima uma mensagem de erro.
print("Quest�o n5")
nome_arquivo = "exemplo.txt"

try:
    with open(nome_arquivo, 'w') as arquivo:
        pass
except FileExistsError:
    print(f"Erro: O arquivo '{nome_arquivo}' j� existe. N�o � poss�vel abrir no modo de escrita.")
except Exception as e:
    print(f"Erro desconhecido: {e}")
print("\n")

#Q6 Escreva uma fun��o que recebe um n�mero inteiro positivo como argumento e retorna o fatorial desse n�mero. Use um bloco `try/except` para tratar o caso em que o argumento � negativo ou n�o � um inteiro e lance uma exce��o personalizada com a mensagem �Argumento inv�lido�.
print("Quest�o n6")
def calcular_fatorial(numero):
    try:
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("Argumento inv�lido. Deve ser um n�mero inteiro positivo.\n")
        
        if numero == 0 or numero == 1:
            return 1
        else:
            return numero * calcular_fatorial(numero - 1)
    except ValueError as e:
        raise ValueError(e)

def calcular_fatorial(numero):
    try:
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("Argumento inv�lido. Deve ser um n�mero inteiro positivo.\n")
        
        if numero == 0 or numero == 1:
            return 1
        else:
            return numero * calcular_fatorial(numero - 1)
    except ValueError as e:
        raise ValueError(e)

try:
    numero_input = int(input("Digite um n�mero inteiro positivo: "))
    resultado_fatorial = calcular_fatorial(numero_input)
    print(f"O fatorial de {numero_input} �: {resultado_fatorial}\n")
except ValueError as e:
    print(f"Erro: {e}\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")
    
#Q7. Escreva uma fun��o que recebe uma string como argumento e retorna o n�mero de vogais contidas nessa string. Use um bloco `try/except` para tratar o caso em que o argumento n�o � uma string e lance uma exce��o personalizada com a mensagem �Argumento inv�lido�.
print("Quest�o n7")
def contar_vogais(texto):
    try:
        if not isinstance(texto, str):
            raise ValueError("Argumento inv�lido. Deve ser uma string.\n")
       
        vogais = "aeiouAEIOU"
        contador_vogais = sum(1 for char in texto if char in vogais)

        return contador_vogais
    except ValueError as e:
        raise ValueError(e)

try:
    texto_input = input("Digite uma string: ")
    resultado_contagem = contar_vogais(texto_input)
    print(f"O n�mero de vogais na string �: {resultado_contagem}\n")
except ValueError as e:
    print(f"Erro: {e}\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")

#Q8. Escreva uma fun��o que recebe uma lista de strings como argumento e retorna uma nova lista com estas strings ordenadas alfabeticamente. Use um bloco `try/except` para tratar o caso em que a lista cont�m algum elemento que n�o � uma string e lance uma exce��o personalizada com a mensagem �Lista inv�lida�.
print("Quest�o n8")
def ordenar_strings(lista):
    try:
        if not all(isinstance(elemento, str) for elemento in lista):
            raise ValueError("Lista inv�lida. Todos os elementos devem ser strings.\n")
        
        return sorted(lista)
    except ValueError as e:
        raise ValueError(e)

try:
    lista_input = ["banana", "abacaxi", "laranja", "uva"]
    lista_ordenada = ordenar_strings(lista_input)
    print(f"Lista ordenada alfabeticamente: {lista_ordenada}\n")
except ValueError as e:
    print(f"Erro: {e}\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")

#Q9 Escreva um programa que solicite ao usu�rio um �ndice e, em seguida, tente um elemento em uma lista. Trate exce��es caso o �ndice esteja fora dos limites da lista.
print("Quest�o n9")
lista = ["a", "b", "c", "d", "e"]

try:
    indice_input = int(input("Digite um �ndice para acessar na lista: "))
    
    # Tentar acessar o elemento na lista
    elemento = lista[indice_input]
    print(f"Elemento na posi��o {indice_input}: {elemento}\n")
except IndexError:
    print("Erro: �ndice fora dos limites da lista.\n")
except ValueError:
    print("Erro: Digite um n�mero inteiro como �ndice.\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")
    
#Q10. Pe�a ao usu�rio para digitar um n�mero inteiro e, em seguida, tente converter esse n�mero em uma string. Trate a exce��o que pode ocorrer.
print("Quest�o n10")
try:
    numero_input = int(input("Digite um n�mero inteiro: "))
    
    # Tentar converter o n�mero em uma string
    numero_string = str(numero_input)
    print(f"O n�mero convertido em string: {numero_string}\n")
except ValueError:
    print("Erro: Digite um n�mero inteiro v�lido.\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")

#Q11. Crie um programa que leia as configura��es de um arquivo e trate exce��es caso o arquivo contenha erros de formata��o.
print("Quest�o n11")
def ler_configuracoes(arquivo):
    try:
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            
            configuracoes = {}
            for linha in linhas:
                chave, valor = linha.strip().split('=')
                configuracoes[chave] = valor
            
            return configuracoes
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' n�o encontrado.\n")
    except ValueError as e:
        print(f"Erro de formata��o no arquivo: {e}\n")
    except Exception as e:
        print(f"Erro desconhecido: {e}\n")

arquivo_config = "configuracoes.txt"

configuracoes = ler_configuracoes(arquivo_config)

if configuracoes:
    print("Configura��es lidas com sucesso:")
    for chave, valor in configuracoes.items():
        print(f"{chave}: {valor}")
print("\n")

#Q12. Pe�a ao usu�rio para digitar uma chave e, em seguida, tente acessar um valor em um dicion�rio. Trate exce��es caso a chave n�o exista.
print("Quest�o n12")
meu_dicionario = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}

try:
    chave_input = input("Digite uma chave para acessar no dicion�rio: ")
    
    valor = meu_dicionario[chave_input]
    print(f"O valor associado � chave {chave_input} �: {valor}\n")
except KeyError:
    print(f"Erro: A chave '{chave_input}' n�o existe no dicion�rio.\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")

#Q13. Escreva um programa que trate uma exce��o gen�rica, como `Exception`, e imprima uma mensagem personalizada.
print("Quest�o n13")
try:
    resultado = 10 / 0  
except Exception as e:
    print(f"Erro: {e}. Ocorreu uma exce��o gen�rica.\n")


#Q14. Crie um programa que pe�a ao usu�rio para digitar uma senha com pelo menos 8 caracteres. Trate exce��es caso a senha seja muito curta.
print("Quest�o n14")
try:
    senha = input("Digite uma senha com pelo menos 8 caracteres: ")
    
    if len(senha) < 8:
        raise ValueError("Senha muito curta. Deve ter pelo menos 8 caracteres.")
    
    print("Senha v�lida.")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro desconhecido: {e}")
print("\n")

#Q15. Escreva um programa que divida uma lista em partes iguais e trate exce��es se o n�mero de partes n�o for v�lido.
print("Quest�o n15")
def dividir_lista(lista, num_partes):
    try:
        if not isinstance(num_partes, int) or num_partes <= 0:
            raise ValueError("N�mero de partes deve ser um inteiro positivo.")

        tamanho_parte = len(lista) // num_partes
        partes = [lista[i:i + tamanho_parte] for i in range(0, len(lista), tamanho_parte)]

        return partes
    except ValueError as e:
        print(f"Erro: {e}")
        return None
    except Exception as e:
        print(f"Erro desconhecido: {e}")
        return None

minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    num_partes_input = int(input("Digite o n�mero de partes para dividir a lista: "))
    partes_resultantes = dividir_lista(minha_lista, num_partes_input)

    if partes_resultantes:
        print(f"A lista dividida em {num_partes_input} partes �: {partes_resultantes}")
except ValueError:
    print("Erro: Digite um n�mero inteiro positivo v�lido para o n�mero de partes.")
except Exception as e:
    print(f"Erro desconhecido: {e}")
print("\n")

#Q16. Escreva um programa que manipule m�ltiplas exce��es em um bloco `try/except`.
print("Quest�o n16")
def manipular_excecoes():
    try:
        valor = int(input("Digite um n�mero: "))
        resultado = 10 / valor
        lista = [1, 2, 3]
        elemento = lista[10]
        string = "abc"
        numero = int(string)
    except ValueError:
        print("Erro: Digite um n�mero v�lido.")
    except ZeroDivisionError:
        print("Erro: Divis�o por zero.")
    except IndexError:
        print("Erro: �ndice fora dos limites da lista.")
    except Exception as e:
        print(f"Erro desconhecido: {e}")
    else:
        print("Nenhum erro ocorreu.")
    finally:
        print("Este bloco sempre � executado, independentemente de exce��es.")

manipular_excecoes()
print("\n")

#Q17. Escreva um programa que contenha um loop infinito e trate exce��es para permitir ao usu�rio interromp�-lo.
print("Quest�o n17")
while True:
    try:
        numero = int(input("Digite um n�mero (ou '0' para sair): "))

        if numero == 0:
            print("Loop interrompido pelo usu�rio.")
            break  
        
        resultado = 10 / numero
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: Digite um n�mero v�lido.")
    except ZeroDivisionError:
        print("Erro: Divis�o por zero.")
    except KeyboardInterrupt:
        print("\nLoop interrompido pelo usu�rio.")
        break 
    except Exception as e:
        print(f"Erro desconhecido: {e}")
print("\n")

#Q18. Crie um programa que trate exce��es aninhadas em um bloco `try/except`.
print("Quest�o n18")
def exemplo_excecoes_aninhadas():
    try:
        valor = int(input("Digite um n�mero: "))
        resultado = 10 / valor

        try:
            lista = [1, 2, 3]
            indice = int(input("Digite um �ndice para acessar na lista: "))
            elemento = lista[indice]
        except IndexError as inner_error:
            print(f"Erro no bloco interno: {inner_error}")
        except ValueError as inner_error:
            print(f"Erro no bloco interno: {inner_error}")
        except Exception as inner_error:
            print(f"Erro desconhecido no bloco interno: {inner_error}")
    except ZeroDivisionError as outer_error:
        print(f"Erro no bloco externo: {outer_error}")
    except ValueError as outer_error:
        print(f"Erro no bloco externo: {outer_error}")
    except Exception as outer_error:
        print(f"Erro desconhecido no bloco externo: {outer_error}")

exemplo_excecoes_aninhadas()
print("\n")

#Q19. Escreva um programa que utilize o bloco `else` para tratar exce��es.
print("Quest�o n19")
def exemplo_com_else():
    try:
        numero = int(input("Digite um n�mero: "))
        resultado = 10 / numero
    except ValueError:
        print("Erro: Digite um n�mero v�lido.")
    except ZeroDivisionError:
        print("Erro: Divis�o por zero.")
    except Exception as e:
        print(f"Erro desconhecido: {e}")
    else:
        print(f"Resultado: {resultado}")
        print("Nenhum erro ocorreu.")

exemplo_com_else()
