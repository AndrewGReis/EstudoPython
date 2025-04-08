hora_partida = 6 * 3600 + 52 * 60  # Convertidoconvertendo para segundos (6:52)


passo_lento = 8 * 60 + 15  # 8m 15s
passo_rapido = 7 * 60 + 12  # 7m 12s

tempo_total = (1 * passo_lento) + (3 * passo_rapido) + (1 * passo_lento)
hora_chegada_segundos = hora_partida + tempo_total

horas = hora_chegada_segundos // 3600
minutos = (hora_chegada_segundos % 3600) // 60
segundos = hora_chegada_segundos % 60

print(f"Horário de chegada: {int(horas)}:{int(minutos)}:{int(segundos)}")