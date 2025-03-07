import sys
import os

# Añadir src/ml_flow al path de Python
sys.path.append(os.path.abspath("src/ml_flow"))

from ml_flow_train import main

print("El script se está ejecutando correctamente")

if __name__ == "__main__":
    main()