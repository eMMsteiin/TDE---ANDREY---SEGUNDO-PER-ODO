nome_do_arquivo = input("Nome do Arquivo de Texto: ")


abrir = open(nome_do_arquivo, "r")
indice = 0
ler = abrir.readlines()

num_de_linhas = len(ler)

for i in range(num_de_linhas):
    linha_especifica = ler[indice].strip()
    
    if linha_especifica == "U":
        
        organizar = ler[indice + 1].strip()
        organizar_num0 = ler[indice + 2].strip()

        converter = set(list(map(int, organizar.split(","))))
        converter0 = set(list(map(int, organizar_num0.split(","))))

        uniao = converter.union(converter0)

        print("União: conjunto 1 {}, conjunto 2 {}. Resultado: {} ".format(converter, converter0, uniao))


    elif linha_especifica == "I":

        organizar_num1 = ler[indice + 1].strip()
        organizar_num2 = ler[indice + 2].strip()

        converter1 = list(map(int, organizar_num1.split(',')))
        converter2 = list(map(int, organizar_num2.split(',')))

        interseção = set(converter1) & set(converter2)

        print("Interseção: conjunto 1 {}, conjunto 2 {}. Resultado: {} ".format(converter1, converter2, interseção))

    elif linha_especifica == "D":

        organizar_num3 = ler[indice + 1].strip()
        organizar_num4 = ler[indice + 2].strip()

        converter3 = set(list(map(int, organizar_num3.split(","))))
        converter4 = set(list(map(int, organizar_num4.split(","))))

        diferenca = converter3 - converter4

        print("Diferença: conjunto 1 {}, conjunto 2 {}. Resultado: {} ".format(converter3, converter4, diferenca))

       

    
    elif linha_especifica == "C":
        organizar_num5 = ler[indice + 1].strip()
        organizar_num6 = ler[indice + 2].strip()

        converter5 = set(list(map(int, organizar_num5.split(","))))
        converter6 = set(list(map(int, organizar_num6.split(","))))

        produto_cartesiano = []
        
        for elemento in converter5:
            for elemento2 in converter6:
                produto_cartesiano.append((elemento, elemento2))

        print("Produto Cartesiano: conjunto 1 {}, conjunto 2 {}. Resultado: {} ".format(converter5, converter6, produto_cartesiano))




        




        

        
       

        

        




         



        
        

    indice += 1


abrir.close()