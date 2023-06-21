import tkinter as tk

#realizar a operação de acordo com o botão pressionado
def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operacao = entry_operacao.get()

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
    else:
        resultado = "Operação inválida"

    label_resultado["text"] = f"Resultado: {resultado}"

#janela principal
window = tk.Tk()
window.title("Calculadora")

#interface
label_num1 = tk.Label(window, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

label_operacao = tk.Label(window, text="Operação (+, -, *, /):")
label_operacao.pack()

entry_operacao = tk.Entry(window)
entry_operacao.pack()

button_calcular = tk.Button(window, text="Calcular", command=calcular)
button_calcular.pack()

label_resultado = tk.Label(window, text="Resultado:")
label_resultado.pack()

#iniciar o loop da janela
window.mainloop()

#declaração de variáveis
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
resultadoSoma = (num1 + num2)
resultadoSubtracao = (num1 - num2)
resultadoMultiplicacao = (num1 * num2)
resultadoDivisao = (num1/num2)
operacao = '+, -, /, *'

#inicio
operacao = input("Escolha uma operação: ")

if operacao == '+':
    print(resultadoSoma)
elif operacao == '-':
    print(resultadoSubtracao)
elif operacao == '/':
    print (resultadoDivisao)
elif operacao == '*':
    print (resultadoMultiplicacao)   
else:
    print ("Operação Inválida!")        