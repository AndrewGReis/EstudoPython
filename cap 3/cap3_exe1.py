def right_justify(s):
    espacos_necessarios = 70 - len(s)  # len vai calcular quantos espaços faltam para chegar à coluna 70
    string_justificada = ' ' * espacos_necessarios + s  
    print(string_justificada)  

right_justify('python')