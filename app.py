import streamlit as st 

st.title('Cálculadora')

st.sidebar.title('Parámetros')


valor1 = st.sidebar.number_input('Ingrese el primer valor')
valor2 = st.sidebar.number_input('Ingrese el segundo valor')

proceso = st.selectbox('Seleccione el proceso matemático a realizar', options = ['Suma', 'Resta', 'Multiplicación', 'División'])

def calculadora (valor1, valor2, proceso):
	if proceso == 'Suma':
		respuesta = valor1+valor2
	if proceso == 'Resta':
		respuesta = valor1-valor2
	if proceso == 'Multiplicación':
		respuesta = valor1*valor2
	if proceso == 'División':
		respuesta = valor1/valor2
	return respuesta
respuesta = calculadora(valor1,valor2, proceso)

st.write('El resultado es: {}'.format(respuesta))