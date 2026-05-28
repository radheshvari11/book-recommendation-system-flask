import pandas as pd

df = pd.read_csv("data/books.csv")

def recommend(book_name):

    recommendations = df[df['Book'] != book_name]['Book'].head(3).tolist()

    return recommendations
