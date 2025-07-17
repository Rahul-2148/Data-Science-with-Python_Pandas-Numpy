'''
Real-Life Project: Visualizing Netflix Content & Sales Data Using MatPlotLib

Goal of the project:
- To understand Netflix content & sales in a better way. like ye sare Insights jaan sakte h:
  📝 what type of content are there
  📝 how many no. of movies yearly changes or new new movies comes 
  📝 Which country produces the most movies?
  📝 Ratings kitni jyada spread h mtlb PG (parental guided), R (Restrited- only for Adults), TV-MA (Mature audience only), TV14 (Parents strongly questioned)
  📝 Kis Movie ki kya length h ?
  📝 Kn si kn si Top Categories hain ?
  
Note: Hamare paas 8807 rows ka Dataset hain. Isme se hmlog pure charts graph banayenge, Data Visualization karenge using Matplotlib. Inshort hamlog yaha pe Patterns find krenge, trends nikalenge aur Insights nikalenge. 
     Steps: de diye gye h steps file me.
'''
# groupby -> to group the data based on some condition like country (Concept from pandas)


# step-1- Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt

# step-2- Load the data
df = pd.read_csv('MatPlotLib/Projects/netflix_titles.csv')
# print(df.head())

# step-3- Clean Data
df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

# step-4- Find Insights , making bar chart
type_counts = df['type'].value_counts()
plt.figure(figsize=(6, 4)) # figure -> refers to the entire graph
plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'orange']) # bar -> horizontal/vertical bar
plt.title('Number of Movies Vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('MatPlotLib/Projects/Movies_vs_TV_Shows_on_Netflix.png', dpi=300, bbox_inches='tight')
plt.show()

# making or Visualizing pie chart to see the distribution of ratings
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90) 
plt.title('Percentage of Content Ratings on Netflix')
plt.tight_layout()
plt.savefig('MatPlotLib/Projects/Content_Ratings_on_Netflix_Pie.png', dpi=300, bbox_inches='tight')
plt.show()

# movie ka duration kitna jyada distributed h wo dekhne ke liye Histogram - filter movies
movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min', '').astype(int)
plt.figure(figsize=(8, 6))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black', linewidth=2)
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('MatPlotLib/Projects/Distribution_of_Movie_Durations_histogram.png', dpi=300,  bbox_inches='tight') # savefig -> to save the figure
plt.show()

# Visualizing Release Year Vs No. of Shows
release_year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.scatter(release_year_counts.index, release_year_counts.values, color='red')
plt.title('Release Year vs Number of Movies and TV Shows on Netflix')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies and TV Shows')
plt.tight_layout()
plt.savefig('MatPlotLib/Projects/Release_year_scatter.png', dpi=300, bbox_inches='tight')
plt.show()

# Visualizing which country have highest number of movies & tv shows
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8, 6))
plt.barh(country_counts.index, country_counts.values, color='teal') # barh -> horizontal bar
plt.title('Top 10 Countries By Number of Shows')
plt.xlabel('Number of Movies & Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('MatPlotLib/Projects/Top_10_Countries_with_Most_Movies.png', dpi=300, bbox_inches='tight')
plt.show()

# making subplot of movies vs tv shows by year
content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0) # fillna -> to fill empty values # unstack -> to convert columns to rows # size -> to count the number of rows

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# first subplot: movies 
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue', marker='o', label='Movies')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')
ax[0].legend()

# second subplot: Tv Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange', marker='o', label='TV Shows')
ax[1].set_title('TV Shows Released Per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')
ax[1].legend()

fig.suptitle('Comparison of Movies & TV Shows Released Over Years', fontsize=16)
plt.tight_layout()
plt.savefig('MatPlotLib/Projects/Movies_TV_Shows_comparison.png', dpi=300, bbox_inches='tight')
plt.show()