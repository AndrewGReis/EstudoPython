# Dados
distancia_km = 10
tempo_minutos = 42
tempo_segundos = 42

# Converter distância para milhas
milhas = distancia_km / 1.61

# Converter tempo total para segundos
tempo_total_segundos = (tempo_minutos * 60) + tempo_segundos

#  Calcular passo médio (tempo por milha) 
# // para pegar apenas números inteiros, se não a conta daria 6.870666... minutos
# % para ficar mais ituitivo e fazer menos contas, já pegando apenas o resto da conta, auxilia com calculos de tempo
segundos_por_milha = tempo_total_segundos / milhas
minutos_passo = int(segundos_por_milha // 60)
segundos_passo = int(segundos_por_milha % 60)

#  Calcular velocidade média (mph)
tempo_total_horas = tempo_total_segundos / 3600
velocidade_media = milhas / tempo_total_horas

# Resultados
print(f"Passo médio: {minutos_passo} minutos e {segundos_passo} segundos por milha")
print(f"Velocidade média: {velocidade_media:.2f} milhas por hora (mph)")