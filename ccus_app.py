# Import Python Libraries
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.express as px
from sqlalchemy import create_engine
from matplotlib import ticker
from matplotlib.ticker import AutoMinorLocator
#sns.set_style('white')

from streamlit_option_menu import option_menu

# Desing of the app
st.set_page_config(page_title="CCUS app")
# Create title of web app
st.title("CO2 Emissions App")


# List of options
#options = st.sidebar.radio(
#    "Choose your option",
#    ("Home", "Refineries data", "Thermal plants data", "Surface Facilities"),
#)

#MENU DE OPCIONES PRINCIPAL

with st.sidebar:
    options = option_menu(menu_title="main menu",options=["Home", "Refineries data", "Thermal plants data", "Surface Facilities"],icons=["house","clipboard-data","tv","calculator"])

#OPCION HOME
if options == "Home":

    #INTRODUCCION
    st.markdown("El problema decisivo de nuestro tiempo sigue siendo el brutal cambio climático. Los cinco años más cálidos desde que comenzó el registro fueron los últimos. La producción de gases de efecto invernadero (GEI), principalmente CO2, CH, N2O y gases fluorados, está aumentando exponencialmente con el tiempo. Como resultado, la temperatura global promedio ha aumentado 1,1 °C en comparación con los niveles preindustriales. El CO2, el gas de efecto invernadero más prevalente, ha aumentado sus emisiones globales de 2 Gt/año en 1990 a 35 Gt/año en 2010. Tres factores principales que explican este aumento de las emisiones de gases de efecto invernadero son el crecimiento de la población, la expansión económica mundial y la reducción de la capacidad ambiental para absorber, reflejar y liberar CO2. (Rubén et al., 2021)")
    st.markdown("Para reducir las emisiones globales de CO2, la captura, uso y almacenamiento de carbono (CCUS) se ha convertido en una posible estrategia complementaria. Por un lado, el CO2 queda atrapado, reduciendo su papel en el cambio climático. El plan CCUS consta de cuatro fases: recolección, transporte, almacenamiento y uso. ")
    # Load video
    video = open("resources/ccus.mp4", "rb")
    st.video(video)
    st.caption("*CCUS Value Chain.*")

    #OBJETIVO GENERAL
    st.header("""-**Objetivo General:** """)
    st.markdown("Recopilación de información de emisiones de CO2 de facilidades petroleras utilizando información de fuentes gubernamentales, para diseño de un aplicativo web que permita visualizar las tendencias de emisiones de estas fuentes estacionarias con la finalidad de evaluar la factibilidad del uso de estas emisiones en un proyecto CCUS.")

    #OBJETIVOS ESPECIFICOS
    st.header("-Objetivos Específicos")
    st.markdown("Identificar los distintos factores de emisión que se pueden hallar dentro de las facilidades petroleras.")
    st.markdown("Determinar y utilizar el lenguaje de programación que mejor se acomode para la presentación de los datos de las emisiones de CO2.")

    #METODOLOGIA
    st.header("""-**Metodología:**""")
    st.markdown("Con la ayuda de entidades gubernamentales y a una previa investigación se hallarán los datos de las emisiones de CO2 dentro de las facilidades petroleras de los campos destinados a investigar, y mostrarlos de forma preliminar en tablas tabuladas para posteriormente ser cargada al aplicativo web. ")
    st.markdown("Emisiones por Venteo: son emisiones de gases de efecto invernadero liberados a la atmósfera. Estos gases pueden ser liberado intencionadamente, en procesos o actividades que están diseñados para ventear gas, o de forma no intencionada, en caso de fallos o por un mal funcionamiento de los equipos. Entre los equipos que pueden liberar estas emisiones tenemos:")
    st.markdown("•Tanques	de	almacenamiento	de	líquidos	producidos,	como condensado, petróleo crudo.")
    st.markdown("•Compresores.")
    st.markdown("•	Deshidratadores de glicol.")
    st.markdown("•	Cabezal de pozo.")
    st.markdown("Entre las actividades que liberan emisiones de venteo tenemos:")
    st.markdown("•	Terminaciones de pozo.")
    st.markdown("•	Extracción de líquidos en pozos de gas.")
    st.markdown("Las emisiones de gases de efecto invernadero se cuantifican y expresan como un caudal, masa por unidad de tiempo, y puede ser estimado mediante cálculos de ingeniería, por medición directa de las fuentes de emisión, o mediante el uso de modelos. Las emisiones de venteo se cuantifican en base a los métodos siguientes, enumerados a continuación en orden creciente de precisión y fiabilidad.(Change, n.d.)")
    image_venteo = Image.open("resources/emisiones_venteo.jpg")
    st.image(image_venteo)
    st.caption("*Pueden existir emisiones por vento en distintas partes en las facilidades de superficie.*")
    st.markdown("Emisiones por Quemado: Para evitar riesgos, el gas amargo rechazado es enviado a quemadores  elevados tipo antorcha. Como resultado de la combustión del gas amargo, además de CO2 y agua, se emite bióxido de azufre (SO2), óxidos de nitrógeno (NOx), partículas suspendidas (PS), monóxido de carbono (CO), compuestos orgánicos no quemados y H2S no oxidado. Estimados recientes (Villasenor et al., 2003), indican que cerca del 82% del total de contaminantes emitidos a la atmósfera proviene de estas operaciones de quemado de gas. Para la estimación de las emisiones de CO2 se trabaja con la fórmula de emisiones del IPCC ya que no se obtienes muchas medidas directas en estas emisiones.")
    image_quemado = Image.open("resources/emisiones_quemado.jpg")
    st.image(image_quemado)
    st.caption("*Actividad en la industria petrolera que provoca emisiones por quemado.*")
    st.markdown("Emisiones fugitivas: En general, la cantidad de emisiones fugitivas provenientes de actividades que involucran petróleo o gas no muestra una correlación directa con los niveles de producción o los rendimientos del sistema. Está más relacionada con la cantidad, tipo y antigüedad de la infraestructura del proceso (es decir, el equipo), las características de los hidrocarburos que se producen procesan o manipulan, el diseño industrial y las prácticas de operación y mantenimiento. En general, la cantidad relativa de emisiones fugitivas depende de muchos factores, pero estas tienden a aumentar cuanto más se retrocede en la cadena de procesado del sistema y disminuyen con la concentración de ácido sulfhídrico (H2S) en el petróleo y el gas producidos. En general, el gas y el petróleo crudo contienen una combinación de hidrocarburos y varias impurezas, entre las cuales se encuentran H2O, N2, Ar, H2S y CO2. Si el gas natural contiene más de 10 ppmv de H2S, se denomina normalmente «gas ácido»; de lo contrario, se denomina «gas dulce». Las impurezas se eliminan por medio de procesamiento, tratamiento o refinamiento, según sea lo más adecuado. El CO2 crudo que se elimina de los hidrocarburos en general se ventea a la atmósfera y constituye una fuente de emisiones fugitivas.(Change, n.d.)")
    image_fugitiva = Image.open("resources/emisiones_fugitivas.jpg")
    st.image(image_fugitiva)
    st.caption("*Emisiones fugitivas que se pueden producir en los equipos de facilidades petroleras.*")

    #RESULTADOS ESPERADOS
    st.header("""-Resultados Esperados""")
    st.markdown("Mediante la creación y uso de la aplicación web creada se espera poder presentar los datos de las emisiones de CO2 de manera más atractiva y representativa para que los datos puedan ser evaluados y determinar si son aptos para futuros Proyectos CCUS.")
    st.markdown("El acogimiento de la herramienta y el impulso a la comunidad en ampliar su interés en representar futuros proyectos con ayuda de herramientas de lenguaje de programación como una alternativa llamativa y colaborativa en proyectos de mayor grado.")

    #CONCLUSIONES
    st.header("Conclusiones")
    st.markdown("Gracias al uso de la herramienta de lenguaje de programación Python se podrá representar los datos de las emisiones de CO2 y cargarlo a la plataforma de Github donde cualquier persona ya sea investigadora o natural pueda tener conocimiento acerca de las emisiones que se producen en los campos de estudio, al mismo tiempo tenemos que estas personas si están interesadas en el proyecto o quieren aportar mayor información recopilada pueden añadir datos de más fuentes de emisión estacionarias ya que el aplicativo queda abierto a mayor aportaciones.")
    # Load image
    image = Image.open("resources/ccs.jpg")
    st.image(image)
    st.caption("*CCUS Framework.*")

#OPCION REFINIRIES DATA
if options == "Refineries data":
    #LLAMADO DE LA DATA REFINERIA SHUSHUFINDI
    st.header("Refineria Shushufindi ")
    st.markdown("La Refinería Shushufindi abastece de gasolina y diésel a las provincias de Sucumbíos, Orellana y Napo, y de GLP a la ciudad de Quito y su zona de influencia. La capacidad de procesamiento de la Refinería Shushufindi, es de 20 mil barriles de crudo por día.")
    st.markdown("A continuación se presenta una base de datos recopilada de entidades gubernamentales sobre las emisiones de CO2 consecuencia de las actividades de refinación del crudo que se maneja dentro de esta fuente de emision estacionaria.")

    engine = create_engine('sqlite:///Refineries/CO2_EOR.db')

    df = pd.read_sql_query("SELECT* FROM R_Shushufindi", engine)
    df
    st.caption("*Base de datos sobre la Refineria Shushuindi del año 2010 al 2020.*")

    #GRAFICO DE BARRAS DE LOS BARRILES REFINADOS SHUSHUFINDI
    st.header("Producción de la Refinería Shushufindi 2010-2020")
    st.markdown("Con la ayuda de un gráfico de barras se puede observar la producción del petróleo refinado y sus variaciones en los años del 2010 al 2020 en unidades de Millones de barriles (MMbbl).")
    fig1, ax = plt.subplots(figsize=(14, 8))

    ax.bar(df['año'], df['RefinacionBarriles'], color='navy')
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Oil refined (MMbbl)', fontsize=14)
    ax.set_title('Oil refined of the refinery Sushufindi',
                 fontname="Times New Roman", size=20, fontweight="bold")
    plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    st.pyplot(fig1)
    st.caption("*Producción Refinería Shushufindi (2010-2020).*")

    #GRAFICO BARRAS EMICIONES CO2 SHUSHUFINDI
    st.header("Emisiones de CO2 producidas en la Refinería Shushufindi 2010-2020.")
    st.markdown("Todo proceso industrial genera emisiones de CO2, en la refinería Shushufinfi se pudo cuantificar estas emisiones provenientes de la producción dentro de la planta en unidades de Toneladas (Ton), las cuales se presentan a continuación:")

    fig2, ax = plt.subplots(figsize=(12, 8))

    ax.bar(df['año'], df['Emisiones_CO2'], color='brown')
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=14)
    ax.set_title(r'$CO_{2}$ emissions of the refinery Sushufindi',
                 fontname="Times New Roman", size=20, fontweight="bold")
    plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    st.pyplot(fig2)
    st.caption("*Emisiones de CO2 emitidas en la Refinería Shushufinfi (2010-2020).*")

    #GRAFICO DE BARRAS DE COMPARATIVA ENTRE LOS BARRILES REFINADOS Y EL CO2 QUE EMITEN
    st.header("Comparativa de la Refinación de Barriles y las Emisiones de CO2 que emiten.")
    st.markdown("Una vez obtenidos los datos de la producción y las emisiones de CO2 que estas actividades producen, podemos compararlas para saber cuantos barriles refinados corresponden a cada tonelada de CO2 emitida.")

    formatter = ticker.EngFormatter()
    fig3 = plt.figure(figsize=(12, 8), edgecolor='black')
    ax1 = fig3.add_subplot()
    ax2 = ax1.twinx()

    ener = df.plot.bar(x='año', y='RefinacionBarriles', width=0.4, color='navy',
                       ax=ax1, align='center', label='Oil refined', position=1)
    emi = df.plot.bar(x='año', y='Emisiones_CO2', width=0.4, color='brown',
                      ax=ax2, align='center', label=r'$CO_{2}$ emissions', position=0)

    ax1.set_xlabel('', fontsize=14)
    ax1.set_ylabel('Oil refined (bbl)', fontsize=16)
    ax2.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=16)
    ax1.tick_params(axis='x', labelsize=14)
    ax1.tick_params(axis='y', labelsize=14)
    ax2.tick_params(axis='y', labelsize=14)
    ax1.yaxis.set_major_formatter(formatter)
    ax2.yaxis.set_major_formatter(formatter)
    ax2.set_ylim(0, 250E3)
    ax1.legend(loc='upper center', fontsize=12)
    ax2.legend(loc='upper right', fontsize=12)
    ax2.grid(visible=False)
    ax1.tick_params(axis='x', labelrotation=0)
    ax1.set_ylim(0, 10E6)
    st.pyplot(fig3)
    st.caption("*Comparación de la producción con las emisiones de CO2 (2010-2020).*")

elif options == "Thermal plants data":

    st.header("Plantas Termoeléctricas")
    st.markdown("Las centrales térmicas convencionales,  también llamadas termoeléctricas convencionales, utilizan combustibles fósiles (gas natural, carbón o fueloil) para generar energía eléctrica mediante un ciclo termodinámico de agua-vapor. El término ‘convencional’ se utiliza para diferenciarlas de otras centrales térmicas, como las de ciclo combinado o las nucleares. ")
    video_ter = open("resources/Termo.mp4", "rb")
    st.video(video_ter)
    st.caption("*Thermal Plants Value Chain*")
    st.markdown("Las centrales térmicas convencionales están compuestas de varios elementos que posibilitan la transformación de los combustibles fósiles en energía eléctrica. Sus componentes principales son:")
    st.markdown("•Caldera: espacio donde el agua se transforma en vapor gracias a la quema de combustible. En este proceso la energía química se transforma en térmica.")
    st.markdown("•Serpentines: cañerías por donde circula el agua que se transforma en vapor. En ellos se produce el intercambio de calor entre los gases de la combustión y el agua.")
    st.markdown("•Turbina de vapor: máquina que recoge el vapor de agua y que, gracias a un complejo sistema de presiones y temperaturas, consigue que se mueva el eje que la atraviesa. Esta turbina normalmente tiene varios cuerpos, de alta, media y baja presión, para aprovechar al máximo el vapor de agua.")
    st.markdown("•Generador: máquina que recoge la energía mecánica generada en el eje que atraviesa la turbina y la transforma en eléctrica mediante inducción electromagnética. Las centrales eléctricas transforman la energía mecánica del eje en una corriente eléctrica trifásica y alterna. El generador conecta el eje que atraviesa los diferentes cuerpos. ")
    image_thermal = Image.open("resources/image_termo.jpeg")
    st.image(image_thermal)
    st.caption("*Instalaciones de centrales o plantas Térmicas*")

    #LLAMADO A LA DATA THERMAL PLANTS
    st.header("Base de datos de Plantas Termoeléctricas en Ecuador 2016-2020.")
    st.markdown("Entre las plantas térmicas en Ecuador enunciamos algunas de las que hemos podido obtener los datos, tanto de la Energía Neta producida y de las emisiones de CO2 que provocan estas actividades, ya que son las variables que más nos interesan en este proyecto.")
    engine = create_engine('sqlite:///Refineries/CO2_EOR.db')
    ter = pd.read_sql_query("SELECT* FROM Datos_termoelectricas", engine)
    ter
    st.caption("*Base de datos de la energía neta producida y las emisiones de CO2 de la plantas termoeléctricas de Ecuador (2016-2020).*")

    #GRAFICO ENGLOBADOS DE LAS PLANTAS TERMNALES Y SUS EMISIONES DE CO2
    st.markdown("Representamos la base de datos en forma de un gráfico de barras para una mejor interpretación de la cantidas de Energía Neta producida y al mismo tiempo observar la cantidad de CO2 que se emiten.")
    fig7 = plt.figure(figsize=(12, 8), edgecolor='black')
    ax1 = fig7.add_subplot()
    ax2 = ax1.twinx()

    ter.groupby(['año', 'Termoelectrica'])['EnergiaBruta(MWH)'].sum().plot(kind='bar', width=0.5, color='seagreen',
                                                                           ax=ax1, label='Net energy')
    ter.groupby(['año', 'Termoelectrica'])['EmisionCO2[Ton]'].sum().plot(kind='bar', width=0.5, color='red',
                                                                         ax=ax2, label=r'$CO_{2}$ emissions')
    ax1.set_xlabel('Year', fontsize=14)
    ax1.set_ylabel('Net energy (MWh)', fontsize=14)
    ax2.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=14)
    ax1.legend(loc='upper center')
    ax2.legend(loc='upper right')
    ax2.grid(visible=False)
    plt.title(r'Energy production and $CO_{2}$ emissions of the thermal plants',
              fontname="Times New Roman", size=20, fontweight="bold")
    st.pyplot(fig7)
    st.caption("*Energía Neta producida y emisiones de CO2 en plantas Termoeléctricas en Ecuador (2016-2020).*")

    #LLAMADO A LA DATA THERMAL PLANTS AMAZONAS
    st.header("Planta Termoeléctrica Amazonas")
    ter_ama = ter[ter['Termoelectrica'] == 'Amazonas']
    ter_ama
    st.caption("*Base de datos de la Energía Neta Producida y las emisiones de CO2 en la Planta Termoeléctrica Amazonas (2016-2020).*")

    #GRAFICO DE LA PRODUCCION DE ENERGIA THERMA PLANT AMAZONAS
    st.subheader("*Energía Neta Producida en la Planta Termoeléctrica Amazonas.*")
    st.markdown("De la base de datos agarrando únicamente la variable de 'Energía Neta' podemos representar de manera gráfica para visualizar de mejor manera cuantos Megavatios-Hora (MWH) la planta termoeléctrica produjo.")
    fig4, ax = plt.subplots(figsize=(12, 8))

    ax.bar(ter_ama['año'], ter_ama['EnergiaBruta(MWH)'], color='seagreen')
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Net energy (MWH)', fontsize=14)
    ax.set_title('Anual energy production of the thermal plant Amazonas',
                 fontname="Times New Roman", size=20, fontweight="bold")
    st.pyplot(fig4)
    st.caption("*Gráfico de barras de la Energía Neta producida en la Planta Termoeléctrica Amazonas (2016-2020).*")

    #GRAFICO DE BARRAS DE LAS EMISIONES DE CO2 EN THERMAL PLANT AMAZONAS
    st.subheader("*Emisiones de CO2 por las actividades realizadas en la Planta Termoeléctrica Amazonas.*")
    st.markdown("Al tratarse de ser una planta termoeléctrica convencional, el combustible se quema en una cladera provocando la energía térmica que se utiliza para calentar el agua , que se transforma en vapor a una presión muy elevada. En este proceso por la quema de combustible tenemos las emisiones de CO2 las cuáles podemos representarlas gráficamente en unidades de Toneladas (Ton). ")
    fig5, ax = plt.subplots(figsize=(12, 8))

    ax.bar(ter_ama['año'], ter_ama['EmisionCO2[Ton]'], color='red')
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=14)
    ax.set_title(r'Anual $CO_{2}$ emissions of the thermal plant Amazonas',
                 fontname="Times New Roman", size=20, fontweight="bold")
    st.pyplot(fig5)
    st.caption("*Gráfico de barras de las Emisiones de CO2 consecuencia de la producción de Energia en la Termoeléctrica Amazonas (2016-2020).*")

    #GRAFICO DE BARRAS DE COMPARATIVA ENTRE LAS PRODUCCION DE ENERGIA Y EMISIONES DE CO2 EN THERMAL PLANT AMAZONAS
    st.subheader("*Comparación entre la Energía Neta producida y las emisiones de CO2 en la pLanta Termoeléctrica Amazonas.*")
    st.markdown("Ya teniendo las dos variables representadas podemos combinarlas en un solo gráfico donde podamos tener una rápida inferencia de la cantidad de CO2 se liberan al momento de producir Energía en la planta termoeléctrica Amazonas.")
    fig6 = plt.figure(figsize=(12, 8), edgecolor='black')
    ax1 = fig6.add_subplot()
    ax2 = ax1.twinx()

    ener = ter_ama.set_index('año')['EnergiaBruta(MWH)'].plot(kind='bar', width=0.4, color='seagreen',
                                                              ax=ax1, align='center', label='Net energy', position=1)
    emi = ter_ama.set_index('año')['EmisionCO2[Ton]'].plot(kind='bar', width=0.4, color='red',
                                                           ax=ax2, align='center', label=r'$CO_{2}$ emissions',
                                                           position=0)
    ax1.set_xlabel('Year', fontsize=14)
    ax1.set_ylabel('Net energy (MWH)', fontsize=14)
    ax2.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=14)
    ax1.legend(loc='upper center')
    ax2.legend(loc='upper right')
    plt.title(r'Energy production and $CO_{2}$ emissions of the thermal plant Amazonas',
              fontname="Times New Roman", size=20, fontweight="bold")
    ax1.tick_params(axis='x', labelrotation=0)
    ax2.grid(visible=False)
    st.pyplot(fig6)
    st.caption("*Comparación directa entre la Energía Neta producida y las emisiones de CO2 en la Planta Termoeléctrica Amazonas (2016-2020).*")

    #LLAMADO A DATA THERMAL PLANT SECOYA
    st.header("Planta Termoeléctrica Secoya")
    st.markdown("Central Térmica Celec Secoya se encuentra en Provincia de Sucumbíos. Esta empresa se desempeña en la siguiente industria: Instalaciones eléctricas.")
    st.markdown("De la base de datos se filtró solo la información de la planta termoeléctrica Secoya para su análisis:")
    ter_se = ter[ter['Termoelectrica'] == 'Secoya'].sort_values(by='año')
    ter_se
    st.caption("*Base de datos de la Planta Termoeléctrica Secoya (2016-2020).*")

    #GRAFICO DE BARRAS DE LA PRODUCCION DE ENERGIA EN LA PLANTA TERMICA SECOYA
    st.subheader("*Energía Neta Producida en la Planta Termoeléctrica Secoya.*")
    st.markdown("De los datos filtrados construimos un gráfico para representar mejor la cantidad de Energía que se produce en la planta termoeléctrica Secoya en unidades de Megavatios-Hora (MWH).")
    fig8, ax = plt.subplots(figsize=(12, 8))

    ax.bar(ter_se['año'], ter_se['EnergiaBruta(MWH)'], color='seagreen')
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Net energy (MWH)', fontsize=14)
    ax.set_title('Anual energy production of the thermal plant Secoya',
                 fontname="Times New Roman", size=20, fontweight="bold")
    st.pyplot(fig8)
    st.caption("*Gráfico de barras de la Energía Neta producida en la Planta Termoeléctrica Secoya (2016-2020).*")

    #GRAFICO DE BARRA DE LAS EMISIONES DE CO2 EN LA PLANTA TERMICA SECOYA
    st.subheader("*Emisiones de CO2 por las actividades realizadas en la Planta Termoeléctrica Secoya.*")
    st.markdown("De igual manera hablamos que se trata de una planta termoeléctrica convencional, donde se quema el combustible para poder producir la Energía por medio de actividades industriales y las emisiones que liberan estos procesos se las puede medir en unidades de Toneladas (Ton).")
    fig9, ax = plt.subplots(figsize=(12, 8))

    ax.bar(ter_se['año'], ter_se['EmisionCO2[Ton]'], color='red')
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=14)
    ax.set_title(r'Anual $CO_{2}$ emissions of the thermal plant Amazonas',
                 fontname="Times New Roman", size=20, fontweight="bold")
    st.pyplot(fig9)
    st.caption("*Gráfico de barras de las Emisiones de CO2 consecuencia de la producción de Energia en la Termoeléctrica Secoya (2016-2020).*")


    #COMPARATIVA DE LA PRODUCCION DE ENERGIA Y LAS EMISIONES DE CO2 EN LA PLANTA TERMICA SECOYA
    st.subheader("*Comparación entre la Energía Neta producida y las emisiones de CO2 en la pLanta Termoeléctrica Secoya.*")
    st.markdown("Al tener representado los datos de las producción de Energía Neta y la de las emisiones de CO2 que ocurren en la planta termoeléctrica, podemos armar un gráfico comparativo para analizarlo de mejor manera como se relacionan estas dos variables.")
    formatter = ticker.EngFormatter()
    fig10 = plt.figure(figsize=(12, 8), edgecolor='black')
    ax1 = fig10.add_subplot()
    ax2 = ax1.twinx()

    ener = ter_se.set_index('año')['EnergiaBruta(MWH)'].plot(kind='bar', width=0.4, color='seagreen',
                                                             ax=ax1, align='center', label='Net energy', position=1)
    emi = ter_se.set_index('año')['EmisionCO2[Ton]'].plot(kind='bar', width=0.4, color='red',
                                                          ax=ax2, align='center', label=r'$CO_{2}$ emissions',
                                                          position=0)
    ax1.set_xlabel('', fontsize=14)
    ax1.set_ylabel('Net energy (MWH)', fontsize=16)
    ax2.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=16)
    ax1.tick_params(axis='x', labelsize=14)
    ax1.tick_params(axis='y', labelsize=14)
    ax2.tick_params(axis='y', labelsize=14)
    ax1.yaxis.set_major_formatter(formatter)
    ax2.yaxis.set_major_formatter(formatter)
    ax1.set_ylim(0, 200E3)
    ax2.set_ylim(0, 200E3)
    ax1.legend(loc='upper center', fontsize=12)
    ax2.legend(loc='upper right', fontsize=12)
    ax1.tick_params(axis='x', labelrotation=0)
    ax2.grid(visible=False)
    st.pyplot(fig10)
    st.caption("*Comparación directa entre la Energía Neta producida y las emisiones de CO2 en la Planta Termoeléctrica Secoya (2016-2020).*")
    #PROMEDIO
    st.header("Presentación de los datos promedio de las Plantas Termoeléctricas.")
    terP = pd.read_sql_query("SELECT* FROM Termoelectricas_datos_promedio", engine)
    terP
    st.caption("*Promedio de cada una de las Plantas Termoeléctricas (2016-2020).*")

    #PROMEDIO DE LA ENERGIA NETA PRODUCIDA EN LAS PLANTAS TERMOELECTRICAS
    st.subheader("*Promedio de la Energía Neta producida en las plantas Termoeléctricas.*")

    fig11, ax = plt.subplots(figsize=(12, 8))

    ax.bar(terP['Termoeléctrica'], terP['EnergiaBruta_MWH'], color='blue')
    ax.set_xlabel('Thermal plants', fontsize=14)
    ax.set_ylabel('Net energy (MWH)', fontsize=14)
    plt.xticks(rotation=45)
    ax.set_title('Average energy production (2016-2020) of thermal plants located in the amazon region of Ecuador',
                 fontname="Times New Roman", size=20, fontweight="bold")
    st.pyplot(fig11)
    st.caption("*Gráfico de barras de los promedios de la Energía producida de las Planta Termoeléctrica en Ecuador (2016-2020).*")

    #PROMEDIO DE LAS EMISIONES DE CO2 EN LAS PLANTAS TERMOELECTRICAS ECUADOR
    st.subheader("*Promedio de las emisiones de CO2 en las plantas Termoeléctricas.*")
    fig12, ax = plt.subplots(figsize=(12, 8))

    ax.bar(terP['Termoeléctrica'], terP['Emision_TCO2'], color='red')
    ax.set_xlabel('Thermal plants', fontsize=14)
    ax.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=14)
    plt.xticks(rotation=45)
    ax.set_title(r'Average $CO_{2}$ emissions (2016-2020) of thermal plants located in the amazon region of Ecuador',
                 fontname="Times New Roman", size=20, fontweight="bold")
    st.pyplot(fig12)
    st.caption("*Gráfico de barras de los promedios de las emisiones de CO2 de las Planta Termoeléctrica en Ecuador (2016-2020).*")

    #COMPARACION DE LOS PROMEDIOS DE LA ENERGIA NETA PRODUCIDA Y EL PROMEDIO DE LAS EMISIONES DE CO2 EN LAS PLANTAS TERMOELECTRICAS
    st.subheader("*Comparación entre los promedios de la Energía Neta producida y el promedio de las emisiones de CO2 en las Plantas Termoeléctricas en Ecuador.*")
    st.markdown("")
    formatter = ticker.EngFormatter()
    fig13 = plt.figure(figsize=(15, 11), edgecolor='black')
    ax1 = fig13.add_subplot()
    ax2 = ax1.twinx()

    ener = terP.plot.bar(x='Termoeléctrica', y='EnergiaBruta_MWH', width=0.4, color='blue',
                         ax=ax1, align='center', label='Net energy', position=1)
    emi = terP.plot.bar(x='Termoeléctrica', y='Emision_TCO2', width=0.4, color='red',
                        ax=ax2, align='center', label=r'$CO_{2}$ emissions', position=0)

    ax1.set_xlabel('', fontsize=14)
    ax1.set_ylabel('Net energy (MWH)', fontsize=16)
    ax2.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=16)
    ax1.tick_params(axis='x', labelrotation=45, labelsize=14)
    ax1.tick_params(axis='y', labelsize=14)
    ax2.tick_params(axis='y', labelsize=14)
    ax1.yaxis.set_major_formatter(formatter)
    ax2.yaxis.set_major_formatter(formatter)
    ax1.set_ylim(0, 200E3)
    ax2.set_ylim(0, 200E3)
    ax1.legend(loc='upper center', fontsize=12)
    ax2.legend(loc='upper right', fontsize=12)
    ax2.grid(visible=False)
    st.pyplot(fig13)
    st.caption("*Gráfico de barras del promedio de la Energía Neta producida y el promedio de las emisiones de CO2 en las Plantas Termoeléctricas en Ecuador (2016-2020).*")



