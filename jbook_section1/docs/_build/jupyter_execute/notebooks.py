#!/usr/bin/env python
# coding: utf-8

# <h1>Tabla de contenido<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introducción-a-la-visualización-de-datos-con-Python" data-toc-modified-id="Introducción-a-la-visualización-de-datos-con-Python-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introducción a la visualización de datos con Python</a></span><ul class="toc-item"><li><span><a href="#Manejo-de-datos-con-pandas-DataFrame" data-toc-modified-id="Manejo-de-datos-con-pandas-DataFrame-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Manejo de datos con pandas DataFrame</a></span><ul class="toc-item"><li><span><a href="#Ejercicio-1:-Lectura-de-datos-desde-archivos" data-toc-modified-id="Ejercicio-1:-Lectura-de-datos-desde-archivos-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Ejercicio 1: Lectura de datos desde archivos</a></span></li><li><span><a href="#Ejercicio-2:-Observación-y-descripción-de-datos" data-toc-modified-id="Ejercicio-2:-Observación-y-descripción-de-datos-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Ejercicio 2: Observación y descripción de datos</a></span></li><li><span><a href="#Ejercicio-3:-Añadir-nuevas-columnas-al-DataFrame" data-toc-modified-id="Ejercicio-3:-Añadir-nuevas-columnas-al-DataFrame-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Ejercicio 3: Añadir nuevas columnas al DataFrame</a></span></li><li><span><a href="#Ejercicio-4:-Aplicación-de-funciones-a-las-columnas-de-DataFrame" data-toc-modified-id="Ejercicio-4:-Aplicación-de-funciones-a-las-columnas-de-DataFrame-1.1.4"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Ejercicio 4: Aplicación de funciones a las columnas de DataFrame</a></span></li><li><span><a href="#Ejercicio-5:-Aplicación-de-funciones-en-varias-columnas" data-toc-modified-id="Ejercicio-5:-Aplicación-de-funciones-en-varias-columnas-1.1.5"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span>Ejercicio 5: Aplicación de funciones en varias columnas</a></span></li><li><span><a href="#Ejercicio-6:-Eliminación-de-columnas-de-un-DataFrame" data-toc-modified-id="Ejercicio-6:-Eliminación-de-columnas-de-un-DataFrame-1.1.6"><span class="toc-item-num">1.1.6&nbsp;&nbsp;</span>Ejercicio 6: Eliminación de columnas de un DataFrame</a></span></li><li><span><a href="#Ejercicio-7:-Escribir-un-DataFrame-en-un-archivo" data-toc-modified-id="Ejercicio-7:-Escribir-un-DataFrame-en-un-archivo-1.1.7"><span class="toc-item-num">1.1.7&nbsp;&nbsp;</span>Ejercicio 7: Escribir un DataFrame en un archivo</a></span></li><li><span><a href="#Exercise-8:-Trazado-y-análisis-de-un-histograma" data-toc-modified-id="Exercise-8:-Trazado-y-análisis-de-un-histograma-1.1.8"><span class="toc-item-num">1.1.8&nbsp;&nbsp;</span>Exercise 8: Trazado y análisis de un histograma</a></span></li><li><span><a href="#Exercise-9:-Creación-de-un-gráfico-de-barras-y-cálculo-de-la-distribución-del-precio-medio" data-toc-modified-id="Exercise-9:-Creación-de-un-gráfico-de-barras-y-cálculo-de-la-distribución-del-precio-medio-1.1.9"><span class="toc-item-num">1.1.9&nbsp;&nbsp;</span>Exercise 9: Creación de un gráfico de barras y cálculo de la distribución del precio medio</a></span></li><li><span><a href="#Exercise-10:-Creación-de-gráficos-de-barras-agrupados-por-una-característica-específica" data-toc-modified-id="Exercise-10:-Creación-de-gráficos-de-barras-agrupados-por-una-característica-específica-1.1.10"><span class="toc-item-num">1.1.10&nbsp;&nbsp;</span>Exercise 10: Creación de gráficos de barras agrupados por una característica específica</a></span></li><li><span><a href="#Exercise-11:-Cómo-ajustar-los-parámetros-de-un-gráfico-de-barras-agrupadas" data-toc-modified-id="Exercise-11:-Cómo-ajustar-los-parámetros-de-un-gráfico-de-barras-agrupadas-1.1.11"><span class="toc-item-num">1.1.11&nbsp;&nbsp;</span>Exercise 11: Cómo ajustar los parámetros de un gráfico de barras agrupadas</a></span></li><li><span><a href="#Exercise-12:-Anotar-un-gráfico-de-barras" data-toc-modified-id="Exercise-12:-Anotar-un-gráfico-de-barras-1.1.12"><span class="toc-item-num">1.1.12&nbsp;&nbsp;</span>Exercise 12: Anotar un gráfico de barras</a></span></li><li><span><a href="#Tarea-1.1" data-toc-modified-id="Tarea-1.1-1.1.13"><span class="toc-item-num">1.1.13&nbsp;&nbsp;</span>Tarea 1.1</a></span></li></ul></li></ul></li><li><span><a href="#Visualización-estática" data-toc-modified-id="Visualización-estática-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Visualización estática</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Ejercicio-13:-Creación-de-un-gráfico-de-dispersión-estático" data-toc-modified-id="Ejercicio-13:-Creación-de-un-gráfico-de-dispersión-estático-2.0.1"><span class="toc-item-num">2.0.1&nbsp;&nbsp;</span>Ejercicio 13: Creación de un gráfico de dispersión estático</a></span></li><li><span><a href="#Ejercicio-14:-Creación-de-un-gráfico-hexagonal-estático-Binning" data-toc-modified-id="Ejercicio-14:-Creación-de-un-gráfico-hexagonal-estático-Binning-2.0.2"><span class="toc-item-num">2.0.2&nbsp;&nbsp;</span>Ejercicio 14: Creación de un gráfico hexagonal estático Binning</a></span></li><li><span><a href="#Ejercicio-15:-Creación-de-un-gráfico-de-contorno-estático" data-toc-modified-id="Ejercicio-15:-Creación-de-un-gráfico-de-contorno-estático-2.0.3"><span class="toc-item-num">2.0.3&nbsp;&nbsp;</span>Ejercicio 15: Creación de un gráfico de contorno estático</a></span></li><li><span><a href="#Ejercicio-16:-Creación-de-un-gráfico-de-líneas-estáticas" data-toc-modified-id="Ejercicio-16:-Creación-de-un-gráfico-de-líneas-estáticas-2.0.4"><span class="toc-item-num">2.0.4&nbsp;&nbsp;</span>Ejercicio 16: Creación de un gráfico de líneas estáticas</a></span></li><li><span><a href="#Ejercicio-17:-Presentación-de-datos-a-través-del-tiempo-con-múltiples-gráficos-de-líneas" data-toc-modified-id="Ejercicio-17:-Presentación-de-datos-a-través-del-tiempo-con-múltiples-gráficos-de-líneas-2.0.5"><span class="toc-item-num">2.0.5&nbsp;&nbsp;</span>Ejercicio 17: Presentación de datos a través del tiempo con múltiples gráficos de líneas</a></span></li><li><span><a href="#Ejercicio-18:-Creación-y-exploración-de-un-mapa-de-calor-estático" data-toc-modified-id="Ejercicio-18:-Creación-y-exploración-de-un-mapa-de-calor-estático-2.0.6"><span class="toc-item-num">2.0.6&nbsp;&nbsp;</span>Ejercicio 18: Creación y exploración de un mapa de calor estático</a></span></li><li><span><a href="#Ejercicio-19:-Creación-de-vínculos-en-mapas-térmicos-estáticos" data-toc-modified-id="Ejercicio-19:-Creación-de-vínculos-en-mapas-térmicos-estáticos-2.0.7"><span class="toc-item-num">2.0.7&nbsp;&nbsp;</span>Ejercicio 19: Creación de vínculos en mapas térmicos estáticos</a></span></li><li><span><a href="#Creación-de-gráficos-para-representar-estadísticas" data-toc-modified-id="Creación-de-gráficos-para-representar-estadísticas-2.0.8"><span class="toc-item-num">2.0.8&nbsp;&nbsp;</span>Creación de gráficos para representar estadísticas</a></span></li><li><span><a href="#Ejemplo-1:-Histograma-revisado" data-toc-modified-id="Ejemplo-1:-Histograma-revisado-2.0.9"><span class="toc-item-num">2.0.9&nbsp;&nbsp;</span>Ejemplo 1: Histograma revisado</a></span></li><li><span><a href="#Ejercicio-20:-Creación-y-exploración-de-un-gráfico-de-caja" data-toc-modified-id="Ejercicio-20:-Creación-y-exploración-de-un-gráfico-de-caja-2.0.10"><span class="toc-item-num">2.0.10&nbsp;&nbsp;</span>Ejercicio 20: Creación y exploración de un gráfico de caja</a></span></li><li><span><a href="#Ejercicio-21:-Creación-de-un-gráfico-de-violín" data-toc-modified-id="Ejercicio-21:-Creación-de-un-gráfico-de-violín-2.0.11"><span class="toc-item-num">2.0.11&nbsp;&nbsp;</span>Ejercicio 21: Creación de un gráfico de violín</a></span></li><li><span><a href="#Tarea-1.2" data-toc-modified-id="Tarea-1.2-2.0.12"><span class="toc-item-num">2.0.12&nbsp;&nbsp;</span>Tarea 1.2</a></span></li></ul></li></ul></li><li><span><a href="#De-la-visualización-estática-a-la-interactiva" data-toc-modified-id="De-la-visualización-estática-a-la-interactiva-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>De la visualización estática a la interactiva</a></span><ul class="toc-item"><li><span><a href="#Introducción" data-toc-modified-id="Introducción-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Introducción</a></span></li><li><span><a href="#Visualización-estática-versus-interactiva" data-toc-modified-id="Visualización-estática-versus-interactiva-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Visualización estática versus interactiva</a></span><ul class="toc-item"><li><span><a href="#Ejemplo" data-toc-modified-id="Ejemplo-3.2.1"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>Ejemplo</a></span></li></ul></li><li><span><a href="#Aplicaciones-de-las-visualizaciones-interactivas-de-datos" data-toc-modified-id="Aplicaciones-de-las-visualizaciones-interactivas-de-datos-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Aplicaciones de las visualizaciones interactivas de datos</a></span></li><li><span><a href="#Visualización-interactiva-de-datos-con-Bokeh" data-toc-modified-id="Visualización-interactiva-de-datos-con-Bokeh-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Visualización interactiva de datos con Bokeh</a></span><ul class="toc-item"><li><span><a href="#Ejercicio-22:-Preparación-de-nuestro-conjunto-de-datos" data-toc-modified-id="Ejercicio-22:-Preparación-de-nuestro-conjunto-de-datos-3.4.1"><span class="toc-item-num">3.4.1&nbsp;&nbsp;</span>Ejercicio 22: Preparación de nuestro conjunto de datos</a></span></li><li><span><a href="#Ejercicio-23:-Creación-del-gráfico-estático-base-para-una-visualización-de-datos-interactiva" data-toc-modified-id="Ejercicio-23:-Creación-del-gráfico-estático-base-para-una-visualización-de-datos-interactiva-3.4.2"><span class="toc-item-num">3.4.2&nbsp;&nbsp;</span>Ejercicio 23: Creación del gráfico estático base para una visualización de datos interactiva</a></span></li><li><span><a href="#Ejercicio-24:-Añadir-una-herramienta-Hover" data-toc-modified-id="Ejercicio-24:-Añadir-una-herramienta-Hover-3.4.3"><span class="toc-item-num">3.4.3&nbsp;&nbsp;</span>Ejercicio 24: Añadir una herramienta Hover</a></span></li><li><span><a href="#Ejercicio-24:-Añadir-un-deslizador-al-gráfico-estático" data-toc-modified-id="Ejercicio-24:-Añadir-un-deslizador-al-gráfico-estático-3.4.4"><span class="toc-item-num">3.4.4&nbsp;&nbsp;</span>Ejercicio 24: Añadir un deslizador al gráfico estático</a></span></li></ul></li><li><span><a href="#Visualización-interactiva-de-datos-con-Plotly-Express" data-toc-modified-id="Visualización-interactiva-de-datos-con-Plotly-Express-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Visualización interactiva de datos con Plotly Express</a></span><ul class="toc-item"><li><span><a href="#Ejercicio-26:-Creación-de-un-gráfico-de-dispersión-interactivo" data-toc-modified-id="Ejercicio-26:-Creación-de-un-gráfico-de-dispersión-interactivo-3.5.1"><span class="toc-item-num">3.5.1&nbsp;&nbsp;</span>Ejercicio 26: Creación de un gráfico de dispersión interactivo</a></span></li><li><span><a href="#Tarea-1.3" data-toc-modified-id="Tarea-1.3-3.5.2"><span class="toc-item-num">3.5.2&nbsp;&nbsp;</span>Tarea 1.3</a></span></li></ul></li></ul></li><li><span><a href="#Visualización-de-datos-a-través-de-estratos" data-toc-modified-id="Visualización-de-datos-a-través-de-estratos-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Visualización de datos a través de estratos</a></span><ul class="toc-item"><li><span><a href="#Introducción" data-toc-modified-id="Introducción-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Introducción</a></span></li><li><span><a href="#Gráficos-de-dispersión-interactivos" data-toc-modified-id="Gráficos-de-dispersión-interactivos-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Gráficos de dispersión interactivos</a></span><ul class="toc-item"><li><span><a href="#Ejercicio-27:-Añadir-Zoom-In-y-Zoom-Out-a-un-gráfico-de-dispersión-estático" data-toc-modified-id="Ejercicio-27:-Añadir-Zoom-In-y-Zoom-Out-a-un-gráfico-de-dispersión-estático-4.2.1"><span class="toc-item-num">4.2.1&nbsp;&nbsp;</span>Ejercicio 27: Añadir Zoom-In y Zoom-Out a un gráfico de dispersión estático</a></span></li><li><span><a href="#Ejercicio-28:-Añadir-la-funcionalidad-Hover-y-Tooltip-a-un-gráfico-de-dispersión" data-toc-modified-id="Ejercicio-28:-Añadir-la-funcionalidad-Hover-y-Tooltip-a-un-gráfico-de-dispersión-4.2.2"><span class="toc-item-num">4.2.2&nbsp;&nbsp;</span>Ejercicio 28: Añadir la funcionalidad Hover y Tooltip a un gráfico de dispersión</a></span></li><li><span><a href="#Ejercicio-29:-Explorar-la-funcionalidad-de-seleccionar-y-resaltar-en-un-gráfico-de-dispersión" data-toc-modified-id="Ejercicio-29:-Explorar-la-funcionalidad-de-seleccionar-y-resaltar-en-un-gráfico-de-dispersión-4.2.3"><span class="toc-item-num">4.2.3&nbsp;&nbsp;</span>Ejercicio 29: Explorar la funcionalidad de seleccionar y resaltar en un gráfico de dispersión</a></span></li><li><span><a href="#Ejercicio-30:-Generación-de-un-trazado-con-las-funciones-de-selección,-zoom-y-hover/hoja-de-cálculo" data-toc-modified-id="Ejercicio-30:-Generación-de-un-trazado-con-las-funciones-de-selección,-zoom-y-hover/hoja-de-cálculo-4.2.4"><span class="toc-item-num">4.2.4&nbsp;&nbsp;</span>Ejercicio 30: Generación de un trazado con las funciones de selección, zoom y hover/hoja de cálculo</a></span></li><li><span><a href="#Ejercicio-31:-Selección-a-través-de-múltiples-parcelas" data-toc-modified-id="Ejercicio-31:-Selección-a-través-de-múltiples-parcelas-4.2.5"><span class="toc-item-num">4.2.5&nbsp;&nbsp;</span>Ejercicio 31: Selección a través de múltiples parcelas</a></span></li><li><span><a href="#Ejercicio-32:-Selección-basada-en-los-valores-de-una-característica" data-toc-modified-id="Ejercicio-32:-Selección-basada-en-los-valores-de-una-característica-4.2.6"><span class="toc-item-num">4.2.6&nbsp;&nbsp;</span>Ejercicio 32: Selección basada en los valores de una característica</a></span></li><li><span><a href="#Ejercicio-33:-Añadir-una-función-de-Zoom-In/Zoom-Out-y-calcular-la-media-en-un-gráfico-de-barras-estático" data-toc-modified-id="Ejercicio-33:-Añadir-una-función-de-Zoom-In/Zoom-Out-y-calcular-la-media-en-un-gráfico-de-barras-estático-4.2.7"><span class="toc-item-num">4.2.7&nbsp;&nbsp;</span>Ejercicio 33: Añadir una función de Zoom-In/Zoom-Out y calcular la media en un gráfico de barras estático</a></span></li><li><span><a href="#Ejercicio-34:-Un-atajo-alternativo-para-representar-la-media-en-un-gráfico-de-barras" data-toc-modified-id="Ejercicio-34:-Un-atajo-alternativo-para-representar-la-media-en-un-gráfico-de-barras-4.2.8"><span class="toc-item-num">4.2.8&nbsp;&nbsp;</span>Ejercicio 34: Un atajo alternativo para representar la media en un gráfico de barras</a></span></li><li><span><a href="#Ejercicio-35:-Añadir-una-función-de-zoom-en-un-mapa-de-calor-estático" data-toc-modified-id="Ejercicio-35:-Añadir-una-función-de-zoom-en-un-mapa-de-calor-estático-4.2.9"><span class="toc-item-num">4.2.9&nbsp;&nbsp;</span>Ejercicio 35: Añadir una función de zoom en un mapa de calor estático</a></span></li><li><span><a href="#Ejercicio-36:-Creación-de-un-diagrama-de-barras-y-un-mapa-de-calor-contiguos" data-toc-modified-id="Ejercicio-36:-Creación-de-un-diagrama-de-barras-y-un-mapa-de-calor-contiguos-4.2.10"><span class="toc-item-num">4.2.10&nbsp;&nbsp;</span>Ejercicio 36: Creación de un diagrama de barras y un mapa de calor contiguos</a></span></li><li><span><a href="#Ejercicio-37:-Vincular-dinámicamente-un-gráfico-de-barras-y-un-mapa-de-calor" data-toc-modified-id="Ejercicio-37:-Vincular-dinámicamente-un-gráfico-de-barras-y-un-mapa-de-calor-4.2.11"><span class="toc-item-num">4.2.11&nbsp;&nbsp;</span>Ejercicio 37: Vincular dinámicamente un gráfico de barras y un mapa de calor</a></span></li><li><span><a href="#Tarea-1.4" data-toc-modified-id="Tarea-1.4-4.2.12"><span class="toc-item-num">4.2.12&nbsp;&nbsp;</span>Tarea 1.4</a></span></li></ul></li></ul></li></ul></div>

# In[1]:


from bokeh.resources import INLINE
import bokeh.io
from bokeh import *
bokeh.io.output_notebook(INLINE)


# ## Introducción a la visualización de datos con Python

# - La visualización de datos es el arte y la ciencia de contar historias cautivadoras con datos.
# 
# - <b>¿Por qué Python?</b>
#     
# - <b>Python</b> realiza cálculos numéricos y científicos avanzados con librerías como: <b>numpy</b> y <b>scipy</b>, alberga una amplia gama de métodos de de métodos de aprendizaje automático gracias a la disponibilidad del paquete <b>scikit-learn</b>
# 
# - Proporciona una gran interfaz para manipulación de **big data** gracias a la disponibilidad del paquete `pandas` y su compatibilidad con Apache Spark
# 
# - Genera gráficos y figuras estéticamente con librerías como <b>seaborn, plotly</b>, etc.

# ### Manejo de datos con pandas DataFrame

# - La biblioteca **pandas** es un conjunto de herramientas de código abierto extremadamente ingenioso para manejar manipular y analizar datos estructurados. Las tablas de datos se pueden almacenar en el objeto **DataFrame** disponible en **pandas**, y los datos en múltiples formatos (por ejemplo, **.csv, .tsv, .xlsx** y **.json**) pueden leerse directamente en un **DataFrame**.  

# #### Ejercicio 1: Lectura de datos desde archivos

# - En este ejercicio, leeremos de un conjunto de datos. En este ejemplo se utiliza el conjunto de datos **diamantes**
# - Abre un cuaderno **jupyter** y carga la librería **pandas**

# In[2]:


import pandas as pd


# In[3]:


import warnings
warnings.filterwarnings('ignore')


# - Especifique la **UR**L del conjunto de datos:

# In[4]:


diamonds_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/diamonds.csv"


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[5]:


diamonds_df = pd.read_csv(diamonds_url)


# In[6]:


diamonds_df.head()


# - Use the **usecols** parameter if only specific columns need to be read.

# In[7]:


diamonds_df_specific_cols = pd.read_csv(diamonds_url, usecols=['carat','cut','color','clarity'])


# In[8]:


diamonds_df_specific_cols.head()


# #### Ejercicio 2: Observación y descripción de datos

# - En este ejercicio, veremos cómo observar y describir datos en un **DataFrame**. Volveremos a utilizar el conjunto de datos de diamantes
# - Cargue la librería pandas:

# In[9]:


import pandas as pd


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[10]:


diamonds_df = pd.read_csv(diamonds_url)


# - Observe los datos utilizando la función **head**:

# In[11]:


diamonds_df.head()


# Los datos contienen diferentes características de los diamantes, como **quilates, calidad de corte, color** y **precio**: `carat, cut, color, clarity, depth, table, price`  como columnas. Ahora, **corte, claridad** y **color** son **variables categóricas**, y **x, y, z, profundidad, tabla** y **precio** son **variables continuas**. Mientras que las variables categóricas toman como valores categorías/nombres únicos, los valores continuos toman números reales como valores.

# - Contar el número de filas y columnas en el **DataFrame** utilizando la función **shape** 

# In[12]:


diamonds_df.shape


# - Resumir las columnas utilizando `describe()` para obtener la distribución de las variables, incluyendo la media, la mediana, el mínimo, el máximo y los diferentes cuartiles

# In[13]:


diamonds_df.describe()


# - Esto funciona para las variables continuas. Sin embargo, para las variables categóricas, necesitamos utilizar el parámetro **include=object**. 

# In[14]:


diamonds_df.describe(include=object)


# - Para obtener información sobre el conjunto de datos, utilice el método `info()`:

# In[15]:


diamonds_df.info()


# - Podemos acceder a la columna corte del **DataFrame diamonds_df** con **diamonds_df.cut** o **diamonds_df['cut']**
# - Ahora, ¿qué tal si seleccionamos todas las filas correspondientes a los diamantes que tienen la talla **Ideal** y almacenarlas en un **DataFrame** separado? Podemos seleccionarlas utilizando la función **loc** para seleccionarlos:

# In[16]:


diamonds_low_df = diamonds_df.loc[diamonds_df['cut']=='Ideal']
diamonds_low_df.head()


# #### Ejercicio 3: Añadir nuevas columnas al DataFrame

# - En este ejercicio, vamos a añadir nuevas columnas al conjunto de datos de diamantes en la biblioteca **pandas**. Empezaremos con la adición simple de columnas y luego avanzaremos y veremos la adición condicional de columnas. Para ello, vamos a seguir los siguientes pasos:
# 
# - Cargue la biblioteca `pandas`

# In[17]:


import pandas as pd


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[18]:


diamonds_df = pd.read_csv(diamonds_url)
diamonds_df.head()


# - Añade una columna `price_per_carat` al `DataFrame`. En este ejemplo el precio por quilates. Del mismo modo, también podemos utilizar la suma, la resta y otros operadores matemáticos sobre dos columnas numéricas.

# In[19]:


diamonds_df['price_per_carat'] = diamonds_df['price']/diamonds_df['carat']


# - Llame a la función **head** de **DataFrame** para comprobar si la nueva columna se ha añadido como como se esperaba:

# In[20]:


diamonds_df.head()


# - Ahora, veremos la adición condicional de columnas. Vamos a intentar añadir una columna basada en el valor de `price_per_carat`, digamos que todo lo que sea más de 3500 como alto (codificado como 1) y todo lo que sea inferior a 3500 como bajo (codificado como 0).

# In[21]:


import numpy as np

diamonds_df['price_per_carat_is_high'] = np.where(diamonds_df['price_per_carat'] > 3500, 1, 0)
diamonds_df.tail()


# #### Ejercicio 4: Aplicación de funciones a las columnas de DataFrame

# - En este ejercicio, consideraremos un escenario en el que el precio de los diamantes ha aumentado y queremos aplicar un factor de incremento de 1.3 al precio de todos los diamantes en nuestro registro. Podemos conseguirlo aplicando una sencilla función. A continuación, redondearemos el precio de los diamantes hasta su tope. Para ello, vamos a seguir los siguientes pasos

# - Cargue la biblioteca `pandas`

# In[22]:


import pandas as pd


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[23]:


diamonds_df = pd.read_csv(diamonds_url)
diamonds_df.head()


# - Aplique una función simple en las columnas utilizando el siguiente código:

# In[24]:


diamonds_df['price'] = diamonds_df['price']*1.3


# In[25]:


diamonds_df.head()


# - Aplicar la función `math.ceil` para redondear el precio de los diamantes hasta su tope

# In[26]:


import math

diamonds_df['rounded_price'] = diamonds_df['price'].apply(math.ceil)
diamonds_df.head()


# - Puede haber ocasiones en las que tenga que escribir su propia función para realizar la tarea que desea llevar a cabo. 
# - Por ejemplo, digamos que quiere añadir otra columna al **DataFrame** indicando el precio redondeado de los diamantes al múltiplo de 100 (igual o superior al precio).
# - Utilice la función `lambda` como sigue para redondear el precio de los diamantes al múltiplo de 100 más cercano

# In[27]:


import math

diamonds_df['rounded_price_to_100multiple'] = diamonds_df['price'].apply(lambda x: 100*math.ceil(x/100))
diamonds_df.head()


# - Por supuesto, no todas las funciones pueden ser escritas en una sola línea y es importante saber cómo incluir funciones definidas por el usuario en la función `apply`. Vamos a escribir el mismo código con una función definida por el usuario para ilustrarlo.

# In[28]:


import math

def get_100_multiple_ceil(x):
    y = 100*math.ceil(x/100)
    return y
 
diamonds_df['rounded_price_to_100multiple']=diamonds_df['price'].apply(get_100_multiple_ceil)
diamonds_df.head()


# #### Ejercicio 5: Aplicación de funciones en varias columnas

# - Supongamos que estamos interesados en comprar diamantes que tengan **Ideal** **cut** y **color** **D** (totalmente incoloro). Este ejercicio consiste en añadir una nueva columna, **desired**, al **DataFrame**, cuyo valor será **yes** si se cumplen nuestros criterios y **no** si no se cumplen. Veamos cómo lo hacemos:

# - Cargue la biblioteca **pandas**

# In[29]:


import pandas as pd


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[30]:


diamonds_df_exercise = pd.read_csv(diamonds_url)
diamonds_df_exercise.head()


# - Write a function to determine whether a record, **x**, is desired or not:

# In[31]:


def is_desired(x):
    bool_var = 'yes' if (x['cut']=='Ideal' and x['color']=='D') else 'no'
    return bool_var


# - Utilice la función `apply` para añadir la nueva columna, **desired**:

# In[32]:


diamonds_df_exercise['desired'] = diamonds_df_exercise.apply(is_desired, axis = 'columns')
diamonds_df_exercise.tail()


# #### Ejercicio 6: Eliminación de columnas de un DataFrame 

# - Por último, vamos a ver cómo eliminar columnas de un **DataFrame** de **pandas**. Por ejemplo, borraremos las columnas **rounded_price** y **rounded_price_to_100multiple**

# - Cargue la biblioteca **pandas**

# In[33]:


import pandas as pd


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[34]:


diamonds_df = pd.read_csv(diamonds_url)
diamonds_df.head()


# - Añadir la columna **price_per_carat** al **DataFrame**

# In[35]:


diamonds_df['price_per_carat'] = diamonds_df['price']/diamonds_df['carat']
diamonds_df.head()


# - Utilice la función **np.where** del paquete **numpy** de Python:

# In[36]:


import numpy as np

diamonds_df['price_per_carat_is_high'] = np.where(diamonds_df['price_per_carat'] > 3500, 1, 0)
diamonds_df.tail()


# - Aplicar una función compleja para redondear el precio de los diamantes hasta su tope:

# In[37]:


import math

diamonds_df['rounded_price'] = diamonds_df['price'].apply(math.ceil)
diamonds_df.head()


# - Escribe un código para crear una función definida por el usuario:

# In[38]:


import math

def get_100_multiple_ceil(x):
    y = math.ceil(x/100)*100
    return y
 
diamonds_df['rounded_price_to_100multiple']=diamonds_df['price'].apply(get_100_multiple_ceil)
diamonds_df.head()


# - Eliminar las columnas **rounded_price** y **rounded_price_to_100multiple** utilizando la función **drop**:

# In[39]:


diamonds_df = diamonds_df.drop(columns = ['rounded_price', 'rounded_price_to_100multiple'])
diamonds_df.head()


# #### Ejercicio 7: Escribir un DataFrame en un archivo

# - En este ejercicio, escribiremos un **DataFrame** de diamantes en un archivo **.csv**. Para ello, utilizaremos el siguiente código:

# - Cargue la biblioteca **pandas**

# In[40]:


import pandas as pd


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[41]:


diamonds_df = pd.read_csv(diamonds_url)
diamonds_df.head()


# - Escriba el conjunto de datos de los diamantes en un archivo **.csv**:

# In[42]:


diamonds_df.to_csv('diamonds_modified.csv')


# - Por defecto, la función **to_csv** genera un archivo que incluye las cabeceras de las columnas y los números de las filas. así como los números de fila. Añade un parámetro `index=False` para excluir los números de fila:

# In[43]:


diamonds_df.to_csv('diamonds_modified.csv', index = False)


# - Ahora que tenemos una idea básica de cómo cargar y manejar los datos en un objeto **DataFrame** de **pandas**, vamos a empezar a hacer algunos gráficos simples a partir de los datos.
# - **matplotlib** es una biblioteca de trazado disponible en la mayoría de las distribuciones de **Python** y es la es la base de varios paquetes de ploteo, incluyendo la funcionalidad de ploteo incorporada en **pandas** y **seaborn**. **matplotlib** permite controlar todos los aspectos de una figura y es conocido por ser muy detallado.

# #### Exercise 8: Trazado y análisis de un histograma

# - En este ejercicio, crearemos un **histograma** de la frecuencia de los diamantes en el conjunto de datos con sus respectivas especificaciones de **carat** (quilates) en el eje $x$:

# - Cargue la biblioteca **pandas**

# In[44]:


import pandas as pd
import seaborn as sns


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[45]:


diamonds_df = pd.read_csv(diamonds_url)
diamonds_df.head()


# - Trazar un histograma utilizando el conjunto de datos de diamantes donde el eje **x axis = carat**. El eje $y$ de este gráfico indica el número de diamantes del conjunto de datos con la especificación de **carat** en el eje $x$.

# In[46]:


diamonds_df.hist(column='carat')


# - La función **hist** tiene un parámetro llamado **bins**, que se refiere literalmente al número de intervalos de igual tamaño en los que se dividen los puntos de datos. Por defecto el parámetro **bins** está fijado en 10 en **pandas**. Podemos cambiarlo por un número diferente diferente, si lo deseamos.

# In[47]:


diamonds_df.hist(column = 'carat', bins = 50)


# - Ahora, veamos la misma función utilizando `seaborn`. Note que `pandas` establece el parámetro **bins** a un valor por defecto de 10, pero **seaborn** infiere un **bin** de tamaño apropiado basado en la distribución estadística del conjunto de datos.

# In[48]:


import seaborn as sns

sns.distplot(diamonds_df.carat)


# - Por defecto, la función **distplot** también incluye una curva suavizada sobre el histograma, llamada **estimación de la densidad del kernel (KDE)**. Si queremos eliminar el **KDE** y mirar sólo el histograma, podemos utilizar el parámetro **kde=False**.

# In[49]:


sns.distplot(diamonds_df.carat, kde = False)


# - Una **transformación logarítmica** ayuda a identificar más tendencias. Por ejemplo, en el siguiente gráfico, el eje $x$ muestra los valores transformados en logaritmos de la variable del precio, y vemos que hay dos picos que indican dos tipos de diamantes: uno con un precio alto y otro con un precio bajo

# In[50]:


import numpy as np
sns.distplot(np.log(diamonds_df.price))


# Qué valores de las características son más frecuentes en el conjunto de datos (en este caso, hay un pico en torno a 6.8 y otro pico entre 8.5 y 9, nótese que `log(price) = valores`, en este caso

# #### Exercise 9: Creación de un gráfico de barras y cálculo de la distribución del precio medio

# - En este ejercicio, aprenderemos a crear una tabla utilizando la función `pandas crosstab`. Utilizaremos una tabla para generar un gráfico de barras. A continuación, exploraremos un gráfico de barras generado con la biblioteca `seaborn` y calcularemos la distribución del precio medio. Para ello, vamos a realizar los siguientes pasos

# - Cargue la biblioteca **pandas**

# In[51]:


import pandas as pd
import seaborn as sns


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[52]:


diamonds_df = pd.read_csv(diamonds_url)
diamonds_df.head()


# - Imprime los valores únicos de la columna *corte*:

# In[53]:


diamonds_df.cut.unique()


# - Imprime los valores únicos de la columna *claridad*:

# In[54]:


diamonds_df.clarity.unique()


# - `unique()` devuelve un array. Hay cinco cualidades únicas de *cut* y ocho valores únicos en *clarity*. El número de valores únicos se puede obtener utilizando `nunique()` en `pandas.

# - Para obtener los recuentos de diamantes de cada calidad de *cut*, primero creamos una tabla utilizando la función **pandas crosstab()**:

# In[55]:


cut_count_table = pd.crosstab(index = diamonds_df['cut'], columns = 'count')
cut_count_table


# - Pase estos recuentos a otra función **pandas**, **plot(kind='bar')**:

# In[56]:


cut_count_table.plot(kind = 'bar')


# Vemos que la mayoría de los diamantes del conjunto de datos son de la calidad de corte *Ideal*, seguidos de *Premium, Very Good, Good y Fair*. Ahora, veamos cómo generar el mismo gráfico utilizando `seaborn`.

# - Generate the same bar plot using `seaborn`

# In[57]:


sns.catplot("cut", data = diamonds_df, aspect = 1.5, kind = "count", color = "b")


# Observe cómo la función `catplot()` no requiere que creemos la tabla de recuento intermedia (utilizando `pd.crosstab()`), y reduce un paso en el proceso de trazado.

# - A continuación, se muestra cómo se obtiene la **distribución del precio medio** de las diferentes calidades de *cut* utilizando **seaborn**

# In[58]:


import seaborn as sns
from numpy import median, mean

sns.set(style = "whitegrid")
ax = sns.barplot(x = "cut", y = "price", data = diamonds_df, estimator = mean)


# Aquí, las líneas negras (barras de error) de los rectángulos indican la incertidumbre (o dispersión de los valores) en torno a la estimación de la media. Las funciones mencionadas van mucho más allá de un simple recuento: aplican una función que calcula una medida de tendencia central (por defecto es el valor medio) y muestran, aplicando `bootstrapping`, el intervalo de confianza del 95% para dicha medida. Por defecto, este valor está fijado en un 95% de confianza. ¿Cómo lo cambiamos? Utilizando el parámetro **ci=68**, por ejemplo, lo fijamos en el 68%. También podemos representar la desviación estándar en los precios utilizando **ci=sd**.

# - Reordenar las barras del eje x utilizando el orden: 

# In[59]:


ax = sns.barplot(x = "cut", y = "price", data = diamonds_df, estimator = mean, ci = 68, 
                 order=['Ideal','Good','Very Good','Fair','Premium'])


# #### Exercise 10: Creación de gráficos de barras agrupados por una característica específica

# - En este ejercicio, utilizaremos el conjunto de datos de los diamantes para generar la distribución de los precios con respecto al color para cada calidad de corte. En el ejercicio 7, vimos la distribución de precios para diamantes de diferentes calidades de talla. Ahora, nos gustaría ver la variación de cada color:

# - Cargue la biblioteca **pandas**

# In[60]:


import pandas as pd
import seaborn as sns


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[61]:


diamonds_df = pd.read_csv(diamonds_url)
diamonds_df.tail()


# - Utilice el parámetro `hue` para trazar grupos anidados:

# In[62]:


ax = sns.barplot(x = "cut", y = "price", hue = 'color', data = diamonds_df)


# Aquí podemos observar que los patrones de precios de los diamantes de diferentes colores son similares para cada calidad de talla. 

# #### Exercise 11: Cómo ajustar los parámetros de un gráfico de barras agrupadas

# - En este ejercicio, modificaremos los parámetros de los gráficos, por ejemplo, `hue`, de un gráfico de barras agrupadas. Veremos cómo colocar las leyendas y las etiquetas de los ejes en los lugares adecuados y también exploraremos la función de rotación

# - Cargue la biblioteca **pandas**

# In[63]:


import pandas as pd
import seaborn as sns


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[64]:


diamonds_df = pd.read_csv(diamonds_url)
diamonds_df.head()


# In[65]:


ax = sns.barplot(x = "cut", y = "price", hue = 'color', data = diamonds_df)


# In[66]:


ax = sns.barplot(x='cut', y='price', hue='color', data=diamonds_df)
ax.legend(loc='upper right', ncol=4)


# En la llamada anterior a `ax.legend()`, el parámetro `ncol` denota el número de columnas en las que deben organizarse los valores de la leyenda, y el parámetro `loc` especifica la ubicación de la leyenda y puede tomar cualquiera de los ocho valores `'upper left', 'upper right', 'lower left', 'lower right'`.

# - Para modificar las etiquetas de los ejes $𝑥$ y $𝑦$, introduzca el siguiente código

# In[67]:


ax = sns.barplot(x='cut', y='price', hue='color', data=diamonds_df)
ax.legend(loc='upper right', ncol=4)
ax.set_xlabel('Cut', fontdict={'fontsize' : 12})
ax.set_ylabel('Price', fontdict={'fontsize' : 12})


# - Del mismo modo, utilice esto para modificar el tamaño de la fuente y la rotación del eje $x$ de la garrapata etiquetas:

# In[68]:


ax = sns.barplot(x='cut', y='price', hue='color', data=diamonds_df)
ax.legend(loc='upper right',ncol=4)
ax.set_xticklabels(ax.get_xticklabels(), fontsize=13, rotation=45)
ax.set_xlabel('Cut', fontdict={'fontsize' : 12})
ax.set_ylabel('Price', fontdict={'fontsize' : 12})


# La función de rotación es especialmente útil cuando las etiquetas de ticks son largas y se amontonan en el eje $x$.

# #### Exercise 12: Anotar un gráfico de barras

# - En este ejercicio, anotaremos un gráfico de barras, generado con la función **catplot** de **seaborn**, utilizando una nota justo encima del gráfico.

# - Cargue la biblioteca **pandas**

# In[69]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# - Leer los archivos de la **URL** en el **DataFrame** de **pandas**

# In[70]:


diamonds_df = pd.read_csv(diamonds_url)
diamonds_df.head()


# - Generar un gráfico de barras utilizando la función `catplot` de la biblioteca `seaborn`

# In[71]:


ax = sns.catplot("cut", data=diamonds_df, aspect=1.5, kind="count", color="b")


# - Anote la columna que pertenece a la categoría *Ideal*:

# In[72]:


ideal_group = diamonds_df.loc[diamonds_df['cut']=='Ideal']
ideal_group.head()


# - Encuentre la ubicación de la coordenada $x$ donde debe colocarse la anotación:

# In[73]:


x = ideal_group.index.tolist()[0]


# - Encuentre la ubicación de la coordenada $y$ donde debe colocarse la anotación:

# In[74]:


y = len(ideal_group)


# - Imprime la ubicación de las coordenadas $x$ e $y$:

# In[75]:


print(x)
print(y)


# - Anota la gráfica con una nota:

# In[76]:


sns.catplot("cut", data=diamonds_df, aspect=1.5, kind="count", color="b")
plt.annotate('excellent polish and symmetry ratings;\nreflects almost all the light that enters it', 
             xy=(x,y), xytext=(x+0.3, y+2000), arrowprops=dict(facecolor='red'))


# - Ahora, parece que hay muchos parámetros en la función de anotación. La documentación oficial de [Matplotlib](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.annotate.html) cubre todos los detalles

# #### Tarea 1.1

# - Trabajaremos con el conjunto de datos de 120 años de historia olímpica adquirido por Randi Griffin en [Randi-Griffin](https://www.sports-reference.com/) y puesto a disposición en [athlete_events](https://raw.githubusercontent.com/lihkirun/AppliedStatisticMS/main/DataVisualizationRPython/Lectures/Python/PythonDataSets/athlete_events.csv). - Su tarea consiste en identificar los cinco deportes más importantes según el mayor número de medallas otorgadas en el año 2016, y luego realizar el siguiente análisis:

# 1. Genere un gráfico que indique el número de medallas concedidas en cada uno de los cinco principales deportes en 2016.
# 2. Trace un gráfico que represente la distribución de la edad de los ganadores de medallas en los cinco principales deportes en 2016.
# 3. Descubre qué equipos nacionales ganaron el mayor número de medallas en los cinco principales deportes en 2016.
# 4. Observe la tendencia del peso medio de los atletas masculinos y femeninos ganadores en los cinco principales deportes en 2016

# - Pasos principales

# 1. Descargue el conjunto de datos y formatéelo como un DataFrame de pandas.
# 2. Filtra el **DataFrame** para incluir solo las filas correspondientes a los ganadores de medallas de 2016.
# 3. Descubre las medallas concedidas en 2016 en cada deporte.
# 4. Enumera los cinco deportes más importantes en función del mayor número de medallas concedidas. Filtra el **DataFrame** una vez más para incluir solo los registros de los cinco deportes principales en 2016.
# 5. Genere un gráfico de barras con los recuentos de registros correspondientes a cada uno de los cinco deportes principales.
# 6. Generar un histograma para la característica Edad de todos los ganadores de medallas en los cinco deportes principales (2016).
# 7. Genera un gráfico de barras que indique cuántas medallas ganó el equipo de cada país en los cinco deportes principales en 2016.
# 8. Genere un gráfico de barras que indique el peso medio de los jugadores, clasificados en función del género, que ganaron en los cinco principales deportes en 2016.

# ## Visualización estática

# - Este capítulo es un manual sobre los diferentes tipos de visualización estática y los contextos en los que son más eficaces. Utilizando **seaborn**, aprenderá a crear una variedad de variedad de gráficos y a seleccionar el tipo correcto de visualización para la representación más adecuada de sus datos.
# - En esta sección, estudiaremos el contexto de los gráficos que presentan patrones globales en los datos,
# como por ejemplo:
# 1. Gráficos que muestran la varianza de las características individuales de los datos, como los histogramas
# 2. Gráficos que muestran cómo varían las diferentes características presentes en los datos entre sí, como los gráficos de dispersión, los gráficos de líneas y los mapas de calor.

# - **Scatter plot**

# 1. Un gráfico de dispersión es un gráfico simple que presenta los valores de dos características en un conjunto de datos.
# 2. Cada punto de datos se representa mediante un punto con la coordenada $x$ como valor de la primera característica y la coordenada $y$ como valor de la segunda característica. 
# 3. Un gráfico de dispersión es una gran herramienta para aprender más sobre dos atributos numéricos. 
# 4. Los gráficos de dispersión pueden ayudar a descubrir las relaciones entre diferentes características de los datos, como el tiempo y las ventas, la ingesta de alimentos y las estadísticas de salud en varios contextos.

# #### Ejercicio 13: Creación de un gráfico de dispersión estático

# - En este ejercicio, generaremos un gráfico de dispersión para examinar la relación entre el *peso* (weight) y el *millaje (mpg)* de los vehículos del conjunto de datos **mpg**. Para ello, vamos a seguir los siguientes pasos:

# - Abra un cuaderno Jupyter e importe los módulos de Python necesarios:

# In[77]:


import seaborn as sns


# - Importe el conjunto de datos de **seaborn**:

# In[78]:


mpg_df = sns.load_dataset("mpg")


# - Generar un gráfico de dispersión utilizando la función **scatterplot()**:

# In[79]:


ax = sns.scatterplot(x="weight", y="mpg", data=mpg_df)


# **Observación:** Nótese que el gráfico de dispersión muestra una disminución del *mileage (mpg)* con un aumento del *weight*. Es una visión útil de las relaciones entre las diferentes características del conjunto de datos.

# #### Ejercicio 14: Creación de un gráfico hexagonal estático Binning

# - También existe una versión más elegante de los gráficos de dispersión, llamada **hexagonal binning plot (hexbin plot)**. En este ejercicio, generaremos un diagrama de dispersión hexagonal para comprender mejor la relación entre el peso *(weight)* y el millaje *(mileage (mpg))*:

# - Abra un cuaderno Jupyter e importe los módulos de Python necesarios:

# In[80]:


import seaborn as sns


# - Importe el conjunto de datos de **seaborn**:

# In[81]:


mpg_df = sns.load_dataset("mpg")


# - Trazar un gráfico **hexbin** usando **jointplot** con el tipo establecido en **hex**:

# In[82]:


sns.set(style="ticks")
sns.jointplot(mpg_df.weight, mpg_df.mpg, kind="hex", color="#4CB391")


# **Observación:** Como puede observar, el histograma de los ejes superior y derecho representa la varianza de las características representadas por los ejes $x$ e $y$ respectivamente (*mpg* y *weight*, en este ejemplo). Además, es posible que haya notado en el gráfico de dispersión anterior que los datos se superponían fuertemente en ciertas áreas, ocultando la distribución real de las características. Los gráficos **Hexbin** son una buena herramienta de visualización utilizada cuando los datos son muy densos.

# #### Ejercicio 15: Creación de un gráfico de contorno estático

# - Otra alternativa a los gráficos de dispersión cuando los puntos de datos están densamente poblados en regiones específicas es un gráfico de contorno. En este ejercicio, crearemos un gráfico de contorno para mostrar la relación entre *weight* y el *mileage* en el conjunto de datos *mpg*. Podremos ver que la relación entre *weight* y *mileage* es más fuerte cuando hay mayor volumen de datos

# - Abra un cuaderno Jupyter e importe los módulos de Python necesarios:

# In[83]:


import seaborn as sns


# - Importe el conjunto de datos de **seaborn**:

# In[84]:


mpg_df = sns.load_dataset("mpg")


# - Crea un gráfico de contorno utilizando el método **set_style**

# In[85]:


sns.set_style("white")


# - Generar un gráfico de estimación de la densidad del núcleo (KDE). Los dos primeros parámetros son matrices de $X$ e $Y$ coordenadas de los puntos de datos, el parámetro shade se establece en **True** para que los contornos se rellenen con un gradiente de color basado en el número de puntos de datos

# In[86]:


sns.kdeplot(mpg_df.weight, mpg_df.mpg, shade=True)


# **Observación:** En nuestro ejemplo de *weight* frente a *mileage (mpg)*, el diagrama hexagonal y el diagrama de contorno indican que hay una determinada curva a lo largo de la cual la relación negativa entre el peso y el kilometraje es más fuerte, como es evidente por el mayor número de puntos de datos. La relación negativa se vuelve relativamente más débil a medida que nos alejamos de la curva (menos volumen de datos).

# #### Ejercicio 16: Creación de un gráfico de líneas estáticas

# - Los gráficos de líneas representan la información como una serie de puntos de datos conectados por segmentos de líneas rectas. Son útiles para indicar la relación entre una característica numérica discreta (en el eje $x$), como **model_year**, y una característica numérica continua (en el eje $y$), como *mpg* del conjunto de datos **mpg**. En este ejercicio, crearemos un gráfico de dispersión para un par de características diferentes, **model_year** y **mpg**.
# 

# - Abra un cuaderno Jupyter e importe los módulos de Python necesarios:

# In[87]:


import seaborn as sns


# - Importe el conjunto de datos de **seaborn**:

# In[88]:


mpg_df = sns.load_dataset("mpg")


# - Slecciones el estilo para la figura con `set_style`

# In[89]:


sns.set_style("white")


# - Crear un gráfico de dispersión bidimensional

# In[90]:


ax1 = sns.scatterplot(x="model_year", y="mpg", data=mpg_df)


# **Observación:** En este ejemplo, vemos que la característica **model_year** sólo toma valores discretos entre 70 y 82. Ahora, cuando tenemos una característica numérica discreta como esta (**modelo_año**), dibujar un gráfico de líneas uniendo los puntos de datos es una buena idea. Podemos dibujar un simple gráfico de líneas que muestre la relación entre año_modelo y kilometraje con el siguiente código.

# - Dibuja un gráfico lineal simple para mostrar la relación entre **model_year** y **mileage**

# In[91]:


ax = sns.lineplot(x="model_year", y="mpg", data=mpg_df)


# **Observación:** Como podemos ver, los puntos conectados por la línea sólida representan la media de la característica del eje $y$ en la coordenada $x$ correspondiente. El área sombreada alrededor de la línea muestra el intervalo de confianza para la característica del eje $y$ (por defecto, **seaborn** establece el intervalo de confianza del 95%). El parámetro `ci` puede utilizarse para cambiar a un intervalo de confianza diferente.

# - Cambiar el intervalo de confianza a 68

# In[92]:


sns.lineplot(x="model_year", y="mpg", data=mpg_df, ci=68)


# **Observación:** Como podemos ver en el gráfico anterior, el intervalo de confianza del 68% se traduce en un rango de valores de características en el que están presentes el 68% de los puntos de datos. Los gráficos de líneas son excelentes técnicas de visualización para escenarios en los que tenemos datos que cambian con el tiempo, eje $x$, podría representar la fecha o el tiempo, y el gráfico ayudaría a visualizar cómo un valor varía a lo largo de ese periodo

# #### Ejercicio 17: Presentación de datos a través del tiempo con múltiples gráficos de líneas

# - En este ejemplo, veremos cómo presentar los datos a través del tiempo con múltiples gráficos de líneas. En este ejemplo utilizamos el conjunto de datos de vuelos

# - Abra un cuaderno Jupyter e importe los módulos de Python necesarios:

# In[93]:


import seaborn as sns


# - Importe el conjunto de datos de **seaborn**:

# In[94]:


flights_df = sns.load_dataset("flights")
print(flights_df.head())


# Supongamos que quiere observar cómo varía el número de pasajeros entre meses en diferentes años. ¿Cómo mostraría esta información? Una opción es dibujar varios gráficos de líneas en una sola figura.

# - Crear varias gráficas para los meses de diciembre y enero

# In[95]:


fig,ax=plt.subplots()
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Jan'], color='green')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Feb'], color='red')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Mar'], color='blue')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Apr'], color='cyan')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='May'], color='pink')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Jun'], color='black')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Jul'], color='grey')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Aug'], color='yellow')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Sep'], color='turquoise')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Oct'], color='orange')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Nov'], color='darkgreen')
ax = sns.lineplot(x="year", y="passengers", data=flights_df[flights_df['month']=='Dec'], color='darkred')


# **Observación** Con este ejemplo de 12 gráficos de líneas, podemos ver cómo una figura con demasiados gráficos de líneas rápidamente comienza a abarrotarse y a confundirse. Por lo tanto, para ciertos escenarios, los gráficos de líneas no son no son atractivos ni útiles. Entonces, ¿cuál es la alternativa para nuestro caso de uso? Lo veremos en el siguiente ejercicio

# #### Ejercicio 18: Creación y exploración de un mapa de calor estático

# - Un **heatmap** es una representación visual de una característica numérica continua específica en función de otras dos características discretas (ya sea una categórica o una numérica discreta) en el conjunto de datos. En este ejercicio, exploraremos y crearemos un mapa de calor. Utilizaremos el conjunto de datos de vuelos de la biblioteca **seaborn** para generar un **mapa de calor** que represente el número de pasajeros por mes en los años 1949-1960

# - Abra un cuaderno Jupyter e importe los módulos de Python necesarios:

# In[96]:


import seaborn as sns


# - Importe el conjunto de datos de **seaborn**:

# In[97]:


flights_df = sns.load_dataset("flights")
print(flights_df.head())


# - Ahora tenemos que hacer pivotar el conjunto de datos sobre las variables requeridas utilizando la función **pivot()** antes de generar el mapa de calor. La función **pivot** toma primero como argumentos la característica que se mostrará en filas, luego la que se muestra en columnas y, por último, la característica cuya variación nos interesa observar. Utiliza los valores únicos de los índices/columnas especificados para formar los ejes del **DataFrame** resultante

# In[98]:


df_pivoted = flights_df.pivot("month", "year", "passengers")
ax = sns.heatmap(df_pivoted)


# **Observación:** Aquí podemos observar que el número total de vuelos anuales aumentó de forma constante desde 1949 a 1960. Además, los meses de julio y agosto parecen tener el mayor número de vuelos (en comparación con el resto de los meses) en todos los años de observación.

# - Utilice la opción **clustermap** para agrupar filas y columnas:

# In[99]:


ax = sns.clustermap(df_pivoted, col_cluster=False, row_cluster=True)


# **Observación:** Nótese que el orden de los meses se ha reordenado en los gráficos, pero algunos meses (por ejemplo, julio y agosto) se han mantenido juntos debido a sus tendencias similares. Tanto en julio como en agosto, el número de vuelos aumentó de forma relativamente más drástica en los últimos años hasta 1960. ¿Cómo se calcula la similitud entre filas y columnas? La respuesta es que depende de la métrica de distancia

# - Establecer la métrica como euclidiana

# In[100]:


ax = sns.clustermap(df_pivoted, col_cluster=False)


# - Cambiar la métrica a correlación

# In[101]:


ax = sns.clustermap(df_pivoted, row_cluster=False, metric='correlation')


# **Observación:** Al leer sobre la métrica de la distancia, aprendemos que define la distancia entre dos filas/columnas. Sin embargo, si nos fijamos bien, vemos que el mapa de calor también agrupa no sólo filas o columnas individuales, sino también grupos de filas y columnas. filas o columnas individuales. Aquí es donde entra en juego la vinculación.

# #### Ejercicio 19: Creación de vínculos en mapas térmicos estáticos

# 1. Si definimos la distancia entre dos clusters como la **distancia entre los dos puntos de los clusters más cercanos** entre sí, la regla se denomina enlace único (**single linkage**).
# 2. Si la regla es definir la distancia entre dos clusters como la **distancia entre los puntos más alejados entre sí**, se denomina vinculación completa (**complete linkage**).
# 3. Si la regla es definir la distancia como **la media de todos los posibles pares de filas en los dos clústeres**, se denomina vinculación media (**average linkage**).

# - En este ejercicio, generaremos un mapa de calor y comprenderemos el concepto de enlace único, completo y promedio en los mapas de calor utilizando el conjunto de datos **flights**.

# - Abra un cuaderno Jupyter e importe los módulos de Python necesarios:

# In[102]:


import seaborn as sns


# - Importe el conjunto de datos de **seaborn**:

# In[103]:


flights_df = sns.load_dataset("flights")
print(flights_df.head())


# - Ahora necesitamos pivotar el conjunto de datos en las variables requeridas utilizando la función **pivot()** antes de generar el mapa de calor:

# In[104]:


df_pivoted = flights_df.pivot("month", "year", "passengers")
ax = sns.heatmap(df_pivoted)


# - Enlaza los mapas de calor utilizando el código que sigue

# In[105]:


ax = sns.clustermap(df_pivoted, col_cluster=False, metric='correlation', method='average')
ax = sns.clustermap(df_pivoted, row_cluster=False, metric='correlation', method='complete')
ax = sns.clustermap(df_pivoted, row_cluster=False, metric='correlation', method='single')


# **Observación** Los mapas de calor también son una buena forma de visualizar lo que ocurre en un espacio 2D. Por ejemplo, pueden utilizarse para mostrar dónde hay más acción en el campo en un partido de fútbol. Del mismo modo, en un sitio web, los mapas de calor se pueden utilizar para mostrar las áreas que son más más frecuentadas por los usuarios.

# #### Creación de gráficos para representar estadísticas

# - Cuando los conjuntos de datos son enormes, a veces resulta útil observar las estadísticas de resumen de una serie de características diferentes y hacerse una idea preliminar del conjunto de datos. Por ejemplo, las estadísticas de resumen de cualquier característica numérica incluyen medidas de tendencia central, como la media, y medidas de dispersión, como la desviación estándar. Los histogramas muestran la distribución de una característica dada en los datos, podemos hacer un gráfico un poco más informativo mostrando algunas estadísticas de resumen en el mismo gráfico.

# #### Ejemplo 1: Histograma revisado

# - Importar los módulos de Python necesarios; cargar el conjunto de datos; elegir el número de intervalos y si la estimación de la densidad del kernel debe mostrarse o no; usar el color rojo para mostrar media utilizando una línea recta en el eje $x$ (paralela al eje $y$); definir la ubicación de la leyenda:

# In[106]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

mpg_df = sns.load_dataset("mpg")
ax = sns.distplot(mpg_df.weight, bins=50, kde=False)
plt.axvline(x=np.mean(mpg_df.weight), color='red', label='mean')
plt.axvline(x=np.median(mpg_df.weight), color='orange', label='median')
plt.legend(loc='upper right')


# Este histograma muestra la distribución de la característica de peso junto con la media y la mediana. Observe que la media no es igual a la mediana, lo que significa que la característica no está distribuida normalmente.

# #### Ejercicio 20: Creación y exploración de un gráfico de caja

# Los gráficos de caja son una forma excelente de examinar la relación entre las estadísticas de resumen de una característica numérica en relación con otras características categóricas. En este ejercicio crearemos un diagrama para establecer la relación entre **model_year** and **mileage** using the **mpg** dataset. We'll analyze manufacturing efficiency and the mileage of vehicles over a period of years. To do so, let's go through the following steps

# - Importe la libreria **seaborn**

# In[107]:


import seaborn as sns


# - Cargue el **dataset**

# In[108]:


mpg_df = sns.load_dataset("mpg")
mpg_df.head()


# - Crear un diagrama de cajas

# In[109]:


sns.boxplot(x='model_year', y='mpg', data=mpg_df)


# Como podemos ver, los límites de la caja indican el rango intercuartil, el límite superior marca el cuartil del 25% y el límite inferior el cuartil del 75%. La línea horizontal dentro de la caja indica la mediana. Cualquier punto aislado fuera de los bigotes (las barras en forma de $T$ por encima y por debajo de la caja) marca los valores atípicos, mientras que los propios bigotes muestran los valores mínimos y máximos que no son valores atípicos. Aparentemente, el millaje mejoró sustancialmente en los 80 en comparación con los 70.

# - Añadamos otra característica a nuestro **mpg** DataFrame que denote si el coche fue fabricado en los 70 o en los 80. Modifica el DataFrame **mpg** creando una nueva característica, **model_decade**

# In[110]:


import numpy as np
mpg_df['model_decade'] = np.floor(mpg_df.model_year/10)*10
mpg_df['model_decade'] = mpg_df['model_decade'].astype(int)
mpg_df.tail()


# - Ahora, volvamos a dibujar nuestro gráfico de caja para ver la distribución de los millajes en las dos décadas

# In[111]:


sns.boxplot(x='model_decade', y='mpg', data=mpg_df)


# También podemos añadir otra característica, por ejemplo, la región de origen, y ver cómo afecta a la relación entre el kilometraje y el tiempo de fabricación, las dos características que hemos estado considerando hasta ahora

# - Use the hue parameter to group by origin

# In[112]:


sns.boxplot(x='model_decade', y='mpg', data=mpg_df, hue='origin')


# Como podemos ver, según el conjunto de datos de mpg, en los años 70 y principios de los 80, Europa y Japón produjeron coches con mejor millaje que los Estados Unidos.

# #### Ejercicio 21: Creación de un gráfico de violín

# - ¿Y si pudiéramos obtener una pista sobre la distribución completa de una característica numérica específica agrupada por otras características categóricas? La tipo de técnica de visualización adecuada en este caso es un gráfico de violín. Un gráfico de violín es similar a un grafico de caja pero incluye más detalles sobre las variaciones de los datos. En este ejercicio, utilizaremos el conjunto de datos **mpg** y generaremos un gráfico de violín que represente la variación detallada del **millaje (mpg)** en función de **model_decade** y la región de origen

# - Importe la libreria **seaborn**

# In[113]:


import seaborn as sns


# - Cargue el **dataset**

# In[114]:


mpg_df = sns.load_dataset("mpg")


# - Generar el gráfico de violín utilizando la función **violinplot** en **seaborn**

# In[115]:


import numpy as np

mpg_df['model_decade'] = np.floor(mpg_df.model_year/10)*10
mpg_df['model_decade'] = mpg_df['model_decade'].astype(int)
sns.violinplot(x='model_decade', y='mpg', data=mpg_df, hue='origin')


# - Podemos ver aquí que, durante los años 70, mientras que la mayoría de los vehículos de EE.UU. tenían un millaje medio de 19 mpg, los vehículos de Japón y Europa tenían millajes medios de alrededor de 27 y 25 mpg. Mientras que el kilometraje de los vehículos en Europa y Japón aumentó entre 7 y 8 puntos en los años 80, el kilometraje medio de los vehículos en EE.UU. seguía siendo similar al de los vehículos en Japón y Europa en la década anterior.

# #### Tarea 1.2

# **Estadísticas:** Seguiremos trabajando con el conjunto de datos de 120 años de historia olímpica adquirido por Randi Griffin en [Randi Griffin](https://www.sports-reference.com/)

# Como especialista en visualización, su tarea consiste en crear dos parcelas para los ganadores de medallas de 2016 de cinco deportes: atletismo, natación, remo, fútbol y hockey

# - Crea un gráfico utilizando una técnica de visualización adecuada que presente de la mejor manera posible el patrón global de las características de **height** y **weight** de los ganadores de medallas de 2016 de los cinco deportes.

# - Crea un gráfico utilizando una técnica de visualización adecuada que presente de la mejor manera posible la estadística de resumen para la altura y el peso de los jugadores que ganaron cada tipo de medalla (oro/plata/bronce) en los datos.

# Utilizar su creatividad y sus habilidades para sacar conclusiones importantes de los datos

# **Pasos importantes**

# - Descargue el conjunto de datos y formatéelo como un **pandas** DataFrame

# - Filtrar el DataFrame para incluir únicamente las filas correspondientes a los ganadores de medallas de 2016 en los deportes mencionados en la descripción de la actividad

# - Observe las características del conjunto de datos y anote su tipo de datos: ¿son categóricos o numéricos?

# - Evaluar cuál sería la visualización adecuada para que un patrón global represente las características de **height** y **weight**

# - Evaluar cuál sería la visualización adecuada para representar las estadísticas resumidas de las características de **height** y **weight** en función de las medallas, separadas además por género de los atletas.

# ## De la visualización estática a la interactiva

# **Objetivos**
# `
# - Explicar las diferencias entre las visualizaciones estáticas e interactivas
# - Explicar la aplicación de las visualizaciones interactivas en diversos sectores
# - Crear gráficos interactivos con funcionalidades de `zoom, hover` y `slide`
# - Utilizar las librerías `Bokeh` y `Plotly` (Express) de `Python` para crear visualizaciones de datos interactivas
# 
# En este capítulo, pasaremos de las visualizaciones estáticas a las interactivas y estudiaremos las aplicaciones
# de las visualizaciones interactivas para diferentes escenarios.

# ### Introducción

# - En la sección anterior hablamos de las visualizaciones de datos estáticas, es decir, gráficos y diagramas que están inmóviles y no pueden ser modificados o interactuados en tiempo real por el público.
# - Las visualizaciones de datos interactivas están un paso por delante de las estáticas. La definición de interactivo es algo que implica la comunicación entre dos o más cosas o personas que trabajan juntas. Por lo tanto, las visualizaciones interactivas son representaciones gráficas de datos analizados (estáticos o dinámicos) que pueden reaccionar y responder a las acciones del usuario en el momento. 

# ![](figures/Figure301.png)

# ### Visualización estática versus interactiva

# + Aunque las visualizaciones estáticas de datos son un gran avance hacia el objetivo de extraer y explicar el valor y la información que contienen los conjuntos de datos, la adición de interactividad hace que estas visualizaciones vayan un paso más allá.

# **Las visualizaciones de datos interactivas tienen las siguientes cualidades**:
# 
# - Son más fáciles de explorar ya que permiten interactuar con los datos cambiando colores, parámetros y gráficos.
# - Se pueden manipular fácilmente y al instante. Ya que se puede interactuar con ellas, los gráficos se pueden cambiar delante del usuario.  Por ejemplo, usando un deslizador interactivo. Cuando la posición de este deslizador cambia el gráfico también lo hace, además se úeden crear casillas de verificación que le permitan seleccionar los parámetros que desea ver.
# - Permiten acceder a los datos en tiempo real y a la información que proporcionan. Esto permite el análisis eficaz y rápido de las tendencias.
# - Son más fáciles de comprender, lo que permite a las organizaciones tomar mejores decisiones basadas en datos.
# - Eliminan la necesidad de tener varios gráficos para la misma información. Un solo gráfico interactivo es capaz de transmitir la misma información. Permiten observar relaciones (por ejemplo, causa y efecto).

# #### Ejemplo

# - Empecemos con un ejemplo para entender lo que podemos conseguir mediante la visualización interactiva. Consideremos un dataset de socios inscritos en un gimnasio:

# ![](figures/Figure303.png)

# - La siguiente es una visualización de datos estática en forma de gráfico de caja que describe el peso de las personas clasificadas por su sexo (0 es hombre, 1 es mujer y 2 es otro):

# ![](figures/Figure304.png)

# - El único dato que podemos obtener de este gráfico es la relación entre el peso y el sexo. Sin embargo, hay una tercera característica presente en el conjunto de datos que se utiliza para  generar este gráfico de caja: la edad. La adición de esta característica al gráfico estático anterior puede llevar a la confusión en cuanto a la comprensión de los datos. 
# - Por lo tanto, estamos un poco atascados con respecto a mostrar la relación entre las tres características utilizando una visualización estática. Este problema de problema puede resolverse fácilmente creando una visualización interactiva, como se muestra aquí:

# ![](figures/Figure305.png)

# - En el gráfico de caja anterior, se ha introducido un control deslizante para la característica de la edad. El usuario puede deslizar manualmente la posición del deslizador para observar la relación entre peso, el sexo y la edad en diferentes valores de edad. Además, hay una herramienta de desplazamiento que permite al usuario obtener más información sobre los datos.

# - El gráfico de caja anterior describe que, en este gimnasio, los únicos clientes de 46 años son los que se identifican como otros, y el más pesado de 46 años pesa 82 kilogramos, mientras que el más ligero pesa 56 kilogramos. El usuario puede deslizarse a otra posición para observar la relación entre peso y sexo a una edad diferente, como se muestra en el siguiente gráfico:

# ![](figures/Figure306.png)

# - El gráfico anterior describe los datos a la edad de 34 años: no hay clientes masculinos del gimnasio; Sin embargo, la clienta más pesada de 34 años pesa 100 kilogramos, mientras que la más ligera pesa 71 kilogramos. más ligera pesa 71 kilogramos.

# - Pero aún hay más aspectos a tener en cuenta a la hora de diferenciar entre visualizaciones estáticas e interactivas. Veamos la siguiente tabla:

# | | Visualización Estática | Visualización Interactiva |
# | --- | --- | --- |
# | Medios/campos objetivo | Medios impresos y presentaciones | Aplicaciones web, social media, BI |
# | Coste de creación | Bajo | Alto |
# | Conexión a fuente de datos | No requerida | Requerida en caso dinamico |
# | Visualización | Renderización facil | Requiere diseño de UI |
# | Librerias de Python | Matplotlib, Seaborn | Bokeh, Plotly | 

# - En última instancia, las visualizaciones de datos interactivas transforman el debate sobre los datos en el arte de contar historias, simplificando así el proceso de comprensión de lo que los datos intentan decirnos. Estos aspectos son los que separan las visualizaciones interactivas de las estáticas. Veamos algunas aplicaciones de las visualizaciones de datos interactivas.

# ### Aplicaciones de las visualizaciones interactivas de datos

# - El aspecto clave de las visualizaciones de datos interactivas es su capacidad de responder y reaccionar a las entradas humanas en el momento o en un lapso de tiempo muy corto. En esta sección, veremos algunas entradas humanas, cómo pueden introducirse en las visualizaciones de datos, y el impacto que tienen en la comprensión de los datos

# - `Slider`: Un deslizador permite al usuario ver los datos correspondientes a un rango de algo. A medida que el usuario cambia la posición del deslizador, el gráfico cambia en tiempo real. Este permite al usuario ver varios gráficos en tiempo real:

# ![](figures/Figure310.png)

# - `Hover`: Al pasar (hovering) el cursor por encima de un elemento de un gráfico, el usuario puede recibir más información sobre el punto de datos que la que se puede ver simplemente observando el gráfico. Esto es útil cuando la información que se desea transmitir no cabe en el propio gráfico (como valores precisos o descripciones breves). Veamos una herramienta de hover:

# ![](figures/Figure311.png)

# - `Zoom`:  Acercarse y alejarse de un gráfico es una característica que bastantes bibliotecas de visualización de datos interactivos crean por sí mismas. Le permiten centrarse en puntos de un gráfico y verlos más de cerca.

# - `Clickable parameters`: Hay varios tipos de parámetros clicables, como casillas de verificación y menús desplegables, que permiten al usuario elegir qué aspectos de los datos desea analizar y ver. 

# ![](figures/Figure312.png)

# - Hay bibliotecas de Python que se utilizan para crear estas funciones interactivas, que permiten que las visualizaciones tomen la entrada humana. En los capítulos anteriores, vimos dos bibliotecas de Python incorporadas:
#     + `matplotlib`
#     + `seaborn`

# - Ambos son populares en la comunidad de visualización de datos. Con estas, podemos construir una visualización estática (un gráfico de dispersión estático que muestra la relación entre dos variables) como ésta:

# ![](figures/Figure313.png)

# - Mientras que tanto matplotlib como seaborn son excelentes para las visualizaciones de datos estáticos, hay otras bibliotecas disponibles que hacen un buen trabajo de diseño de características interactivas. Dos de las bibliotecas **Python** de visualización de datos interactivos más populares son 
#     - `bokeh`
#     - `plotly`

# - Esto nos ayuda a crear visualizaciones como las siguientes. Utilizaremos tanto `bokeh` como `plotly` en los ejercicios de este capítulo para crear visualizaciones de datos interactivas.

# ![](figures/Figure314.jpg)

# ### Visualización interactiva de datos con Bokeh

# - `bokeh` es una biblioteca de **Python** para la visualización interactiva de datos. Los gráficos de `Bokeh` se se crean apilando capas una encima de otra. El primer paso es crear una figura vacía figura, a la que se añaden elementos en capas. Estos elementos se conocen como `glifos`, que pueden ser cualquier cosa, desde líneas hasta barras o círculos. A cada `glifo` se le adjuntan propiedades como el color, el tamaño y las coordenadas.

# - `bokeh` es muy popular porque las visualizaciones se renderizan utilizando `HTML` y `JavaScript`, por lo que se suele elegir cuando se diseñan visualizaciones interactivas basadas en la web. Además, el módulo `bokeh.io` crea un archivo `.html` que contiene estático básico, junto con las características interactivas, y no requiere necesariamente un servidor para ejecutarse, lo que hace que la visualización sea muy fácil de desplegar.

# - En este capítulo, los siguientes ejercicios tienen como objetivo crear una visualización de datos interactiva para representar la relación entre las emisiones de dióxido de carbono y el PIB de un país utilizando la biblioteca `bokeh` de **Python**.

# #### Ejercicio 22: Preparación de nuestro conjunto de datos

# - En este ejercicio, descargaremos y prepararemos nuestro conjunto de datos utilizando las bibliotecas incorporadas `pandas` y `numpy`. Al final de este ejercicio, tendremos un `DataFrame` sobre el que construiremos nuestras visualizaciones interactivas de datos. Utilizaremos los archivos `co2.csv` y `gapminder.csv`. El primero consiste en las emisiones de dióxido de carbono por persona por año y por país, mientras que el segundo consiste en el PIB por año y por país.

# - Los siguientes pasos le ayudarán a preparar los datos:

# - Importar las bibliotecas `pandas` y `numpy`:

# In[116]:


import pandas as pd
import numpy as np


# - Guarde el archivo *co2.csv* en un DataFrame llamado *co2*, y el archivo *gapminder.csv* en un DataFrame llamado *gm*:

# In[117]:


url_co2 = 'https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/co2.csv'
co2 = pd.read_csv(url_co2)
co2.head()


# In[118]:


url_gm = 'https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/gapminder.csv'
gm = pd.read_csv(url_gm)
gm.head()


# - Actualmente tenemos dos DataFrames separados, cada uno de ellos compuesto por datos que necesitamos para crear nuestra visualización de datos interactiva. Para crear la visualización, necesitamos combinar estos dos DataFrames y eliminar las columnas no deseadas.

# - Utilice `.drop_duplicates()` para eliminar las instancias duplicadas del *gm* y guárdelo en un nuevo DataFrame llamado *df_gm*:

# In[119]:


df_gm = gm[['Country', 'region']].drop_duplicates()
df_gm.head()


# - Utilice `.merge()` para combinar el DataFrame *co2* con el DataFrame *df_gm*. Esta función función `merge` básicamente realiza una unión interna en los dos DataFrames (lo mismo como el inner join cuando se utiliza en bases de datos). Esta fusión es necesaria para garantizar que tanto el DataFrame *co2* como el DataFrame *gm* estén formados por los mismos países, garantizando así que los valores de las emisiones de CO2 correspondan a sus respectivos países. `how ='inner'` Devuelve un marco de datos con sólo las filas que tienen características comunes. Una unión interna requiere que cada fila de los dos marcos de datos unidos tenga **valores de columna que coincidan**. Esto es similar a la intersección de dos conjuntos.

# - **Outer Join or Full outer join**: Manitene todas las filas de ambos marcos de datos, especifique `how='outer'`
# - **Left Join or Left outer join**: Para incluir todas las filas de su marco de datos $x$ y sólo las de $y$ que coincidan, especifique `how='left'`.
# - **Right Join or Right outer join**: Para incluir todas las filas de su marco de datos $y$ y sólo las de $x$ que coincidan, especifique `how='right'`.

# ![](figures/join-or-merge-in-python-pandas-1.png)

# In[120]:


df_w_regions = pd.merge(co2, df_gm, left_on ='country', right_on ='Country', how ='inner')
df_w_regions.head()


# - Elimina una de las columnas de países ya que hay dos:

# In[121]:


df_w_regions = df_w_regions.drop('Country', axis='columns')
df_w_regions.head()


# - A continuación, vamos a aplicar la función `.melt()` a este DataFrame y a almacenarlo en un nuevo DataFrame llamado *new_co2*. Esta función cambia el formato de un DataFrame en uno que tenga variables identificadoras de nuestra elección. En nuestro caso queremos que las variables identificadoras sean país y región, ya que son las constantes. También vamos a cambiar el nombre de las columnas:

# In[122]:


new_co2 = pd.melt(df_w_regions, id_vars=['country', 'region'])
new_co2.tail(10)


# In[123]:


columns = ['country', 'region', 'year', 'co2']
new_co2.columns = columns
new_co2.tail(10)


# - Establezca el límite inferior de la columna del año como 1964 para que la columna consista en valores int64 para 1964 y en adelante. Haga esto dentro del DataFrame new_co2 que creamos en el paso anterior, y almacénelo en un nuevo DataFrame llamado df_co2. Ordene los valores del DataFrame df_co2 por la columna del país y luego haga lo mismo con la columna del año utilizando .sort_values().

# In[124]:


df_co2 = new_co2[new_co2['year'].astype('int64') > 1963]
df_co2 = df_co2.sort_values(by=['country', 'year'])
df_co2['year'] = df_co2['year'].astype('int64')
df_co2.head()


# - Ahora tenemos un DataFrame que consiste en las emisiones de dióxido de carbono por año y por país. Los números de serie no están en orden ascendente porque hemos ordenado los datos por la columna del país y luego por la del año. A continuación, vamos a crear una tabla similar para el PIB por año y por país.

# - Cree un nuevo DataFrame llamado **df_gdp** que conste de las columnas **country, year** y **gdp** del DataFrame **gm**

# In[125]:


df_gdp = gm[['Country', 'Year', 'gdp']]
df_gdp.columns = ['country', 'year', 'gdp']
df_gdp.head()


# - Finalmente tenemos dos DataFrames que consisten en lo siguiente: Las emisiones de dióxido de carbono y el PIB. Combine los dos **DataFrames** utilizando la función **.merge()** en las columnas país y año. Guarde esto en un nuevo **DataFrame** llamado data. Utilice la función **dropna()** para eliminar los valores **NaN**

# In[126]:


data = pd.merge(df_co2, df_gdp, on=['country', 'year'], how='left')
data = data.dropna()
data.head()


# - Por último, comprobemos la correlación entre las emisiones de dióxido de carbono y el PIB para asegurarnos de que estamos analizando datos que merecen ser visualizados. Crea un array `numpy` con las columnas **co2** y **gdp**:

# In[127]:


np_co2 = np.array(data['co2'])
np_gdp = np.array(data['gdp'])


# - Utilice la función `.corrcoef()` para imprimir la correlación entre las emisiones de y el **PIB**:

# In[128]:


np.corrcoef(np_co2, np_gdp)


# - Como se puede ver en el resultado anterior, hay una alta correlación entre las emisiones de dióxido de carbono y el **PIB**.

# #### Ejercicio 23: Creación del gráfico estático base para una visualización de datos interactiva

# - En este ejercicio, vamos a crear un gráfico estático para nuestro conjunto de datos y a añadirle glifos circulares circulares. Los siguientes pasos te ayudarán con la solución:

# - Import the following:
#     + `curdoc` de `bokeh.io`: Esto devuelve el estado actual por defecto del documento/ gráfico.
#     + La figura de `bokeh.plotting`: Esto crea la figura para el trazado.
#     + **HoverTool, ColumnDataSource, CategoricalColorMapper** y **Slider** de `bokeh.models`: Son herramientas y métodos interactivos para mapear datos de pandas DataFrames a una fuente de datos para su trazado.
#     + **Spectral6** de `bokeh.palettes`: Una paleta de colores para la gráfica.
#     + `widgetbox` y `row` de `bokeh.layouts`: `widgetbox` crea una columna de herramientas predefinidas (incluyendo el zoom), mientras que `row` crea una fila de objetos de diseño `bokeh`, lo que les obliga a tener el mismo **sizing_mode**:

# In[129]:


from bokeh.io import curdoc, output_notebook
from bokeh.models import HoverTool, ColumnDataSource, CategoricalColorMapper, Slider, CustomJS
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row
from ipywidgets import interact
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import column
from bokeh.plotting import Figure, output_file, show


# - Ejecute la función **output_notebook()** para cargar **BokehJS**. Esto es lo que permite que el que se muestre en el notebook:

# In[130]:


output_notebook()


# - Vamos a codificar por colores nuestros puntos de datos (que serán los países individuales) en función de la región a la que pertenecen. Para ello, cree una lista de regiones aplicando la función **.unique()** a la columna región del **DataFrame**. Haga que una lista utilizando el método **.tolist()**:

# In[131]:


regions_list = data.region.unique().tolist()


# - Utilice **CategoricalColorMapper** para asignar un color del paquete **Spectral6** a las diferentes regiones presentes en la lista **regions_list**:

# In[132]:


color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)


# - Utilizando la función `ColumnDataSource` construimos un diccionaro con las variables utlizadas en la grafica el cual llamaremos **source_init**. También crearemos otro que utlizaremos para actualizar la figura no estática por año la cual llamamos **source_last**

# In[133]:


source_init = ColumnDataSource(data={'x': data.gdp[data.year == min(data.year)],
                                     'y': data.co2[data.year == min(data.year)],
                                     'country': data.country[data.year == min(data.year)],
                                     'region': data.region[data.year == min(data.year)],
                                     'year': data.year[data.year == min(data.year)]})


# In[134]:


source_last = ColumnDataSource(data={'x': data.gdp, 'y': data.co2, 'year': data.year})


# - Creamos la figura vacía:
#     - Establece el título como Emisiones de CO2 versus PIB en 1964
#     - Establece el rango del eje x de xmin a xmax
#     - Establece el rango del eje y desde ymin hasta ymax
#     - Establezca el tipo de eje y como logarítmico

# In[135]:


plot = Figure(title='CO2 Emissions vs GDP in 1964', y_axis_type='log')


# - Añadimos glifos circulares a la gráfica:

# In[136]:


plot.circle(x='x', y='y', 
            fill_alpha=0.8, 
            source=source_init, 
            legend_label='region', 
            color=dict(field='region', transform=color_mapper),
            size=7)


# - Establezca la ubicación de la leyenda en la esquina inferior derecha del gráfico, y agregue títulos a los ejes

# In[137]:


plot.legend.location = 'bottom_right'
plot.xaxis.axis_label = 'Income Per Person'
plot.yaxis.axis_label = 'CO2 Emissions (tons per person)'


# #### Ejercicio 24: Añadir una herramienta Hover

# - En este ejercicio, vamos a permitir que el usuario pase por encima de un punto de datos en nuestro gráfico para ver el nombre del país, las emisiones de dióxido de carbono y el PIB. Los siguientes pasos te ayudarán con la solución:
# 

# - Crear una herramienta de rastreo llamada hover. Añade la herramienta hover a la gráfica

# In[138]:


hover = HoverTool(tooltips=[('Country', '@country'), ('GDP', '@x'), ('CO2 Emission', '@y')])
plot.add_tools(hover)


# In[139]:


show(plot)


# #### Ejercicio 24: Añadir un deslizador al gráfico estático

# - Nombramos el archivo **HTML** de salida como **co2_emissions**

# In[140]:


output_file("co2_emissions.html")


# - Creamos la función **callback** usando `CustomJS` de la libreria `bokeh` la cual permitira actualizar nuestra figura. Usamos algunas pocas ordenes en lenguaje `JavaScript`.

# In[141]:


callback = CustomJS(args=dict(source_last=source_last, source_init=source_init), code="""
    var data_init = source_init.data;
    var yr = cb_obj.value;
    var year = source_last.data['year'];
    var x_new = [];
    var y_new = [];
    for(var i = 0; i < year.length; i++) {
        if(year[i] == yr) {
            x_new.push(source_last.data['x'][i]);
            y_new.push(source_last.data['y'][i]);
        }
    }
    data_init['x'] = x_new;
    data_init['y'] = y_new;
    source_init.change.emit();
    """)


# - Construimos el slider que utlizaremos para actualizar las figuras, y realizamos el llamado de la función **callback** que recibirá como input cada año que proviende del slider

# In[142]:


slider = Slider(start=min(data.year), end=max(data.year), step=1, value=min(data.year), title='Year')
slider.js_on_change('value', callback)

layout = column(slider, plot)
show(layout)


# - Como puede ver, en la esquina derecha, hay varias herramientas. Estas son generadas automáticamente por **Bokeh** cuando se crea un gráfico

# ![](figures/Figure324.png)

# Estas herramientas son las siguientes:
# - **Pan**: La herramienta de desplazamiento le permite mover y cambiar la vista de su parcela
# - **Box Zoom**: Le permite ampliar una sección cuadrada concreta de la cuadrado de la parcela
# - **Wheel Zoom**: Le permite acercarse arbitrariamente a cualquier punto del gráfico.
# - **Save Plot**: Permite guardar el gráfico actual.
# - **Reset**: Esto restablece el gráfico y le lleva de vuelta al gráfico original en el que aterrizó. a la parcela original.
# - **Hover**: Creamos una herramienta de hover en nuestra parcela y la programamos para que muestre cierta información. Sin embargo, Bokeh también genera automáticamente una herramienta hover que puede ser activada y desactivada por este icono. Esta herramienta puede no mostrar siempre lo que que queremos, por lo que hemos creado una nosotros mismos.

# ### Visualización interactiva de datos con Plotly Express

# - **Plotly** es una biblioteca de Python muy popular y se utiliza para crear sorprendentes e informativas visualizaciones de datos interactivos. 
# - Es una herramienta de ploteo basada en **JSON**, por lo que cada ploteo está definido por dos objetos JSON - datos y diseño. 
# - El despliegue de una visualización **Plotly** requiere un poco más de esfuerzo que una visualización **Bokeh** porque tenemos que construir una aplicación separada (más comúnmente una aplicación **Flask**) utilizando el marco **Dash**. 
# - En comparación con **Bokeh**, las herramientas y la sintaxis de **Plotly** son mucho más sencillas. Sin embargo, el código que se requiere para crear estas visualizaciones de datos interactivos es un poco más extenso.

# #### Ejercicio 26: Creación de un gráfico de dispersión interactivo

# - En este ejercicio, vamos a crear una visualización de datos interactiva del **DataFrame** que creamos en el ejercicio anterior, de las emisiones de dióxido de carbono y el PIB. Los siguientes pasos te ayudarán con la solución
# - Abra un nuevo cuaderno Jupyter. Importe las siguientes bibliotecas y paquetes:
#     - `pandas`: Para preparar el **DataFrame**
#     - `plotly.express`: Para crear las gráficas

# In[143]:


import pandas as pd
import plotly.express as px


# - Cree el **DataFrame** de emisiones de dióxido de carbono y PIB del ejercicio anterior en este notebook:

# In[144]:


url_co2 = 'https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/co2.csv'
co2 = pd.read_csv(url_co2)
url_gm = 'https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/gapminder.csv'
gm = pd.read_csv(url_gm)

df_gm = gm[['Country', 'region']].drop_duplicates()
df_w_regions = pd.merge(co2, df_gm, left_on='country', right_on='Country', how='inner')
df_w_regions = df_w_regions.drop('Country', axis='columns')
new_co2 = pd.melt(df_w_regions, id_vars=['country', 'region'])
columns = ['country', 'region', 'year', 'co2']
new_co2.columns = columns

df_co2 = new_co2[new_co2['year'].astype('int64') > 1963]
df_co2 = df_co2.sort_values(by=['country', 'year'])
df_co2['year'] = df_co2['year'].astype('int64')
df_gdp = gm[['Country', 'Year', 'gdp']]
df_gdp.columns = ['country', 'year', 'gdp']
data = pd.merge(df_co2, df_gdp, on=['country', 'year'], how='left')
data = data.dropna()

data.head()


# - Guarda los valores mínimo y máximo del **PIB** como **xmin** y **xmax** respectivamente

# In[145]:


xmin, xmax = min(data.gdp), max(data.gdp)


# - Repita el paso 4 para los valores mínimos y máximos de emisión de dióxido de carbono

# In[146]:


ymin, ymax = min(data.co2), max(data.co2)


# - Crea el gráfico de dispersión y guárdalo como **fig**:
#     - El parámetro data será el nombre de nuestro **DataFrame**, es decir, **data**.
#     - Asigna la columna **gdp** al eje **x**.
#     - Asigna la columna **co2** al eje **y**.
#     - Establecer el parámetro **animation_frame** como la columna del año.
#     - Establezca el parámetro **animation_group** como la columna del país.
#     - Establezca el **color** de los puntos de datos como la columna región.
#     - Asigna la columna **country** al parámetro **hover_name**.
#     - Establecer el parámetro **facet_col** como la columna región (esto divide nuestro gráfico en seis columnas, una para cada región).
#     - Establece la anchura como 1579 y la altura como 400.
#     - El eje **x** debe ser logarítmico.
#     - Establezca el parámetro **size_max** como 45.
#     - Asigna el rango del eje **x** y del eje **y** como **xmin, xmax** y **ymin, ymax**, respectivamente

# In[147]:


fig = px.scatter(data, 
                 x="gdp", y="co2", 
                 animation_frame="year",
                 animation_group="country", 
                 color="region", 
                 hover_name="country",
                 facet_col="region", 
                 width=1579, height=400, 
                 log_x=True, 
                 size_max=45,
                 range_x=[xmin,xmax],
                 range_y=[ymin,ymax])


# In[148]:


fig


# **Observaciones**
# - Como puede ver, tenemos un gráfico con seis subplots; uno para cada región. 
# - Cada región está codificada por colores. 
# - Cada subgrupo tiene las emisiones de dióxido de carbono en toneladas por persona como eje **y** la renta por persona en el eje de abscisas. 
# - En la parte inferior del gráfico hay un control deslizante que nos permite comparar la correlación entre las emisiones de dióxido de carbono y la renta por año entre regiones y países por año. 
# - Al pulsar el botón de reproducción en la esquina inferior izquierda, el gráfico progresa automáticamente desde el año 1964 hasta el 2013, mostrándonos cómo los puntos de datos con el tiempo. 
# - También podemos mover manualmente el deslizador
# - Además, podemos pasar el ratón por encima de un punto de datos para obtener más información sobre él
# - Como puede ver, la creación de una visualización de datos interactivos con **Plotly Express** toma muy pocas líneas de código y la sintaxis es fácil de aprender y utilizar. Además de los gráficos de dispersión, la biblioteca biblioteca tiene muchos otros tipos de gráficos que puede utilizar para visualizar interactivamente diferentes tipos de datos los cuales serán estudiandos en las siguientes actividades.

# - *Haga clic en el siguiente enlace para consultar otras gráficas disponibles con*: [`Plotly Express`](https://plotly.com/python/plotly-express/)

# #### Tarea 1.3

# - En esta actividad, trabajará con el mismo conjunto de datos que trabajó en los ejercicios de este capítulo. Es importante que pruebes varios tipos de visualización para para determinar la visualización que mejor transmite el mensaje que está tratando de dar con sus datos. Vamos a crear algunas visualizaciones interactivas utilizando la biblioteca **`Plotly Express`** para determinar cuál es la que mejor se adapta a nuestros datos.
#     1. Vuelve a crear el **DataFrame** de las emisiones de dióxido de carbono y del PIB.
#     2. Crea un gráfico de dispersión con los ejes **x** e **y** como **year** y **co2** respectivamente. Añada un para los valores de **co2** con el parámetro **marginaly_y**.
#     3. Crea un gráfico de caja para los valores del PIB con el parámetro **marginal_x**. Añada los parámetros de parámetros de animación en la columna del año
#     4. Crea un gráfico de dispersión con los ejes **x** e **y** como **gdp** y **co2** respectivamente.
#     5. Cree un contorno de densidad con los ejes **x** e **y** como **pib** y **co2** respectivamente.

# **Resumen**
# - En este capítulo, hemos aprendido que las visualizaciones de datos interactivas están un paso por delante de las de las visualizaciones de datos estáticas debido a su capacidad para responder a las entradas humanas en tiempo real.
# - La gama de aplicaciones de las visualizaciones de datos interactivas es muy amplia, y podemos visualizar casi cualquier tipo de datos de forma interactiva.
# - Las entradas humanas que pueden incorporarse a las visualizaciones de datos interactivas incluyen, pero no se limitan a los controles deslizantes, las funciones de zoom, las herramientas de desplazamiento y los parámetros en los que se puede hacer clic.
# - `Bokeh` y `Plotly Express` son dos de las bibliotecas de `Python` más populares y sencillas para crear visualizaciones de datos interactivas. 
# - En la proxima sección, veremos cómo crear hermosas visualizaciones de datos interactivas basadas en el contexto.

# ## Visualización de datos a través de estratos

# **Objetivos**
# 
# - Crear interactividad en los gráficos de dispersión utilizando altair
# - Utilizar el zoom in y out, hover y tooltip, y seleccionar y resaltar en los gráficos de dispersión
# - Crear gráficos de barras y mapas de calor interactivos
# - Crear enlaces dinámicos entre diferentes tipos de gráficos dentro de una única visualización interactiva
# 
# En este capítulo, aprenderá a crear visualizaciones interactivas para datos estratificados con respecto a cualquier variable categórica.

# ### Introducción

# - Una observación hecha en la sección anterior fue que cuando cuando se trata de introducir interactividad en ciertos tipos de gráficos de **Python**, `plotly` puede a veces ser verboso, y puede implicar una curva de aprendizaje empinada. Por lo tanto, en este capítulo, presentaremos `altair`, una biblioteca diseñada especialmente para generar gráficos interactivos. - Demostraremos cómo crear visualizaciones interactivas con `altair` para datos estratificados con respecto a cualquier variable categórica. A modo de ilustración, utilizaremos un conjunto de datos para generar gráficos de dispersión y de barras con las características del conjunto de datos y añadir una variedad de elementos interactivos a los gráficos. También conoceremos algunas ventajas específicas del uso de `altair` sobre una biblioteca más polivalente como `plotly`.
# - Utilizaremos el conjunto de datos del Índice de Felicidad Planetaria (IPH) http://happyplanetindex.org/ a lo largo de esta sección. Este conjunto de datos muestra en qué lugares del mundo la gente utiliza recursos ecológicos de forma más eficiente para vivir una vida larga y feliz. No sólo es un recurso interesante para conocer mejor las condiciones ecológicas y el bienestar socioeconómico de bienestar socioeconómico en varias partes de nuestro planeta, sino que también tiene una interesante mezcla de características que nos ayudan a demostrar ciertos conceptos clave de la visualización interactiva.

# ### Gráficos de dispersión interactivos

# - Como ya sabe, los gráficos de dispersión son uno de los tipos de gráficos más esenciales para presentar patrones globales dentro de un conjunto de datos. Naturalmente, es importante saber cómo introducir la interactividad en estos gráficos. En primer lugar, veremos las acciones de zoom y restablecimiento de los gráficos. Antes de eso, sin embargo, vamos a echar un vistazo al conjunto de datos. Podemos ver el conjunto de datos del **IPH** utilizando el siguiente código

# In[149]:


import pandas as pd

hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')
hpi_df.head()


# - Tenga en cuenta que hay 5 características numéricas/cuantitativas en este conjunto de datos: 
#     - **Life Expectancy (years)**
#     - **Wellbeing (0-10)**
#     - **Inequality of outcomes**
#     - **Ecological Footprint (gha/capita)**
#     - **Happy Planet Index**
# - Hay dos características categóricas/nominales: Country y Region. En `altair` los rasgos cuantitativos se denotan como **Q**, y los rasgos nominales se denotan como **N**. Veremos pronto cómo utilizar esto en nuestras visualizaciones.
# - Generemos y observemos un gráfico de dispersión estático, mediante un ejercicio, de las caracteristicas **Wellbeing (0-10)** and **Happy Planet Index** para cada país, utilizando diferentes colores para denotar la región a la que pertenece el país y seguir adelante y añadirle interactividad.

# #### Ejercicio 27: Añadir Zoom-In y Zoom-Out a un gráfico de dispersión estático

# - En este ejercicio, generaremos un gráfico de dispersión estático utilizando `matplotlib`. Utilizaremos el conjunto de datos **hpi_data_countries** para el gráfico y analizaremos las puntuaciones de **Wellbeing** de cada país representado por la leyenda del gráfico. Seguiremos adelante y añadiremos una función de `zoom`. Para ello utilizaremos la biblioteca `altair`.

# - Cargar el conjunto de datos **hpi** y leer desde el conjunto de datos usando pandas:

# In[150]:


import pandas as pd

hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')


# - Trazar un gráfico de dispersión estático utilizando `matplotlib`

# In[151]:


import seaborn as sns
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax = sns.scatterplot(x='Wellbeing (0-10)', y='Happy Planet Index', hue='Region', data=hpi_df)
plt.show()


# - Cada punto representa un país de una de las 7 regiones. El **Wellbeing** y el **Happy Planet Index** parecen estar correlacionados. Vemos una tendencia en las puntuaciones del **Happy Planet Index** y las puntuaciones de **Wellbeing** de las distintas regiones. Ahora que tenemos un gráfico de dispersión estático, vamos a explorar la interactividad de este gráfico. Veremos cómo hacer `zoom in` y `zoom out`.

# - Importa el módulo `altair` como `alt`. Antes debe instalar `altair` usando `pip install altair vega_datasets`. En versiones anteriores de **notebook** (<5.3) es necesario habilitar adicionalmente la extensión: `jupyter nbextension install --sys-prefix --py vega`

# In[152]:


import altair as alt


# - Proporcione el **DataFrame** elegido (**hpi_df** en nuestro caso) a la función `altair Chart`. Utilice la función `mark_circle()` para denotar puntos de datos en el gráfico de dispersión utilizando círculos rellenos.
# - Utilice la función `encode` para especificar las características en los ejes $x$ e $y$. Aunque también usamos el parámetro de `color` en esta función para color-code los puntos de datos usando la característica de la región, esto es opcional. Por último, añada la función `interactive()` para que el gráfico sea interactivo para `zooming`

# In[153]:


alt.Chart(hpi_df).mark_circle().encode(
    x='Wellbeing (0-10):Q',
    y='Happy Planet Index:Q',
    color='Region:N',).interactive()


# - ¿Se ha dado cuenta de que hemos añadido un sufijo: **Q** junto a nuestras características cuantitativas y un sufijo: **N** junto a nuestras características nominales? Añadir sufijos como éste ayuda a altair a conocer el tipo de antemano, en lugar de tener que inferirlo por sí mismo. 
# - Puede intentar eliminar los sufijos en este gráfico y verá que el gráfico se sigue generando sin errores porque altair puede adivinar el tipo de característica en este caso. Es una buena práctica incluir los sufijos ya que hay casos en los que `altair` no puede inferir el tipo de característica.
# - Los diversos parámetros, como $x$, y $y$ el color, que especificamos en la función de codificación son llamados canales en `altair`.

# #### Ejercicio 28: Añadir la funcionalidad Hover y Tooltip a un gráfico de dispersión

# - Cargar el conjunto de datos **hpi** y leer desde el conjunto de datos usando pandas:

# In[154]:


import pandas as pd

hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')


# - Importa el módulo `altair` como `alt`

# In[155]:


import altair as alt


# - Proporcione el `DataFrame` elegido (`hpi_df` en nuestro caso) a la función `altair Chart` de `altair`. Utilice la función `mark_circle()` para indicar los puntos de datos en el gráfico de dispersión de dispersión mediante círculos rellenos. Utilice la función encode para especificar las características en los ejes $x$ y $y$. Aunque utilizamos el parámetro de `color` en esta función para codificar en color los puntos de datos utilizando la característica de región, esto es opcional.

# In[156]:


alt.Chart(hpi_df).mark_circle().encode(
    x = 'Wellbeing (0-10):Q',
    y = 'Happy Planet Index:Q',
    color = 'Region:N',
    tooltip = ['Country', 'Region', 'Wellbeing (0-10)', 'Happy Planet Index', 'Life Expectancy (years)']
)


# - En el gráfico anterior, verá que las características mencionadas en el parámetro "tooltip" de la función de codificación se muestran cuando el cuando el cursor se acerca a cualquier punto de datos. Sin embargo, la función de zoom se ha perdido. ¿Cómo puede recuperarla? Muy sencillo: ¡añada la función `interactive()`!
# - Añade la función `interactive()` para recuperar la función de `zoom` en el gráfico como como se muestra aquí

# In[157]:


alt.Chart(hpi_df).mark_circle().encode(
    x = 'Wellbeing (0-10):Q',
    y = 'Happy Planet Index:Q',
    color = 'Region:N',
    tooltip = ['Country', 'Region', 'Wellbeing (0-10)', 'Happy Planet Index', 'Life Expectancy (years)']
).interactive()


# - Consideremos ahora un escenario más interesante. Supongamos que queremos seleccionar un área en el gráfico para examinar los puntos de datos dentro de ella

# #### Ejercicio 29: Explorar la funcionalidad de seleccionar y resaltar en un gráfico de dispersión

# - En este ejercicio, vamos a utilizar la funcionalidad de seleccionar y resaltar utilizando `altair`. Nosotros podemos hacer esto usando una función llamada `add_selection`. Primero tenemos que definir una variable que almacenará un intervalo de selección y luego generar el gráfico al que queremos añadir la función de selección. En el gráfico resultante, podemos hacer clic y luego arrastrar el cursor para crear un área de selección, que se coloreará de gris. Sigamos los siguientes pasos para hacerlo

# - Cargar el conjunto de datos **hpi** y leer desde el conjunto de datos usando pandas:

# In[158]:


import pandas as pd

hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')


# - Importa el módulo `altair` como `alt`

# In[159]:


import altair as alt


# - Defina la variable `selected_area` para almacenar el intervalo de selección

# In[160]:


selected_area = alt.selection_interval()


# - Proporcione el `DataFrame` elegido (`hpi_df` en nuestro caso) a la función `altair Chart` de `altair`
# - Utilice la función `mark_circle()` para denotar puntos de datos en el gráfico de dispersión utilizando círculos rellenos. Utilice la función `encode` para especificar las características en los ejes $x$ e y $y$. Aunque hemos utilizado el parámetro de color en esta función para colorear los puntos de datos utilizando la característica de región, esto es opcional. Utilice la función `add_selection()` para especificar el área seleccionada

# In[161]:


alt.Chart(hpi_df).mark_circle().encode(
    x = 'Wellbeing (0-10):Q',
    y = 'Happy Planet Index:Q',
    color = 'Region:N'
).add_selection(
    selected_area
)


# - Añade `alt_value` como `lightgray` para que todos los puntos fuera de la selección sean grises

# In[162]:


selected_area = alt.selection_interval()
alt.Chart(hpi_df).mark_circle().encode(
    x = 'Wellbeing (0-10):Q',
    y = 'Happy Planet Index:Q',
    color = alt.condition(selected_area, 'Region:N', alt.value('lightgray'))
).add_selection(
    selected_area
)


# - Establecemos el parámetro de `color` en la función de codificación a una condición de `altair` que retiene los colores de sólo los puntos dentro del área seleccionada. Esto puede ser útil cuando se desea obtener información sobre un rango particular de características en los ejes de un gráfico de dispersión.

# #### Ejercicio 30: Generación de un trazado con las funciones de selección, zoom y hover/hoja de cálculo

# - En este ejercicio, seguiremos trabajando con el conjunto de datos del **Happy Planet Index**.  La tarea de tarea consiste en crear un gráfico de dispersión para **Well-being** vs **Happy Planet Index** y hacer `zoom` en el área con un alto **Well-being** y un alto **Happy Planet index**. Tendrá que determinar qué región predomina en el área de selección y, a continuación, enumerar los países de la zona. Sigamos los siguientes pasos:

# - Cargar el conjunto de datos **hpi** y leer desde el conjunto de datos usando pandas:

# In[163]:


import pandas as pd

hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')


# - Importa el módulo `altair` como `alt`

# In[164]:


import altair as alt


# - Cree un gráfico de dispersión de `altair` para **Wellbeing** vs **Happy Planet Index** junto con la función de `zoom`, utilizando la función `interactive()`, y haz un `zoom` en el área que incluye el conjunto de puntos de datos en la parte superior derecha

# In[165]:


alt.Chart(hpi_df).mark_circle().encode(
    x = 'Wellbeing (0-10):Q',
    y = 'Happy Planet Index:Q',
    color = 'Region:N'
).interactive()


# - Ahora añada la característica de selección cambiando el parámetro de `color` para incluir la condición de selección de `altair`

# In[166]:


selected_area = alt.selection_interval()
alt.Chart(hpi_df).mark_circle().encode(
    x = 'Wellbeing (0-10):Q',
    y = 'Happy Planet Index:Q',
    color = alt.condition(selected_area, 'Region:N', alt.value('lightgray'))
).interactive().add_selection(
    selected_area
)


# - Obsérvese que la mayoría de los países de la zona de selección (arriba a la derecha) pertenecen a América (de color azul). ¿Esperabas esto basándote en tus conocimientos generales? Añadamos la función para saber qué países aparecen en nuestra área de interés.
# - Añade la función `tooltip` para localizar el área de interés

# In[167]:


selected_area = alt.selection_interval()
alt.Chart(hpi_df).mark_circle().encode(
    x = 'Wellbeing (0-10):Q',
    y = 'Happy Planet Index:Q',
    color=alt.condition(selected_area, 'Region:N', alt.value('lightgray')),
    tooltip= ['Country', 'Region', 'Wellbeing (0-10)', 
              'Happy Planet Index', 'Life Expectancy (years)']
).interactive().add_selection(
    selected_area
)


# - Si pasa el ratón por encima de la zona de interés, verá que los principales países son **Costa Rica, México, Panamá** y **Colombia**. Ahora, pasemos a la siguiente sección para observar cómo se puede utilizar la función de selección a través de múltiples figuras.

# #### Ejercicio 31: Selección a través de múltiples parcelas

# - La función de selección puede ser mucho más potente cuando se vincula a varios gráficos. Consideraremos el ejemplo de dos gráficos de dispersión:
#     - **wellbeing** vs **happy planet index**
#     - **life expectancy** vs **happy planet index**
# - En este ejercicio, vamos a ir paso a paso para generar un gráfico interactivo. Para nuestro primer gráfico de dispersión, ya que queremos que el eje y sea común en ambos gráficos, especificaremos sólo el eje $y$ en la función de codificación de nuestro gráfico de `altair`, y luego añadiremos las características del eje $x$ por separado en el objeto `Chart`. Además, para poner los dos gráficos uno detrás de otro y permitir la selección entre ellos, utilizaremos la función `altair` `vconcat`

# - Cargar el conjunto de datos **hpi** y leer desde el conjunto de datos usando pandas:

# In[168]:


import pandas as pd

hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')


# - Importa el módulo `altair` como `alt`

# In[169]:


import altair as alt


# - Trace el gráfico de dispersión con la función `Chart altair vconcat` para colocar dos gráficos verticalmente uno tras otro

# In[170]:


chart = alt.Chart(hpi_df).mark_circle().encode(
    y='Happy Planet Index',
    color='Region:N'
)
chart1 = chart.encode(x = 'Wellbeing (0-10)')
chart2 = chart.encode(x = 'Life Expectancy (years)')
alt.vconcat(chart1, chart2)


# - Por cierto, existen atajos para las funciones `hconcat` y `vconcat`. Podemos sustituir `alt.hconcat(chart1, chart2)` por `chart1 | chart2` y `alt.vconcat(chart1, chart2)` por `chart1 & chart2`
# - Añade las funciones `hover` y `tooltip` que enlazan los dos gráficos utilizando el siguiente código

# In[171]:


# hover and tooltip across multiple charts
selected_area = alt.selection_interval()
chart = alt.Chart(hpi_df).mark_circle().encode(
    y = 'Happy Planet Index',
    color=alt.condition(selected_area, 'Region', alt.value('lightgray'))
).add_selection(
    selected_area
)
chart1 = chart.encode(x = 'Wellbeing (0-10)')
chart2 = chart.encode(x = 'Life Expectancy (years)')
chart1 | chart2


# - Intente seleccionar un área en cualquiera de las gráficas. Observará que la selección en un gráfico automáticamente lleva a resaltar los mismos puntos de datos en el otro gráfico.

# #### Ejercicio 32: Selección basada en los valores de una característica

# - En este ejercicio, crearemos un gráfico interactivo donde podremos ver los puntos de datos en función de una **Region** determinada. Utilizaremos la función `selection_single()` para obtener un conjunto seleccionado de puntos de datos. Si se estudia el código con atención, se verá que los parámetros de esta función se explican por sí mismos. Para cualquier aclaración, por favor lea sobre ellos en la documentación oficial en 
# https://altair-viz.github.io/user_guide/generated/api/altair.selection_single.html.

# - Importe los módulos de Python necesarios

# In[172]:


import altair as alt
import pandas as pd


# - Lectura del conjunto de datos:

# In[173]:


hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')


# - Cree una variable `input_dropdown` utilizando la función `binding_select()` y establezca el parámetro options en la lista de regiones de nuestro conjunto de datos. Utilice la función `selection_single()` para seleccionar un conjunto de puntos de datos. Utilice la variable de color para almacenar la condición bajo la cual se seleccionarán los puntos de dato

# In[174]:


input_dropdown = alt.binding_select(options = list(set(hpi_df.Region)))
selected_points = alt.selection_single(fields = ['Region'], bind = input_dropdown, name = 'Select')
color = alt.condition(selected_points,
                      alt.Color('Region:N'),
                      alt.value('lightgray'))
alt.Chart(hpi_df).mark_circle().encode(
    x = 'Wellbeing (0-10):Q',
    y = 'Happy Planet Index:Q',
    color = color,
    tooltip='Region:N'
).add_selection(
    selected_points
)


# - El gráfico anterior tiene inicialmente todos sus puntos de datos en color. Sin embargo, al seleccionar un valor para la característica **Region** en el menú desplegable de entrada, observará que los correspondientes países están resaltados en color, mientras que todos los demás países están en gris. En los dos gráficos anteriores, el primero muestra los puntos de datos de la región de **Americas** y el segundo gráfico muestra los puntos de datos de la región **Post-communist**.

# - Ahora que sabemos cómo añadir interactividad a los gráficos de dispersión, vamos a aprender a introducir la interactividad en otros dos tipos de visualización importantes: los gráficos de barras y los mapas de calor

# #### Ejercicio 33: Añadir una función de Zoom-In/Zoom-Out y calcular la media en un gráfico de barras estático

# - En este ejercicio, primero generaremos un simple gráfico de barras (estático) y luego exploraremos la interactividad, como el acercamiento y el alejamiento. A continuación, utilizaremos el mismo gráfico de barras y averiguaremos la media del **Happy Planet Index** de cada región. Utilizaremos la biblioteca `altair` y el conjunto de datos del **Happy Planet Index**

# - Importe los módulos de Python necesarios

# In[175]:


import altair as alt
import pandas as pd


# - Lectura del conjunto de datos:

# In[176]:


hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')


# - Utilice la función `mark_bar()` para señalar puntos de datos en el gráfico de barras. Utilice la función encode para especificar las características en los ejes $x$ e $y$

# In[177]:


mean(hpi_df['Happy Planet Index'])
# hpi_df.head()


# In[178]:


alt.Chart(hpi_df).mark_bar().encode(
    x='Region:N',
    y='mean(Happy Planet Index):Q',
)


# - Sin embargo, el gráfico anterior parece demasiado estrecho. Podemos arreglar esto fácilmente estableciendo el anchura del gráfico a un valor diferente utilizando la función de propiedades. Establezca el ancho a 400 utilizando la función de propiedades para aumentar el ancho del gráfico de barras:

# In[179]:


alt.Chart(hpi_df).mark_bar().encode(
    x = 'Region:N',
    y = 'mean(Happy Planet Index):Q'
).properties(width=400)


# - Utiliza la función `interactive` para zoom in/out:

# In[180]:


import altair as alt

alt.Chart(hpi_df).mark_bar().encode(
    x = 'Region:N',
    y = alt.Y('Happy Planet Index')
).properties(width=400).interactive()


# - Utilice el operador | para mostrar la media del IPH en todas las regiones:

# In[181]:


import altair as alt

bars = alt.Chart(hpi_df).mark_bar().encode(
    x = 'Region:N',
    y = 'mean(Happy Planet Index):Q'
).properties(width=400)

line = alt.Chart(hpi_df).mark_rule(color='firebrick').encode(
    y = 'mean(Happy Planet Index):Q',
    size = alt.SizeValue(3)
)
bars | line


# - No queremos que la línea se coloque junto a nuestro gráfico de barras. La queremos en el gráfico. Entonces, ¿cómo lo hacemos? Para ello, tenemos que utilizar el concepto de capa en `altair`. La idea es crear variables para almacenar el gráfico de barras y el gráfico de líneas, y luego superponerlos uno encima del otro.
# - Add the layer function from the `altair` library

# In[182]:


import altair as alt

bars = alt.Chart().mark_bar().encode(
    x = 'Region:N',
    y = 'mean(Happy Planet Index):Q'
).properties(width=400)

line = alt.Chart().mark_rule(color='firebrick').encode(
    y='mean(Happy Planet Index):Q',
    size = alt.SizeValue(3)
)

alt.layer(bars, line, data=hpi_df)


# - Así pues, ahora sabemos que la media del Índice del Planeta Feliz en todas las regiones es de alrededor de 26. Además, también hay que tener en cuenta que no especificamos el conjunto de datos hasta que utilizamos la función de capa. Es decir, no proporcionamos el conjunto de datos **hpi_df** en la función `Chart()` como es habitual. En su lugar, lo mencionamos en la función de capa con el parámetro **data = hpi_df**. 
# - Ahora que conoce el concepto de estratificación en `altair`, puede confiar en un atajo para ello. Sólo tienes que escribir el código de forma independiente para diferentes parcelas, como lo harías normalmente, y luego utilizar el operador `+`, como se muestra en el siguiente ejemplo

# #### Ejercicio 34: Un atajo alternativo para representar la media en un gráfico de barras

# - En este ejercicio, calcularemos la media del índice **HPI** en un gráfico de barras utilizando un del código utilizado en el Ejercicio 33, añadiendo  cálculo de la media en un gráfico de barras estático.

# In[183]:


import altair as alt

bars = alt.Chart(hpi_df).mark_bar().encode(
    x = 'Region:N',
    y = 'mean(Happy Planet Index):Q',
).properties(width=400)

line = alt.Chart(hpi_df).mark_rule(color = 'firebrick').encode(
    y = 'mean(Happy Planet Index):Q',
    size = alt.SizeValue(3)
)

bars + line


# - Utilice el mecanismo de clic y arrastre utilizando el siguiente código en `altair`. Puede utilizar el mecanismo de clic y arrastre para seleccionar cualquier conjunto de barras y ver cómo la línea que indica la media del **Happy Planet Index** se desplaza en consecuencia.

# In[184]:


import altair as alt

selected_bars = alt.selection(type = 'interval', encodings = ['x'])

bars = alt.Chart(hpi_df).mark_bar().encode(
    x = 'Region:N',
    y = 'mean(Happy Planet Index):Q',
    opacity = alt.condition(selected_bars, alt.OpacityValue(1), alt.OpacityValue(0.7)),
).properties(width=400).add_selection(
    selected_bars
)

line = alt.Chart(hpi_df).mark_rule(color = 'firebrick').encode(
    y = 'mean(Happy Planet Index):Q',
    size = alt.SizeValue(3)

).transform_filter(
    selected_bars
)

bars + line


# #### Ejercicio 35: Añadir una función de zoom en un mapa de calor estático

# - En este ejercicio, utilizaremos `altair` para crear un mapa de calor que indique el número de países con el **IPH** y el **Wellbeing** en varios rangos. A continuación, añadiremos la función de zoom al mapa. También añadiremos círculos en el mapa de calor para mostrar diferentes países. 

# - Importe los módulos de Python necesarios

# In[185]:


import altair as alt
import pandas as pd


# - Lectura del conjunto de datos:

# In[186]:


hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')


# - Proporcione el **DataFrame** elegido (**hpi_df** en nuestro caso) a la función `altair Chart`. Utilice la función `mark_rect()` para indicar los puntos de datos en el gráfico de barras. Utilice la función encode para especificar las características en los ejes $x$ e $y$. Asigne a el parámetro `bin` en **True** para que ajuste automáticamente cada `bin`

# In[187]:


alt.Chart(hpi_df).mark_rect().encode(
    alt.X('Happy Planet Index:Q', bin=True),
    alt.Y('Wellbeing (0-10):Q', bin=True),
    alt.Color('count()', scale=alt.Scale(scheme='greenblue'), legend=alt.Legend(title='Total Countries'))
)


# - Utilice la función `interactive` y añada la capacidad de zoom. Utilice el siguiente código

# In[188]:


alt.Chart(hpi_df).mark_rect().encode(
    alt.X('Happy Planet Index:Q', bin = True),
    alt.Y('Wellbeing (0-10):Q', bin = True),
    alt.Color('count()', scale = alt.Scale(scheme='greenblue'), legend = alt.Legend(title='Total Countries'))
).interactive()


# - Al igual que podemos utilizar una paleta de colores para indicar el número de países en cada celda del mapa de calor, también podemos dibujar círculos de distintos tamaños en un mapa de calor para indicar el número de países. Dibuja círculos en el mapa térmico utilizando la función **heatmap+circles**. Los distintos tamaños de los círculos indican el número de países con un rango de **Wellbeing** variable. 

# In[189]:


heatmap = alt.Chart(hpi_df).mark_rect().encode(
    alt.X('Happy Planet Index:Q', bin=True),
    alt.Y('Wellbeing (0-10):Q', bin=True)
)

circles = heatmap.mark_point().encode(
    alt.ColorValue('lightgray'),
    alt.Size('count()', legend=alt.Legend(title='Records in Selection'))
)
heatmap + circles


# #### Ejercicio 36: Creación de un diagrama de barras y un mapa de calor contiguos

# - En este ejercicio, seguiremos trabajando con el conjunto de datos del IPH. El objetivo es dibujar un diagrama de barras que represente el número de países en cada región y un mapa de calor al lado, indicando el número de países en varios rangos de **wellbeing** y **life-expectancy**

# - Importe los módulos de Python necesarios

# In[190]:


import altair as alt
import pandas as pd


# - Lectura del conjunto de datos:

# In[191]:


hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')


# - Genere el gráfico de barras requerido utilizando la función `mark_bar()`

# In[192]:


alt.Chart(hpi_df).mark_bar().encode(
    x = 'Region:N',
    y = 'count():Q'
).properties(width=350)


# - Genera el mapa de calor requerido utilizando la función `mark_rect()`

# In[193]:


alt.Chart(hpi_df).mark_rect().encode(
    alt.X('Wellbeing (0-10):Q', bin = True),
    alt.Y('Life Expectancy (years):Q', bin = True),
    alt.Color('count()', scale=alt.Scale(scheme='greenblue'), legend=alt.Legend(title='Total Countries'))
).properties(width=350)


# - Combine el código para colocar el gráfico de barras y el mapa de calor uno al lado del otro utilizando la función `bars | heatmap`

# In[194]:


bars = alt.Chart(hpi_df).mark_bar().encode(
    x = 'Region:N',
    y = 'count():Q'
).properties(width=350)

heatmap = alt.Chart(hpi_df).mark_rect().encode(
    alt.X('Wellbeing (0-10):Q', bin = True),
    alt.Y('Life Expectancy (years):Q', bin = True),
    alt.Color('count()', scale = alt.Scale(scheme = 'greenblue'), legend = alt.Legend(title = 'Total Countries'))
).properties(width=350)
bars | heatmap


# #### Ejercicio 37: Vincular dinámicamente un gráfico de barras y un mapa de calor

# - En este ejercicio, enlazaremos un gráfico de barras y un mapa de calor de forma dinámica. Considere un escenario en el que desea poder hacer clic en cualquiera de las barras de un gráfico de barras y tener un mapa de calor correspondiente a la región representada por la barra. Así, por ejemplo, quiere actualizar el mapa térmico de la **Life Expectancy** frente al **Well Being** sólo para los países de una región determinada. 

# - Importe los módulos de Python necesarios

# In[195]:


import altair as alt
import pandas as pd


# - Lectura del conjunto de datos:

# In[196]:


hpi_url = "https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/hpi_data_countries.tsv"
hpi_df = pd.read_csv(hpi_url, sep='\t')
hpi_df.head()


# - Seleccione la región mediante el método de `selection`

# In[197]:


selected_region = alt.selection(type="single", encodings=['x'])

heatmap = alt.Chart(hpi_df).mark_rect().encode(
    alt.X('Wellbeing (0-10):Q', bin=True),
    alt.Y('Life Expectancy (years):Q', bin=True),
    alt.Color('count()', scale = alt.Scale(scheme = 'greenblue'), legend = alt.Legend(title = 'Total Countries'))
).properties(
    width=350
)


# - Colocar los círculos en un mapa de calor

# In[198]:


circles = heatmap.mark_point().encode(
    alt.ColorValue('grey'),
    alt.Size('count()', legend = alt.Legend(title='Records in Selection'))
).transform_filter(
    selected_region
)


# - Utilice la función `heatmap+circles | bars` para vincular dinámicamente el gráfico de barras y el mapa de calor

# In[199]:


bars = alt.Chart(hpi_df).mark_bar().encode(
    x = 'Region:N',
    y = 'count()',
    color = alt.condition(selected_region, alt.ColorValue("steelblue"), alt.ColorValue("grey"))
).properties(
    width=350
).add_selection(selected_region)

heatmap + circles | bars


# - Al hacer clic en cada gráfico de barras, verás que la paleta de colores que indica el total de países en de bienestar y esperanza de vida permanece constante, mientras que los círculos los círculos se actualizan para reflejar el número de países en el rango correspondiente para la región seleccionada. 
# - La galería de ejemplos en https://altair-viz.github.io/gallery/index.html le proporcionará con una comprensión aún más profunda de las posibilidades de visualización en `altair`

# - En la sección anterior, presentamos una visión general de algunas formas importantes de añadir interactividad a los gráficos de barras y a los mapas de calor. En concreto, se ha aprendido
#     - Cómo generar un gráfico de barras con la función `altair` `mark_bar()`
#     - Cómo generar un mapa de calor utilizando la función `altair mark_rect()`, y cómo utilizar paletas de colores y círculos para representar visualmente los datos del mapa de calor
#     - Cómo añadir capacidades de zoom a los gráficos de barras y a los mapas de calor utilizando la función función `interactive()`
#     - Cómo utilizar la capacidad de estratificación en `altair` para presentar gráficos uno encima del otro utilizando la función `layer()` o el operador `+`
#     - Cómo enlazar dinámicamente gráficos de barras y mapas de calor para crear una única y atractiva visualización

# #### Tarea 1.4

# - Trabajaremos con el conjunto de datos de **Google Play Store Apps** alojado en [googleplaystore.csv](https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/googleplaystore.csv). Su tarea es crear una visualización con:
#     - Un gráfico de barras de un número de aplicaciones estratificado por cada categoría *Content Rating* (calificado por **Everyone/Teen**).
#     - Un mapa de calor que indica el número de aplicaciones estratificadas por *app Category* y rangos de rangos segmentados por *Rating*. El usuario debe poder interactuar con el gráfico seleccionando cualquiera de los tipos de **Content Rating** y el cambio correspondiente debería reflejarse en el mapa de calor para incluir sólo el número de aplicaciones en la categoría *Content Rating*.

# - Pasos principales
#     - Descargue el conjunto de datos [googleplaystore.csv](https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/googleplaystore.csv) y formatéelo como un `pandas` `DataFrame`
#     - Elimina las entradas del `DataFrame` que tienen valores de característica de `NA`.
#     - Cree el gráfico de barras necesario del número de aplicaciones en cada categoría **Content Rating**
#     - Cree el mapa de calor necesario indicando el número de aplicaciones en la app en rangos **Category** y **Rating**
#     - Combine el código del gráfico de barras y del mapa de calor y cree una visualización con ambos gráficos vinculados dinámicamente entre sí.
#     - Interprete cada visualización

# - Algunas visualizaciones esperadas

# In[200]:


df = pd.read_csv("https://raw.githubusercontent.com/lihkir/Uninorte/main/AppliedStatisticMS/DataVisualizationRPython/Lectures/Python/PythonDataSets/googleplaystore.csv")
df.head()


# ![](figures/Figure1_430.png)
