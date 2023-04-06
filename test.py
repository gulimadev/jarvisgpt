import main as Main



    
#texto = "Olá, meu nome é GPT-3, sou um robô que fala e entende o que você fala. Vamos conversar?"
texto = input ("Digite o texto: ")
classe_principal = Main.Main()
classe_principal.voz_reprodutor(classe_principal.motor_gpt(classe_principal.reconhecedor_voz()))
#classe_principal.voz_reprodutor(classe_principal.motor_gpt(texto))

