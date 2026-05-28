import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/books.csv")

# Create similarity matrix
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['Book'])

similarity = cosine_similarity(count_matrix)

def recommend(book_name):

    recommendations = []

    try:
        index = df[df['Book'] == book_name].index[0]

        scores = list(enumerate(similarity[index]))

        sorted_scores = sorted(
            scores,
            key=lambda x: x[1],
            reverse=True
        )

        for i in sorted_scores[1:4]:
            recommendations.append(df.iloc[i[0]]['Book'])

    except:
        recommendations = ["No recommendations found"]

    return recommendations
