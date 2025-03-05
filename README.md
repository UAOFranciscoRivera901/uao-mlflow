# Monitoreo de proyectos ML-IA

Este repositorio presenta el monitoreo de un modelo de red neuronal diseñado para la clasificación de URLs con el objetivo de detectar phishing. Para el entrenamiento, se utilizó el conjunto de datos "pirocheto/phishing-url" disponible en Hugging Face.

Además, el proceso de experimentación y gestión del modelo se llevó a cabo utilizando plataformas especializadas en seguimiento y optimización de modelos de machine learning las cuales son:

- MLflow
-	Comet ML

El repositorio incluye diversos scripts para cada una de las funciones de las plataformas utilizadas. También se detallan los requisitos necesarios para su funcionamiento óptimo, las instrucciones de instalación y la licencia correspondiente.

# Tabla de contenido
- [Introducción](#introducción)
 - [Pishing](#Pishing)
  
 
# Introducción
## Pishing

El phishing es un tipo de ciberataque basado en ingeniería social, en el cual los atacantes utilizan correos electrónicos, mensajes de texto o sitios web fraudulentos para engañar a las personas y robar información confidencial, como contraseñas, datos bancarios o credenciales de acceso.
Para prevenir estos ataques, es posible aplicar análisis de URLs y patrones de comportamiento mediante técnicas de inteligencia artificial y aprendizaje automático. Estas estrategias permiten detectar actividades sospechosas y bloquear posibles amenazas antes de que los usuarios sean víctimas del fraude.

## Dataset 

el dataset utilizado....

## Modelo clasificación de URLs

El modelo de clasificación elegido fue una red neuronal multicapa (MLP) debido a su capacidad para aprender patrones complejos y generalizar el conocimiento en datos de alta dimensión. Su adaptabilidad le permite ajustarse a cambios en la información, mejorando su rendimiento frente a nuevas amenazas de phishing. Además, su habilidad para manejar grandes volúmenes de datos contribuye a reducir el número de falsas detecciones, asegurando un sistema robusto y eficiente en la identificación de URLs maliciosas.

la estructura de la red es la siguiente
![imagen 1](imagenes/estructura_red.PNG)

los parametros utilizados son:

- Neuronas:64
- Activación: Relu
- Optimizer: RMSprop
- Epochs: 10
- Batch size: 32

# Estructura del repositorio

En este repositorio, los archivos han sido organizados de manera estructurada para diferenciar claramente las implementaciones destinadas a las plataformas Comet-ML y MLflow. Esta división permite una mejor gestión del monitoreo y experimentación del modelo, facilitando la integración con cada plataforma según sus características y funcionalidades específicas.

A nivel general, la estructura del proyecto es la siguiente:

1. Directorios principales:

- Images/ Contiene las imágenes utilizadas en el proyecto.

2. Comlet

