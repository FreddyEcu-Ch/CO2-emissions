# Import Python Libraries
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.express as px
#from sqlalchemy import create_engine
#from pandas_profiling import ProfileReport
from matplotlib import ticker
#sns.set_style('white')

# from streamlit_option_menu import option_menu

# Desing of the app
st.set_page_config(page_title="CCUS app")
# Create title of web app
st.title("CO2 Emissions App")


# List of options
options = st.sidebar.radio(
    "Choose your option",
    ("Home", "Refineries data", "Thermal plants data", "Surface Facilities"),
)

if options == "Home":
    st.text("El problema decisivo de nuestro tiempo sigue siendo el brutal cambio climático. Los \ncinco años más cálidos desde que comenzó el registro fueron los últimos. La \nproducción de gases de efecto invernadero (GEI), principalmente CO2, CH, N2O y gases \nfluorados, está aumentando exponencialmente con el tiempo. Como resultado, la \ntemperatura global promedio ha aumentado 1,1 °C en comparación con los niveles \npreindustriales. El CO2, el gas de efecto invernadero más prevalente, ha aumentado \nsus emisiones globales de 2 Gt/año en 1990 a 35 Gt/año en 2010. Tres factores \nprincipales que explican este aumento de las emisiones de gases de efecto \ninvernadero son el crecimiento de la población, la expansión económica mundial y la \nreducción de la capacidad ambiental para absorber, reflejar y liberar CO2. \n(Rubén et al., 2021)")
    st.text("Para reducir las emisiones globales de CO2, la captura, uso y almacenamiento de \ncarbono (CCUS) se ha convertido en una posible estrategia complementaria. Por un \nlado, el CO2 queda atrapado, reduciendo su papel en el cambio climático. El plan \nCCUS consta de cuatro fases: recolección, transporte, almacenamiento y uso. ")
    # Load video
    video = open("resources/ccus.mp4", "rb")
    st.video(video)
    st.caption("*CCUS Value Chain*")
    st.header("""-**General Objetive:** """)
    st.text("Recopilación de información de emisiones de CO2 de facilidades petroleras utilizando \ninformación de fuentes gubernamentales, para diseño de un aplicativo web que permita \nvisualizar las tendencias de emisiones de estas fuentes estacionarias con la \nfinalidad de evaluar la factibilidad del uso de estas emisiones en un proyecto CCUS.")
    st.header("-Specific Objetives")
    st.text("Identificar los distintos factores de emisión que se pueden hallar dentro de las \nfacilidades petroleras.")
    st.text("Determinar y utilizar el lenguaje de programación que mejor se acomode para la \npresentación de los datos de las emisiones de CO2.")
    st.header("""-**Methodology:**""")
    st.text("Con la ayuda de entidades gubernamentales y a una previa investigación se hallarán \nlos datos de las emisiones de CO2 dentro de las facilidades petroleras de los campos \ndestinados a investigar, y mostrarlos de forma preliminar en tablas tabuladas para \nposteriormente ser cargada al aplicativo web. ")
    st.text("Emisiones por Venteo: son emisiones de gases de efecto invernadero liberados a la \natmósfera. Estos gases pueden ser liberado intencionadamente, en procesos o \nactividades que están diseñados para ventear gas, o de forma no intencionada, en \ncaso de fallos o por un mal funcionamiento de los equipos. Entre los equipos que \npueden liberar estas emisiones tenemos:")
    st.text("•	Tanques	de	almacenamiento	de	líquidos	producidos,	como \n        condensado, petróleo crudo.\n•	Compresores.\n•	Deshidratadores de glicol.\n•	Cabezal de pozo.")
    st.text("Entre las actividades que liberan emisiones de venteo tenemos:")
    st.text("•	Terminaciones de pozo.\n•	Extracción de líquidos en pozos de gas.")
    st.text("Las emisiones de gases de efecto invernadero se cuantifican y expresan como un \ncaudal, masa por unidad de tiempo, y puede ser estimado mediante cálculos de \ningeniería, por medición directa de las fuentes de emisión, o mediante el uso de \nmodelos. Las emisiones de venteo se cuantifican en base a los métodos siguientes, \nenumerados a continuación en orden creciente de precisión y fiabilidad.(Change, n.d.)")
    image_venteo = Image.open("resources/emisiones_venteo.jpg")
    st.image(image_venteo)
    st.caption("*Pueden existir emisiones por vento en distintas partes en las facilidades de superficie*")
    st.text("Emisiones por Quemado: Para evitar riesgos, el gas amargo rechazado es enviado a \nquemadores  elevados tipo antorcha. Como resultado de lacombustión del gas amargo, \ndemás de CO2 y agua, se emite bióxido de azufre (SO2), óxidos de nitrógeno (NOx), \npartículas suspendidas (PS), monóxido de carbono (CO), compuestos orgánicos no \nquemados y H2S no oxidado. Estimados recientes (Villasenor et al., 2003), indican \nque cerca del 82% del total de contaminantes emitidos a la atmósfera proviene de \nestas operaciones de quemado de gas. Para la estimación de las emisiones de CO2 se \ntrabaja con la fórmula de emisiones del IPCC ya que no se obtienes muchas medidas \ndirectas en estas emisiones.")
    image_quemado = Image.open("resources/emisiones_quemado.jpg")
    st.image(image_quemado)
    st.caption("*Actividad en la industria petrolera que provoca emisiones por quemado*")
    st.text("Emisiones fugitivas: En general, la cantidad de emisiones fugitivas provenientes de \nactividades que involucran petróleo o gas no muestra una correlación directa con los \nniveles de producción o los rendimientos del sistema. Está más relacionada con la \ncantidad, tipo y antigüedad de la infraestructura del proceso (es decir, el equipo), \nlas características de los hidrocarburos que se producen procesan o manipulan, el \ndiseño industrial y las prácticas de operación y mantenimiento. En general, la \ncantidad relativa de emisiones fugitivas depende de muchos factores, pero estas \ntienden a aumentar cuanto más se retrocede en la cadena de procesado del sistema y \ndisminuyen con la concentración de ácido sulfhídrico (H2S) en el petróleo y el gas \nproducidos. En general, el gas y el petróleo crudo contienen una combinación de \nhidrocarburos y varias impurezas, entre las cuales se encuentran H2O, N2, Ar, H2S y \nCO2. Si el gas natural contiene más de 10 ppmv de H2S, se denomina normalmente \n«gas ácido»; de lo contrario, se denomina «gas dulce». Las impurezas se eliminan por \nmedio de procesamiento, tratamiento o refinamiento, según sea lo más adecuado. El \nCO2 crudo que se elimina de los hidrocarburos en general se ventea a la atmósfera y \nconstituye una fuente de emisiones fugitivas.(Change, n.d.)")
    image_fugitiva = Image.open("resources/emisiones_fugitivas.jpg")
    st.image(image_fugitiva)
    st.caption("*Emisiones fugitivas que se pueden producir en los equipos de facilidades petroleras*")
    st.header("""-Expected Results""")
    st.text("Mediante la creación y uso de la aplicación web creada se espera poder presentar los \ndatos de las emisiones de CO2 de manera más atractiva y representativa para que los \ndatos puedan ser evaluados y determinar si son aptos para futuros Proyectos CCUS.")
    st.text("El acogimiento de la herramienta y el impulso a la comunidad en ampliar su interés \nen representar futuros proyectos con ayuda de herramientas de lenguaje de \nprogramación como una alternativa llamativa y colaborativa en proyectos de mayor \ngrado.")
    st.header("Conclusions")
    st.text("Gracias al uso de la herramienta de lenguaje de programación Python se podrá \nrepresentar los datos de las emisiones de CO2 y cargarlo a la plataforma de Github \ndonde cualquier persona ya sea investigadora o natural pueda tener conocimiento \nacerca de las emisiones que se producen en los campos de estudio, al mismo tiempo \ntenemos que estas personas si están interesadas en el proyecto o quieren aportar \nmayor información recopilada pueden añadir datos de más fuentes de emisión \nestacionarias ya que el aplicativo queda abierto a mayor aportaciones.")
    # Load image
    image = Image.open("resources/ccs.jpg")
    st.image(image)
    st.caption("*CCUS Framework*")

if options == "Refineries data":
    %config Completer.use_jedi = False
    engine = create_engine('Refineries:///CO2_EOR.db')

    df = pd.read_sql_query("SELECT* FROM R_Shushufindi", engine)
    df.head()
    df.columns