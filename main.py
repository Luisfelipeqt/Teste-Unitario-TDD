from funcionario import Funcionario

#lucas = Funcionario("Lucas Carbalho", "13/02/1995", 1000)
#print(lucas.idade())


def teste_idade():
    funcionario_teste = Funcionario("Teste", "13/02/1995", 1111)
    print(f"Teste = {funcionario_teste.idade()}")
    
    funcionario_teste2 = Funcionario("Teste2", "13/02/1895", 1111)
    print(f"Teste = {funcionario_teste2.idade()}")
    
    funcionario_teste3 = Funcionario("Teste3", "13/02/1795", 1111)
    print(f"Teste = {funcionario_teste3.idade()}")

    funcionario_teste4 = Funcionario("Teste4", "13/02/1695", 1111)
    print(f"Teste = {funcionario_teste4.idade()}")

teste_idade()