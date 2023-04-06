import main as Main

c = Main.Main()

man = "Gustavo"

def validador (voz):
    try:
        palavras = voz.split()
    except AttributeError:
        print ("variavel 'voz' vazia")
        execucao()
    print(voz)
    if "Oi" in palavras and "Ana" in palavras:
        print ("Oi eu estou te ouvindo!")
        c.voz_reprodutor(f"Oi {man}, eu estou te ouvindo!")
        
        c.voz_reprodutor(c.motor_gpt(c.reconhecedor_voz()))
        del palavras
        execucao()
    # elif "Jarvis" in palavras:
    #     voz_user = c.reconhecedor_voz()
    #     prompt = f"Crie um comando para usar no Powershell, sem enm uma esplicacao apois mandar o comando, somente o comando puro, a partir da descricao a seguir: {voz_user}"        
    #     comando_texto = c.motor_gpt(prompt)
    #     print (comando_texto)
    #     resposta = input("Deseja executar o comando acima?\n")
    #     if resposta == "sim":
    #         print (comando_texto)
    #         c.voz_reprodutor("Comando executado com sucesso")
    #         execucao()
    else:
        print ("Continuo escutando")
        execucao()
        
        
def execucao ():
    while True:
        #exto = input ("digite um texto")
        validador(c.reconhecedor_voz())
        #validador (texto)
        #c.voz_reprodutor(c.motor_gpt(texto))
execucao()