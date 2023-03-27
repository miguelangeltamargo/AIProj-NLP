#You Got Python

import pandas as pd
import re

# Load dataset
def handle_bad_line(line):
	print(f"Skipping bad line: {line}")
	
data = pd.read_csv('training.1600000.csv', encoding='ISO-8859-1')

# Remove URLs, special characters, and usernames
data['tweet'] = data['tweet'].apply(lambda x: re.sub(r'http\S+', '', x))  # remove URLs
data['tweet'] = data['tweet'].apply(lambda x: re.sub(r'[^\w\s]', '', x))  # remove special characters
data['tweet'] = data['tweet'].apply(lambda x: re.sub(r'@\w+', '', x))  # remove usernames

# Remove hashtags (#)
data['tweet'] = data['tweet'].apply(lambda x: re.sub(r'#\S+', '', x))

# Remove punctuation marks
data['tweet'] = data['tweet'].str.replace('[^\w\s]','', regex=True)

# Convert all letters to lowercase
data['tweet'] = data['tweet'].str.lower()

# Remove leading and trailing whitespaces
data['tweet'] = data['tweet'].str.strip()

# Save the preprocessed data to a new CSV file
data.to_csv('preprocessed_tweets.csv', index=False)

