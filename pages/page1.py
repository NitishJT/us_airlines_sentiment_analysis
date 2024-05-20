import streamlit as st
import pandas as pd
import numpy as np
# from main import *
from check import *
st.title('SENTIMENT ANALYSIS')
st.header('US AIRLINES')

option = st.selectbox(
    'Select Any US Airline',
    ('Virgin America', 'United', 'Delta', 'US Airways', 'American', 'Southwest'))

print(Virgin_America['tweet_date_formatted'])
value = ['Virgin America', 'United', 'Delta', 'US Airways', 'American', 'Southwest']
value = [item for item in value if item != option]


options = st.multiselect(
    'Comparison Vs other US airlines',
    value)
# chart datas
A = pd.DataFrame(
    {
        "February 2015": Virgin_America['tweet_date_formatted'],
        "Sentiment Score": Virgin_America['average_airline_sentiment_confidence'],
        "List Of US Airlines": np.random.choice(["Virgin_America"], len(Virgin_America['tweet_date_formatted'])),
    }
)
B = pd.DataFrame(
    {
        "February 2015": United['tweet_date_formatted'],
        "Sentiment Score": United['average_airline_sentiment_confidence'],
        "List Of US Airlines": np.random.choice(["United"], len(United['tweet_date_formatted'])),
    }
)
C = pd.DataFrame(
    {
        "February 2015": Delta['tweet_date_formatted'],
        "Sentiment Score": Delta['average_airline_sentiment_confidence'],
        "List Of US Airlines": np.random.choice(["Delta"], len(Delta['tweet_date_formatted'])),
    }
)
D = pd.DataFrame(
    {
        "February 2015": US_Airways['tweet_date_formatted'],
        "Sentiment Score": US_Airways['average_airline_sentiment_confidence'],
        "List Of US Airlines": np.random.choice(["US_Airways"], len(US_Airways['tweet_date_formatted'])),
    }
)
E = pd.DataFrame(
    {
        "February 2015": American['tweet_date_formatted'],
        "Sentiment Score": American['average_airline_sentiment_confidence'],
        "List Of US Airlines": np.random.choice(["American"], len(American['tweet_date_formatted'])),
    }
)
F = pd.DataFrame(
    {
        "February 2015": Southwest['tweet_date_formatted'],
        "Sentiment Score": Southwest['average_airline_sentiment_confidence'],
        "List Of US Airlines": np.random.choice(["Southwest"], len(Southwest['tweet_date_formatted'])),
    }
)
if option == 'Virgin America':
    value = A
else:
    if option == 'United':
        value = B
    else:
        if option == 'Delta':
            value = C
        else:
            if option == 'US Airways':
                value = D
            else:
                if option == 'American':
                    value = E
                else:
                    value = F

#Variable dictionary
variable_dict={
'Virgin America':A, 'United':B, 'Delta':C, 'US Airways':D, 'American':E, 'Southwest':F
}
#Variable dictionary
# chart1 = st.line_chart(value, x="February 2015", y="Sentiment Score", color="List Of US Airlines")
# chart1.add_rows(variable_dict['United'])
# print(f'Hello{variable_dict['United']}')
chart1 = st.line_chart(value, x="February 2015", y="Sentiment Score", color="List Of US Airlines")
for item in options:
    if item in variable_dict:
        chart_value = variable_dict[item]
        chart1.add_rows(chart_value)



# chart datas



