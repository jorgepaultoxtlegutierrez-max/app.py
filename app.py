tab1, tab2 = st.tabs(["📝 Examen", "📊 Informe de Resultados"])

with tab1:
    # Aquí iría todo el código del formulario (with st.form...)
    pass

with tab2:
    if boton_enviar:
        st.markdown(f"### Tu nota es: {nota}")
        # Bucle para mostrar qué fallaron
        for i in range(len(preguntas)):
            if respuestas_usuario[i] == preguntas[i]["correcta"]:
                st.write(f"✅ Pregunta {i+1}: Correcta")
            else:
                st.write(f"❌ Pregunta {i+1}: Incorrecta (Era: {preguntas[i]['correcta']})")
