import time

timestamp = time.time()
print(f"Timestamp atual: {timestamp}")

dias_total = timestamp // (24 * 60 * 60)
segundos_restantes = timestamp % (24 * 60 * 60)

horas = segundos_restantes // (60 * 60)
segundos_restantes %= 60 * 60

minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(f"\nTempo desde a época (1º de janeiro de 1970):")
print(f"- Dias: {int(dias_total)}")
print(f"- Horas: {int(horas)}")
print(f"- Minutos: {int(minutos)}")
print(f"- Segundos: {int(segundos)}")