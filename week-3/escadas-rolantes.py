n_people_detected = int(input()) # número de pessoas detectadas pelo sensor
instants_detected = []

for _ in range(n_people_detected):
    instants_detected.append(int(input())) # lista com os instantes de cada pessoa que foi detectada pelo sensor

time_on = 0

for i in range(n_people_detected - 1): # menos um já que o último instante não pode ser comparada a um instante posterior (inexistente)
    interval = instants_detected[i + 1] - instants_detected[i]
    if interval < 10: time_on += interval
    else: time_on += 10
time_on += 10 # adiciona-se o tempo que a escada ficou ligada para a última pessoa que foi detectada

print(time_on)
