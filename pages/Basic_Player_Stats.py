import streamlit as st
import pandas as pd
import base64

st.title('NBA Basic Player Stats')

st.markdown("""
Simple webscraping of NBA player stats data.
* **Data Source:** [basketball-reference.com](https://www.basketball-reference.com/)
""")

st.sidebar.header('User Input Features')
year_selected = st.sidebar.selectbox('Year', list(reversed(range(1950,2024))))

# webscraping of NBA player stats 
@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(year_selected)

# team selection
sorted_teams = sorted(playerstats.Tm.unique())
team_selected = st.sidebar.multiselect('Team', sorted_teams, sorted_teams)

# position selection
positions = ['PG', 'SG', 'SF', 'PF', 'C']
position_selected = st.sidebar.multiselect('Position', positions, positions)

# filtering data
df_team_selected = playerstats[(playerstats.Tm.isin(team_selected)) & (playerstats.Pos.isin(position_selected))]

st.header('Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_team_selected.shape[0]) + ' rows and ' + str(df_team_selected.shape[1]) + ' columns')
st.dataframe(df_team_selected)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(file_download(df_team_selected), unsafe_allow_html=True)