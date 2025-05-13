n = int(input())
m = int(input())
Mndistancia = m - n
Nmdistancia = n - m
if n > m:
    if Nmdistancia < 50:
        print(f"{Nmdistancia} veces arriba")
    if Nmdistancia > 50:
        Final_distancia = (100 - n) + m
        print(f"{Final_distancia} veces abajo")
if n < m:
    if Mndistancia < 50:
        print(f"{Mndistancia} veces abajo")
    if Mndistancia > 50:
        Final_distancia = (100 - m) + n
        print(f"{Final_distancia} veces arriba")