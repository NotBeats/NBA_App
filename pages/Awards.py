import streamlit as st
import pandas as pd
import base64

st.title('NBA Awards')

st.markdown("""
Simple webscraping of NBA player stats data.
* **Data Source:** [basketball-reference.com](https://www.basketball-reference.com/)
""")

st.sidebar.header('User Input Features')
year_selected = st.sidebar.selectbox('Year', list(reversed(range(1956,2023))))

# webscraping of NBA player stats 
@st.cache
def load_mvp_data(year):
    url = "https://www.basketball-reference.com/awards/awards_" + str(year) + ".html"
    html = pd.read_html(url, header=1)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rank'], axis=1)
    return playerstats
playerstats = load_mvp_data(year_selected)

st.header('MVP Award')
st.dataframe(playerstats)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download MVP CSV File</a>'
    return href

st.markdown(file_download(playerstats), unsafe_allow_html=True)

@st.cache
def load_roty_data(year):
    url = "https://www.basketball-reference.com/awards/awards_" + str(year) + ".html"
    html = pd.read_html(url, header=1)
    df = html[1]
    raw = df.drop(df[df.Age == 'Age'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rank'], axis=1)
    return playerstats
playerstats = load_roty_data(year_selected)

st.header('ROTY Award')
st.dataframe(playerstats)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download ROTY CSV File</a>'
    return href

st.markdown(file_download(playerstats), unsafe_allow_html=True)

@st.cache
def load_allnba_data(year):
    url = "https://www.basketball-reference.com/awards/awards_" + str(year) + ".html"
    html = pd.read_html(url, header=1)
    df = html[2]
    raw = df.drop(df[df.Age == 'Age'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Pts Max'], axis=1)
    return playerstats
playerstats = load_allnba_data(year_selected)

st.header('All-NBA Teams')
st.dataframe(playerstats)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download All-NBA Teams CSV File</a>'
    return href

st.markdown(file_download(playerstats), unsafe_allow_html=True)