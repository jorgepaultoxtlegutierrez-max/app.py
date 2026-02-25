import streamlit as st
# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("La Calculadora de Rebajas ")
st.markdown("**Bienvenido**, introduce tus datos para calcular lo que tienes que pagar despues de las rebajas.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio_original= st.sidebar.number_input("El precio (€)", min_value=0, max_value=100000, value=15000)
descuento= st.sidebar.slider("La rebaja (%)", 0.00, 100.00, 50.00)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
   
    # Fórmula Matemática: Precio por el descuento entre 100
    ahorro = precio_original * (descuento / 100)
    precio_final = precio_original - ahorro
   
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
     
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu precio final", value=f"{precio_final:.2f}")
       
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if descuento < 10:
            st.warning("Buen descuento")
            st.write("algo es algo.")
            st.snow()
        elif descuento < 50 > 30 :
            st.success("descuentazo")
        elif descuento > 50 :
            st.warning("¡Menudo Chollo!")
            st.write("que suertee.")
            st.balloons() # ¡Premio!
