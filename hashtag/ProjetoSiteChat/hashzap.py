# frontend -> usuário vê/interage
# backend -> logica por tras do site

# titulo Hashzap
# botao iniciar o chat
    # popup
        # bem vindo ao hashzap
        # escreva seu nome
        # entrar no chat

# chat
    # lira entrou no chat
    # mensagem do usuário

# campo para enviar mensagem
# botao de enviar

import flet as ft
def main(pagina):
    titulo = ft.Text("PCD Tecnologia")
    
    def iniciar_chat(evento):
        print('Iniciar chat')

    botao = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)
        
    pagina.add(titulo)
    pagina.add(botao)

    
    



ft.app(main)