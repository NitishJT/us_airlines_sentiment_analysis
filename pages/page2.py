import streamlit as st
from check2 import *
import matplotlib.pyplot as plt

A = Virgin_America
B = United
C = Delta
D = US_Airways
E = American
F = Southwest
variable_dict = {
    'Virgin America': A, 'United': B, 'Delta': C, 'US Airways': D, 'American': E, 'Southwest': F
}

value = ['Virgin America', 'United', 'Delta', 'US Airways', 'American', 'Southwest']

genre = st.radio(
    "Select US Airlines",
    ['Virgin America', 'United', 'Delta', 'US Airways', 'American', 'Southwest'],
    index=None,
)

date_value = []
if genre is not None:
    date_value = variable_dict[genre]['tweet_date']
st.write("You selected:", genre)
option = st.selectbox(
    'Select The dates',
    (date_value))

st.write('You selected:', option)
pie_value = []
date = []
reasons_on_specific_date = ['Select any US Airlines']
if option is not None:
    date = f'{option}'
    specific_date = date
    temp = variable_dict[genre]
    filtered_df = temp[temp['tweet_date'] == specific_date]

    # Access the reasons for the filtered date
    reasons_on_specific_date = filtered_df['reasons'].iloc[0]

    reason_for_missing = "Missing Reason"  # You can change this string if you prefer

    reasons_on_specific_date = [reason_for_missing if x is np.NAN else x for x in reasons_on_specific_date]

# Sample data (replace with your actual data)
data_list = reasons_on_specific_date

value_counts = pd.Series(reasons_on_specific_date).value_counts().sort_values(ascending=False)
print(value_counts)
# Extract labels and sizes for the pie chart
labels = value_counts.index.to_numpy()
sizes = value_counts.to_numpy()

# Ensure explode has the same length as sizes
explode_length = len(value_counts)
explode = [0.1] + [0 for _ in range(explode_length - 1)]

# Create the pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, **{'textprops': {'fontsize': 5}})
ax1.axis('equal')  # Equal aspect ratio ensures a circular pie

# Display the chart in Streamlit
st.pyplot(fig1)

# Print additional information (optional)
st.write(f'Count of each complaints:')
for item, count in value_counts.items():
    st.write(f"- {item}: {count}")
