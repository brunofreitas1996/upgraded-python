from tkinter import *
from tkinter import messagebox
import BancoDados
try:
    #Configuração da janela
    jan = Tk()
    jan.title('MENU')
    jan.geometry('220x301')
    jan.resizable(width=False, height=False)
    jan.attributes('-alpha', 0.8)

    logo         = PhotoImage(file='C:/Users/User/Desktop/Python/imagens/menu.png')
    icoUsuarios  = PhotoImage(file='C:/Users/User/Desktop/Python/imagens/usuarios.png')
    icoCadastrar = PhotoImage(file='C:/Users/User/Desktop/Python/imagens/cadastrar.png')
    corPadrao = 'black'
    corDaFonte = 'white'

    #Frame principal
    fr1 = Frame(jan, width=500, height=400, bg=corPadrao, relief='raise')
    fr1.pack()

    #wisgets
    lblLogo = Label(fr1, image=logo, bg=corPadrao)
    lblLogo.place(x=10,y=5)
    lblUsuarios = Label(fr1, image=icoUsuarios, bg=corPadrao)
    lblUsuarios.place(x=10, y=183)
    #Tela de usuarios cadastrados
    def usuariosCad():
        #Remover widgets da tela
        lblLogo.place(x=1000)
        lblUsuarios.place(x=1000)
        btnUsuarios.place(x=1000)
        lblCadatrar.place(x=1000)
        btnCadastrar.place(x=1000)
        #lblNome.palce(x=1000)
        ##################################################################################
        lb = Listbox(fr1, bg='black', fg='white')                                        #
        lb['width'] = 34                                                                 #
        lb['height'] = 100                                                               #
        lb.pack(side=LEFT,expand=True,fill="both")                                       #
        sb = Scrollbar(fr1)                                                              #
        sb.pack(side=RIGHT,fill="y")                                                     #
        sb.configure(command=lb.yview)
        lb.configure(yscrollcommand=sb.set)
        BancoDados.cursor.execute('''SELECT * FROM Usuarios''')
        dados = BancoDados.cursor.fetchall()
        for i in dados:
            s = str(i)
            lb.insert(END,"-"*50,s.split())
        ##################################################################################
        #Voltando a tela de Menu
        def voltarDo():
            lb.destroy()
            sb.destroy()
            btnVoltarD.place(x=1000)
            #Voltando a tela de Menu
            lblLogo.place(x=10)
            lblUsuarios.place(x=10)
            btnUsuarios.place(x=40)
            lblCadatrar.place(x=13)
            btnCadastrar.place(x=40)
        #Botao voltar dos usuarios cadastrados
        btnVoltarD = Button(fr1, text='Voltar', bg=corPadrao, fg=corDaFonte, command=voltarDo)
        btnVoltarD.place(x=162 , y=270)
        

    #Botão usuarios cadastrados
    btnUsuarios = Button(fr1, text='Usuarios Cadastradados', font=('Arial', '10', 'bold'), bg=corPadrao, fg=corDaFonte)
    btnUsuarios['command'] = usuariosCad
    btnUsuarios.place(x=40, y=183)
    lblCadatrar = Label(fr1, image=icoCadastrar, bg=corPadrao)
    lblCadatrar.place(x=13, y=230)

    #Função da tela Cadastrar
    def cadastrar():
        #Remover widgets da tela
        lblLogo.place(x=1000)
        lblUsuarios.place(x=1000)
        btnUsuarios.place(x=1000)
        lblCadatrar.place(x=1000)
        btnCadastrar.place(x=1000)
        #Campos de Cadastro
        #Nome
        txtNome = Label(fr1, text='Nome:', font=('Arial 10 bold'), fg=corDaFonte, bg=corPadrao)
        txtNome.place(x=5, y=6)
        entNome = Entry(fr1, width=25, bg=corPadrao, fg=corDaFonte)
        entNome.place(x=60, y=9)
        #Idade
        txtIdade = Label(fr1, text='Idade:', font=('Arial 10 bold'), fg=corDaFonte, bg=corPadrao)
        txtIdade.place(x=5, y=42)
        entIdade = Entry(fr1, width=10, bg=corPadrao, fg=corDaFonte)
        entIdade.place(x=60, y=44)
        #Cidade
        txtCidade = Label(fr1, text='Cidade:', font=('Arial 10 bold'), fg=corDaFonte, bg=corPadrao)
        txtCidade.place(x=5, y=72)
        entCidade = Entry(fr1, width=25, bg=corPadrao, fg=corDaFonte)
        entCidade.place(x=60, y=76)
        #Função do botão voltar
        def voltar():
            #Limpando a tela
            txtNome.place(x=1000)
            entNome.place(x=1000)
            txtIdade.place(x=1000)
            entIdade.place(x=1000)
            txtCidade.place(x=1000)
            entCidade.place(x=1000)
            btnCadastrarNoBanco.place(x=1000)
            btnVoltar.place(x=1000)
            #Voltando a tela de Menu
            lblLogo.place(x=10)
            lblUsuarios.place(x=10)
            btnUsuarios.place(x=40)
            lblCadatrar.place(x=13)
            btnCadastrar.place(x=40)
        #Botao voltar
        btnVoltar = Button(fr1, text='Voltar', bg=corPadrao, fg=corDaFonte, command=voltar)
        btnVoltar.place(x=70, y=250)

        #Cadastrar no BD
        def concluirCdastro():
            nome = entNome.get()
            idade = entIdade.get()
            cidade = entCidade.get()
            if(nome == '' or idade == '' or cidade == ''):
                messagebox.showerror(title='DADOS INCORRETOS', message='INSIRA OS DADOS')
            else:
                #Inserindo dados no BD
                BancoDados.cursor.execute('''
                INSERT INTO Usuarios (nome, idade, cidade)
                VALUES (?, ?, ?)
                ''',(nome, idade,cidade))
                BancoDados.conn.commit()
                messagebox.showinfo(title='STATUS', message='Dados inseridos com sucesso.')
            

        #Botão Cadastrar
        btnCadastrarNoBanco = Button(fr1, text='Cadastrar', bg=corPadrao, fg=corDaFonte)
        btnCadastrarNoBanco['command'] = concluirCdastro
        btnCadastrarNoBanco.place(x=120, y=250)
        
        
    #Botão cadastrar
    btnCadastrar = Button(fr1, text='Cadastrar Usuarios', font=('Arial 10 bold'), bg=corPadrao,fg=corDaFonte, width=19)
    btnCadastrar['command'] =cadastrar
    btnCadastrar.place(x=40, y=230)
except:
    print('ERRO!')




jan.mainloop()
        

