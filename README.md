# Diseño de redes de transporte con métodos de clusterización y algoritmo Kruskal

![cluster kruskal](https://github.com/jhontd03/TransportNetworks/blob/master/img/cluster_kruskal.png "cluster_kruskal")

## [Contenido](#Contenido)

- [Introducción](#Introduccón)
- [Instalación](#Instalación)
- [Requisitos](#Requisitos)
- [Uso](#Uso)
- [Estructura del repositorio](#Estructura-del-repositorio)
- [Resultados](#Resultados)
- [Autor](#Autor)

## Introducción

Este proyecto se enfoca en el diseño de una red de transporte urbano en Nueva York, utilizando un conjunto de datos representativo de la demanda de Uber en la ciudad. El objetivo es complementar la red de transporte existente, no reemplazarla, aprovechando herramientas basadas en aprendizaje automático.

Utilizando métodos de clusterización, se identificaron entre 100 y 200 ubicaciones con alta demanda de transporte para establecer paradas potenciales. Los métodos de clusterización aplicados incluyen k-means y algoritmos jerárquicos, evaluando su efectividad en la creación de agrupaciones uniformes y bien definidas. La elección del método se basa en la capacidad de formar grupos claramente separados y uniformes, siendo k-means el seleccionado por su rendimiento en este contexto.

Posteriormente, se aplica el algoritmo de Kruskal, un enfoque de árbol de expansión mínima, para determinar las conexiones óptimas entre las paradas, minimizando la longitud total de la red mientras se cubre la mayor demanda posible. Este paso es crucial para garantizar que la inversión en la nueva tecnología de transporte sea rentable, dado su alto costo.

El análisis incluye una evaluación detallada de la densidad de cada grupo y la preparación de los datos para la aplicación del algoritmo de Kruskal. Se visualizan los resultados, mostrando la importancia de cada conexión en la red propuesta y su impacto en la cobertura de la demanda de transporte.

## Instalación

## Requisitos

Para la ejecución del programa es necesario instalar la version de python 3.9.16, vscode y los paquetes del archivo sinfo-requirements.txt

Instale [python](https://www.python.org/downloads/) y [vscode](https://code.visualstudio.com/download)

## Uso

Clone el presente repositorio cree un entorno virtual, instale las librerias y ejecute el notebook con vscode.

```
conda create -n TestEnv python=3.9.16 
activate TestEnv
python -m pip install --upgrade pip
pip install -r  sinfo-requirements.txt
git clone https://github.com/jhontd03/RedesTransporte.git
```

## Estructura del repositorio

El árbol de directorios del repositorio es el siguiente:
```
.
│   kruskal.py
│   LICENSE
│   notebook.ipynb
│   README.md
│   sinfo-requirements.txt
│   utils.py
│
├───.vscode
│       settings.json
│
├───data
│       uber-raw-data-aug14.csv
│       uber_sample.csv
│
├───img
│       cluster_kruskal.png
│
└───__pycache__
        kruskal.cpython-39.pyc
        utils.cpython-39.pyc
```

## Conclusiones

Este proyecto fue una gran oportunidad para combinar mis habilidades en data science con mi interés en mejorar la movilidad urbana. Utilizando el conjunto de datos de Uber en Nueva York, he diseñado una red de transporte básica que busca optimizar el servicio en áreas de alta demanda.

Principales Aprendizajes:

- Eficiencia del k-means: El método k-means resultó ser la herramienta más efectiva para identificar áreas clave para nuevas paradas de transporte. Este método fue directo y produjo clusters claros y manejables, facilitando la siguiente fase de diseño de la red.

- Implementación del algoritmo de Kruskal: Aplicar Kruskal para conectar estas nuevas paradas fue una decisión técnica clave que ayudó a minimizar los costos y maximizar la eficiencia de la red propuesta. Fue satisfactorio ver cómo una técnica teórica se traduce en aplicaciones prácticas que podrían, en teoría, implementarse en la vida real.

Desafíos Encarados:

- Determinar el número óptimo de clusters y manejar outliers fueron desafíos constantes. Ajustar estos parámetros requirió un equilibrio entre precisión técnica y practicidad.

- El costo de implementación y la logística de introducir nuevas tecnologías en sistemas establecidos siempre estuvo en mente, lo que añadió una capa de complejidad al enfoque del proyecto.

Trabajos Futuros:

Para futuras versiones de este proyecto, me gustaría integrar datos en tiempo real para adaptar la red a las condiciones dinámicas de la ciudad. También, probar la red en un entorno simulado podría ofrecer insights adicionales sobre su viabilidad y eficiencia.

## Autor

Jhon Jairo Realpe

jhon.td.03@gmail.com
