import streamlit as st
import pandas as pd
import altair as alt

database = pd.read_csv('data\RS_2022.csv', encoding="latin1", sep=",")
siglas = pd.read_csv('data\SIGLAS-2022.csv', encoding="latin1", sep=",")

title, select = st.columns(2)

with title:
    st.title('RS 2022 - Candidatos a Deputado Federal')

with select:
    graph_por_linha, colunas_graph = st.columns(2)
    with graph_por_linha:
        selectedlinhas = select.selectbox('selecione quantidade por linha', ["2","3"])
    with colunas_graph:
        selectedcolunas = select.selectbox('selecione quantidade de colunas', ["12","32","72", "96",'128'])

if selectedlinhas == "2":
    for i in range(1, 17):
        exec(f"col{i * 2 - 1}, col{i * 2} = st.columns(2)")

if selectedlinhas == "3":
    for i in range(1, 12):
        exec(f"col{i * 3 - 2}, col{i * 3 - 1}, col{i * 3} = st.columns(3)")

federais = []
database = database.groupby(['NR_VOTAVEL',"DS_CARGO","NM_VOTAVEL"]).sum({"QT_VOTOS": "sum"})
database = pd.DataFrame(database)
for row in database.itertuples():
    if len(str(row[0][0])) == 4:
        if int(str(row[0][0])[0:2]) in siglas['NUMERO'].values:
            federais.append({
                "NR_PARTIDO": str(row[0][0])[0:2],
                "SIGLA": siglas[siglas['NUMERO'] == int(str(row[0][0])[0:2])]['SIGLA'].values[0],
                "NR_VOTAVEL": row[0][0],
                "NM_VOTAVEL": row[0][2],
                "QT_VOTOS": row[1]
            })

federais = pd.DataFrame(federais)
federais_por_partido = []
partidos = federais['NR_PARTIDO'].unique()
for partido in partidos:
    federais_por_partido.append({
        "NR_PARTIDO": partido,
        "SIGLA": siglas[siglas['NUMERO'] == int(str(partido)[0:2])]['SIGLA'].values[0],
        "DADOS": federais[federais['NR_PARTIDO'] == partido],
        "TOTAL_VOTOS": federais[federais['NR_PARTIDO'] == partido]['QT_VOTOS'].sum()
    })
federais_por_partido = pd.DataFrame(federais_por_partido)
federais_por_partido = federais_por_partido.sort_values(by='TOTAL_VOTOS', ascending=False, ignore_index=True)
for index, partido in federais_por_partido.iterrows():
    candidatos = partido['DADOS'].sort_values(by='QT_VOTOS', ascending=False)
    record_votos = candidatos['QT_VOTOS'].max()
    ranges = []
    graph_data = []
    fraction = record_votos / int(selectedcolunas)
    for i in range(int(selectedcolunas)):
        ranges.append({
            "Quantidade de Votos": f"{int(i * fraction)} - {int((i + 1) * fraction)}",
            "range": {"min": int(i * fraction), "max": int((i + 1) * fraction)},
            "candidatos": [],
            "Quantidade de Candidatos": 0
        })
    for candidato in candidatos.itertuples():
        for r in ranges:
            if r["range"]["min"] <= candidato.QT_VOTOS <= r["range"]["max"]:
                r["candidatos"].append(candidato.NM_VOTAVEL)
                r["Quantidade de Candidatos"] += 1
    ranges = pd.DataFrame(ranges)

    chart = (
    alt.Chart(ranges)
    .mark_bar()
    .encode(
        x=alt.X("Quantidade de Votos", sort=None),
        y="Quantidade de Candidatos",
        tooltip=["Quantidade de Votos", "Quantidade de Candidatos"]
    )
    )
    with eval(f'col{str(index + 1)}'):
        st.write(partido['SIGLA'])
        st.altair_chart(chart, use_container_width=True)

coltemp = federais.pop("NM_VOTAVEL")
federais.insert(0, "NM_VOTAVEL", coltemp)
federais = federais.sort_values(by='QT_VOTOS', ascending=False, ignore_index=True)
graph_partidos, graph_politicos = st.columns(2)

with graph_partidos:
    st.dataframe(federais_por_partido,
                 use_container_width=True,
                 hide_index=True,
                 column_config={
                     "NR_PARTIDO": None,
                     "SIGLA": "Sigla",
                     "TOTAL_VOTOS": "Total de Votos",
                     "DADOS": None

                 })

with graph_politicos:
    st.dataframe(federais,
                 hide_index=True,
                 column_config={
                     "NM_VOTAVEL": "Nome do Candidato",
                     "NR_PARTIDO":  None,
                     "NR_VOTAVEL": None,
                     "SIGLA": "Sigla",
                     "QT_VOTOS": "Total de Votos",

                 })