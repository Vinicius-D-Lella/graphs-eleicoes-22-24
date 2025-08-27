import streamlit as st
import pandas as pd
import altair as alt

expo = [
    {"min": 0, "max": 500, "label": "0 - 500"},
    {"min": 501, "max": 1000, "label": "501 - 1000"},
    {"min": 1001, "max": 1500, "label": "1001 - 1500"},
    {"min": 1501, "max": 2000, "label": "1501 - 2000"},
    {"min": 2001, "max": 2500, "label": "2001 - 2500"},
    {"min": 2501, "max": 3000, "label": "2501 - 3000"},
    {"min": 3001, "max": 3500, "label": "3001 - 3500"},
    {"min": 3501, "max": 4000, "label": "3501 - 4000"},
    {"min": 4001, "max": 4500, "label": "4001 - 4500"},
    {"min": 4501, "max": 5000, "label": "4501 - 5000"},
    {"min": 5001, "max": 5500, "label": "5001 - 5500"},
    {"min": 5501, "max": 6000, "label": "5501 - 6000"},
    {"min": 6001, "max": 6500, "label": "6001 - 6500"},
    {"min": 6501, "max": 7000, "label": "6501 - 7000"},
    {"min": 7001, "max": 7500, "label": "7001 - 7500"},
    {"min": 7501, "max": 8000, "label": "7501 - 8000"},
    {"min": 8001, "max": 8500, "label": "8001 - 8500"},
    {"min": 8501, "max": 9000, "label": "8501 - 9000"},
    {"min": 9001, "max": 9500, "label": "9001 - 9500"},
    {"min": 9501, "max": 10000, "label": "9501 - 10000"},
    {"min": 10001, "max": 10500, "label": "10001 - 10500"},
    {"min": 10501, "max": 11000, "label": "10501 - 11000"},
    {"min": 11001, "max": 11500, "label": "11001 - 11500"},
    {"min": 11501, "max": 12000, "label": "11501 - 12000"},
    {"min": 12001, "max": 12500, "label": "12001 - 12500"},
    {"min": 12501, "max": 13000, "label": "12501 - 13000"},
    {"min": 13001, "max": 13500, "label": "13001 - 13500"},
    {"min": 13501, "max": 14000, "label": "13501 - 14000"},
    {"min": 14001, "max": 14500, "label": "14001 - 14500"},
    {"min": 14501, "max": 15000, "label": "14501 - 15000"},
    {"min": 15001, "max": 15500, "label": "15001 - 15500"},
    {"min": 15501, "max": 16000, "label": "15501 - 16000"},
    {"min": 16001, "max": 16500, "label": "16001 - 16500"},
    {"min": 16501, "max": 17000, "label": "16501 - 17000"},
    {"min": 17001, "max": 17500, "label": "17001 - 17500"},
    {"min": 17501, "max": 18000, "label": "17501 - 18000"},
    {"min": 18001, "max": 18500, "label": "18001 - 18500"},
    {"min": 18501, "max": 19000, "label": "18501 - 19000"},
    {"min": 19001, "max": 19500, "label": "19001 - 19500"},
    {"min": 19501, "max": 20000, "label": "19501 - 20000"},
    {"min": 20001, "max": 20500, "label": "20001 - 20500"},
    {"min": 20501, "max": 21000, "label": "20501 - 21000"},
    {"min": 21001, "max": 21500, "label": "21001 - 21500"},
    {"min": 21501, "max": 22000, "label": "21501 - 22000"},
    {"min": 22001, "max": 22500, "label": "22001 - 22500"},
    {"min": 22501, "max": 23000, "label": "22501 - 23000"},
    {"min": 23001, "max": 23500, "label": "23001 - 23500"},
    {"min": 23501, "max": 24000, "label": "23501 - 24000"},
    {"min": 24001, "max": 24500, "label": "24001 - 24500"},
    {"min": 24501, "max": 25000, "label": "24501 - 25000"},
    {"min": 25001, "max": 25500, "label": "25001 - 25500"},
    {"min": 25501, "max": 26000, "label": "25501 - 26000"},
    {"min": 26001, "max": 26500, "label": "26001 - 26500"},
    {"min": 26501, "max": 27000, "label": "26501 - 27000"},
    {"min": 27001, "max": 27500, "label": "27001 - 27500"},
    {"min": 27501, "max": 28000, "label": "27501 - 28000"},
    {"min": 28001, "max": 28500, "label": "28001 - 28500"},
    {"min": 28501, "max": 29000, "label": "28501 - 29000"},
    {"min": 29001, "max": 29500, "label": "29001 - 29500"},
    {"min": 29501, "max": 30000, "label": "29501 - 30000"},
    {"min": 30001, "max": 30500, "label": "30001 - 30500"},
    {"min": 30501, "max": 31000, "label": "30501 - 31000"},
    {"min": 31001, "max": 31500, "label": "31001 - 31500"},
    {"min": 31501, "max": 32000, "label": "31501 - 32000"},
    {"min": 32001, "max": 32500, "label": "32001 - 32500"},
    {"min": 32501, "max": 33000, "label": "32501 - 33000"},
    {"min": 33001, "max": 33500, "label": "33001 - 33500"},
    {"min": 33501, "max": 34000, "label": "33501 - 34000"},
    {"min": 34001, "max": 34500, "label": "34001 - 34500"},
    {"min": 34501, "max": 35000, "label": "34501 - 35000"},
    {"min": 35001, "max": 35500, "label": "35001 - 35500"},
    {"min": 35501, "max": 36000, "label": "35501 - 36000"},
    {"min": 36001, "max": 36500, "label": "36001 - 36500"},
    {"min": 36501, "max": 37000, "label": "36501 - 37000"},
    {"min": 37001, "max": 37500, "label": "37001 - 37500"},
    {"min": 37501, "max": 38000, "label": "37501 - 38000"},
    {"min": 38001, "max": 38500, "label": "38001 - 38500"},
    {"min": 38501, "max": 39000, "label": "38501 - 39000"},
    {"min": 39001, "max": 39500, "label": "39001 - 39500"},
    {"min": 39501, "max": 40000, "label": "39501 - 40000"},
    {"min": 40001, "max": 40500, "label": "40001 - 40500"},
    {"min": 40501, "max": 41000, "label": "40501 - 41000"},
    {"min": 41001, "max": 41500, "label": "41001 - 41500"},
    {"min": 41501, "max": 42000, "label": "41501 - 42000"},
    {"min": 42001, "max": 42500, "label": "42001 - 42500"},
    {"min": 42501, "max": 43000, "label": "42501 - 43000"},
    {"min": 43001, "max": 43500, "label": "43001 - 43500"},
    {"min": 43501, "max": 44000, "label": "43501 - 44000"},
    {"min": 44001, "max": 44500, "label": "44001 - 44500"},
    {"min": 44501, "max": 45000, "label": "44501 - 45000"},
    {"min": 45001, "max": 45500, "label": "45001 - 45500"},
    {"min": 45501, "max": 46000, "label": "45501 - 46000"},
    {"min": 46001, "max": 46500, "label": "46001 - 46500"},
    {"min": 46501, "max": 47000, "label": "46501 - 47000"},
    {"min": 47001, "max": 47500, "label": "47001 - 47500"},
    {"min": 47501, "max": 48000, "label": "47501 - 48000"},
    {"min": 48001, "max": 48500, "label": "48001 - 48500"},
    {"min": 48501, "max": 49000, "label": "48501 - 49000"},
    {"min": 49001, "max": 49500, "label": "49001 - 49500"},
    {"min": 49501, "max": 50000, "label": "49501 - 50000"},
    {"min": 50001, "max": 60000, "label": "50001 - 60000"},
    {"min": 60001, "max": 70000, "label": "50001 - 60000"},
    {"min": 70001, "max": 80000, "label": "70001 - 80000"},
    {"min": 80001, "max": 90000, "label": "80001 - 90000"},
    {"min": 90001, "max": 100000, "label": "90001 - 100000"},
    {"min": 100001, "max": 125000, "label": "100001 - 125000"},
    {"min": 125001, "max": 150000, "label": "125001 - 150000"},
    {"min": 150001, "max": 175000, "label": "150001 - 175000"},
    {"min": 175001, "max": 200000, "label": "175001 - 200000"},
    {"min": 200001, "max": 225000, "label": "200001 - 225000"},
    {"min": 225001, "max": 250000, "label": "225001 - 250000"},
    {"min": 250001, "max": 275000, "label": "250001 - 275000"},
    {"min": 275001, "max": 300000, "label": "275001 - 300000"},
    {"min": 300001, "max": 350000, "label": "300001 - 350000"},
    {"min": 350001, "max": 400000, "label": "350001 - 400000"},
    {"min": 400001, "max": 450000, "label": "400001 - 450000"},
    {"min": 450001, "max": 500000, "label": "450001 - 500000"},
    {"min": 500001, "max": 600000, "label": "500001 - 600000"},
    {"min": 600001, "max": 700000, "label": "600001 - 700000"},
    {"min": 700001, "max": 800000, "label": "700001 - 800000"},
    {"min": 800001, "max": 900000, "label": "800001 - 900000"},
    {"min": 900001, "max": 1000000, "label": "900001 - 1000000"},
    {"min": 1000001, "max": 3000000, "label": "1000001 - 3000000"},
]

titulo , ano = st.columns(2)

with ano:
    ano_atual = st.selectbox('Selecione o ano:', [2022, 2024])
with titulo:
    if ano_atual == 2022:
        st.title(f'RJ 2022 - Candidatos à Deputado Federal')
    if ano_atual == 2024:
        st.title(f'RJ 2024 - Candidatos à Vereador')


database = pd.read_csv(f'data/AC_{ano_atual}.csv', encoding="latin1", sep=",")
siglas = pd.read_csv(f'data/SIGLAS-{ano_atual}.csv', encoding="latin1", sep=",")

if ano_atual == 2022:
    for i in range(1, 17):
        exec(f"col{i * 2 - 1}, col{i * 2} = st.columns(2)")
else:
    for i in range(1, 12):
        exec(f"col{i * 3 - 2}, col{i * 3 - 1}, col{i * 3} = st.columns(3)")
federais = []
if ano_atual == 2024:
    database = database.rename(columns={"NR_CANDIDATO": "NR_VOTAVEL", "NM_URNA_CANDIDATO": "NM_VOTAVEL", "QT_VOTOS_NOMINAIS": "QT_VOTOS"})
database = database.groupby(['NR_VOTAVEL',"DS_CARGO","NM_VOTAVEL"]).sum({"QT_VOTOS": "sum"})
database = pd.DataFrame(database)
for row in database.itertuples():
    if len(str(row[0][0])) == 4 if ano_atual == 2022 else 5:
        print(row)
        if ano_atual == 2022:
            votos = row[1]
        else:
            votos = row[2]
        federais.append({
                "NR_PARTIDO": str(row[0][0])[0:2],
                "SIGLA": siglas[siglas['NUMERO'] == int(str(row[0][0])[0:2])]['SIGLA'].values[0],
                "NR_VOTAVEL": row[0][0],
                "NM_VOTAVEL": row[0][2],
                "QT_VOTOS": votos
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
    for i in range(123):
        if record_votos < expo[i]['min']:
            break
        total = candidatos[candidatos['QT_VOTOS'] <= expo[i]['max']]['QT_VOTOS'].sum()
        porcentagem = total / candidatos['QT_VOTOS'].sum() * 100
        porcentagems = str(porcentagem).split(".")
        ranges.append({
            "Quantidade de Votos": f"{expo[i]['min']} - {expo[i]['max']}",
            "range": {"min": expo[i]['min'], "max": expo[i]['max']},
            "candidatos": [],
            "Quantidade de Candidatos": 0,
            "Porcentagem de votos até aqui": float(porcentagems[0] + "." + porcentagems[1][0:2]),
            "Votos nesse range": 0

        })
    for candidato in candidatos.itertuples():
        for r in ranges:
            if r["range"]["min"] <= candidato.QT_VOTOS <= r["range"]["max"]:
                r["candidatos"].append(candidato.NM_VOTAVEL)
                r["Quantidade de Candidatos"] += 1
                r["Votos nesse range"] += candidato.QT_VOTOS
    ranges = pd.DataFrame(ranges)
    barras = (
    alt.Chart(ranges)
    .mark_bar(opacity=0.7, color="orange")
    .encode(
        x=alt.X("Quantidade de Votos", sort=None),
        y="Quantidade de Candidatos",
    tooltip=["Quantidade de Votos", "Porcentagem de votos até aqui","Quantidade de Candidatos","Votos nesse range"]
    )
    )

    area = alt.Chart(ranges).mark_area(opacity=0.3, color="steelblue").encode(
    x=alt.X("Quantidade de Votos", sort=None),
    y=alt.Y("Porcentagem de votos até aqui", axis=alt.Axis(title="Votos (%)")),
    tooltip=["Quantidade de Votos", "Porcentagem de votos até aqui","Quantidade de Candidatos","Votos nesse range"]
    )


    chart = (barras + area  ).resolve_scale(
    y='independent'
    ).properties(
    title="Candidatos e quantitade de votos"
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