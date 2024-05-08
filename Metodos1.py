import numpy as np
import matplotlib.pyplot as plt

# Datos conocidos (puntos x, y)
x_datos = np.array([3, 4, 5])  # Suponiendo que tienes puntos en x
y_datos = np.array([1, 3, 8])  # Suponiendo que tienes puntos en y

# Implementación del algoritmo de interpolación de Newton
def interpolacion_newton(x, y):
    n = len(x)
    coeficientes = np.zeros(n)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            y[i] = (y[i] - y[i-1]) / (x[i] - x[i-j])
    coeficientes = y
    return coeficientes

# Coeficientes del polinomio de interpolación
coeficientes = interpolacion_newton(x_datos, y_datos)

# Función del polinomio de interpolación de Newton de segundo grado
def polinomio_interpolacion(coeficientes, x):
    n = len(coeficientes)
    resultado = coeficientes[0]
    for i in range(1, n):
        producto = coeficientes[i]
        for j in range(i):
            producto *= (x - x_datos[j])
        resultado += producto
    return resultado

# Puntos para la estimación
x_estimado = 3.3
y_estimado = polinomio_interpolacion(coeficientes, x_estimado)

# Imprimir el resultado estimado
print("Estimación para x = 3.3:", y_estimado)

# Cálculo del error relativo
valor_real = 2.05  # Valor real (hipotético) para x = 3.3
error_relativo = abs((y_estimado - valor_real) / valor_real) * 100
print("Error relativo:", error_relativo, "%")

# Graficar el polinomio de interpolación y los puntos de datos
x_valores = np.linspace(min(x_datos), max(x_datos), 100)
y_valores = polinomio_interpolacion(coeficientes, x_valores)

plt.plot(x_valores, y_valores, label='Polinomio de interpolación')
plt.scatter(x_datos, y_datos, color='red', label='Datos conocidos')
plt.scatter(x_estimado, y_estimado, color='green', label=f'Estimación para x={x_estimado}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de Newton de segundo grado')
plt.legend()
plt.grid(True)
plt.show()
