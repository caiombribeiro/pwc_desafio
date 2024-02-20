import pandas as pd

entrada_df = pd.read_excel("entrada.xlsx")

def armazenar_endereco(endereco):
    #Separação da palavra em lista e remoção da vírgula
    endereco_separado = endereco.split(" ")
    # Remoção da virgula de todas as palavras para facilitar o manejamento
    endereco_separado = [e.replace(",","") for e in endereco_separado]


    # Casos Simples - Se a lista tiver menos de 2 itens, ela retorna a lista normal ou revertida caso o número venha primeiro
    if len(endereco_separado) == 2:
        if endereco_separado[0].isdigit() == False:
            return {'endereco': endereco_separado[0], 'numero': endereco_separado[1]}
        else:
            return {'endereco': endereco_separado[1], 'numero': endereco_separado[0]}
    else:
        # Aqui eu contarei quantas vezes algum número aparece. Se for mais de uma, terá uma tratativa diferente
        contador = sum(1 for e in endereco_separado if e.isdigit())

        conjunto_final = {}

        if contador == 1:
            # Se o contador for 1 e o primeiro campo for digito, ele irá jogar o digito no último campo
            if endereco_separado[0].isdigit():
                logradouro = " ".join([e for e in endereco_separado if e.isdigit() == False])
                num_string = "".join([e for e in endereco_separado if e.isdigit()])
                conjunto_final['endereco'] = logradouro
                conjunto_final['numero'] = num_string
            
            # Se o contador for 1 e o primeiro campo não for digito, ele irá concatenar o logradouro até achar o campo que for digito
            else:
                logradouro = ""
                # Indice começa negativo -1, pois ele vai considerar o indice do valor em diante 
                indice = -1
                
                for e in endereco_separado:
                    indice += 1
                    if e.isdigit():
                        break
                    elif logradouro == "":
                        logradouro += e
                    else: 
                        logradouro += f" {e}"
                num_string = " ".join(endereco_separado[indice:])
                conjunto_final['endereco'] = logradouro
                conjunto_final['numero'] = num_string

            

        # Se o contador for maior que 2, o código concatenará até o primeiro digito para logradouro e o restante será considerado número do endereço 
        else:
            logradouro = ""
            # Indice começa no zero, pois ele vai considerar um valor após o primeiro 
            indice = 0

            for e in endereco_separado:
                indice += 1
                if e.isdigit():
                    logradouro += f" {e}"
                    break
                elif logradouro == "":
                    logradouro += e
                else: 
                    logradouro += f" {e}"  
            num_string = " ".join(endereco_separado[indice:])
            conjunto_final['endereco'] = logradouro
            conjunto_final['numero'] = num_string
        
        # retorno da lista com logradouro e número
        return conjunto_final  
    
saida_df = entrada_df["testes"].apply(armazenar_endereco).apply(pd.Series)

saida_df.to_excel("saida.xlsx",index=False)
  