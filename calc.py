import streamlit as st 
import numpy as np

def main():

	st.title("Demo web kalkulator EUR")

	with st.form(key='myform', clear_on_submit = True):
		cijena_u_EUR = st.number_input("Molimo unesite cijenu ulaznice u EUR", step=1.00)
		cijena_u_KN = float(7.53450) * float(cijena_u_EUR)
		primljeno_u_KN = st.number_input("Molimo unesite iznos primljen u KUNAMA", step=10.00)
		povrat_u_KN = float(primljeno_u_KN) - float(cijena_u_KN)
		povrat_u_EUR = float(povrat_u_KN)/float(7.53450)
		
		submit_button = st.form_submit_button("Unesi podatke")

		if submit_button:
			st.header('Iznos povrata u EUR je:', )
			st.header(np.round(float(povrat_u_EUR),2))
			


if __name__ == '__main__':
	main()