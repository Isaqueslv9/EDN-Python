print("=-= CALCULADORA =-=")

while True:
    try:
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
    
        operacao = input("Digite a operação (+, -, *, /): ")
        
        
        if operacao not in ['+', '-', '*', '/']:
            print("ERRO: Operação inválida! Use +, -, * ou /")
            print()
            continue
        
      
        if operacao == '/' and num2 == 0:
            print("ERRO: Divisão por zero não é permitida!")
            print()
            continue
        
        
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        else:  
            resultado = num1 / num2

       
        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
        break
        
    except ValueError:
        print("ERRO: Entrada inválida! Por favor, digite números válidos.")
        print()
    except Exception as e:
        print(f"ERRO inesperado: {e}")
        print()