import numpy as np
from scipy.interpolate import interp1d

"""

B Utilice el método de interpolación por trazadores o Spline LINEALES para encontrar el polinomio y estimar 𝑥 = 2.5, 𝑥 = 4 
Realizar este ejercicio manualmente y con el código de programación. Además, 
calcule el error relativo porcentual con base en el valor verdadero. 


"""

x_datos = np.array([2, 3, 5, 7])  
y_datos = np.array([4, 6, 10, 14])  

interp_lineal = interp1d(x_datos, y_datos, kind='linear')

valores_estimados = [2.5, 4]

resultados_estimados = interp_lineal(valores_estimados)

for valor, resultado in zip(valores_estimados, resultados_estimados):
    print(f"Estimación para x = {valor}: {resultado}")

valores_verdaderos = [5, 8]

errores_relativos = [abs((verdadero - estimado) / verdadero) * 100 for verdadero, estimado in zip(valores_verdaderos, resultados_estimados)]

for valor, error in zip(valores_estimados, errores_relativos):
    print(f"Error relativo para x = {valor}: {error}%")
