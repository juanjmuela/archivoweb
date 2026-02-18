import streamlit as st

# Configuración básica
st.set_page_config(page_title="Archivo Logroño", page_icon="📚​")

# Función de reinicio
if 'año_key' not in st.session_state:
    st.session_state.año_key = ""

def limpiar():
    st.session_state.año_key = ""

st.title("UBICACIÓN EXPEDIENTES 📚​")

# 1. Selector de JUZGADO
opciones = [
    "1 INSTANCIA 1", "2 INSTANCIA 2", "3 INSTANCIA 3", "4 INSTANCIA 4",
    "5 INSTANCIA 5", "6 INSTANCIA 6", "7 INSTANCIA 7", "8 INSTRUCCIÓN 1",
    "9 INSTRUCCIÓN 2", "10 INSTRUCCIÓN 3 / VIGILANCIA PENITENCIARIA",
    "11 PENAL 1", "12 PENAL 2", "13 PENAL 3 (Creado en 2020)", "14 VIOLENCIA SOBRE LA MUJER",
    "15 MENORES", "16 SOCIAL 1", "17 SOCIAL 2", "18 SOCIAL 3",
    "19 CONT. ADM 1", "20 CONT. ADM. 2", "21 AUDIENCIA PROV."
]
seleccion = st.selectbox("SELECCIONA JUZGADO:", opciones)
juzgado = int(seleccion.split()[0])

# 2. Entrada de AÑO
año_input = st.text_input("TECLEA AÑO (4 DÍGITOS):", key="año_key")

if st.button("🔄 NUEVA CONSULTA"):
    limpiar()
    st.rerun()

st.divider()

# 3. LÓGICA DE BÚSQUEDA
if año_input.isdigit():
    año = int(año_input)
    st.subheader("RESULTADO:")
    
    # Aquí aplicamos tu lógica original
    if juzgado == 1:
        st.success("BLOQUE C PLANTA 1º NORTE C1.4 - DIGITALIZADO") if año > 2014 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 2:
        st.success("BLOQUE C PLANTA 1º SUR C1.3 - DIGITALIZADO") if año > 2018 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 3:
        st.success("BLOQUE C PLANTA 1º SUR C1.2 - NO DIGITALIZADO") if año > 2017 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 4:
        st.success("BLOQUE B PLANTA 1º SUR - DIGITALIZADO") if año > 2018 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 5:
        st.success("BLOQUE B PLANTA 1º NORTE B1.4 - DIGITALIZADO") if año > 2015 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 6:
        st.success("BLOQUE B PLANTA 2º SUR B2.4 - DIGITALIZADO") if año > 2020 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 7:
        st.success("BLOQUE C PLANTA 1º SUR C1.1 - DIGITALIZADO") if año > 2019 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 8:
        if 2013 < año < 2019: st.success("BLOQUE B PLANTA 1º SUR B1.3 - NO DIGITALIZADO")
        elif año >= 2019: st.warning("COLEGIO DE ABOGADOS")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado == 9:
        st.warning("BLOQUE B PLANTA 1º SUR B1.2 - NO DIGITALIZADO. CONSULTAR A CRISTINA")
    elif juzgado == 10:
        if 2014 < año < 2022: st.success("BLOQUE B PLANTA 1º SUR B1.3 - NO DIGITALIZADO")
        elif año >= 2022: st.warning("COLEGIO DE ABOGADOS")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado == 11:
        st.success("BLOQUE B PLANTA 2º NORTE B2.4 - NO DIGITALIZADO") if año > 2015 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 12:
        st.success("BLOQUE C PLANTA 2º NORTE C2.4 - NO DIGITALIZADO") if año > 2013 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 13:
        st.success("EJECUTORIAS BLOQUE B PLANTA 2º NORTE / RESTO EN COLEGIO DE ABOGADOS")
    elif juzgado == 14:
        st.success("BLOQUE A PLANTA 1º SUR A1.3- NO DIGITALIZADO") if año > 2013 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 15:
        st.success("BLOQUE A PLANTA 2º SUR A2.3- DIGITALIZADO") if año > 2015 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 16:
        st.success("BLOQUE A PLANTA 2º SUR A2.1- NO DIGITALIZADO") if año > 2017 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 17:
        st.success("BLOQUE A PLANTA 2º SUR A2.2- NO DIGITALIZADO") if año > 2019 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 18:
        st.success("BLOQUE C PLANTA 2º SUR C2.1- DIGITALIZADO") if año > 2017 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 19:
        st.success("BLOQUE B PLANTA 2º SUR B2.2- NO DIGITALIZADO") if año > 2017 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 20:
        st.success("BLOQUE B PLANTA 2º SUR B2.3- NO DIGITALIZADO") if año > 2014 else st.info("PEDIR AL ARCHIVO")
    elif juzgado == 21:
        st.success("BLOQUE C PLANTA 3º NORTE - DIGITALIZADO")
elif año_input != "":
    st.error("Por favor, introduce solo números para el año.")
