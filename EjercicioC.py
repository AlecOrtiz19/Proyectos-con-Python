import numpy as np
from scipy.interpolate import CubicSpline

x_datos = np.array([2, 3, 4, 5]) 
y_datos = np.array([4, 6, 10, 14])

"""
c) Utilice el método de interpolación por trazadores o Spline CÚBICOS para encontrar el polinomio y estimar 𝑥 = 2.5, 𝑥 = 4. 
Realizar este ejercicio solo con el código de programación. Además, calcule el error relativo porcentual con base en el valor verdadero. 


"""

spline_cubico = CubicSpline(x_datos, y_datos)

valores_estimados = [2.5, 4]

resultados_estimados = spline_cubico(valores_estimados)

for valor, resultado in zip(valores_estimados, resultados_estimados):
    print(f"Estimación para x = {valor}: {resultado}")

valores_verdaderos = [5, 8]

errores_relativos = [abs((verdadero - estimado) / verdadero) * 100 for verdadero, estimado in zip(valores_verdaderos, resultados_estimados)]

for valor, error in zip(valores_estimados, errores_relativos):
    print(f"Error relativo para x = {valor}: {error}%")
