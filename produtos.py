def setor():   
    
    print("Olá!! Bem vindo(a) ao Super Mercado do Ximbica, está tudo bem? Espero que sim!, bem agora eu irei lhe mostrar nossos setores, por favor escolha o de sua preferência.")
    print("   ")
    print(" 1. Higiene e Beleza\n","2. Lipeza\n","3. Bebidas\n","4. Mercearia\n","5. Laticinios\n","6. Refrigerados\n","7. Horti-fruti\n","8. Padaria\n","9. Açougue")
    print("   ")
    setor = int(input("decidiu qual Setor irá visitar primeiro? se sim, digite seu numero aqui: "))

    return setor


def biblioteca(valor):    
    d = {}
    d[1] = "Papel Higiênico"
    d[2] = "Shampoo"
    d[3] = "Condicionador"
    d[4] = "Maquiagens"
    d[5] = "Detergente"
    d[6] = "Desenfetante"
    d[7] = "Amaciante"
    d[8] = "Sabão em Pó"
    d[9] = "Cervejas"
    d[10] = "Refrigerantes"
    d[11] = "Vinhos"
    d[12] = "Sucos Naturais"
    d[13] = "Serrote"
    d[14] = "Furadeiras e Pregos"
    d[15] = "Serra Circular"
    d[16] = "Lixadeira"
    d[17] = "Leite"
    d[18] = "Legumes de laticinios"
    d[19] = "Proteina"
    d[20] = "Grãos"
    d[21] = "Hamburguer"
    d[22] = "Comida Congelada"
    d[23] = "Nuggets"
    d[24] = "Massas Congeladas"
    d[25] = "Legumes"
    d[26] = "Verduras"
    d[27] = "Vegetais"
    d[28] = "Frutas"
    d[29] = "Pães"
    d[30] = "Doces"
    d[31] = "Frios"
    d[32] = "Bebidas Quentes"
    d[33] = "Carne de Boi"
    d[34] = "Carne de Porco"
    d[35] = "Carne pra Churrasco"
    d[36] = "Linguiça"

    return d[valor]




def produtos_1():    
    produtos_1 = (" 1. Papel Higiênico\n 2. Shampoo\n 3. Condicionador\n 4. Maquiagens")
    return print(produtos_1)
def produtos_2():
    produtos_2 = (" 5. Detergente\n 6. Desinfetante\n 7. Amaciante\n 8. Sabão em pó")
    return print(produtos_2)
def produtos_3():
    produtos_3 = (" 9. Cervejas\n 10. Refrigerantes\n 11. Vinhos\n 12. Sucos Naturais")
    return print(produtos_3)
def produtos_4():
    produtos_4 = (" 13. Serrote\n 14. Furadeira e Pregos\n 15. Serra Circular\n 16. Lixadeira")
    return print(produtos_4)
def produtos_5():
    produtos_5 = (" 17. Leite\n 18. Legumes\n 19. Proteína\n 20. Grãos")
    return print(produtos_5)
def produtos_6():
    produtos_6 = (" 21. Hamburguer\n 22. Comida Congelada\n 23. Nuggets\n 24. Massas Congeladas")
    return print(produtos_6)
def produtos_7():
    produtos_7 = (" 25. Legumes\n 26. Verduras\n 27. Vegetais\n 28. Frutas")
    return print(produtos_7)
def produtos_8():
    produtos_8 = (" 29. Pães\n 30. Doces\n 31. Frios\n 32. Bebidas quentes")
    return print(produtos_8)
def produtos_9():
    produtos_9 = (" 33. Carne de Boi\n 34. Carne de Porco\n 35. Carne para Churrasco\n 36. Linguiça")
    return print(produtos_9)



def escolha_produto():
        
    numo = setor() 

    if numo == 1:
        print("certo agora iremos te mostrar os produtos do setor 1, por favor escolha o de seu agrado.")
        print(' ')
        produtos_1()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 2:
        print("certo agora iremos te mostrar os produtos do setor 2, por favor escolha o de seu agrado.")
        print(' ')
        produtos_2()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 3:
        print("certo agora iremos te mostrar os produtos do setor 3, por favor escolha o de seu agrado.")
        print(' ')
        produtos_3()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 4:
        print("certo agora iremos te mostrar os produtos do setor 4, por favor escolha o de seu agrado.")
        print(' ')
        produtos_4()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 5:
        print("certo agora iremos te mostrar os produtos do setor 5, por favor escolha o de seu agrado.")
        print(' ')
        produtos_5()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 6:
        print("certo agora iremos te mostrar os produtos do setor 6, por favor escolha o de seu agrado.")
        print(' ')
        produtos_6()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 7:
        print("certo agora iremos te mostrar os produtos do setor 7, por favor escolha o de seu agrado.")
        print(' ')
        produtos_7()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 8:
        print("certo agora iremos te mostrar os produtos do setor 8, por favor escolha o de seu agrado.")
        print(' ')
        produtos_8()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 9:
        print("certo agora iremos te mostrar os produtos do setor 9, por favor escolha o de seu agrado.")
        print(' ')
        produtos_9()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")
    
    return num_produto



def carrinho():
    prod = escolha_produto()
    carrinho_compras = []
    carrinho_compras.append(biblioteca(prod))

    mais_prod = int(input(" Deseja adicionar mais produtos para seu carrinho?\n digite 55 para sim,  digite 56 para não: "))
    print(" ")

    while mais_prod == 55:
        print(" ")
        prod = escolha_produto()
        carrinho_compras.append(biblioteca(prod))
        mais_prod = int(input(" Deseja adicionar mais produtos para seu carrinho?\n digite 55 para sim,  digite 56 para não: "))
        print(" ")
    
    else:
        print("Carrinhos:", carrinho_compras)
        confirmação = int(input(" o carrinho está correto ou gostaria de acrescentar algo?\n digite 00 para confirmar o carrinho digite 11 para acrescentar algo mais: "))
        print(" ")

        while confirmação == 11:
            prod = escolha_produto()
            carrinho_compras.append(biblioteca(prod))
            print(" ")
            mais_prod = int(input(" Deseja adicionar mais produtos para seu carrinho?\n digite 55 para sim,  digite 56 para não: "))
            print(" ")

            if mais_prod == 56:
                print("Carrinhos:", carrinho_compras)
                print("Obrigado pro vir ao mercado do Xinbica, Até Mais!!!")
                break
                

        if confirmação == 00:
            
            print("Obrigado pro vir ao mercado do Xinbica, Até Mais!!!")
            
        


carrinho()
