# Monitoreo de proyectos ML-IA

Este repositorio presenta el monitoreo de un modelo de red neuronal diseñado para la clasificación de URLs con el objetivo de detectar phishing. Para el entrenamiento, se utilizó el conjunto de datos "pirocheto/phishing-url" disponible en Hugging Face.

Además, el proceso de experimentación y gestión del modelo se llevó a cabo utilizando plataformas especializadas en seguimiento y optimización de modelos de machine learning las cuales son:

- MLflow
-	Comet ML

El repositorio incluye diversos scripts para cada una de las funciones de las plataformas utilizadas. También se detallan los requisitos necesarios para su funcionamiento óptimo, las instrucciones de instalación y la licencia correspondiente.

# Tabla de contenido
- [Introducción](#introducción)
 - [Phishing](#Phishing)
 - [Dataset](#Dataset)
- [Estructura del repositorio](#Estructura-del-repositorio)
- [Archivos del repositorio](#archivos-del-repositorio)
    - [comet/comet_logger.py](#comet/comet_logger-py)
    - [comet/train.py](#comet/train-py) 
    - [ml_flow/callbacks.py](#ml_flow/callbacks-py)  
    - [ml_flow/evaluate.py](#ml_flow/evaluate-py)
    - [config.py](#config-py)
    - [data.py](#data-py)
    - [model.py](#model-py) 
  
# Introducción
## Phishing

El phishing es un tipo de ciberataque basado en ingeniería social, en el cual los atacantes utilizan correos electrónicos, mensajes de texto o sitios web fraudulentos para engañar a las personas y robar información confidencial, como contraseñas, datos bancarios o credenciales de acceso.
Para prevenir estos ataques, es posible aplicar análisis de URLs y patrones de comportamiento mediante técnicas de inteligencia artificial y aprendizaje automático. Estas estrategias permiten detectar actividades sospechosas y bloquear posibles amenazas antes de que los usuarios sean víctimas del fraude.

## Dataset 

El dataset Phishing URL (https://huggingface.co/datasets/pirocheto/phishing-url) consta de un total de 11430 registros, donde cada registro tiene 89 columnas y la última de ellas es la variable objetivo llamada "status" con dos posibles valores que son: legitimate y/o phishing. Con este dataset es posible entrenar un modelo de Machine Learning con el fin de determinar si una página es phising o es legítima.

Las columnas o características del dataset corresponden a tres clases diferentes que son:

- 56 características son extraídas de la estructura y sintaxis de las URL.
- 24 características son extraídas del contenido de sus páginas correspondientes.
- 7 características son extraídas consultando servicios externos.

Es importante aclarar que la característica URL no se tendrá en cuenta en el estudio porque se han extraído 56 características a partir de la estructura y sintaxis de las URL tales como longitud, número de subdominios, uso de caracteres sospechosos, entonces no sería necesario la URL completa en el dataset, ayudando a evitar que el modelo dependa de información irrelevante o difícil de procesar directamente.

El dataset proporcionado por Hugging Face ya tiene dividido los datos de tal manera que las dos terceras partes de los datos, que equivale a 7658 registros son datos de entrenamiento. El otro tercerio de datos que equivale a 3772 registros son datos de prueba.

Hablando del tipo de datos de las características se observa que la mayoría de los datos son numéricos, a excepción de las características URL y de la variable objetivo status que contiene dos posibles valores que son: legitimate y/o phishing. Además, el dataset está completo ya que no presenta valores vacíos o nulos.

Por último y no menos importante, se indica que el dataset está balanceado ya que contiene el 50% de los datos pertenecientes al estado legítimo y la otra mitad de los datos corresponden a phising.

## Modelo clasificación de URLs

El modelo de clasificación elegido fue una red neuronal multicapa (MLP) debido a su capacidad para aprender patrones complejos y generalizar el conocimiento en datos de alta dimensión. Su adaptabilidad le permite ajustarse a cambios en la información, mejorando su rendimiento frente a nuevas amenazas de phishing. Además, su habilidad para manejar grandes volúmenes de datos contribuye a reducir el número de falsas detecciones, asegurando un sistema robusto y eficiente en la identificación de URLs maliciosas.

La estructura de la red es la siguiente

![imagen 1](imagenes/estructura_red.PNG)

Los parametros utilizados son:

- Neuronas: 64
- Activación: Relu
- Optimizer: RMSprop
- Epochs: 10
- Batch size: 32

# Estructura del repositorio

En este repositorio, los archivos han sido organizados de manera estructurada para diferenciar claramente las implementaciones destinadas a las plataformas Comet-ML y MLflow. Esta división permite una mejor gestión del monitoreo y experimentación del modelo, facilitando la integración con cada plataforma según sus características y funcionalidades específicas.

A nivel general, la estructura del proyecto es la siguiente:

1. Directorios principales:

- imagenes/ Contiene las imágenes utilizadas en el proyecto.
- src (source)/ Contiene el código fuente del proyecto, organizado en los siguientes subdirectorios:
    - comet/ Almacena toda la lógica relacionada con la plataforma Comet-ML.
    - ml_flow/ Almacena toda la lógica relacionada con la plataforma MLflow.
    - Scripts .py que contienen funcionalidad generica para ambas plataformas.

2. Archivos en la raíz del proyecto:
- gitignore: Define los archivos y carpetas que deben ser ignorados en el control de versiones con Git.
- main_comet.py: Archivo principal que sirve como punto de entrada para ejecutar Comet-ML.
- main_ml_flow.py: Archivo principal que sirve como punto de entrada para ejecutar MLflow.
- README.md: Documento con información detallada sobre el uso y configuración del proyecto.
- requirements.txt: Lista de dependencias de Python necesarias para la ejecución del proyecto.
- LICENSE.txt: Contiene la licencia del proyecto, especificando los términos de uso y distribución del código.

# Archivos del repositorio

## comet/comet_logger.py

Este script maneja la configuración inicial de Comet-ML para iniciar el experimento que requiere datos como api_key, project_name y workspace.

## comet/train.py

Este script contiene toda la parametrización necesaria y requerida por Comet-ML para poder iniciar con el experimento, estableciendo las métricas que se harán seguimiento, carga de datos, carga del modelo y Callbacks para realizar los cálculos de las métricas durante el entrenamiento del modelo a través del tiempo y poder realizar las gráficas.

## ml_flow/callbacks.py

Este script establece las métricas como accuracy y precisión que se harán seguimiento en MLflow después de cada época.

## ml_flow/evaluate.py

Este script contiene funciones para evaluar el modelo, calcular las métricas y generar la matriz de confusión.

## config.py

Este script aloja las credenciales para acceder a Comet-ML, además de tener los parámetros de la Red Neuronal Artificial tales como cantidad de neuronas, función de activación, optimizador, etc. Centralizar la configuración en este archivo facilita la modificación y mantenimiento del sistema sin afectar otros módulos.

## data.py

Este script contiene la función para cargar los datos desde Hugging Face, de tal manera que separa los datos de entrenamiento y de prueba. Al tener este archivo con una única responsabilidad, cuando sea necesario cambiar la fuente de datos, solo se necesitaría modificar este archivo.

## model.py

Este script contiene la función para crear el modelo, en este caso una Red Neuronal Artificial con dos capas ocultas. Al separar esta funcionalidad, se garantiza un mejor desacoplamiento del sistema, permitiendo reutilizar el modelo en diferentes partes de la aplicación.

# Integrantes del proyecto

- Francisco Javier Rivera Rozo
- Carlos Armando Daza Rendón
- Andrés Felipe Coral
- Alejandro Sánchez Murillo
