import io
import pandas as pd


def load_data(path: str, airline):
    # Read the CSV data directly
    df = pd.read_csv(path)

    # Extract date from tweet_created
    df['tweet_date'] = pd.to_datetime(df['tweet_created']).dt.date
    # print(f"ch{df}")

    # Filter for Virgin America on specified dates
    filtered_df = df[(df['airline'] == airline)]
    print(f"Data here: {filtered_df}")

    # Group by date and calculate average airline sentiment confidence
    df_grouped = filtered_df.groupby('tweet_date')['compound'].mean().reset_index()

    # Rename columns for clarity (optional)
    df_grouped.columns = ['tweet_date', 'average_airline_sentiment_confidence']

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


print(US_Airways)

# Print the results
