"""o objetivo do código é criar uma API que busque as citações do Kanye West toda vez
que o botão com a cara dele for apertado e as projete nas figuras
abaixo importadas, para isso, primeiro importa o tkinter que vai ser usado para as imagens,
 e o requests que é um módulo usado para essas importações.
  Depois, a função def_quote vai guardar dentro
 da variável response o conteúdo do link, conhecido como endpoint, ou seja, o endereço
 onde as informações serão tiradas. Atentar que o link para buscar informações normalmente
  é de um site já para api, onde as informações podem ser obtidas no formato json,
   que é um formato simplificado, parece um dicionário, o response.raise_for_status()
    serve para trabalhar com os códigos de erro, 400 e alguma coisa.
Depois, o response, já no formato json, é guardado na variável data e quote é a parte da
 dicionário onde está a citação (quote).
  Por fim, o item.config modifica a tela para inserir a citação"""


from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()