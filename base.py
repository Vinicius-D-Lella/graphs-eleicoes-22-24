import streamlit as st

pages = {
    "Home": [
        st.Page("home.py", title="Home"),
    ],
    "Estados": [
        st.Page("estados/acre.py", title="Acre"),
        st.Page("estados/alagoas.py", title="Alagoas"),
        st.Page("estados/amazonas.py", title="Amazonas"),
        st.Page("estados/amapa.py", title="Amapá"),
        st.Page("estados/bahia.py", title="Bahia"),
        st.Page("estados/ceara.py", title="Ceará"),
        st.Page("estados/distrito_federal.py", title="Distrito Federal"),
        st.Page("estados/espirito_santo.py", title="Espírito Santo"),
        st.Page("estados/goias.py", title="Goiás"),
        st.Page("estados/maranhao.py", title="Maranhão"),
        st.Page("estados/minas_gerais.py", title="Minas Gerais"),
        st.Page("estados/mato_grosso_do_sul.py", title="Mato Grosso do Sul"),
        st.Page("estados/mato_grosso.py", title="Mato Grosso"),
        st.Page("estados/para.py", title="Pará"),
        st.Page("estados/paraiba.py", title="Paraíba"),
        st.Page("estados/pernambuco.py", title="Pernambuco"),
        st.Page("estados/piaui.py", title="Piauí"),
        st.Page("estados/parana.py", title="Paraná"),
        st.Page("estados/rio_de_janeiro.py", title="Rio de Janeiro"),
        st.Page("estados/rio_grande_do_norte.py", title="Rio Grande do Norte"),
        st.Page("estados/rondonia.py", title="Rondônia"),
        st.Page("estados/roraima.py", title="Roraima"),
        st.Page("estados/rio_grande_do_sul.py", title="Rio Grande do Sul"),
        st.Page("estados/santa_catarina.py", title="Santa Catarina"),
        st.Page("estados/sergipe.py", title="Sergipe"),
        st.Page("estados/sao_paulo.py", title="São Paulo"),
        st.Page("estados/tocantins.py", title="Tocantins")
    ]
}

st.set_page_config(layout="wide")
pg = st.navigation(pages)
pg.run()