import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Starting program...")

# LOAD DATASET

df = pd.read_csv(r"movies.csv")
print("Dataset loaded successfully!")


# CHECK REQUIRED COLUMNS

required_cols = {'movieId', 'title', 'genres'}
if not required_cols.issubset(df.columns):
    print("❌ Required columns not found!")
    print("Available columns:", df.columns.tolist())
    exit()


# KEEP REQUIRED COLUMNS

df = df[['movieId', 'title', 'genres']]
df.dropna(inplace=True)


# LIMIT DATASET SIZE 

df = df.head(3000)


# SHOW SAMPLE 

print("\nSample movies you can search:\n")
print(df[['movieId', 'title', 'genres']].sample(5).to_string(index=False))


# CLEAN GENRES

df['genres'] = df['genres'].str.replace('|', ' ', regex=False)


# VECTORIZE GENRES

print("\nProcessing movie data...")
cv = CountVectorizer(stop_words='english')
matrix = cv.fit_transform(df['genres'])

# COSINE SIMILARITY

similarity = cosine_similarity(matrix)


# RECOMMENDATION FUNCTION

def recommend(movie_name):
    movie_name = movie_name.lower().strip()

    # Case-insensitive comparison
    titles_lower = df['title'].str.lower()

    if movie_name not in titles_lower.values:
        print("\n❌ Movie not found!")
        print("\nTry one of these movies:")
        print(df['title'].sample(5).to_string(index=False))
        return

    index = df[titles_lower == movie_name].index[0]
    scores = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )

    print(f"\n🎬 Recommended movies for '{df.loc[index, 'title']}':\n")
    for i in scores[1:6]:
        row = df.iloc[i[0]]
        print(f"{row.movieId} - {row.title}")
 
# USER INTERACTION

print("\n=== MOVIE RECOMMENDATION SYSTEM ===")
print("Type movie name EXACTLY as shown above")

movie = input("\nEnter movie name: ")
recommend(movie)

input("\nPress Enter to exit...")
