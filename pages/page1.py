import streamlit as st
import pandas as pd
import numpy as np
# from main import *
from check import *


option = st.selectbox(
    'Select US Airlines',
    ('Virgin America', 'United', 'Delta', 'US Airways', 'American', 'Southwest'))

print(Virgin_America['tweet_date'])
value = ['Virgin America', 'United', 'Delta', 'US Airways', 'American', 'Southwest']
value = [item for item in value if item != option]


options = st.multiselect(
    'Comparison Vs US airlines',
    value)
# chart datas
A = pd.DataFrame(
    {
        "col1": Virgin_America['tweet_date'],
        "col2": Virgin_America['average_airline_sentiment_confidence'],
        "col3": np.random.choice(["Virgin_America"], len(Virgin_America['tweet_date'])),
    }
)
B = pd.DataFrame(
    {
        "col1": United['tweet_date'],
        "col2": United['average_airline_sentiment_confidence'],
        "col3": np.random.choice(["United"], len(United['tweet_date'])),
    }
)
C = pd.DataFrame(
    {
        "col1": Delta['tweet_date'],
        "col2": Delta['average_airline_sentiment_confidence'],
        "col3": np.random.choice(["Delta"], len(Delta['tweet_date'])),
    }
)
D = pd.DataFrame(
    {
        "col1": US_Airways['tweet_date'],
        "col2": US_Airways['average_airline_sentiment_confidence'],
        "col3": np.random.choice(["US_Airways"], len(US_Airways['tweet_date'])),
    }
)
E = pd.DataFrame(
    {
        "col1": American['tweet_date'],
        "col2": American['average_airline_sentiment_confidence'],
        "col3": np.random.choice(["American"], len(American['tweet_date'])),
    }
)
F = pd.DataFrame(
    {
        "col1": Southwest['tweet_date'],
        "col2": Southwest['average_airline_sentiment_confidence'],
        "col3": np.random.choice(["Southwest"], len(Southwest['tweet_date'])),
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
# chart1 = st.line_chart(value, x="col1", y="col2", color="col3")
# chart1.add_rows(variable_dict['United'])
# print(f'Hello{variable_dict['United']}')
chart1 = st.line_chart(value, x="col1", y="col2", color="col3")
for item in options:
    if item in variable_dict:
        chart_value = variable_dict[item]
        chart1.add_rows(chart_value)



# chart datas



