# login.py
import streamlit as st
from bd import verificarLogin



def login():
    st.title("Login")

    email = st.text_input("Email:")
    password = st.text_input("Contrasenia:", type="password")

    if st.button("Login"):
        if verificarLogin(email, password):
            st.success("login valido")
            container = st.empty()
            container.text("ess")
            #st.sidebar.success("test")
        else:
            st.error("usuario o contrasenia inc")
    
    return False




if __name__ == "__main__":
    login()


# def mostrar_info(destino, origen, infodestino, listadestinos):

#     st.write("Distancia (en horas) total del recorrido hasta el destino: ", destino)
#     st.write("El camino mas corto en horas para llegar de ", origen, " a ", infodestino, "Es")  
#     for i in listadestinos: 
#         st.write(i)