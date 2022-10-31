import streamlit as st
import pandas as pd
import base64

st.title('NBA Team Standings')

st.markdown("""
Simple webscraping of NBA team stats data.
* **Data Source:** [basketball-reference.com](https://www.basketball-reference.com/)
""")

st.sidebar.header('User Input Features')
year_selected = st.sidebar.selectbox('Year', list(reversed(range(1950,2024))))

# webscraping of NBA player stats 
@st.cache
def load_east_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_standings.html"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.W == 'W'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['SRS'], axis=1)
    return teamstats
teamstats = load_east_data(year_selected)

st.header('East Team Standings')
st.dataframe(teamstats)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="teamstats.csv">Download East CSV File</a>'
    return href

st.markdown(file_download(teamstats), unsafe_allow_html=True)

@st.cache
def load_west_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_standings.html"
    html = pd.read_html(url, header=0)
    df = html[1]
    raw = df.drop(df[df.W == 'W'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['SRS'], axis=1)
    return teamstats
teamstats = load_west_data(year_selected)

st.header('West Team Standings')
st.dataframe(teamstats)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="teamstats.csv">Download West CSV File</a>'
    return href

st.markdown(file_download(teamstats), unsafe_allow_html=True)