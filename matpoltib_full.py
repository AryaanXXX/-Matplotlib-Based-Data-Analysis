#Complete matplotlib python data science for ml
import matplotlib.pyplot as plt
import pandas as pd

# x=[1,2,3,4] #list
# y=[10,20,15,25]
# plt.plot(x,y)  # FOR LINE GRAPH
# plt.show()

# x=['Mon','Tues','Wed','Thur','Fri']
# y=[10,15,7,20,12]
# plt.plot(x,y)
# plt.title('Bakeray Sales this week!')
# plt.xlabel('Day of the week')
# plt.ylabel('Sales per day')
# plt.show()






#PYPLOT FUNTIONS
# months=[1,2,3,4]
# sales=[1000,1500,1200,1800]
# plt.plot(months, sales, color='blue', linestyle='--', linewidth=2, marker='o', label='2025 sales data')
#
# #plt.plot(x,y, color='color name',linestyle='line_style',linewidth=value,marker=marker_symbol,label='label name')
# plt.xlabel('Months')
# plt.ylabel('Sales per month')
# plt.title('Monthly sales Data Report')
# plt.legend(loc='upper left',fontsize=12)
# plt.grid(color='gray',linestyle=':',linewidth=1)
# plt.xlim(1,4)
# plt.ylim(0,2000)
# plt.xticks([1,2,3,4],['M1','M2','M3','M4'])
# plt.show()






#Plotting bar charts,pie charts,and histograms
#plt.bar(x,height,color='color name',width=value,label='label name')
# product=['A','B','C','D']
# sales=[1000,1500,800,1200]
# plt.bar(product,sales,color='orange',label='Sales 2025',) #FOR BAR GRAPH
# plt.xlabel('Product')
# plt.ylabel('Sales')
# plt.title('Product Sale Comparison')
# plt.legend()
# plt.show()







#working with pie chart
#plt.pie(values,labels=label_list,colors=color_list,autopct='%1.1f%%')
# regions=['Nprth','South','East','West']
# revenue=[3000,2000,1500,1000]
# plt.pie(revenue, labels=regions, autopct='%1.1f%%', colors=['gold', 'skyblue', 'lightgreen', 'coral']) #FOR PIE CHART
# plt.title('Revenue Contrbution by Region')
# plt.show()







#HISTOGRAMS
#plt.hist(data,bins=number_of_bins,color='colorname',edgecolor='black')
# scores=[45,67,89,56,78,88,92,60,74,81,59,66,75,82,90,85,70,73,68,77]
# plt.hist(scores,bins=5,color='purple',edgecolor='black')  #bins 5 mane 5 bag kore nicci.
# plt.xlabel('Score Range')
# plt.ylabel('Number of Students')
# plt.title('Score distribution of Students')
# plt.show()






#SCATTER PLOT
#plt.scatter(x,y,color='color_name',marker='marker style',label='label name')
# hours_studies=[1,2,3,4,5,6,7,8]
# exam_score=[50,55,60,65,70,75,80,85]
# plt.scatter(hours_studies,exam_score,color='green',marker='o',label='Student Data') #SCATTER TYPE GRAPH
# plt.xlabel('Houres Studied')
# plt.ylabel('Exam scores')
# plt.title('Relation between study time and exam score')
# plt.legend()
# plt.grid(True)
# plt.show()







#now working with 2 data sets
# plt.scatter([1,2,3],[50,55,60],color='blue',label='class A')  #group 1
# plt.scatter([1,2,3],[45,50,52],color='orange',label='class B') #group 2
# plt.xlabel('Houres Studied')
# plt.ylabel('Exam scores')
# plt.title('Comparison of Two Classes')
# plt.legend()
# plt.grid(True)
# plt.show()







#SUBPLOTS AND LAYOUT ADJUSTMENTS
#plt.subplot(nrows,ncols,index)
# x=[1,2,3,4]
# y=[10,20,15,25]
# plt.subplot(1,2,1)  #1st row,2nd col,1st subplot
# plt.plot(x,y)
# plt.grid()
# plt.title('Line chart')
# plt.subplot(1,2,2) #1st row,2nd col,2nd subplot
# plt.bar(x,y)
# plt.title('Bar chart')
# plt.grid()
# #plt.tight_layout()
# plt.show()






#New Way
#fig,ax=plt.subplots(nrows,ncols,sigsize=(width,height))

# fig, ax = plt.subplots(1, 2, figsize=(10, 5))
#
# x = [1, 2, 3, 4]
# y = [10, 20, 15, 25]
#
# ax[0].plot(x, y)  # Correct function call
# ax[0].set_title("Line plot")  # Correct function call
#
# ax[1].bar(x, y)  # Correct function call
# ax[1].set_title("Bar chart")  # Correct function call
# fig.suptitle('Comparison of line and bar chart')
# plt.tight_layout()  # Call the function with ()
# plt.show()







#SAVE FIG DUNCTION:SAVING VISUALIZATION
#savefig('Filename.extension',dpi=value,bbox_inches='tight')
# x = [1, 2, 3, 4]
# y = [10, 20, 15, 25]
# plt.plot(x,y,color='blue',marker='o')
# plt.title('Simple line plot')
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# plt.savefig('Line_plot.png',dpi=300,bbox_inches='tight')
# plt.show()






#PROJECT
#WORKING WITH PANDAS ALSO HERE
#REAL DATA PROJECT:VISUALIZING SALES DATA USING MATPLOTLIB
#load the data
df=pd.read_csv('netflix_titles.csv')
pd.set_option('display.max_columns', None)   # Show all columns in output
print(df.head())






#CLEAN DATA
# df=df.dropna(subset=['type','release_year','rating','country','duration'])
# type_counts=df['type'].value_counts()   #need to know bout this line
# plt.figure(figsize=(6,4))
# plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
# plt.title('Number of Movies vs shows on Netflix')
# plt.xlabel('Type')
# plt.ylabel('Count')
# plt.tight_layout()
# plt.savefig('movies_vs_tvshows.png')
# plt.show()


# #NOW WE WANNA SEE THE RATING COUNTS
# rating_count=df['rating'].value_counts()
# plt.figure(figsize=(8,6))
# plt.pie(rating_count,labels=rating_count.index,autopct='%1.1f%%',startangle=90)
# plt.title('Percentage of content rating')
# plt.tight_layout()
# plt.savefig('contents_rating-pie.png')
# plt.show()







#FILTER MOVIES
# movie_df=df[df['type']=='Movie'].copy()
# movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)
#
# plt.figure(figsize=(8,6))
# plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='black')
# plt.title('Distribution of Movie Duration')
# plt.xlabel('Duration(minutes)')
# plt.ylabel('Number of Movies')
# plt.tight_layout()
# plt.savefig('movie_duration_histogram.png')
# plt.show()

#FOR ANOTHER PART
# release_counts=df['release_year'].value_counts().sort_index()
# plt.figure(figsize=(10,6))
# plt.scatter(release_counts.index,release_counts.values,color='red')
# plt.title('Release Year vs Number of Shows')
# plt.xlabel('Release Year')
# plt.ylabel('Number of Shows')
# plt.tight_layout()
# plt.savefig('release_year_scatter.png')
# plt.grid()
# plt.show()






#FOR COUNTRY
# country_counts=df['country'].value_counts().head(10)
# plt.figure(figsize=(8,6))
# plt.barh(country_counts.index,country_counts.values,color='teal')  #for horizontal bar we use (barh)
# plt.title('Top 10 Countries by Number of Shows')
# plt.xlabel('Number of Shows')
# plt.ylabel('Country')
# plt.tight_layout()
# plt.savefig('top_10_countirs.png')
# plt.show()






#FOR MOVIE AND TV SHOWS
# Grouping
# content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
#
# # Create subplots
# fig, ax = plt.subplots(1, 2, figsize=(12, 5))
#
# # Movie subplot
# ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
# ax[0].set_title('Movies released per year')
# ax[0].set_xlabel('Year')
# ax[0].set_ylabel('Number of Movies')
#
# # TV Show subplot (fixed key and subplot index!)
# ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
# ax[1].set_title('TV Shows released per year')
# ax[1].set_xlabel('Year')
# ax[1].set_ylabel('Number of TV Shows')
#
# # Final touches
# fig.suptitle('Comparison of Movies and TV Shows released over the years')
# plt.tight_layout()
# plt.savefig('movies_tv_shows_comparison.png')
# plt.show()


