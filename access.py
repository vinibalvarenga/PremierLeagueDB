
from select import select
from tkinter import * 
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


class Table:

    def _init_(self, root, lst):
        total_rows = len(lst)
        total_columns = len(lst[0])
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='black',
                               font=('Arial', 14, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


def novaJanela1(time, tecnico):
    resultado = Toplevel(root)
    resultado.title("Resultado")
    resultado.geometry('300x150')
    resultado.minsize(300, 150)
    resultado.maxsize(300, 150)
    var = StringVar()
    if (tecnico != []):
        var.set("O técnico do " + time + " é: " + tecnico[0][0])
        Label(resultado, textvariable=var).pack()
    else:
        var.set("Time sem técnico")
        Label(resultado, textvariable=var).pack()


def novaJanela2(time, jogadores):
    resultado = Toplevel(root)
    resultado.title("Resultado")
    resultado.geometry('300x150')
    resultado.minsize(450, 300)

    if (jogadores != []):
        i = 0
        for jogador in jogadores:
            var = StringVar()
            j = str(i + 1)
            var.set("O " + j + "° jogador do " + time + " é o " + jogadores[i][0])
            Label(resultado, textvariable=var, font=("Courier", 10)).place(y=i * 18)
            i = i + 1
    else:
        var = StringVar()
        var.set("Time sem dados")
        Label(resultado, textvariable=var).pack()


def novaJanela3(time, partidas):
    resultado = Toplevel(root)
    resultado.title("Resultado")
    resultado.geometry('300x150')
    resultado.minsize(450, 300)

    if (partidas != []):
        i = 0
        for partida in partidas:
            var = StringVar()
            golsCasa = str(partida[1])
            golsVisitante = str(partida[3])
            var.set(partida[0] + ": " + golsCasa + " x " + golsVisitante + " " + partida[2])
            Label(resultado, textvariable=var, font=("Courier", 10)).place(y=i * 18)
            i = i + 1
    else:
        var = StringVar()
        var.set("Time sem dados")
        Label(resultado, textvariable=var).pack()


def novaJanela4(arbitro, partidas):
    resultado = Toplevel(root)
    resultado.title("Resultado")
    resultado.geometry('300x150')
    resultado.minsize(450, 300)

    if (partidas != []):
        i = 0
        for partida in partidas:
            var = StringVar()
            golsCasa = str(partida[1])
            golsVisitante = str(partida[3])
            var.set(arbitro + " apitou " + partida[0] + ": " + golsCasa + " x " + golsVisitante + " " + partida[2])
            Label(resultado, textvariable=var, font=("Courier", 10)).place(y=i * 18)
            i = i + 1
    else:
        var = StringVar()
        var.set("Time sem dados")
        Label(resultado, textvariable=var).pack()


def novaJanela5(time, partidas):
    resultado = Toplevel(root)
    resultado.title("Resultado")
    resultado.geometry('300x150')
    resultado.minsize(450, 300)

    if (partidas != []):
        i = 0
        for partida in partidas:
            var = StringVar()
            golsCasa = str(partida[1])
            golsVisitante = str(partida[3])
            var.set("O " + time + " não tomou gols em: " + partida[0] + ": " + golsCasa + " x " + golsVisitante + " " +
                    partida[2])
            Label(resultado, textvariable=var, font=("Courier", 10)).place(y=i * 18)
            print(partida)
            i = i + 1
    else:
        var = StringVar()
        var.set("Time sem dados")
        Label(resultado, textvariable=var).pack()


def novaJanela6(arbitros):
    resultado = Toplevel(root)
    resultado.title("Resultado")
    resultado.geometry('300x150')
    resultado.minsize(450, 300)

    if (arbitros != []):
        i = 0
        for arbitro in arbitros:
            var = StringVar()
            var.set(arbitro[0])
            Label(resultado, textvariable=var, font=("Courier", 10)).place(y=i * 18)
            i = i + 1
    else:
        var = StringVar()
        var.set("Sem dados")
        Label(resultado, textvariable=var).pack()


def tecnicoFromTime():
    time = e1.get()
    if (time == ""):
        MessageBox.showwarning = ("Tecnico do time Status", "Preencha o campo")
    else:
        epl_db = mysql.connect(host="localhost", user="root", password="L95$hq4e@35HYP", database="mydb")
        cursor = epl_db.cursor()
        cursor.execute("select Nome from mydb.tecnico where Time_Nome = '" + time + "'")
        tecnico = cursor.fetchall()
        novaJanela1(time, tecnico)
        epl_db.close()


def jogadoresFromTime():
    time = e2.get()
    if (time == ""):
        MessageBox.showwarning = ("Tecnico do time Status", "Preencha o campo")
    else:
        epl_db = mysql.connect(host="localhost", user="root", password="L95$hq4e@35HYP", database="mydb")
        cursor = epl_db.cursor()
        cursor.execute("select Nome from mydb.jogador where Time_Nome = '" + time + "'")
        jogadores = cursor.fetchall()
        novaJanela2(time, jogadores)
        epl_db.close()


def partidasFromTime():
    time = e3.get()
    if (time == ""):
        MessageBox.showwarning = ("Tecnico do time Status", "Preencha o campo")
    else:
        epl_db = mysql.connect(host="localhost", user="root", password="L95$hq4e@35HYP", database="mydb")
        cursor = epl_db.cursor()
        cursor.execute(
            "select TimeCasa, GolsCasa, TimeVisitante, GolsVisitante from mydb.partida where TimeCasa = '" + time + "' or TimeVisitante = '" + time + "'")
        partidas = cursor.fetchall()
        novaJanela3(time, partidas)
        epl_db.close()


def partidasFromArbitro():
    arbitro = e4.get()
    if (arbitro == ""):
        MessageBox.showwarning = ("Tecnico do time Status", "Preencha o campo")
    else:
        epl_db = mysql.connect(host="localhost", user="root", password="L95$hq4e@35HYP", database="mydb")
        cursor = epl_db.cursor()
        cursor.execute("select idÁrbitro, Nome from mydb.arbitro where Nome = '" + arbitro + "'")
        arbitro_nome = cursor.fetchall()
        arbitro_nome = str(arbitro_nome[0][1])
        cursor.execute(
            "select TimeCasa, GolsCasa, TimeVisitante, GolsVisitante from mydb.partida where Arbitro = '" + arbitro_nome + "'")
        jogos = cursor.fetchall()
        print(jogos)
        novaJanela4(arbitro, jogos)
        epl_db.close()


def semGolFromTime():
    time = e5.get()
    if (time == ""):
        MessageBox.showwarning = ("Tecnico do time Status", "Preencha o campo")
    else:
        epl_db = mysql.connect(host="localhost", user="root", password="L95$hq4e@35HYP", database="mydb")
        cursor = epl_db.cursor()
        print(time)
        cursor.execute(
            "select TimeCasa, GolsCasa, TimeVisitante, GolsVisitante from mydb.partida "
            "where (TimeCasa = '" + time + "' and GolsVisitante = 0) or (TimeVisitante = '" + time + "' and GolsCasa = 0)")
        partidas = cursor.fetchall()
        print(partidas)
        novaJanela5(time, partidas)
        epl_db.close()


def arbitros():
    epl_db = mysql.connect(host="localhost", user="root", password="L95$hq4e@35HYP", database="mydb")
    cursor = epl_db.cursor()
    cursor.execute(
        "select Nome from mydb.arbitro")
    arbitros = cursor.fetchall()
    novaJanela6(arbitros)
    epl_db.close()


def tecnicos():
    epl_db = mysql.connect(host="localhost", user="root", password="L95$hq4e@35HYP", database="mydb")
    cursor = epl_db.cursor()
    cursor.execute(
        "select Nome, Data_Nascimento, Nacionalidade, Time_Nome from mydb.tecnico")
    tecnicos = cursor.fetchall()
    # novaJanela7(tecnicos)
    tecnicos_lst = []
    for tecnico in tecnicos:
        tecnicos_lst.append([tecnico[3], tecnico[0], str(tecnico[1]), tecnico[2]])
    root = Tk()
    t = Table(root, tecnicos_lst)
    epl_db.close()


def times():
    epl_db = mysql.connect(host="localhost", user="root", password="L95$hq4e@35HYP", database="mydb")
    cursor = epl_db.cursor()
    cursor.execute(
        "select Nome, Cidade, Estádio from mydb.time")
    times_lst = list(cursor.fetchall())
    # novaJanela7(tecnicos)
    # times_lst = []
    # for time in times:
    #     times_lst.append([time[0], str(time[1]), time[2]])
    root = Tk()
    t = Table(root, times_lst)
    epl_db.close()


def jogadores():
    epl_db = mysql.connect(host="localhost", user="root", password="L95$hq4e@35HYP", database="mydb")
    cursor = epl_db.cursor()
    cursor.execute(
        "select Nome, Time_Nome, Nacionalidade, Data_Nascimento from mydb.jogador")
    jogadores = cursor.fetchall()
    # novaJanela7(tecnicos)
    jogadores_lst = []
    for jogador in jogadores:
        jogadores_lst.append([jogador[0], str(jogador[1]), jogador[2], jogador[3]])
    root = Tk()
    t = Table(root, jogadores_lst)
    epl_db.close()


def partidasContra():
    timeCasa = e9.get()
    timeVisitante = e9_2.get()
    if timeCasa == "" or timeVisitante == "":
        MessageBox.showwarning = ("Tecnico do time Status", "Preencha o campo")
    else:
        epl_db = mysql.connect(host="localhost", user="root", password="L95$hq4e@35HYP", database="mydb")
        cursor = epl_db.cursor()
        cursor.execute("select TimeCasa, GolsCasa, GolsVisitante, TimeVisitante, Data, Estádio from mydb.partida "
                       "where (TimeCasa = '" + timeCasa + "' AND TimeVisitante = '" + timeVisitante + "') "
                       "OR (TimeCasa = '" + timeVisitante + "' AND TimeVisitante = '" + timeCasa + "')")
        partidas_lst = list(cursor.fetchall())
        root = Tk()
        t = Table(root, partidas_lst)
        epl_db.close()



root = Tk()
root.title("English Premier League Database")
root.geometry('1300x500')
root.minsize(640, 300)
titulo = Label(root, text="English Premier League database", font=("Courier bold", 25), height=0).pack()
subtitulo = Label(root, text="Escolha uma das opções abaixo e faça a sua pesquisa!", font=("Courier", 15),
                     height=0).pack()

e_Label1 = Label(root, text="Digite o time:", font=("Courier", 15)).place(anchor=NW, rely=0.2, relx=0.005)
e1 = Entry()
e1.place(anchor=NW, rely=0.25, relx=0.005)
b1 = Button(root, text="Descubra o técnico", font=("Courier bold", 10), command=tecnicoFromTime).place(anchor=NW,
                                                                                                          rely=0.29,
                                                                                                          relx=0.005)

e_Label2 = Label(root, text="Digite o time:", font=("Courier", 15)).place(anchor=NW, rely=0.2, relx=0.2)
e2 = Entry()
e2.place(anchor=NW, rely=0.25, relx=0.205)
b2 = Button(root, text="Descubra os jogadores", font=("Courier bold", 10), command=jogadoresFromTime).place(
    anchor=NW, rely=0.29, relx=0.205)

e_Label3 = Label(root, text="Digite o time:", font=("Courier", 15)).place(anchor=NW, rely=0.2, relx=0.37)
e3 = Entry()
e3.place(anchor=NW, rely=0.25, relx=0.375)
b3 = Button(root, text="Descubra os jogos", font=("Courier bold", 10), command=partidasFromTime).place(anchor=NW,
                                                                                                          rely=0.29,
                                                                                                          relx=0.375)

e_Label4 = Label(root, text="Digite o árbitro:", font=("Courier", 15)).place(anchor=NW, rely=0.2, relx=0.55)
e4 = Entry()
e4.place(anchor=NW, rely=0.25, relx=0.55)
b4 = Button(root, text="Descubra os jogos apitados", font=("Courier bold", 10), command=partidasFromArbitro).place(
    anchor=NW, rely=0.29, relx=0.55)

e_Label5 = Label(root, text="Digite o time:", font=("Courier", 15)).place(anchor=NW, rely=0.2, relx=0.78)
e5 = Entry()
e5.place(anchor=NW, rely=0.25, relx=0.78)
b5 = Button(root, text="Descubra os jogos que o time não sofreu gol", font=("Courier bold", 10),
               command=semGolFromTime).place(anchor=NW, rely=0.29, relx=0.78)

b6 = Button(root, text="Listar os árbitros", font=("Courier bold", 10),
               command=arbitros).place(anchor=NW, rely=0.59, relx=0.005)

b7 = Button(root, text="Listar os técnicos", font=("Courier bold", 10),
               command=tecnicos).place(anchor=NW, rely=0.59, relx=0.2)

b8 = Button(root, text="Listar os times", font=("Courier bold", 10),
               command=times).place(anchor=NW, rely=0.59, relx=0.37)

e_Label9 = Label(root, text="Digite os times:", font=("Courier", 15)).place(anchor=NW, rely=0.45, relx=0.55)
e9 = Entry()
e9.place(anchor=NW, rely=0.50, relx=0.55)
e9_2 = Entry()
e9_2.place(anchor=NW, rely=0.55, relx=0.55)
b9 = Button(root, text="Listar jogos entre os times", font=("Courier bold", 10), command=partidasContra).place(
    anchor=NW, rely=0.59, relx=0.55)


root.mainloop()
