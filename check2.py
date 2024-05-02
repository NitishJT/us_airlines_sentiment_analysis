import io
import pandas as pd
import numpy as np

def load_data(path: str, airline):
    # Read the CSV data directly
    df = pd.read_csv(path)

    # Extract date from tweet_created
    df['tweet_date1'] = pd.to_datetime(df['tweet_created']).dt.date
    # print(f"ch{df}")
    df['tweet_date'] = pd.to_datetime(df['tweet_created']).dt.strftime('%Y-%m-%d')


    # Filter for Virgin America on specified dates
    filtered_df = df[(df['airline'] == airline)]
    print(f"Data here: {filtered_df}")

    # Group by date and calculate average airline sentiment confidence
    df_grouped = filtered_df.groupby('tweet_date')['negativereason'].apply(list).reset_index()

    # Rename columns for clarity (optional)
    df_grouped.columns = ['tweet_date','reasons']

    # Return the DataFrame
    return df_grouped


# Example usage
# dates = ["2015-02-24", "2015-02-23", "2015-02-22","2015-02-21","2015-02-20","2015-02-19","2015-02-18","2015-02-17"]
# dates = pd.to_datetime(dates1).dt.date
# Call the function and store the result in a variable
path = 'Sentiment.csv'
Virgin_America = load_data( path,'Virgin America')
United = load_data(path, 'United')
Delta = load_data(path, 'Delta')
US_Airways = load_data(path, 'US Airways')
American = load_data(path, 'American')
Southwest = load_data(path, 'Southwest')
specific_date = '2015-02-18'
filtered_df = Virgin_America[Virgin_America['tweet_date'] == specific_date]

# Access the reasons for the filtered date


reasons_on_specific_date = filtered_df['reasons'].iloc[0]

reason_for_missing = "Missing Reason"  # You can change this string if you prefer

reasons_on_specific_date = [reason_for_missing if x is np.NAN else x for x in reasons_on_specific_date]



print(reasons_on_specific_date)
# print(f'hello iam here{Virgin_America[]}')

# Print the results
