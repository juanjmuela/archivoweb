import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Archivo Logroño", page_icon="⚖️")

# Función para reiniciar la búsqueda
def reiniciar():
    st.session_state.juzgado_key = "1 INSTANCIA 1"
    st.session_state.año_key = ""

# Título principal
st.title("UBICACIÓN EXPEDIENTES")

# 1. Selector de JUZGADO
opciones_juzgados = [
    "1 INSTANCIA 1", "2 INSTANCIA 2", "3 INSTANCIA 3", "4 INSTANCIA 4",
    "5 INSTANCIA 5", "6 INSTANCIA 6", "7 INSTANCIA 7", "8 INSTRUCCIÓN 1",
    "9 INSTRUCCIÓN 2", "10 INSTRUCCIÓN 3 / VIGILANCIA PENITENCIARIA",
    "11 PENAL 1", "12 PENAL 2", "13 PENAL 3 (Creado en 2020)", "14 VIOLENCIA SOBRE LA MUJER",
    "15 MENORES", "16 SOCIAL 1", "17 SOCIAL 2", "18 SOCIAL 3",
    "19 CONT. ADM 1", "20 CONT. ADM. 2", "21 AUDIENCIA PROV."
]

# Inicializamos el estado si no existe
if 'juzgado_key' not in st.session_state:
    st.session_state.juzgado_key = "1 INSTANCIA 1"
if 'año_key' not in st.session_state:
    st.session_state.año_key = ""

seleccion = st.selectbox("TECLEA O SELECCIONA EL JUZGADO:", opciones_juzgados, key="juzgado_key")
juzgado = int(seleccion.split()[0])

# 2. Cuadro de texto para el AÑO
año_input = st.text_input("TECLEA AÑO (CUATRO DÍGITOS):", key="año_key")

# Botón de reinicio
st.button("🔄 NUEVA CONSULTA (REINICIAR)", on_click=reiniciar)

st.divider()

# 3. Lógica de resultados
if año_input:
    try:
        año = int(año_input)
        st.subheader("RESULTADO:")
        
        # --- TU LÓGICA ORIGINAL ---
        if juzgado == 1 and año > 2014:
            st.success("BLOQUE C PLANTA 1º NORTE C1.4 - DIGITALIZADO")
        if juzgado == 1 and año < 2015:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 2 and año > 2018:
            st.success("BLOQUE C PLANTA 1º SUR C1.3 - DIGITALIZADO")
        if juzgado == 2 and año < 2019:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 3 and año > 2017:
            st.success("BLOQUE C PLANTA 1º SUR C1.2 - NO DIGITALIZADO")
        if juzgado == 3 and año < 2018:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 4 and año > 2018:
            st.success("BLOQUE B PLANTA 1º SUR - DIGITALIZADO")
        if juzgado == 4 and año < 2019:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 5 and año > 2015:
            st.success("BLOQUE B PLANTA 1º NORTE B1.4 - DIGITALIZADO")
        if juzgado == 5 and año < 2016:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 6 and año > 2020:
            st.success("BLOQUE B PLANTA 2º SUR B2.4 - DIGITALIZADO")
        if juzgado == 6 and año < 2021:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 7 and año > 2019:
            st.success("BLOQUE C PLANTA 1º SUR C1.1 - DIGITALIZADO")
        if juzgado == 7 and año < 2020:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 8:
            if 2013 < año < 2019:
                st.success("BLOQUE B PLANTA 1º SUR B1.3 - NO DIGITALIZADO")
            elif año > 2020:
                st.warning("COLEGIO DE ABOGADOS")
            elif año < 2014:
                st.info("PEDIR AL ARCHIVO")
                
        if juzgado == 9:
            st.warning("BLOQUE B PLANTA 1º SUR B1.2 - NO DIGITALIZADO. SI ES MUY NUEVO COLEGIO DE ABOGADOS. SI ES MUY ANTIGUO PEDIR A ARCHIVO. CONSULTAR A CRISTINA")
            
        if juzgado == 10:
            if 2014 < año < 2022:
                st.success("BLOQUE B PLANTA 1º SUR B1.3 - NO DIGITALIZADO")
            elif año > 2021:
                st.warning("COLEGIO DE ABOGADOS")
            elif año < 2015:
                st.info("PEDIR AL ARCHIVO")
                
        if juzgado == 11 and año > 2015:
            st.success("BLOQUE B PLANTA 2º NORTE B2.4 - NO DIGITALIZADO")
        if juzgado == 11 and año < 2016:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 12 and año > 2013:
            st.success("BLOQUE C PLANTA 2º NORTE C2.4 - NO DIGITALIZADO")
        if juzgado == 12 and año < 2014:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 13:
            st.success("EJECUTORIAS BLOQUE B PLANTA 2º NORTE / RESTO EN COLEGIO DE ABOGADOS - DIGITALIZADO")
            
        if juzgado == 14 and año > 2013:
            st.success("BLOQUE A PLANTA 1º SUR A1.3- NO DIGITALIZADO")
        if juzgado == 14 and año < 2014:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 15 and año > 2015:
            st.success("BLOQUE A PLANTA 2º SUR A2.3- DIGITALIZADO")
        if juzgado == 15 and año < 2016:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 16 and año > 2017:
            st.success("BLOQUE A PLANTA 2º SUR A2.1- NO DIGITALIZADO")
        if juzgado == 16 and año < 2018:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 17 and año > 2019:
            st.success("BLOQUE A PLANTA 2º SUR A2.2- NO DIGITALIZADO")
        if juzgado == 17 and año < 2020:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 18 and año > 2017:
            st.success("BLOQUE C PLANTA 2º SUR C2.1- DIGITALIZADO")
        if juzgado == 18 and año < 2018:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 19 and año > 2017:
            st.success("BLOQUE B PLANTA 2º SUR B2.2- NO DIGITALIZADO")
        if juzgado == 19 and año < 2018:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 20 and año > 2014:
            st.success("BLOQUE B PLANTA 2º SUR B2.3- NO DIGITALIZADO")
        if juzgado == 20 and año < 2015:
            st.info("PEDIR AL ARCHIVO")
            
        if juzgado == 21:
            st.success("BLOQUE C PLANTA 3º NORTE - DIGITALIZADO")

    except ValueError:
        st.error("⚠️ El año debe ser un número de 4 cifras.")

st.caption("Recuerda: Si el resultado no aparece, revisa que el año sea correcto.")
