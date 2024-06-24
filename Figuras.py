try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
except ImportError:
    import pip
    pip.main(['install', 'atplotlib'])
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

# Configuración del gráfico
fig, ax = plt.subplots()

# Cuadrado
square = patches.Rectangle((0.1, 0.1), 0.5, 0.5, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(square)

# Rectángulo
rect = patches.Rectangle((0.7, 0.1), 0.8, 0.3, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(rect)

# Triángulo
triangle = patches.Polygon([[0.2, 0.6], [0.4, 0.8], [0.6, 0.6]], linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(triangle)

# Rombo
rhombus = patches.Polygon([[0.3, 0.4], [0.5, 0.6], [0.7, 0.4], [0.5, 0.2]], linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(rhombus)

# Configuración del eje
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Mostrar el gráfico
plt.show()