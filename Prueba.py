
print ("Prueba de ejercicio (Prueba de Hipótesis)")
import scipy.stats as stats

# Datos
mu = 73.2
sigma = 8.6
n = 45
x_bar = 76.7

# Cálculo del estadístico z
z = (x_bar - mu) / (sigma / (n ** 0.5))

# Cálculo del valor p (prueba unilateral, lado derecho)
p_value = 1 - stats.norm.cdf(z)

# Resultados
print(f"Estadístico z: {z:.4f}")
print(f"Valor p: {p_value:.4f}")

# Para prueba bilateral:
p_value_bilateral = 2 * (1 - stats.norm.cdf(abs(z)))
print(f"Valor p (bilateral): {p_value_bilateral:.4f}")