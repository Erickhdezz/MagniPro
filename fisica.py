from Tkinter import *
import tkMessageBox

def conversion():
    resul = DoubleVar()
    #De METROS a:
    numero = numero1.get()
    #Millas Terrestres
    if medida.get() == 1:
        resul =(numero*0.000621371)
        resul1=(" %f Millas") %resul
        tkMessageBox.showinfo("Resultado: ",resul1)

    #Pulgadas
    elif medida.get() == 2:
        resul = (numero*39.37)
        resul1= ("%f Pulgadas") %resul
        tkMessageBox.showinfo("Resultado: ",resul1)


    #Millas Nauticas
    elif medida.get() == 3:
        resul = (numero * 0.000539957)
        resul1= ("%f Millas Nauticas") %resul
        tkMessageBox.showinfo("Resultado: ",resul1)

    #Pies
    elif medida.get() == 4:
        resul = numero * 3.28084
        resul1= ("%f Pies") %resul
        tkMessageBox.showinfo("Resultado: ",resul1)

    #Yardas
    elif medida.get() == 5:
        resul = (numero * 1.09361)
        resul1= ("%f Yardas") %resul
        tkMessageBox.showinfo("Resultado: ",resul1)




window1 = Tk()
numero1 = DoubleVar()
medida = DoubleVar()
window1.title("MagniPro Converter")
window1.geometry("500x480")


inst = Label(window1,text="Escribe la medida que deseas convertir").place(x=10,y=20)
inst1 = Label(window1,text="Escribe una cantidad en metros").place(x=10,y=50)
enum = Entry(window1,textvariable=numero1,text="Valores en metros y litros").place(x=220,y=50)
convertira= Label(window1, text="Convertir a:").place(x=10,y=70)




m_milla= Radiobutton(window1, text="Millas", value=1, variable=medida ).place(x=20,y=100)
m_pulgadas= Radiobutton(window1, text="Pulgadas", value=2, variable=medida, ).place(x=20,y=120)
m_milla_n= Radiobutton(window1, text="Millas Nauticas", value=3, variable=medida).place(x=20,y=140)
m_pies= Radiobutton(window1,text="Pies", value=4,variable=medida).place(x=20,y=160)
m_yarda= Radiobutton(window1,text="Yardas", value=5, variable=medida ).place(x=20,y=180)

realizar = Button(window1, text="Realizar Conversion", command=conversion, background="CadetBlue").place(x=30,y=380)


window1.mainloop()
