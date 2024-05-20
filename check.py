import pandas as pd


def load_data(path: str, airline):
    # Read the CSV data directly
    df = pd.read_csv(path)

    # Extract date from tweet_created
    df['tweet_date'] = pd.to_datetime(df['tweet_created']).dt.date

    # Filter for the specified airline
    filtered_df = df[df['airline'] == airline]
    print(f"Filtered Data for {airline}:\n", filtered_df.head())

    # Group by date and calculate average airline sentiment confidence
    df_grouped = filtered_df.groupby('tweet_date')['compound'].mean().reset_index()
    print(f"Grouped Data for {airline}:\n", df_grouped.head())

    # Rename columns for clarity
    df_grouped.columns = ['tweet_date', 'average_airline_sentiment_confidence']
    print(f"Renamed Grouped Data for {airline}:\n", df_grouped.head())

    # Convert date to the desired format (e.g., "Sun 22")
    df_grouped['tweet_date_formatted'] = pd.to_datetime(df_grouped['tweet_date']).dt.strftime('%d %a')

    # Return the DataFrame with the formatted date
    result = df_grouped[['tweet_date_formatted', 'average_airline_sentiment_confidence']]
    print(f"Final Data for {airline}:\n", result.head())

    return result


# Example usage
path = 'Sentiment.csv'
Virgin_America = load_data(path, 'Virgin America')
United = load_data(path, 'United')
Delta = load_data(path, 'Delta')
US_Airways = load_data(path, 'US Airways')
American = load_data(path, 'American')
Southwest = load_data(path, 'Southwest')

# Print the results
print(US_Airways)
