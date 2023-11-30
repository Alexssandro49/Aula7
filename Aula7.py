#encoding: latin-1

#Todas as questões feitas estão neste arquivo

#Q1 Escreva uma função que recebe dois números como argumentos e retorna a divisão do primeiro pelo segundo.
print("Questão n1")
def dividir_numeros(numero1, numero2):
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        raise ValueError("Divisão por zero não permitida")

# Exemplo de uso
numero1 = 10
numero2 = 0

try:
    resultado_divisao = dividir_numeros(numero1, numero2)
    print(f"Resultado da divisão: {resultado_divisao} \n")
except ValueError as e:
    print(f"Erro: {e} \n")

#Q2 Escreva um programa que solicita ao usuário uma data no formato "dd/mm/aaaa" e verifica se ela é válida.
print("Questão n2")
from datetime import datetime

def validar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        raise ValueError("Data inválida")

data_input = input("Digite uma data no formato 'dd/mm/aaaa': ")

try:
    if validar_data(data_input):
        print(f"A data {data_input} é válida.\n")
except ValueError as e:
    print(f"Erro: {e}\n")

#Q3 Escreva uma função que recebe uma lista de números como argumento e retorna a soma dos elementos da lista. Use um bloco `try/except` para tratar o caso em que a lista contém algum elemento que não é um número e lance uma exceção personalizada com a mensagem “Lista inválida”.
print("Questão n3")
def somar_elementos(lista):
    try:
        soma = sum(lista)
        return soma
    except TypeError:
        raise ValueError("Lista inválida. Certifique-se de que todos os elementos são números.")

lista_numeros = [1, 2, 3, 4, 5]

try:
    resultado_soma = somar_elementos(lista_numeros)
    print(f"A soma dos elementos da lista é: {resultado_soma}\n")
except ValueError as e:
    print(f"Erro: {e}\n")

#Q4 Escreva um programa que solicita ao usuário um nome de arquivo e tenta abri-lo para leitura. Use um bloco `try/except` para tratar o caso em que o arquivo não existe ou não pode ser aberto e lance uma exceção personalizada com a mensagem “Arquivo inválido”.
print("Questão n4")
nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    print(f"Conteúdo do arquivo:\n{conteudo}")
except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Certifique-se de que o nome do arquivo está correto.\n")
except IOError:
    print("Erro: Não foi possível abrir o arquivo. Verifique se o arquivo está acessível.\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")
 
#Q5 Escreva um código que tente abrir um arquivo com o modo de escrita, porém o arquivo já existe. Se ocorrer uma exceção, imprima uma mensagem de erro.
print("Questão n5")
nome_arquivo = "exemplo.txt"

try:
    with open(nome_arquivo, 'w') as arquivo:
        pass
except FileExistsError:
    print(f"Erro: O arquivo '{nome_arquivo}' já existe. Não é possível abrir no modo de escrita.")
except Exception as e:
    print(f"Erro desconhecido: {e}")
print("\n")

#Q6 Escreva uma função que recebe um número inteiro positivo como argumento e retorna o fatorial desse número. Use um bloco `try/except` para tratar o caso em que o argumento é negativo ou não é um inteiro e lance uma exceção personalizada com a mensagem “Argumento inválido”.
print("Questão n6")
def calcular_fatorial(numero):
    try:
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("Argumento inválido. Deve ser um número inteiro positivo.\n")
        
        if numero == 0 or numero == 1:
            return 1
        else:
            return numero * calcular_fatorial(numero - 1)
    except ValueError as e:
        raise ValueError(e)

def calcular_fatorial(numero):
    try:
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("Argumento inválido. Deve ser um número inteiro positivo.\n")
        
        if numero == 0 or numero == 1:
            return 1
        else:
            return numero * calcular_fatorial(numero - 1)
    except ValueError as e:
        raise ValueError(e)

try:
    numero_input = int(input("Digite um número inteiro positivo: "))
    resultado_fatorial = calcular_fatorial(numero_input)
    print(f"O fatorial de {numero_input} é: {resultado_fatorial}\n")
except ValueError as e:
    print(f"Erro: {e}\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")
    
#Q7. Escreva uma função que recebe uma string como argumento e retorna o número de vogais contidas nessa string. Use um bloco `try/except` para tratar o caso em que o argumento não é uma string e lance uma exceção personalizada com a mensagem “Argumento inválido”.
print("Questão n7")
def contar_vogais(texto):
    try:
        if not isinstance(texto, str):
            raise ValueError("Argumento inválido. Deve ser uma string.\n")
       
        vogais = "aeiouAEIOU"
        contador_vogais = sum(1 for char in texto if char in vogais)

        return contador_vogais
    except ValueError as e:
        raise ValueError(e)

try:
    texto_input = input("Digite uma string: ")
    resultado_contagem = contar_vogais(texto_input)
    print(f"O número de vogais na string é: {resultado_contagem}\n")
except ValueError as e:
    print(f"Erro: {e}\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")

#Q8. Escreva uma função que recebe uma lista de strings como argumento e retorna uma nova lista com estas strings ordenadas alfabeticamente. Use um bloco `try/except` para tratar o caso em que a lista contém algum elemento que não é uma string e lance uma exceção personalizada com a mensagem “Lista inválida”.
print("Questão n8")
def ordenar_strings(lista):
    try:
        if not all(isinstance(elemento, str) for elemento in lista):
            raise ValueError("Lista inválida. Todos os elementos devem ser strings.\n")
        
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

#Q9 Escreva um programa que solicite ao usuário um índice e, em seguida, tente um elemento em uma lista. Trate exceções caso o índice esteja fora dos limites da lista.
print("Questão n9")
lista = ["a", "b", "c", "d", "e"]

try:
    indice_input = int(input("Digite um índice para acessar na lista: "))
    
    # Tentar acessar o elemento na lista
    elemento = lista[indice_input]
    print(f"Elemento na posição {indice_input}: {elemento}\n")
except IndexError:
    print("Erro: Índice fora dos limites da lista.\n")
except ValueError:
    print("Erro: Digite um número inteiro como índice.\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")
    
#Q10. Peça ao usuário para digitar um número inteiro e, em seguida, tente converter esse número em uma string. Trate a exceção que pode ocorrer.
print("Questão n10")
try:
    numero_input = int(input("Digite um número inteiro: "))
    
    # Tentar converter o número em uma string
    numero_string = str(numero_input)
    print(f"O número convertido em string: {numero_string}\n")
except ValueError:
    print("Erro: Digite um número inteiro válido.\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")

#Q11. Crie um programa que leia as configurações de um arquivo e trate exceções caso o arquivo contenha erros de formatação.
print("Questão n11")
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
        print(f"Erro: Arquivo '{arquivo}' não encontrado.\n")
    except ValueError as e:
        print(f"Erro de formatação no arquivo: {e}\n")
    except Exception as e:
        print(f"Erro desconhecido: {e}\n")

arquivo_config = "configuracoes.txt"

configuracoes = ler_configuracoes(arquivo_config)

if configuracoes:
    print("Configurações lidas com sucesso:")
    for chave, valor in configuracoes.items():
        print(f"{chave}: {valor}")
print("\n")

#Q12. Peça ao usuário para digitar uma chave e, em seguida, tente acessar um valor em um dicionário. Trate exceções caso a chave não exista.
print("Questão n12")
meu_dicionario = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}

try:
    chave_input = input("Digite uma chave para acessar no dicionário: ")
    
    valor = meu_dicionario[chave_input]
    print(f"O valor associado à chave {chave_input} é: {valor}\n")
except KeyError:
    print(f"Erro: A chave '{chave_input}' não existe no dicionário.\n")
except Exception as e:
    print(f"Erro desconhecido: {e}\n")

#Q13. Escreva um programa que trate uma exceção genérica, como `Exception`, e imprima uma mensagem personalizada.
print("Questão n13")
try:
    resultado = 10 / 0  
except Exception as e:
    print(f"Erro: {e}. Ocorreu uma exceção genérica.\n")


#Q14. Crie um programa que peça ao usuário para digitar uma senha com pelo menos 8 caracteres. Trate exceções caso a senha seja muito curta.
print("Questão n14")
try:
    senha = input("Digite uma senha com pelo menos 8 caracteres: ")
    
    if len(senha) < 8:
        raise ValueError("Senha muito curta. Deve ter pelo menos 8 caracteres.")
    
    print("Senha válida.")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro desconhecido: {e}")
print("\n")

#Q15. Escreva um programa que divida uma lista em partes iguais e trate exceções se o número de partes não for válido.
print("Questão n15")
def dividir_lista(lista, num_partes):
    try:
        if not isinstance(num_partes, int) or num_partes <= 0:
            raise ValueError("Número de partes deve ser um inteiro positivo.")

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
    num_partes_input = int(input("Digite o número de partes para dividir a lista: "))
    partes_resultantes = dividir_lista(minha_lista, num_partes_input)

    if partes_resultantes:
        print(f"A lista dividida em {num_partes_input} partes é: {partes_resultantes}")
except ValueError:
    print("Erro: Digite um número inteiro positivo válido para o número de partes.")
except Exception as e:
    print(f"Erro desconhecido: {e}")
print("\n")

#Q16. Escreva um programa que manipule múltiplas exceções em um bloco `try/except`.
print("Questão n16")
def manipular_excecoes():
    try:
        valor = int(input("Digite um número: "))
        resultado = 10 / valor
        lista = [1, 2, 3]
        elemento = lista[10]
        string = "abc"
        numero = int(string)
    except ValueError:
        print("Erro: Digite um número válido.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
    except IndexError:
        print("Erro: Índice fora dos limites da lista.")
    except Exception as e:
        print(f"Erro desconhecido: {e}")
    else:
        print("Nenhum erro ocorreu.")
    finally:
        print("Este bloco sempre é executado, independentemente de exceções.")

manipular_excecoes()
print("\n")

#Q17. Escreva um programa que contenha um loop infinito e trate exceções para permitir ao usuário interrompê-lo.
print("Questão n17")
while True:
    try:
        numero = int(input("Digite um número (ou '0' para sair): "))

        if numero == 0:
            print("Loop interrompido pelo usuário.")
            break  
        
        resultado = 10 / numero
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: Digite um número válido.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
    except KeyboardInterrupt:
        print("\nLoop interrompido pelo usuário.")
        break 
    except Exception as e:
        print(f"Erro desconhecido: {e}")
print("\n")

#Q18. Crie um programa que trate exceções aninhadas em um bloco `try/except`.
print("Questão n18")
def exemplo_excecoes_aninhadas():
    try:
        valor = int(input("Digite um número: "))
        resultado = 10 / valor

        try:
            lista = [1, 2, 3]
            indice = int(input("Digite um índice para acessar na lista: "))
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

#Q19. Escreva um programa que utilize o bloco `else` para tratar exceções.
print("Questão n19")
def exemplo_com_else():
    try:
        numero = int(input("Digite um número: "))
        resultado = 10 / numero
    except ValueError:
        print("Erro: Digite um número válido.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
    except Exception as e:
        print(f"Erro desconhecido: {e}")
    else:
        print(f"Resultado: {resultado}")
        print("Nenhum erro ocorreu.")

exemplo_com_else()
