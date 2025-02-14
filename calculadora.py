import customtkinter as ctk

class app(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.frame = ctk.CTkFrame(self, width=300, height=50, fg_color='#116')
        self.frame.pack()

        self.lb_title = ctk.CTkLabel(self.frame, text='Calculadora', font=('Roboto bold', 24))
        self.lb_title.place(x=80, y=10)

        self.spam = ctk.CTkLabel(self, text='Esta é uma simples calculadora!\nUse somente para fins acadêmicos.')
        self.spam.pack(pady=6)

        self.entry = ctk.CTkEntry(self, width=250, font=('Roboto bold', 18))
        self.entry.pack(pady=20)

        self.result = ctk.CTkLabel(self, text='', text_color='teal', font=('Roboto bold', 20))
        self.result.pack()

        self.btn = ctk.CTkButton(self, width=250, text='Calcular'.upper(), command=self.calcular)
        self.btn.pack(pady=20)

    def calcular(self):
        try:
            # Obtém a entrada do usuário e avalia a expressão
            resultado = eval(self.entry.get())
            self.result.configure(text=str(resultado))
        except Exception as e:
            # Se houver erro, mostra "Erro!" na tela
            self.result.configure(text='Erro!')

app = app()
app.title('Simples Calculadora')
app.geometry('300x300')
app.resizable(False, False)
app.mainloop()
