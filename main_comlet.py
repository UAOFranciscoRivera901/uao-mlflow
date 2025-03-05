import sys
import os

# Añadir comlet/src al path de Python
sys.path.append(os.path.abspath("comlet/src"))

from train import entrenar_modelo

print("El script se está ejecutando correctamente")

if __name__ == "__main__":
    entrenar_modelo()
