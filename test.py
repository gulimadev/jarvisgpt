import main as Main

c = Main.Main()



def validador (voz):
    palavras = voz.split()
    print(voz)
    if "JARVIS" in palavras:
        print ("Oi eu estou te ouvindo!")
        c.voz_reprodutor(c.motor_gpt(c.reconhecedor_voz()))
        #classe_principal.voz_reprodutor(classe_principal.motor_gpt(texto))
        
    else:
        print ("Continuo escutando")

texto = input ("digite um texto")
#validador(c.reconhecedor_voz())
#validador (texto)
c.voz_reprodutor(c.motor_gpt(texto))
