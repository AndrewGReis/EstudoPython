def linha_horizontal():
    print('+', '- ' * 4 + '+', '- ' * 4 + '+', '- ' * 4 + '+', '- ' * 4 + '+')

def linha_vertical():
    print('|', ' ' * 8 + '|', ' ' * 8 + '|', ' ' * 8 + '|', ' ' * 8 + '|')

def desenhar_grade_4x4():
    linha_horizontal()
    for i in range(4):
        linha_vertical()
    
    linha_horizontal()
    for i in range(4):
        linha_vertical()
    
    linha_horizontal()

desenhar_grade_4x4()