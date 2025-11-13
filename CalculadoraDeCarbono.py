from cProfile import label
from idlelib.configdialog import font_sample_text

#Importando o TK

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Definindo a class Application

root = Tk()
class Application:
    def __init__(self):
        self.root = root
        self.tipousuariovar = StringVar(value="Pessoa Física")
        self.tela()
        self.frames_da_tela()
        self.botoes()
        self.Comboboxs()
        self.textoparalabel()
        self.InserirNmr()
        root.mainloop()

#Configurando a Tela

    def tela(self):
        self.root.title ("Calculadora De Carbono")
        self.root.configure(background="teal")
        self.root.geometry("550x400")
        self.root.resizable(True, True)
        self.root.maxsize(700, 500)
        self.root.minsize(400, 450)

#Configurando os Frames da Tela

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd = 4, bg = "light cyan",
                            highlightbackground= "darkslategray", highlightthickness=3 )
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.frame2 = Frame(self.root, bd = 4, bg = "light cyan",
                            highlightbackground= "darkslategray", highlightthickness=3 )
        self.frame2.place(relx=0.45, rely=0.6, relwidth=0.48, relheight=0.20)

#Criando os Botões do Tipo de Usuario

    def botoes(self):
        self.tipousuariovar = StringVar(value="Pessoa Física")

        self.bt_ind = Radiobutton(
            self.frame1, text="Pessoa Física", variable=self.tipousuariovar, value="Pessoa Física", bg="light cyan")
        self.bt_ind.place(relx=0.13, rely=0.25, relwidth=0.17, relheight=0.07)

        self.bt_ind2 = Radiobutton(
            self.frame1, text="Empresa", variable=self.tipousuariovar, value="Empresa", bg="light cyan")
        self.bt_ind2.place(relx=0.41, rely=0.25, relwidth=0.17, relheight=0.07)

        self.bt_ind3 = Radiobutton(
            self.frame1, text="Evento", variable=self.tipousuariovar, value="Evento", bg="light cyan")
        self.bt_ind3.place(relx=0.69, rely=0.25, relwidth=0.17, relheight=0.07)

#Criando Labels de Informações

    def textoparalabel(self):
        self.titulo = Label (self.frame1, text = "Calculadora De Carbono")
        self.titulo.place(relx=0.13, rely=0.05)
        self.titulo.config(font = ("Times New Roman", 28))
        self.titulo.configure(background="light cyan")
        self.textoparalabel1 = Label (self.frame1, text = "Tipo de Setor/Atividade:")
        self.textoparalabel1.place(relx=0.04, rely=0.40)
        self.textoparalabel1.configure(background="light cyan")
        self.textoparalabel2 = Label (self.frame1, text = "Quantidade Emitida:")
        self.textoparalabel2.place(relx=0.045, rely=0.60)
        self.textoparalabel2.configure(background="light cyan")
        self.textoparalabel3 = Label (self.frame1, text = "Unidade de Medida:")
        self.textoparalabel3.place(relx=0.56, rely=0.40)
        self.textoparalabel3.configure(background="light cyan")
        self.textoresultado = Label (self.frame2, text = "Resultado da Emissão em CO₂e (Equivalente):")
        self.textoresultado.place(relx=0.01, rely=0.01)
        self.textoresultado.configure(background="powderblue")

#Criando Comboboxs para inserir as informações

    def Comboboxs(self ):
        opcoes = ["Combustíveis, Energia elétrica (CO2)", "Decomposição de resíduos orgânicos, Lixo (CH4)", "Fertilizantes, Adubo, Queima de biomassa (N2O)"]
        self.Combobox = ttk.Combobox(self.frame1, values=opcoes, state= "readonly" )
        self.Combobox.set("Insira o Tipo ->")
        self.Combobox.place(relx=0.045, rely=0.45, relwidth=0.51, relheight=0.08)
        opcoes2 = ["Litros (L)", "Toneladas (t)", "Quilos (Kg)", "Watts (W)", "Quilômetros (Km)"]
        self.Combobox2 = ttk.Combobox(self.frame1, values=opcoes2, state= "readonly" )
        self.Combobox2.set("Insira a Unidade ->")
        self.Combobox2.place(relx=0.56, rely=0.45, relwidth=0.4, relheight=0.08)

#Criando local para inserir a quantidade de carbono

    def InserirNmr(self ):
        self.entrynumero = Entry(self.frame1)
        self.entrynumero.place(relx=0.045, rely=0.65, relwidth=0.35, relheight=0.08)
        self.bntcalcular = Button(self.frame1, text = "Calcular", command = self.processarNmr)
        self.bntcalcular.place(relx=0.15, rely=0.8, relwidth=0.15, relheight=0.08)

#Processamento de Informações e Calculos

    def processarNmr(self):

#Mensagens de aviso

        try:
            quantidade = float(self.entrynumero.get())
            messagebox.showinfo ("Número inserido", f"Quantidade Inserida: {quantidade}")
        except ValueError:
            messagebox.showerror ("Erro", "Por favor, digite um numero válido!")
            return

        try:
            tipoGas = self.Combobox.get()
            unidade = self.Combobox2.get()
            quantidadekg = float(self.entrynumero.get())

            if tipoGas == "Insira o Tipo ->" or unidade == "Insira a Unidade ->":
                messagebox.showwarning("Aviso", "Selecione o tipo de gás e a unidade de medida.")
                return

#Conversões das unidades para KG

            if unidade == "Toneladas (t)":
                quantidadekg = quantidade * 1000
            elif unidade == "Quilos (Kg)":
                quantidadekg = quantidade
            elif unidade == "Watts (W)":
                quantidadekg = quantidade * 0.000084
            elif unidade == "Litros (L)":
                quantidadekg = quantidade * 0.00198
            elif unidade == "Quilômetros (Km)":
                quantidadekg = quantidade * 0.12
            else:
                quantidadekg = quantidade

#Fatores de Potencial de Aquecimento Global (GWP)

            if tipoGas == "Dióxido de Carbono (CO2)":
                fator = 1
            elif tipoGas == "Metano (CH4)":
                fator = 25
            elif tipoGas == "Óxido Nitroso (N2O)":
                fator = 298
            else:
                fator = 1

#Resultado em kg CO₂ equivalente

            emissao = quantidadekg * fator
            tipo_usuario = self.tipousuariovar.get()

#Resultado do quanto de carbono foi emitido

            if tipo_usuario == "Pessoa Física":
                msg = f"Você emitiu aproximadamente {emissao:.2f} kg de CO₂eq."
            elif tipo_usuario == "Empresa":
                msg = f"Sua empresa emitiu aproximadamente {emissao:.2f} kg de CO₂eq."
            elif tipo_usuario == "Evento":
                msg = f"Seu evento emitiu aproximadamente {emissao:.2f} kg de CO₂eq."
            else:
                msg = f"Emissão estimada: {emissao:.2f} kg de CO₂eq."

#Limpa os resultados anteriores no frame2 (exceto o texto principal)

            for widget in self.frame2.winfo_children():
                if isinstance(widget, Label) and widget != self.textoresultado:
                    widget.destroy()

#Criando a label de resultado dentro do frame2

            self.resultadolabel = Label(self.frame2, text= msg, bg="light cyan", wraplength=220, justify=LEFT)
            self.resultadolabel.place(relx=0.01, rely=0.3)

#Erro se o Usuario não digitar um Numero

        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número válido!")


Application()

