# Import Python Libraries
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
from sqlalchemy import create_engine
from matplotlib import ticker
from matplotlib.ticker import AutoMinorLocator

# sns.set_style('white')

from streamlit_option_menu import option_menu

# Desing of the app
icon = Image.open("resources/icon.png")
st.set_page_config(page_title="CCUS App",page_icon=icon)
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
</style>""",
    unsafe_allow_html=True,
)

# Create title of web app
st.title("CO2 Emissions App")

Logo = Image.open("Resources/ESPOL.png")
st.sidebar.image(Logo)


# MENU DE OPCIONES PRINCIPAL

with st.sidebar:
    options = option_menu(
        menu_title="Main menu",
        options=[
            "Home",
            "Refineries data",
            "Thermal plants data",
            "Surface Facilities",
        ],
        icons=["house", "bar-chart", "tv", "calculator"],
    )

# OPCION HOME
if options == "Home":

    # INTRODUCCION
    st.markdown(
        """ El problema decisivo de nuestro tiempo sigue siendo el brutal cambio climático. Los cinco años más cálidos
         desde que comenzó el registro fueron los últimos. La producción de gases de efecto invernadero (GEI),
          principalmente CO2, CH, N2O y gases fluorados, está aumentando exponencialmente con el tiempo. Como resultado,
           la temperatura global promedio ha aumentado 1,1 °C en comparación con los niveles preindustriales. El CO2,
            el gas de efecto invernadero más prevalente, ha aumentado sus emisiones globales de 2 Gt/año en 1990 a
             35 Gt/año en 2010. Tres factores principales que explican este aumento de las emisiones de gases de efecto
              invernadero son el crecimiento de la población, la expansión económica mundial y la reducción de la
               capacidad ambiental para absorber, reflejar y liberar CO2. (Rubén et al., 2021) """
    )
    st.markdown(
        """ Para reducir las emisiones globales de CO2, la captura, uso y almacenamiento de carbono (CCUS)
         se ha convertido en una posible estrategia complementaria. Por un lado, el CO2 queda atrapado, reduciendo
          su papel en el cambio climático. El plan CCUS consta de cuatro fases: recolección, transporte, almacenamiento
           y uso. """
    )
    st.markdown(
        """En el **Video 1** podemos observar la cadena de valor de CCUS"""
    )
    # Load video
    video = open("resources/ccus.mp4", "rb")
    st.video(video)
    st.caption("*Video 1. CCUS Value Chain.*")

    # OBJETIVO GENERAL
    st.header("""**Objetivo:** """)
    st.markdown(
        """Diseño de aplicativo web con información de emisiones de CO2 de fuentes estacionarias, con la finalidad de 
        cuantificar estas emisiones para el desarrollo de proyectos CCUS y al mismo tiempo proponer procesos 
        alternativos que nos puedan dar un soporte en la toma de decisiones a nivel de producción y emisiones de gases
         de efecto invernadero.""")


    # DESCRIPCION DE LOS TIPOS DE EMISIONES
    st.header("""**Tipos de Emisiones:**""")
    st.markdown(
        """**Emisiones por venteo** son liberadas a la atmósfera, estas pueden ser liberadas intencionalmente, en
        procesos o actividades que están diseñados para ventear gas, o de forma no intencionada, en caso de fallos o
        por un mal funcionamiento de los equipos."""
    )
    st.markdown(
        """Entre las actividades que se producen estas emisiones por venteo tenemos:""" )
    st.markdown(
        """-En la etapa de completacion de un pozo."""
    )
    st.markdown(
        """-En las descargas de líquidos en los pozos de gas"""
    )
    st.markdown(
        """Una de las principales fuentes de venteo podemos verlos en la **Imagen 1**, donde se observa los tanques de 
        almacenamiento de líquidos producidos como condensado, petróleo crudo o agua. Los tanques pueden tener emisiones
        relacionadas con el "flash" que se produce con la expansión del líquido al llegar al tanque desde otros
        recipientes. Lo más frecuente, es que los tanques estén próximos a la presión atmósferica, pero los recipientes
        de los que proviene el líquido están a mayor presión. El gas se libera cuando se abre la compuerta del tanque
        habilitada para la medición de nivel o cuando se carga en el camión. El gas se libera desde el tanque como
        consecuencia del arrastre de una corriente de gas enviada de forma no intencionada desde el sistema aguas 
        arriba."""
    )
    image_venteo = Image.open("resources/emisiones_venteo.jpg")
    st.image(image_venteo)
    st.caption(
        "*Imagen 1. Tanques de almacenamiento.*"
    )
    st.markdown(
        """**Emisiones por Quemado:** Para evitar riesgos, el gas amargo rechazado es enviado a quemadores  elevados 
        tipo "antorcha" como se observa en la **Imagen 2**. Como resultado de la combustión del gas amargo, además de 
        CO2 y agua, se emite bióxido de azufre (SO2), óxidos de nitrógeno (NOx), partículas suspendidas (PS), monóxido 
        de carbono (CO), compuestos orgánicos no quemados y H2S no oxidado. Estimados recientes 
        (Villasenor et al., 2003), indican que cerca del 82% del total de contaminantes emitidos a la atmósfera proviene 
        de estas operaciones de quemado de gas. Para la estimación de las emisiones de CO2 se trabaja con la fórmula de 
        emisiones del IPCC ya que no se obtienes muchas medidas directas en estas emisiones."""
    )
    image_quemado = Image.open("resources/emisiones_quemado.jpg")
    st.image(image_quemado)
    st.caption(
        "*Imagen 2. Actividad en la industria petrolera que provoca emisiones por quemado.*"
    )
    st.markdown(
        """**Emisiones fugitivas:** En general, la cantidad de emisiones fugitivas provenientes de actividades que 
        involucran petróleo o gas no muestran una correlación directa con los niveles de producción o los rendimientos 
        del sistema. Está más relacionada con la cantidad, tipo y antigüedad de la infraestructura del proceso (es 
        decir, el equipo como se observa en la **Imagen 3**), las características de los hidrocarburos que se producen 
        procesan o manipulan, el diseño industrial y las prácticas de operación y mantenimiento. En general, la cantidad 
        relativa de emisiones fugitivas depende de muchos factores, pero estas tienden a aumentar cuanto más se 
        retrocede en la cadena de procesado del sistema y disminuyen con la concentración de ácido sulfhídrico (H2S) en 
        el petróleo y el gas producidos. En general, el gas y el petróleo crudo contienen una combinación de 
        hidrocarburos y varias impurezas, entre las cuales se encuentran H2O, N2, Ar, H2S y CO2. Si el gas natural 
        contiene más de 10 ppmv de H2S, se denomina normalmente «gas ácido»; de lo contrario, se denomina «gas dulce». 
        Las impurezas se eliminan por medio de procesamiento, tratamiento o refinamiento, según sea lo más adecuado. El 
        CO2 crudo que se elimina de los hidrocarburos en general se ventea a la atmósfera y constituye una fuente de 
        emisiones fugitivas.(Change, n.d.)"""
    )
    image_fugitiva = Image.open("resources/emisiones_fugitivas.jpg")
    st.image(image_fugitiva)
    st.caption(
        "*Imagen 3. Emisiones fugitivas que se pueden producir en los equipos de facilidades petroleras.*"
    )

    #DESCRIPCION SOBRE LOS FACTORES DE EMISION
    st.header("**Factores de Emisión**")


    # CONCLUSIONES
    st.header("Conclusiones")
    st.markdown(
        """Se espera que la implementación de este aplicativo aporte al desarrollo de la tecnología CCUS y captar el 
        interés de Industrias, Gobierno y academia para tener en mayor consideración las emisiones de CO2 que pueden 
        producir, con la finalidad de representar de una mejor manera los diferentes tipos de datos de emisiones de CO2 
        provenientes de fuentes estacionarias, abarcando mayor número de espacios de control potencial, identificando 
        en donde se producen la mayor cantidad de emisiones de gases de efecto invernadero y teniendo una evaluación más 
        rápida y precisa de la cuantificación de los datos. De la misma forma se planea que el aplicativo llame la 
        atención de personas interesadas de tal forma que nos puedan colaborar con la extensión de la base de datos y 
        mejora de la herramienta (aplicativo web) debido a que es una herramienta open-source."""
    )
    # Load image
    image = Image.open("resources/Digitalizacion_2.jpg")
    st.image(image)
    st.caption("*Imagen 4. Digitalization value chain.*")

# OPCION REFINIRIES DATA
if options == "Refineries data":
    # LLAMADO DE LA DATA REFINERIA SHUSHUFINDI
    st.header("Refineria Shushufindi ")
    st.markdown(
        "La Refinería Shushufindi abastece de gasolina y diésel a las provincias de Sucumbíos, Orellana y Napo, y de GLP a la ciudad de Quito y su zona de influencia. La capacidad de procesamiento de la Refinería Shushufindi, es de 20 mil barriles de crudo por día."
    )
    st.markdown(
        "A continuación se presenta una base de datos recopilada de entidades gubernamentales sobre las emisiones de CO2 consecuencia de las actividades de refinación del crudo que se maneja dentro de esta fuente de emision estacionaria."
    )

    engine = create_engine("sqlite:///Data/CO2_EOR.db")

    df = pd.read_sql_query("SELECT* FROM R_Shushufindi", engine)
    df
    st.caption("*Base de datos sobre la Refineria Shushuindi del año 2010 al 2020.*")

    # GRAFICO DE BARRAS DE LOS BARRILES REFINADOS SHUSHUFINDI
    st.header("Producción de la Refinería Shushufindi 2010-2020")
    st.markdown(
        "Con la ayuda de un gráfico de barras se puede observar la producción del petróleo refinado y sus variaciones en los años del 2010 al 2020 en unidades de Millones de barriles (MMbbl)."
    )
    fig1, ax = plt.subplots(figsize=(14, 8))

    ax.bar(df["año"], df["RefinacionBarriles"], color="navy")
    ax.set_xlabel("Year", fontsize=14)
    ax.set_ylabel("Oil refined (MMbbl)", fontsize=14)
    ax.set_title(
        "Oil refined of the refinery Sushufindi",
        fontname="Times New Roman",
        size=20,
        fontweight="bold",
    )
    plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    st.pyplot(fig1)
    st.caption("*Producción Refinería Shushufindi (2010-2020).*")

    # GRAFICO BARRAS EMICIONES CO2 SHUSHUFINDI
    st.header("Emisiones de CO2 producidas en la Refinería Shushufindi 2010-2020.")
    st.markdown(
        "Todo proceso industrial genera emisiones de CO2, en la refinería Shushufinfi se pudo cuantificar estas emisiones provenientes de la producción dentro de la planta en unidades de Toneladas (Ton), las cuales se presentan a continuación:"
    )

    fig2, ax = plt.subplots(figsize=(12, 8))

    ax.bar(df["año"], df["Emisiones_CO2"], color="brown")
    ax.set_xlabel("Year", fontsize=14)
    ax.set_ylabel(r"$CO_{2}$ emissions (Ton)", fontsize=14)
    ax.set_title(
        r"$CO_{2}$ emissions of the refinery Sushufindi",
        fontname="Times New Roman",
        size=20,
        fontweight="bold",
    )
    plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    st.pyplot(fig2)
    st.caption("*Emisiones de CO2 emitidas en la Refinería Shushufinfi (2010-2020).*")

    # GRAFICO DE BARRAS DE COMPARATIVA ENTRE LOS BARRILES REFINADOS Y EL CO2 QUE EMITEN
    st.header(
        "Comparativa de la Refinación de Barriles y las Emisiones de CO2 que emiten."
    )
    st.markdown(
        "Una vez obtenidos los datos de la producción y las emisiones de CO2 que estas actividades producen, podemos compararlas para saber cuantos barriles refinados corresponden a cada tonelada de CO2 emitida."
    )

    formatter = ticker.EngFormatter()
    fig3 = plt.figure(figsize=(12, 8), edgecolor="black")
    ax1 = fig3.add_subplot()
    ax2 = ax1.twinx()

    ener = df.plot.bar(
        x="año",
        y="RefinacionBarriles",
        width=0.4,
        color="navy",
        ax=ax1,
        align="center",
        label="Oil refined",
        position=1,
    )
    emi = df.plot.bar(
        x="año",
        y="Emisiones_CO2",
        width=0.4,
        color="brown",
        ax=ax2,
        align="center",
        label=r"$CO_{2}$ emissions",
        position=0,
    )

    ax1.set_xlabel("", fontsize=14)
    ax1.set_ylabel("Oil refined (bbl)", fontsize=16)
    ax2.set_ylabel(r"$CO_{2}$ emissions (Ton)", fontsize=16)
    ax1.tick_params(axis="x", labelsize=14)
    ax1.tick_params(axis="y", labelsize=14)
    ax2.tick_params(axis="y", labelsize=14)
    ax1.yaxis.set_major_formatter(formatter)
    ax2.yaxis.set_major_formatter(formatter)
    ax2.set_ylim(0, 250e3)
    ax1.legend(loc="upper center", fontsize=12)
    ax2.legend(loc="upper right", fontsize=12)
    ax2.grid(visible=False)
    ax1.tick_params(axis="x", labelrotation=0)
    ax1.set_ylim(0, 10e6)
    st.pyplot(fig3)
    st.caption("*Comparación de la producción con las emisiones de CO2 (2010-2020).*")

elif options == "Thermal plants data":

    st.header("Plantas Termoeléctricas")
    st.markdown(
        """En el **Video 2** Obseramos el funcionamiento de las centrales térmicas convencionales que utilizan 
        combustibles fósiles (gas natural, carbón o fueloil) para generar energía eléctrica mediante un ciclo 
        termodinámico de agua-vapor. El término ‘convencional’ se utiliza para diferenciarlas de otras centrales
        térmicas, como las de ciclo combinado o las nucleares. """
    )
    video_ter = open("resources/Termo.mp4", "rb")
    st.video(video_ter)
    st.caption("*Video 2. Thermal Plants Value Chain*")
    st.markdown(
        """Las centrales térmicas convencionales como en la **Imagen 5** están compuestas de varios elementos que 
        posibilitan la transformación de los combustibles fósiles en energía eléctrica. Sus componentes principales 
        son:"""
    )
    st.markdown(
        """-Caldera: espacio donde el agua se transforma en vapor gracias a la quema de combustible. En este proceso la 
        energía química se transforma en térmica."""
    )
    st.markdown(
        """-Serpentines: cañerías por donde circula el agua que se transforma en vapor. En ellos se produce el 
        intercambio de calor entre los gases de la combustión y el agua."""
    )
    st.markdown(
        """-Turbina de vapor: máquina que recoge el vapor de agua y que, gracias a un complejo sistema de presiones y 
        temperaturas, consigue que se mueva el eje que la atraviesa. Esta turbina normalmente tiene varios cuerpos, de 
        alta, media y baja presión, para aprovechar al máximo el vapor de agua."""
    )
    st.markdown(
        """-Generador: máquina que recoge la energía mecánica generada en el eje que atraviesa la turbina y la 
        transforma en eléctrica mediante inducción electromagnética. Las centrales eléctricas transforman la energía 
        mecánica del eje en una corriente eléctrica trifásica y alterna. El generador conecta el eje que atraviesa los 
        diferentes cuerpos. """
    )
    image_thermal = Image.open("resources/image_termo.jpeg")
    st.image(image_thermal)
    st.caption("*Imagen 5. Instalaciones de centrales o plantas Térmicas*")

    # LLAMADO A LA DATA THERMAL PLANTS
    st.header("Base de datos de Plantas Termoeléctricas en Ecuador 2016-2020.")
    st.markdown(
        """Entre las plantas térmicas en Ecuador enunciamos algunas de las que hemos podido obtener los datos, tanto de 
        la Energía Neta producida, el tipo de combustible que utilizan y la cantidad del mismo, ya que son las variables 
        que más nos interesan en este proyecto."""
    )
    engine = create_engine("sqlite:///Data/CO2_EOR.db")

    df = pd.read_sql_query("SELECT* FROM Termoelectricas_ECU", engine)
    df = df.replace("",0)
    df

    st.caption(
        """*Base de datos de la energía neta producida, tipo de combustible y su cantidad, de las plantas 
        termoeléctricas de Ecuador (2016-2020).*"""
    )
    #CONVERTIR DATAFRAME DIESEL(GALONES) DE STR A FLOAT
    df[["Diesel(galones)"]] = df[["Diesel(galones)"]].astype(float)

    #CALCULO DE EMISIONES CO2 POR DIESEL(GALONES)
    df[["Emisiones de CO2 causadas por Diesel (TON)"]] = (df[["Diesel(galones)"]] * 3.7854 * 0.87 / 1000) * (0.0408 * 72.6)
    df[["termoelectrica","Emisiones de CO2 causadas por Diesel (TON)"]]

    # CONVERTIR DATAFRAME FUEL OIL (GALONES) DE STR A FLOAT
    df[["Fuel Oil(gal)"]] = df[["FuelOil(gal)"]].astype(float)

    #CALCULO DE EMISIONES CO2 POR FUEL OIL (GALONES)
    df[["Emisiones de CO2 causadas por Fuel Oil (TON)"]] = (df[["Fuel Oil(gal)"]] * 3.7854 * 0.992 / 1000) * (0.0392 * 75.5)
    df[["termoelectrica", "Emisiones de CO2 causadas por Fuel Oil (TON)"]]

    # CONVERTIR DATAFRAME GAS NATURAL DE STRA A FLOAT
    df[["Gas Natural"]] = df[["GasNatural(Kpc)"]].astype(float)

    #CALCULO DE EMISIONES DE CO2 POR GAS NATURAL (Kpc)
    df[["Emisiones de CO2 causadas por Gas Natural (TON)"]] = (df[["Gas Natural"]] * 28316.85 * 0.000737 / 1000) * (0.0465 * 54.3)
    df[["termoelectrica", "Emisiones de CO2 causadas por Gas Natural (TON)"]]

    #CONVERTIR DATAFRAME CRUDO DE STR A FLOAT
    df[["Crudo"]] = df[["crudo(galones)"]].astype(float)

    #CALCULO DE EMISIONES DE CO2 POR CRUDO (GAL)
    df[["Emisiones de CO2 causadas por Crudo (TON)"]] = (df[["Crudo"]] * 3.7854 * 0.953 / 1000) * (0.0448 * 79.85)
    df[["termoelectrica", "Emisiones de CO2 causadas por Crudo (TON)"]]

    #EMISIONES TOTALES GENERADAS EN LA TERMOELECTRICAS (TON)
    df["Emisiones de CO2 (TON)"] = df["Emisiones de CO2 causadas por Diesel (TON)"] + df["Emisiones de CO2 causadas por Fuel Oil (TON)"] + df["Emisiones de CO2 causadas por Gas Natural (TON)"] + df["Emisiones de CO2 causadas por Crudo (TON)"]
    df[["termoelectrica", "Emisiones de CO2 (TON)"]]
    list_termo = list(set(df['termoelectrica']))
    paleta = list(sns.color_palette(palette='Spectral', n_colors=len(list_termo)).as_hex())
    dict_color = dict(zip(list_termo, paleta))

    fig = px.bar(df, x='termoelectrica', y='Emisiones de CO2 (TON)',
                 color='termoelectrica',
                 color_discrete_map=dict_color,
                 animation_frame='aסo',
                 animation_group='termoelectrica',
                 range_y=[0, 1.2])
    fig.update_xaxes(title='Termoelectricas', visible=True)
    fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                     visible=True, showticklabels=True)
    fig.update_layout(width=1000,height=600, showlegend=True,
                      xaxis=dict(tickmode='linear',dtick=1))
    fig.update_traces(textfont_size=16,textangle=0)
    fig.show()
