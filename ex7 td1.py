import numpy as np
import matplotlib.pyplot as plt

x = np.array([39, 42, 43, 45, 45, 47, 47, 49])  # Gaz à effet de serre (tT)
y = np.array([0.67, 0.69, 0.72, 0.74, 0.77, 0.80, 0.82, 0.85])  # Température (°C)

# 2. Question 2 : Moyennes et Variances
mean_x = np.mean(x)
mean_y = np.mean(y)

var_x = np.var(x)  # variance empirique
var_y = np.var(y)

print(f"Moyenne de X (Gaz) : {mean_x:.3f} tT")
print(f"Moyenne de Y (Température) : {mean_y:.4f} °C")
print(f"Variance de X : {var_x:.3f}")
print(f"Variance de Y : {var_y:.6f}")

# 3. Question 3 : Calcul des coefficients beta_1 et beta_0
# Covariance entre X et Y
cov_xy = np.cov(x, y, ddof=0)[0, 1]

# Pente (beta_1) = Cov(X,Y) / Var(X)
beta_1 = cov_xy / var_x

# Ordonnée à l'origine (beta_0) = Y_barre - beta_1 * X_barre
beta_0 = mean_y - beta_1 * mean_x

print(f"\nbeta_1 (pente) = {beta_1:.6f}")
print(f"beta_0 (ordonnée à l'origine) = {beta_0:.6f}")
print(f"Équation : y = {beta_1:.4f} * x + ({beta_0:.4f})")