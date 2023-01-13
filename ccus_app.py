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
st.set_page_config(page_title="QFEI",page_icon=icon)
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
st.title("CO2 Emissions App :computer:")

Logo = Image.open("Resources/icon_2.png")
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
        """La producción de gases de efecto invernadero (GEI), principalmente CO2, CH, N2O y gases fluorados, está 
        aumentando exponencialmente con el tiempo. Como resultado, la temperatura global promedio ha aumentado 1,1 °C en 
        comparación con los niveles preindustriales. El CO2, el gas de efecto invernadero más prevalente, ha aumentado 
        sus emisiones globales de 2 Gt/año en 1990 a 35 Gt/año en 2010. Tres factores principales que explican este 
        aumento de las emisiones de gases de efecto invernadero son el crecimiento de la población, la expansión 
        económica mundial y la reducción de la capacidad ambiental para absorber, reflejar y 
        liberar CO2. (Rubén et al., 2021) """
    )
    st.markdown(
        """ Para reducir las emisiones globales de CO2; la captura, uso y almacenamiento de carbono (CCUS)
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
    st.caption("""*Video 1. Aker Carbon Capture.(9 de noviembre del 2020).CCUS - Understanding why 
    [Video]. YouTube. Obtenido de https://www.youtube.com/watch?v=TP3qP83Ah1s*"""
               )

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
    st.markdown("""El Factor de emisión se refiere a un número que intenta relacionar la cantidad de contaminantes 
    liberados a la atmósfera con las actividades involucradas en la liberación del contaminante. Estas variables suelen 
    expresarse como la masa del contaminante dividida por unidades de peso, volumen, longitud o tiempo. (FACTORES DE 
    EMISIÓN – Observatorio Ambiental de Cartagena de Indias, 2021)"""
                )
    engine = create_engine("sqlite:///Data/CO2_EOR.db")
    df = pd.read_sql_query("SELECT* FROM Propiedades_caloríficas_FE", engine)
    df
    st.caption("*Valores de Factor de Emisión de combustibles.*")

    #DESCRIPCION SOBRE PODER CALORÍFICO
    st.header("**Poder Calorífico**")
    st.markdown("""Poder calorífico se refiere al calor generado por un material o combustible por kilogramo o metro 
    cúbico de la sustancia después de la oxidación completa. El valor calorífico se calcula sistemáticamente en función 
    de la masa o el volumen del combustible oxidado (quemado). Cuanto mayor es el poder calorífico del combustible, 
    menos se utiliza. (¿Qué Es El Poder Calorífico? - Vaillant, 2022)"""
                )
    engine = create_engine("sqlite:///Data/CO2_EOR.db")
    df = pd.read_sql_query("SELECT* FROM Propiedades_caloríficas_PC", engine)
    df
    st.caption("*Valores de Poder Calorífico de combustibles.*")

    #DENSIDAD
    st.header("**Densidad**")
    st.markdown("""Densidad es la relación entre la masa de una sustancia y el volumen que ocupa (la misma sustancia). 
    Las unidades de masa más utilizadas son kg/l o g/ml para líquidos y gases y kg/m3 o g/cm3 para sólidos. Cuando 
    hablamos de la densidad de una sustancia, estamos hablando de su peso en relación con su tamaño. (Glosario: 
    Densidad, 2001)"""
                )
    engine = create_engine("sqlite:///Data/CO2_EOR.db")
    df = pd.read_sql_query("SELECT* FROM Propiedades_caloríficas_Total", engine)
    df = df.rename(columns={"Valor pho": "Valor Densidad"})
    df[["Combustible","Valor Densidad","Densidad** (Unidad)"]]
    st.caption("*Valores de Densidad de combustibles*")
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
    st.caption("*Imagen 4. Digitalization Value Chain.*")

# OPCION REFINIRIES DATA
if options == "Refineries data":
    #REFINERIAS - DESCRIPCION DE PROCESOS
    st.header("Refinerías de Petróleo")
    st.markdown("""Las refinerías, que son instalaciones de la industria petroquímica, producen compuestos hechos de 
    petróleo crudo al convertir y refinar productos como gasolina, diésel, asfalto, queroseno, GLP, petróleo y 
    combustible para eliminar las impurezas. También se producen productos petroquímicos como el etileno y el 
    propileno."""
                )
    st.markdown("""El proceso de refinación se basa en dos columnas de destilación, una al vacío y otra a presión 
    atmosférica, con múltiples salidas intermedias. El proceso de destilación química consiste en calentar dos o más 
    sustancias con diferentes puntos de ebullición y separarlas en función de su volatilidad. Si hay más de dos 
    componentes, se crean intermedios para obtener componentes adicionales. Cada una de estas corrientes tiene un 
    proceso correspondiente donde los componentes adicionales se separan, combinan, reaccionan y el producto final se 
    purifica."""
                )
    st.markdown("""En el **video 2** se ilustra el proceso de refinación de hidrocarburos.""")
    video_ref = open("resources/Refinería_Procesos.mp4", "rb")
    st.video(video_ref)
    st.caption("""*Video 2. Visio CAD.(10 de abril del 2021). Refinería - Procesos 
        [Video]. YouTube. Obtenido de https://www.youtube.com/watch?v=K5nTsbzcRlc*"""
               )

    st.markdown("""Las refinerías de petróleo emiten gases como dióxido de azufre, dióxido de nitrógeno, dióxido de 
    carbono, monóxido de carbono, metano, fluoruro de hidrógeno, dioxinas, cloro y otros contaminantes durante el 
    procesamiento químico que contribuyen al smog y la contaminación del aire."""
                )
    # LLAMADO DE LA DATA REFINERIA SHUSHUFINDI
    st.header("Refineria Shushufindi ")
    st.markdown(
        """La Refinería Shushufindi abastece de gasolina y diésel a las provincias de Sucumbíos, Orellana y Napo, y de 
        GLP a la ciudad de Quito y su zona de influencia. La capacidad de procesamiento de la Refinería Shushufindi, es 
        de 20 mil barriles de crudo por día."""
    )
    st.markdown(
        """A continuación se presenta una base de datos recopilada de entidades gubernamentales sobre las emisiones de 
        CO2 consecuencia de las actividades de refinación del crudo que se maneja dentro de esta fuente de emision 
        estacionaria."""
    )

    engine = create_engine("sqlite:///Data/CO2_EOR.db")

    df = pd.read_sql_query("SELECT* FROM R_Shushufindi", engine)
    df
    st.caption("*Base de datos sobre la Refineria Shushuindi del año 2010 al 2020.*")
    # GRAFICO DE BARRAS DE LOS BARRILES REFINADOS SHUSHUFINDI
    st.header("Producción de la Refinería Shushufindi 2010-2020")
    st.markdown(
        """Con la ayuda de un gráfico de barras se puede observar la producción del petróleo refinado y sus variaciones 
        en los años del 2010 al 2020 en unidades de Millones de barriles (MMbbl)."""
    )

    list_refi = list(set(df['año']))
    paleta_refi = list(sns.color_palette(palette='Spectral', n_colors=len(list_refi)).as_hex())
    dict_color_refi = dict(zip(list_refi, paleta_refi))

    fig_refi = px.bar(df, x='Refineria', y='Emisiones_CO2',
                 color='Refineria',
                 color_discrete_map=dict_color_refi,
                 animation_frame='año',
                 animation_group='Refineria',
                 range_y=[0, 1.2])
    fig_refi.update_xaxes(title='Refineria Shushufindi', visible=True)
    fig_refi.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                     visible=True, showticklabels=True)
    fig_refi.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                      xaxis=dict(tickmode='linear', dtick=1))
    fig_refi.update_traces(textfont_size=16, textangle=0)
    st.plotly_chart(fig_refi)

    fig1, ax = plt.subplots(figsize=(14, 8))

    ax.bar(df["año"], df["RefinacionBarriles"], color="black")
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
        """Todo proceso industrial genera emisiones de CO2, en la refinería Shushufinfi se pudo cuantificar estas 
        emisiones provenientes de la producción dentro de la planta en unidades de Toneladas (Ton), las cuales se 
        presentan a continuación:"""
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
        """Una vez obtenidos los datos de la producción y las emisiones de CO2 que estas actividades producen, podemos 
        compararlas para saber cuantos barriles refinados corresponden a cada tonelada de CO2 emitida."""
    )

    engine = create_engine("sqlite:///Data/CO2_EOR.db")

    df_refi = pd.read_sql_query("SELECT* FROM Refineria_Shushufindi", engine)
    df_refi[["Valor"]].astype(float)

    list_refi = list(set(df_refi['Tipo resultado']))
    paleta_refi = list(sns.color_palette(palette='Spectral', n_colors=len(list_refi)).as_hex())
    dict_color_refi = dict(zip(list_refi, paleta_refi))

    fig_refi = px.bar(df_refi, x='Tipo resultado', y='Valor',
                      color='Tipo resultado',
                      color_discrete_map=dict_color_refi,
                      animation_frame='Año',
                      animation_group='Tipo resultado',
                      range_y=[0, 1.2])
    fig_refi.update_xaxes(title='Producción', visible=True)
    fig_refi.update_yaxes(autorange=True, title='',
                          visible=True, showticklabels=True)
    fig_refi.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                           xaxis=dict(tickmode='linear', dtick=1))
    fig_refi.update_traces(textfont_size=16, textangle=0)
    st.plotly_chart(fig_refi)
    st.caption("""Gráfico dinámico de los Barriles refinados y las Emisiones de CO2 en la Refinería Shushufindi."""
               )
    formatter = ticker.EngFormatter()
    fig3 = plt.figure(figsize=(12, 8), edgecolor="black")
    ax1 = fig3.add_subplot()
    ax2 = ax1.twinx()

    ener = df.plot.bar(
        x="año",
        y="RefinacionBarriles",
        width=0.4,
        color="black",
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
        """En el **Video 3** observamos el funcionamiento de las centrales térmicas convencionales que utilizan 
        combustibles fósiles (gas natural, carbón o fueloil) para generar energía eléctrica mediante un ciclo 
        termodinámico de agua-vapor. El término ‘convencional’ se utiliza para diferenciarlas de otras centrales
        térmicas, como las de ciclo combinado o las nucleares. """
    )
    video_ter = open("resources/Termo.mp4", "rb")
    st.video(video_ter)
    st.caption("""*Video 3. Endesa Educa.(25 de enero del 2013). Funcionamiento de una central térmica 
            [Video]. YouTube. Obtenido de https://www.youtube.com/watch?v=Apg_aEwvzGM*"""
               )

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
    st.markdown("""Las dos principales formas en que las centrales térmicas tradicionales afectan al medio ambiente son 
    la emisión de residuos a la atmósfera y la transferencia de calor. En el primer caso, la quema de combustibles 
    fósiles produce partículas que ingresan a la atmósfera y pueden dañar el medio ambiente terrestre. A este tipo de 
    plantas instalan chimeneas para dispersar estas partículas y así reducir sus efectos nocivos en el aire. Además, 
    una parte importante de estas partículas es captada por los filtros de partículas de las centrales térmicas 
    convencionales, impidiendo que se escapen. Para el segundo caso de impacto al ambiente las centrales termoeléctricas 
    de ciclo abierto pueden aumentar la temperatura de los ríos y océanos en términos de transferencia de calor."""
                )
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
    df = df.replace("Repsol YPF-NPF-1", "Repsol YPF-NPF")
    df = df.replace("Repsol YPF-NPF-2", "Repsol YPF-NPF")
    df = df.replace("Repsol YPF-NPF-3", "Repsol YPF-NPF")
    df = df.replace("Repsol YPF-NPF-4", "Repsol YPF-NPF")
    df = df.replace("Repsol YPF-NPF-5", "Repsol YPF-NPF")
    df = df.replace("Shushifindi estaciףn Sur-Oeste", "Shushufindi Estación Sur-Oeste")
    df = df.rename(columns={"aסo": "Año","termoelectrica":"Termoelectricas"})
    df[["EnergiaBruta(GWH)"]] = df[["EnergiaBruta(GWH)"]].astype(float)
    df[["FuelOil(gal)"]] = df[["FuelOil(gal)"]].astype(float)
    df[["FuelOilTEP"]] = df[["FuelOilTEP"]].astype(float)
    df[["GasNatural(Kpc)"]] = df[["GasNatural(Kpc)"]].astype(float)
    df[["GasNatural(TEP)"]] = df[["GasNatural(TEP)"]].astype(float)
    df[["crudo(galones)"]] = df[["crudo(galones)"]].astype(float)
    df[["crudoTEP"]] = df[["crudoTEP"]].astype(float)
    df

    st.caption(
        """*Base de datos de la energía neta producida, tipo de combustible y su cantidad, de las plantas 
        Termoeléctricas de Ecuador (2016-2020).*"""
    )
    st.header("Calculo de las emisiones de CO2")
    st.markdown("""Con los datos proporcionados sobre: la cantidad, factor de emisión y densidad de cada tipo de 
    combustible usado en las diferentes termoelectricas se proceda a estimar las emisiones de CO2."""
                )
    #CONVERTIR DATAFRAME DIESEL(GALONES) DE STR A FLOAT
    df[["Diesel(galones)"]] = df[["Diesel(galones)"]].astype(float)

    #CALCULO DE EMISIONES CO2 POR DIESEL(GALONES)
    df[["Emisiones de CO2 causadas por Diesel (TON)"]] = (df[["Diesel(galones)"]] * 3.7854 * 0.87 / 1000) * (0.0408 * 72.6)
    #df[["Termoelectricas","Emisiones de CO2 causadas por Diesel (TON)"]]

    # CONVERTIR DATAFRAME FUEL OIL (GALONES) DE STR A FLOAT
    df[["Fuel Oil(gal)"]] = df[["FuelOil(gal)"]].astype(float)

    #CALCULO DE EMISIONES CO2 POR FUEL OIL (GALONES)
    df[["Emisiones de CO2 causadas por Fuel Oil (TON)"]] = (df[["Fuel Oil(gal)"]] * 3.7854 * 0.992 / 1000) * (0.0392 * 75.5)
    #df[["Termoelectricas", "Emisiones de CO2 causadas por Fuel Oil (TON)"]]

    # CONVERTIR DATAFRAME GAS NATURAL DE STRA A FLOAT
    df[["Gas Natural"]] = df[["GasNatural(Kpc)"]].astype(float)

    #CALCULO DE EMISIONES DE CO2 POR GAS NATURAL (Kpc)
    df[["Emisiones de CO2 causadas por Gas Natural (TON)"]] = (df[["Gas Natural"]] * 28316.85 * 0.000737 / 1000) * (0.0465 * 54.3)
    #df[["Termoelectricas", "Emisiones de CO2 causadas por Gas Natural (TON)"]]

    #CONVERTIR DATAFRAME CRUDO DE STR A FLOAT
    df[["Crudo"]] = df[["crudo(galones)"]].astype(float)

    #CALCULO DE EMISIONES DE CO2 POR CRUDO (GAL)
    df[["Emisiones de CO2 causadas por Crudo (TON)"]] = (df[["Crudo"]] * 3.7854 * 0.953 / 1000) * (0.0448 * 79.85)
    #df[["Termoelectricas", "Emisiones de CO2 causadas por Crudo (TON)"]]

    #EMISIONES TOTALES GENERADAS EN LA TERMOELECTRICAS (TON)
    df["Emisiones de CO2 (TON)"] = df["Emisiones de CO2 causadas por Diesel (TON)"] + \
                                   df["Emisiones de CO2 causadas por Fuel Oil (TON)"] + \
                                   df["Emisiones de CO2 causadas por Gas Natural (TON)"] + \
                                   df["Emisiones de CO2 causadas por Crudo (TON)"]
    df[["Termoelectricas","Año", "EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]

    st.caption("*Resultado de cálculos para las emisiones de CO2 producidas en las Termoelectricas (2016-2020).*")

    list_termo = list(set(df['Termoelectricas']))
    paleta = list(sns.color_palette(palette='Spectral', n_colors=len(list_termo)).as_hex())
    dict_color = dict(zip(list_termo, paleta))

    fig = px.bar(df, x='Termoelectricas', y='Emisiones de CO2 (TON)',
                 color='Termoelectricas',
                 color_discrete_map=dict_color,
                 animation_frame='Año',
                 animation_group='Termoelectricas',
                 range_y=[0, 1.2])
    fig.update_xaxes(title='Termoelectricas', visible=True)
    fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                     visible=True, showticklabels=True)
    fig.update_layout(template="plotly_dark",width=1000,height=600, showlegend=True,
                      xaxis=dict(tickmode='linear',dtick=1))
    fig.update_traces(textfont_size=16,textangle=0)
    st.plotly_chart(fig)
    st.caption("*Gráfico dinámico de las emisiones de CO2 producidas en las diferentes Termoelectricas (2016-2020).*")
    amazonas=df.loc[df["Termoelectricas"]=="Amazonas"]
    lago_agrio = df.loc[df["Termoelectricas"] == "Lago Agrio"]
    secoya = df.loc[df["Termoelectricas"] == "Secoya"]
    guanta = df.loc[df["Termoelectricas"] == "Guanta"]
    cuyabeno = df.loc[df["Termoelectricas"] == "Cuyabeno"]
    repsol = df.loc[df["Termoelectricas"] == "Repsol YPF-NPF"]
    shushufindi = df.loc[df["Termoelectricas"] == "Shushufindi Estación Sur-Oeste"]
    tapi = df.loc[df["Termoelectricas"] == "Tapi"]
    pakay = df.loc[df["Termoelectricas"] == "Pakay"]
    sacha = df.loc[df["Termoelectricas"] == "Sacha"]

    st.header("Seleccionar Termoelectrica")
    opcion_termo = st.selectbox("Elija la termoelectrica que desea ver a detalle.",
                 ("Amazonas","Lago Agrio","Secoya","Guanta","Cuyabeno",
                  "Repsol YPF-NPF","Shushufindi Estación Sur-Oeste",
                  "Tapi","Pakay","Sacha"))
    if opcion_termo =="Amazonas":
        amazonas[["Termoelectricas","Año","EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]
        st.caption("""*Resultado de Enegía Neta y Emisiones de CO2 producidas en la Termoelectrica Amazonas 
        (2016-2020)*"""
                   )

        st.subheader("Energía Neta vs Emisiones de CO2")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ener = pd.read_sql_query("SELECT* FROM Energia_Emisiones_Amazonas", engine)
        df_ener[["Valor"]].astype(float)

        list_ener = list(set(df_ener['Tipo resultado']))
        paleta_ener = list(sns.color_palette(palette='Spectral', n_colors=len(list_ener)).as_hex())
        dict_color_ener = dict(zip(list_ener, paleta_ener))

        fig_ener = px.bar(df_ener, x='Tipo resultado', y='Valor',
                          color='Tipo resultado',
                          color_discrete_map=dict_color_ener,
                          animation_frame='Año',
                          animation_group='Tipo resultado',
                          range_y=[0, 1.2])
        fig_ener.update_xaxes(title='Producción', visible=True)
        fig_ener.update_yaxes(autorange=True, title='',
                              visible=True, showticklabels=True)
        fig_ener.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                               xaxis=dict(tickmode='linear', dtick=1))
        fig_ener.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig_ener)
        st.caption("""Gráfico dinámico de la Energía Neta producida y las Emisiones de CO2 en la Termoeléctrica 
        Amazonas (2016-2020)."""
                   )
        st.subheader("Tipo de combustibles utilizados y sus Emisiones")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ama = pd.read_sql_query("SELECT* FROM Emisiones_Amazonas", engine)
        df_ama[["Emisiones CO2 (TON)"]].astype(float)

        list_ama = list(set(df_ama['Combustible']))
        paleta_ama = list(sns.color_palette(palette='Spectral', n_colors=len(list_ama)).as_hex())
        dict_color_ama = dict(zip(list_ama, paleta_ama))

        fig = px.bar(df_ama, x='Combustible', y='Emisiones CO2 (TON)',
                     color='Combustible',
                     color_discrete_map=dict_color_ama,
                     animation_frame='Año',
                     animation_group='Combustible',
                     range_y=[0, 1.2])
        fig.update_xaxes(title='Tipo de Combustible', visible=True)
        fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                         visible=True, showticklabels=True)
        fig.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                          xaxis=dict(tickmode='linear', dtick=1))
        fig.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig)
        st.caption("""*Gráfico dinámico de las emisiones de CO2 producidas por los distintos tipos de combustibles 
        usados en la Termoeléctrica Amazonas (2016-2020).*"""
                   )

    elif opcion_termo=="Lago Agrio":
        lago_agrio[["Termoelectricas","Año","EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]
        st.caption("""*Resultado de Enegía Neta y Emisiones de CO2 producidas en la Termoelectrica Lago Agrio 
                (2016-2020)*"""
                   )
        st.subheader("Energía Neta vs Emisiones de CO2")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ener = pd.read_sql_query("SELECT* FROM Energia_Emisiones_LagoAgrio", engine)
        df_ener[["Valor"]].astype(float)

        list_ener = list(set(df_ener['Tipo resultado']))
        paleta_ener = list(sns.color_palette(palette='Spectral', n_colors=len(list_ener)).as_hex())
        dict_color_ener = dict(zip(list_ener, paleta_ener))

        fig_ener = px.bar(df_ener, x='Tipo resultado', y='Valor',
                          color='Tipo resultado',
                          color_discrete_map=dict_color_ener,
                          animation_frame='Año',
                          animation_group='Tipo resultado',
                          range_y=[0, 1.2])
        fig_ener.update_xaxes(title='Producción', visible=True)
        fig_ener.update_yaxes(autorange=True, title='',
                              visible=True, showticklabels=True)
        fig_ener.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                               xaxis=dict(tickmode='linear', dtick=1))
        fig_ener.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig_ener)
        st.caption("""Gráfico dinámico de la Energía Neta producida y las Emisiones de CO2 en la Termoeléctrica 
                Lago Agrio (2016-2020)."""
                   )
        st.subheader("Tipo de combustibles utilizados y sus Emisiones")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_lag = pd.read_sql_query("SELECT* FROM Emisiones_LagoAgrio", engine)
        df_lag[["Emisiones CO2 (TON)"]].astype(float)

        list_lag = list(set(df_lag['Combustible']))
        paleta_lag = list(sns.color_palette(palette='Spectral', n_colors=len(list_lag)).as_hex())
        dict_color_lag = dict(zip(list_lag, paleta_lag))

        fig = px.bar(df_lag, x='Combustible', y='Emisiones CO2 (TON)',
                     color='Combustible',
                     color_discrete_map=dict_color_lag,
                     animation_frame='Año',
                     animation_group='Combustible',
                     range_y=[0, 1.2])
        fig.update_xaxes(title='Tipo de Combustible', visible=True)
        fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                         visible=True, showticklabels=True)
        fig.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                          xaxis=dict(tickmode='linear', dtick=1))
        fig.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig)
        st.caption("""*Gráfico dinámico de las emisiones de CO2 producidas por los distintos tipos de combustibles 
                usados en la Termoeléctrica Lago Agrio (2016-2020).*"""
                   )

    elif opcion_termo=="Secoya":
        secoya[["Termoelectricas","Año","EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]
        st.caption("""*Resultado de Enegía Neta y Emisiones de CO2 producidas en la Termoelectrica Secoya 
                (2016-2020)*"""
                   )
        st.subheader("Energía Neta vs Emisiones de CO2")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ener = pd.read_sql_query("SELECT* FROM Energia_Emisiones_Secoya", engine)
        df_ener[["Valor"]].astype(float)

        list_ener = list(set(df_ener['Tipo resultado']))
        paleta_ener = list(sns.color_palette(palette='Spectral', n_colors=len(list_ener)).as_hex())
        dict_color_ener = dict(zip(list_ener, paleta_ener))

        fig_ener = px.bar(df_ener, x='Tipo resultado', y='Valor',
                          color='Tipo resultado',
                          color_discrete_map=dict_color_ener,
                          animation_frame='Año',
                          animation_group='Tipo resultado',
                          range_y=[0, 1.2])
        fig_ener.update_xaxes(title='Producción', visible=True)
        fig_ener.update_yaxes(autorange=True, title='',
                              visible=True, showticklabels=True)
        fig_ener.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                               xaxis=dict(tickmode='linear', dtick=1))
        fig_ener.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig_ener)
        st.caption("""Gráfico dinámico de la Energía Neta producida y las Emisiones de CO2 en la Termoeléctrica 
                        Secoya (2016-2020)."""
                   )
        st.subheader("Tipo de combustibles utilizados y sus Emisiones")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_sec = pd.read_sql_query("SELECT* FROM Emisiones_Secoya", engine)
        df_sec[["Emisiones CO2 (TON)"]].astype(float)

        list_sec = list(set(df_sec['Combustible']))
        paleta_sec = list(sns.color_palette(palette='Spectral', n_colors=len(list_sec)).as_hex())
        dict_color_sec = dict(zip(list_sec, paleta_sec))

        fig = px.bar(df_sec, x='Combustible', y='Emisiones CO2 (TON)',
                     color='Combustible',
                     color_discrete_map=dict_color_sec,
                     animation_frame='Año',
                     animation_group='Combustible',
                     range_y=[0, 1.2])
        fig.update_xaxes(title='Tipo de Combustible', visible=True)
        fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                         visible=True, showticklabels=True)
        fig.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                          xaxis=dict(tickmode='linear', dtick=1))
        fig.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig)
        st.caption("""*Gráfico dinámico de las emisiones de CO2 producidas por los distintos tipos de combustibles 
                        usados en la Termoeléctrica Secoya (2016-2020).*"""
                   )

    elif opcion_termo=="Guanta":
        guanta[["Termoelectricas","Año","EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]
        st.caption("""*Resultado de Enegía Neta y Emisiones de CO2 producidas en la Termoelectrica Guanta 
                (2016-2020)*"""
                   )
        st.subheader("Energía Neta vs Emisiones de CO2")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ener = pd.read_sql_query("SELECT* FROM Energia_Emisiones_Guanta", engine)
        df_ener[["Valor"]].astype(float)

        list_ener = list(set(df_ener['Tipo resultado']))
        paleta_ener = list(sns.color_palette(palette='Spectral', n_colors=len(list_ener)).as_hex())
        dict_color_ener = dict(zip(list_ener, paleta_ener))

        fig_ener = px.bar(df_ener, x='Tipo resultado', y='Valor',
                          color='Tipo resultado',
                          color_discrete_map=dict_color_ener,
                          animation_frame='Año',
                          animation_group='Tipo resultado',
                          range_y=[0, 1.2])
        fig_ener.update_xaxes(title='Producción', visible=True)
        fig_ener.update_yaxes(autorange=True, title='',
                              visible=True, showticklabels=True)
        fig_ener.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                               xaxis=dict(tickmode='linear', dtick=1))
        fig_ener.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig_ener)
        st.caption("""Gráfico dinámico de la Energía Neta producida y las Emisiones de CO2 en la Termoeléctrica 
                                Guanta (2016-2020)."""
                   )
        st.subheader("Tipo de combustibles utilizados y sus Emisiones")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_guan = pd.read_sql_query("SELECT* FROM Emisiones_Guanta", engine)
        df_guan[["Emisiones CO2 (TON)"]].astype(float)

        list_guan = list(set(df_guan['Combustible']))
        paleta_guan = list(sns.color_palette(palette='Spectral', n_colors=len(list_guan)).as_hex())
        dict_color_guan = dict(zip(list_guan, paleta_guan))

        fig = px.bar(df_guan, x='Combustible', y='Emisiones CO2 (TON)',
                     color='Combustible',
                     color_discrete_map=dict_color_guan,
                     animation_frame='Año',
                     animation_group='Combustible',
                     range_y=[0, 1.2])
        fig.update_xaxes(title='Tipo de Combustible', visible=True)
        fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                         visible=True, showticklabels=True)
        fig.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                          xaxis=dict(tickmode='linear', dtick=1))
        fig.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig)
        st.caption("""*Gráfico dinámico de las emisiones de CO2 producidas por los distintos tipos de combustibles 
                                usados en la Termoeléctrica Guanta (2016-2020).*"""
                   )

    elif opcion_termo=="Cuyabeno":
        cuyabeno[["Termoelectricas","Año","EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]
        st.caption("""*Resultado de Enegía Neta y Emisiones de CO2 producidas en la Termoelectrica Cuyabeno 
                (2016-2020)*"""
                   )
        st.subheader("Energía Neta vs Emisiones de CO2")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ener = pd.read_sql_query("SELECT* FROM Energia_Emisiones_Cuyabeno", engine)
        df_ener[["Valor"]].astype(float)

        list_ener = list(set(df_ener['Tipo resultado']))
        paleta_ener = list(sns.color_palette(palette='Spectral', n_colors=len(list_ener)).as_hex())
        dict_color_ener = dict(zip(list_ener, paleta_ener))

        fig_ener = px.bar(df_ener, x='Tipo resultado', y='Valor',
                          color='Tipo resultado',
                          color_discrete_map=dict_color_ener,
                          animation_frame='Año',
                          animation_group='Tipo resultado',
                          range_y=[0, 1.2])
        fig_ener.update_xaxes(title='Producción', visible=True)
        fig_ener.update_yaxes(autorange=True, title='',
                              visible=True, showticklabels=True)
        fig_ener.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                               xaxis=dict(tickmode='linear', dtick=1))
        fig_ener.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig_ener)
        st.caption("""Gráfico dinámico de la Energía Neta producida y las Emisiones de CO2 en la Termoeléctrica 
                        Cuyabeno (2016-2020)."""
                   )
        st.subheader("Tipo de combustibles utilizados y sus Emisiones")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_cuy = pd.read_sql_query("SELECT* FROM Emisiones_Cuyabeno", engine)
        df_cuy[["Emisiones CO2 (TON)"]].astype(float)

        list_cuy = list(set(df_cuy['Combustible']))
        paleta_cuy = list(sns.color_palette(palette='Spectral', n_colors=len(list_cuy)).as_hex())
        dict_color_cuy = dict(zip(list_cuy, paleta_cuy))

        fig = px.bar(df_cuy, x='Combustible', y='Emisiones CO2 (TON)',
                     color='Combustible',
                     color_discrete_map=dict_color_cuy,
                     animation_frame='Año',
                     animation_group='Combustible',
                     range_y=[0, 1.2])
        fig.update_xaxes(title='Tipo de Combustible', visible=True)
        fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                         visible=True, showticklabels=True)
        fig.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                          xaxis=dict(tickmode='linear', dtick=1))
        fig.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig)
        st.caption("""*Gráfico dinámico de las emisiones de CO2 producidas por los distintos tipos de combustibles 
                                        usados en la Termoeléctrica Cuyabeno (2016-2020).*"""
                   )
    elif opcion_termo=="Repsol YPF-NPF":
        repsol[["Termoelectricas","Año","EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]
        st.caption("""*Resultado de Enegía Neta y Emisiones de CO2 producidas en la Termoelectrica Repsol YPF-NPF 
                (2016-2020)*"""
                   )
        st.subheader("Energía Neta vs Emisiones de CO2")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ener = pd.read_sql_query("SELECT* FROM Energia_Emisiones_Repsol", engine)
        df_ener[["Valor"]].astype(float)

        list_ener = list(set(df_ener['Tipo resultado']))
        paleta_ener = list(sns.color_palette(palette='Spectral', n_colors=len(list_ener)).as_hex())
        dict_color_ener = dict(zip(list_ener, paleta_ener))

        fig_ener = px.bar(df_ener, x='Tipo resultado', y='Valor',
                          color='Tipo resultado',
                          color_discrete_map=dict_color_ener,
                          animation_frame='Año',
                          animation_group='Tipo resultado',
                          range_y=[0, 1.2])
        fig_ener.update_xaxes(title='Producción', visible=True)
        fig_ener.update_yaxes(autorange=True, title='',
                              visible=True, showticklabels=True)
        fig_ener.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                               xaxis=dict(tickmode='linear', dtick=1))
        fig_ener.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig_ener)
        st.caption("""Gráfico dinámico de la Energía Neta producida y las Emisiones de CO2 en la Termoeléctrica 
                                Repsol YPF-NPF (2016-2020)."""
                   )
        st.subheader("Tipo de combustibles utilizados y sus Emisiones")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_rep = pd.read_sql_query("SELECT* FROM Emisiones_Repsol", engine)
        df_rep[["Emisiones CO2 (TON)"]].astype(float)

        list_rep = list(set(df_rep['Combustible']))
        paleta_rep = list(sns.color_palette(palette='Spectral', n_colors=len(list_rep)).as_hex())
        dict_color_rep = dict(zip(list_rep, paleta_rep))

        fig = px.bar(df_rep, x='Combustible', y='Emisiones CO2 (TON)',
                     color='Combustible',
                     color_discrete_map=dict_color_rep,
                     animation_frame='Año',
                     animation_group='Combustible',
                     range_y=[0, 1.2])
        fig.update_xaxes(title='Tipo de Combustible', visible=True)
        fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                         visible=True, showticklabels=True)
        fig.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                          xaxis=dict(tickmode='linear', dtick=1))
        fig.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig)
        st.caption("""*Gráfico dinámico de las emisiones de CO2 producidas por los distintos tipos de combustibles 
                                                usados en la Termoeléctrica Repsol YPF-NPF (2016-2020).*"""
                   )
    elif opcion_termo=="Shushufindi Estación Sur-Oeste":
        shushufindi[["Termoelectricas","Año","EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]
        st.caption("""*Resultado de Enegía Neta y Emisiones de CO2 producidas en la Termoelectrica Shushufindi Sur-Oeste 
                (2016-2020)*"""
                   )
        st.subheader("Energía Neta vs Emisiones de CO2")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ener = pd.read_sql_query("SELECT* FROM Energia_Emisiones_Shushufindi", engine)
        df_ener[["Valor"]].astype(float)

        list_ener = list(set(df_ener['Tipo resultado']))
        paleta_ener = list(sns.color_palette(palette='Spectral', n_colors=len(list_ener)).as_hex())
        dict_color_ener = dict(zip(list_ener, paleta_ener))

        fig_ener = px.bar(df_ener, x='Tipo resultado', y='Valor',
                          color='Tipo resultado',
                          color_discrete_map=dict_color_ener,
                          animation_frame='Año',
                          animation_group='Tipo resultado',
                          range_y=[0, 1.2])
        fig_ener.update_xaxes(title='Producción', visible=True)
        fig_ener.update_yaxes(autorange=True, title='',
                              visible=True, showticklabels=True)
        fig_ener.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                               xaxis=dict(tickmode='linear', dtick=1))
        fig_ener.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig_ener)
        st.caption("""Gráfico dinámico de la Energía Neta producida y las Emisiones de CO2 en la Termoeléctrica 
                                        Shushufindi Sur-Oeste (2016-2020)."""
                   )
        st.subheader("Tipo de combustibles utilizados y sus Emisiones")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_shu = pd.read_sql_query("SELECT* FROM Emisiones_Shushufindi", engine)
        df_shu[["Emisiones CO2 (TON)"]].astype(float)

        list_shu = list(set(df_shu['Combustible']))
        paleta_shu = list(sns.color_palette(palette='Spectral', n_colors=len(list_shu)).as_hex())
        dict_color_shu = dict(zip(list_shu, paleta_shu))

        fig = px.bar(df_shu, x='Combustible', y='Emisiones CO2 (TON)',
                     color='Combustible',
                     color_discrete_map=dict_color_shu,
                     animation_frame='Año',
                     animation_group='Combustible',
                     range_y=[0, 1.2])
        fig.update_xaxes(title='Tipo de Combustible', visible=True)
        fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                         visible=True, showticklabels=True)
        fig.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                          xaxis=dict(tickmode='linear', dtick=1))
        fig.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig)
        st.caption("""*Gráfico dinámico de las emisiones de CO2 producidas por los distintos tipos de combustibles 
                                                        usados en la Termoeléctrica Shushufindi Estacion Sur-Oeste 
                                                        (2016-2020).*"""
                   )
    elif opcion_termo=="Tapi":
        tapi[["Termoelectricas","Año","EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]
        st.caption("""*Resultado de Enegía Neta y Emisiones de CO2 producidas en la Termoelectrica Tapi 
                (2016-2020)*"""
                   )
        st.subheader("Energía Neta vs Emisiones de CO2")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ener = pd.read_sql_query("SELECT* FROM Energia_Emisiones_Tapi", engine)
        df_ener[["Valor"]].astype(float)

        list_ener = list(set(df_ener['Tipo resultado']))
        paleta_ener = list(sns.color_palette(palette='Spectral', n_colors=len(list_ener)).as_hex())
        dict_color_ener = dict(zip(list_ener, paleta_ener))

        fig_ener = px.bar(df_ener, x='Tipo resultado', y='Valor',
                          color='Tipo resultado',
                          color_discrete_map=dict_color_ener,
                          animation_frame='Año',
                          animation_group='Tipo resultado',
                          range_y=[0, 1.2])
        fig_ener.update_xaxes(title='Producción', visible=True)
        fig_ener.update_yaxes(autorange=True, title='',
                              visible=True, showticklabels=True)
        fig_ener.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                               xaxis=dict(tickmode='linear', dtick=1))
        fig_ener.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig_ener)
        st.caption("""Gráfico dinámico de la Energía Neta producida y las Emisiones de CO2 en la Termoeléctrica 
                            Tapi (2016-2020)."""
                   )
        st.subheader("Tipo de combustibles utilizados y sus Emisiones")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_tapi = pd.read_sql_query("SELECT* FROM Emisiones_Tapi", engine)
        df_tapi[["Emisiones CO2 (TON)"]].astype(float)

        list_tapi = list(set(df_tapi['Combustible']))
        paleta_tapi = list(sns.color_palette(palette='Spectral', n_colors=len(list_tapi)).as_hex())
        dict_color_tapi = dict(zip(list_tapi, paleta_tapi))

        fig = px.bar(df_tapi, x='Combustible', y='Emisiones CO2 (TON)',
                     color='Combustible',
                     color_discrete_map=dict_color_tapi,
                     animation_frame='Año',
                     animation_group='Combustible',
                     range_y=[0, 1.2])
        fig.update_xaxes(title='Tipo de Combustible', visible=True)
        fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                         visible=True, showticklabels=True)
        fig.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                          xaxis=dict(tickmode='linear', dtick=1))
        fig.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig)
        st.caption("""*Gráfico dinámico de las emisiones de CO2 producidas por los distintos tipos de combustibles 
        usados en la Termoeléctrica Tapi(2016-2020).*"""
                   )
    elif opcion_termo=="Pakay":
        pakay[["Termoelectricas","Año","EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]
        st.caption("""*Resultado de Enegía Neta y Emisiones de CO2 producidas en la Termoelectrica Pakay 
                (2016-2020)*"""
                   )
        st.subheader("Energía Neta vs Emisiones de CO2")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ener = pd.read_sql_query("SELECT* FROM Energia_Emisiones_Pakay", engine)
        df_ener[["Valor"]].astype(float)

        list_ener = list(set(df_ener['Tipo resultado']))
        paleta_ener = list(sns.color_palette(palette='Spectral', n_colors=len(list_ener)).as_hex())
        dict_color_ener = dict(zip(list_ener, paleta_ener))

        fig_ener = px.bar(df_ener, x='Tipo resultado', y='Valor',
                          color='Tipo resultado',
                          color_discrete_map=dict_color_ener,
                          animation_frame='Año',
                          animation_group='Tipo resultado',
                          range_y=[0, 1.2])
        fig_ener.update_xaxes(title='Producción', visible=True)
        fig_ener.update_yaxes(autorange=True, title='',
                              visible=True, showticklabels=True)
        fig_ener.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                               xaxis=dict(tickmode='linear', dtick=1))
        fig_ener.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig_ener)
        st.caption("""Gráfico dinámico de la Energía Neta producida y las Emisiones de CO2 en la Termoeléctrica 
                                    Pakay (2016-2020)."""
                   )
        st.subheader("Tipo de combustibles utilizados y sus Emisiones")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_pakay = pd.read_sql_query("SELECT* FROM Emisiones_Pakay", engine)
        df_pakay[["Emisiones CO2 (TON)"]].astype(float)

        list_pakay = list(set(df_pakay['Combustible']))
        paleta_pakay = list(sns.color_palette(palette='Spectral', n_colors=len(list_pakay)).as_hex())
        dict_color_pakay = dict(zip(list_pakay, paleta_pakay))

        fig = px.bar(df_pakay, x='Combustible', y='Emisiones CO2 (TON)',
                     color='Combustible',
                     color_discrete_map=dict_color_pakay,
                     animation_frame='Año',
                     animation_group='Combustible',
                     range_y=[0, 1.2])
        fig.update_xaxes(title='Tipo de Combustible', visible=True)
        fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                         visible=True, showticklabels=True)
        fig.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                          xaxis=dict(tickmode='linear', dtick=1))
        fig.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig)
        st.caption("""*Gráfico dinámico de las emisiones de CO2 producidas por los distintos tipos de combustibles 
                usados en la Termoeléctrica Pakay (2016-2020).*"""
                   )
    elif opcion_termo=="Sacha":
        sacha[["Termoelectricas","Año","EnergiaBruta(MWH)","Emisiones de CO2 (TON)"]]
        st.caption("""*Resultado de Enegía Neta y Emisiones de CO2 producidas en la Termoelectrica Sacha 
                (2016-2020)*"""
                   )
        st.subheader("Energía Neta vs Emisiones de CO2")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_ener = pd.read_sql_query("SELECT* FROM Energia_Emisiones_Sacha", engine)
        df_ener[["Valor"]].astype(float)

        list_ener = list(set(df_ener['Tipo resultado']))
        paleta_ener = list(sns.color_palette(palette='Spectral', n_colors=len(list_ener)).as_hex())
        dict_color_ener = dict(zip(list_ener, paleta_ener))

        fig_ener = px.bar(df_ener, x='Tipo resultado', y='Valor',
                          color='Tipo resultado',
                          color_discrete_map=dict_color_ener,
                          animation_frame='Año',
                          animation_group='Tipo resultado',
                          range_y=[0, 1.2])
        fig_ener.update_xaxes(title='Producción', visible=True)
        fig_ener.update_yaxes(autorange=True, title='',
                              visible=True, showticklabels=True)
        fig_ener.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                               xaxis=dict(tickmode='linear', dtick=1))
        fig_ener.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig_ener)
        st.caption("""Gráfico dinámico de la Energía Neta producida y las Emisiones de CO2 en la Termoeléctrica 
                            Sacha (2016-2020)."""
                   )
        st.subheader("Tipo de combustibles utilizados y sus Emisiones")
        engine = create_engine("sqlite:///Data/CO2_EOR.db")

        df_sacha = pd.read_sql_query("SELECT* FROM Emisiones_Sacha", engine)
        df_sacha[["Emisiones CO2 (TON)"]].astype(float)

        list_sacha = list(set(df_sacha['Combustible']))
        paleta_sacha = list(sns.color_palette(palette='Spectral', n_colors=len(list_sacha)).as_hex())
        dict_color_sacha = dict(zip(list_sacha, paleta_sacha))

        fig = px.bar(df_sacha, x='Combustible', y='Emisiones CO2 (TON)',
                     color='Combustible',
                     color_discrete_map=dict_color_sacha,
                     animation_frame='Año',
                     animation_group='Combustible',
                     range_y=[0, 1.2])
        fig.update_xaxes(title='Tipo de Combustible', visible=True)
        fig.update_yaxes(autorange=True, title='Emisiones de CO2 (TON)',
                         visible=True, showticklabels=True)
        fig.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                          xaxis=dict(tickmode='linear', dtick=1))
        fig.update_traces(textfont_size=16, textangle=0)
        st.plotly_chart(fig)
        st.caption("""*Gráfico dinámico de las emisiones de CO2 producidas por los distintos tipos de combustibles 
                        usados en la Termoeléctrica Sacha (2016-2020).*"""
                   )

elif options == "Surface Facilities":
    st.header("Facilidades Petroleras")
    st.markdown("""Las facilidades de superficie del centro de producción y facilidades CPF de un campo petrolero, es una 
    estación de flujo donde se realiza el tratamiento del crudo que viene de las áreas de explotación. La producción de 
    crudo se transporta desde los pozos hasta las estaciones, con el método de impulsión a través de un sistema de 
    tuberías de sección circular. El proceso de tratamiento en la estación se realiza mediante una serie de 
    sub-procesos; entre ellos tenemos separación, deshidratación, almacenamiento, bombeo, entre otros. """
                )
    st.markdown("En el **Video 4** se muestra como está conformada una facilidad petrolera.")
    video_surface = open("resources/Surface_Facilities.mp4", "rb")
    st.video(video_surface)
    st.caption("""*Video 4. Andres Torres.(23 de octubre del 2012). Pacific Rubiales - Producción de crudo 
                [Video]. YouTube. Obtenido de https://www.youtube.com/watch?v=3exCgdxa5CU*"""
               )



st.markdown("***Autores:***")
st.markdown("*Kevin Fernando Real Delgado | Student Petroleum Engineer*")
st.markdown("*M.Sc. Freddy Carrión Maldonado | Petroleum Engineer*")