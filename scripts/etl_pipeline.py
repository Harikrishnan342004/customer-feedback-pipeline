import pandas as pd 
import os


#Load the raw feedback CSV

raw_data_path = r"C:\Users\HARI KRISHNAN\Desktop\happy_customers_project\data\raw_feedback.csv"

df = pd.read_csv(raw_data_path)

print("Raw data loaded:")
print(df.head( ))

#Clean data

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

#Step 3: Add sentiment column based on Rating

def get_sentiment(rating):
    if(rating <= 2):
        return "Negative"
    elif rating == 3:
        return "Neutral"
    else:
        return "Positive"

df["Sentiment"] = df["Rating"].apply(get_sentiment)



# Step 4: Save Clean Data

cleaned_data_path = "data/cleaned_feedback.csv"

# Ensure the output directory exists
os.makedirs(os.path.dirname(cleaned_data_path), exist_ok=True)

df.to_csv(cleaned_data_path, index=False)

print(f"Cleaned data saved to: {cleaned_data_path}")
