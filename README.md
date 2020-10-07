# gauge-soln
TODOs

1) Write code to scrape abstracts from the first 100 search results for the query “neurodegenerative diseases” on pubmed. Print first 10 abstracts.
2) These 100 abstracts is now your data corpus. Remove 10 most frequently occurring words in this corpus from each abstract to create a “cleansed” corpus. Print list of removed words
3) Represent each abstract as a vector. The components of the vector should be the frequency of occurrence of a word within an abstract (remember you are now working on the cleansed corpus). Print the vectors for the first two abstracts as a row
4) Use the cosine similarity between the 100 vectors as a metric to cluster them into exactly six clusters (use any algorithm you want, but the number of clusters should be six).
5) Print three most unique words within each cluster.

Requirements:-

- python 3.6 or above
- BioPython (python library)
- sklearn

Usage:-

- Add your email ID in search function which is required for the get request.
- Update the Number of Clusters in the main function (Initialized to 6 as per assignment).
- Run Gauge_Assignment_Soln.py file.

Steps Taken:-

1) Installed BioPython which will help us connect with Pubmed and also in scrapping the input to get the abstracts.
2) The bad characters were then removed so that they dont affect the results.
3) The most frequently used words were identified and were printed and removed from the data corpus.
4) These were then converted to vectors using the CountVectorizer.
5) K Means was used and the metric was overriden to the Cosine Similarity.
6) The most Unique words within each cluster was then printed.
