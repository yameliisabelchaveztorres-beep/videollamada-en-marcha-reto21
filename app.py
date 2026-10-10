import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Videollamada en Marcha",
    page_icon="🌷",
    layout="centered"
)

st.title("🌷 Videollamada en Marcha")
st.subheader("Reto de 21 días")
st.write("Evaluación de bienestar y seguimiento personalizado")

st.divider()

st.header("1. Datos del prospecto")
nombre = st.text_input("Nombre completo")
edad = st.number_input("Edad", min_value=1, max_value=110, value=30)
fecha = st.date_input("Fecha de evaluación", value=date.today())
contacto = st.text_input("Teléfono o contacto (opcional)")

st.header("2. Conoce sus objetivos")
objetivo = st.selectbox(
    "¿Cuál es tu principal objetivo?",
    [
        "Bajar de peso",
        "Mejorar mis hábitos alimenticios",
        "Tener más energía",
        "Aumentar masa muscular",
        "Mejorar mi bienestar general"
    ]
)

motivacion = st.text_area(
    "¿Por qué es importante para ti lograr este objetivo?"
)

st.header("3. Hábitos diarios")
agua = st.selectbox(
    "¿Cuánta agua tomas al día?",
    ["Menos de 1 litro", "Entre 1 y 2 litros", "Más de 2 litros"]
)
actividad = st.selectbox(
    "¿Realizas actividad física?",
    ["Nunca", "1-2 días por semana", "3-4 días por semana", "5 o más días"]
)
descanso = st.selectbox(
    "¿Cómo calificas tu descanso?",
    ["Bueno", "Regular", "Necesito mejorarlo"]
)
alimentacion = st.text_area(
    "Cuéntame cómo es tu alimentación habitual"
)

st.header("4. Medidas opcionales")
peso = st.number_input(
    "Peso en kg", min_value=0.0, max_value=400.0, value=0.0, step=0.1
)
estatura = st.number_input(
    "Estatura en cm", min_value=0.0, max_value=250.0, value=0.0, step=0.5
)

if peso > 0 and estatura > 0:
    imc = peso / ((estatura / 100) ** 2)
    st.metric("IMC calculado", f"{imc:.1f}")
    st.caption(
        "El IMC es una medida orientativa; no mide directamente la grasa corporal "
        "ni sustituye una evaluación profesional."
    )

st.header("5. Conversación sobre el reto")
dificultad = st.text_area(
    "¿Qué dificultad te impide alcanzar tu objetivo actualmente?"
)
compromiso = st.selectbox(
    "¿Te gustaría trabajar en tus hábitos durante 21 días?",
    ["Sí", "Quiero conocer más información", "Por ahora no"]
)
notas = st.text_area("Notas privadas para tu seguimiento")

if st.button("Preparar resumen de la evaluación", type="primary"):
    resumen = f"""
# Evaluación de bienestar
**Nombre:** {nombre}
**Edad:** {edad}
**Fecha:** {fecha}
**Contacto:** {contacto}
**Objetivo:** {objetivo}
**Motivación:** {motivacion}
**Agua:** {agua}
**Actividad física:** {actividad}
**Descanso:** {descanso}
**Alimentación habitual:** {alimentacion}
**Peso (kg):** {peso if peso > 0 else "No registrado"}
**Estatura (cm):** {estatura if estatura > 0 else "No registrada"}
**Dificultad principal:** {dificultad}
**Interés en el reto:** {compromiso}
**Notas:** {notas}
"""
    st.success("¡Resumen preparado!")
    st.text_area("Puedes copiar el siguiente resumen", resumen, height=350)
    st.download_button(
        "Descargar resumen",
        data=resumen,
        file_name="evaluacion_bienestar.txt",
        mime="text/plain"
    )

st.divider()
st.caption(
    "Los datos introducidos se usan para preparar este resumen. "
    "Esta versión no guarda automáticamente un historial de clientes. "
    "Protege la información personal y utiliza los datos con autorización."
)
