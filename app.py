import streamlit as st

# Inputs
precio_orig = st.number_input("Precio original (€)", min_value=0.0)
desc = st.slider("Descuento (%)", 0, 100)

# Lógica
ahorro = precio_orig * (desc / 100)
precio_final = precio_orig - ahorro

# Salida
st.metric("Precio Final", f"{precio_final:.2f} €")

if desc > 50:
    st.success(f"¡Menudo Chollo! Te ahorras {ahorro:.2f} €")
    st.balloons()
    
