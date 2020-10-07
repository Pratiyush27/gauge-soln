from Bio import Entrez
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.cluster import KMeans
from sklearn.cluster import k_means_

def get_top_n_words(corpus, n=None):
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]


def search(query):
    Entrez.email = 'youremail@email.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='100',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'pratiyuush@gmail.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

def get_data_corpus(papers):
    lines = [] 
    for i, paper in enumerate(papers['PubmedArticle']):
      if i<10:
        print("%d) %s" % (i+1, paper['MedlineCitation']['Article']['ArticleTitle']))
      lines.append(paper['MedlineCitation']['Article']['ArticleTitle'])
    return lines

def get_cleansed_corpus(lines):
    new_lines = []
    bad_chars = [';', ':', '!', '/','.','-',',','(',')','"','[',']']
    for line in lines:
        for e in bad_chars:
            line = line.replace(e,'')
        line = line.lower()
        new_line = line.split()
        line = ""
        for new_word in new_line:
            if new_word in words:
                new_word = new_word.replace(new_word,"")
                continue
            line = line+new_word+" "  
        new_lines.append(line[:-1])
    return new_lines

def convert_to_vectors(new_lines):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(new_lines)
    print(vectorizer.get_feature_names())
    return X,vectorizer

def make_clusters(X,vectorizer,No_of_clusters):

    #override euclidean distance to cosine simlarity
    def euc_dist(X, Y = None, Y_norm_squared = None, squared = False):
        return np.arccos(cosine_similarity(X, Y))/np.pi
    k_means_.euclidean_distances = euc_dist
    km = k_means_.KMeans(n_clusters=No_of_clusters, init='k-means++', max_iter=100, n_init=1)
    y=km.fit(X)
    print("Top terms per  km = KMeans(n_clusters=%d, init='k-means++', max_iter=100, n_init=1 cluster:"%No_of_clusters)
    y=km.fit(X)
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(6):
        print()
        print("Cluster %d:" % i, end='')
        for ind in order_centroids[i, :3]:
            print(' %s' % terms[ind], end='')
            print()

if __name__ == '__main__':
    results = search('neurodegenerative diseases')
    id_list = results['IdList']
    papers = fetch_details(id_list)
    
    
    #scrapping the data corpus

    print("First 10 Lines of data corpus\n")
    lines = get_data_corpus(papers)
    print("\n")
    
    words_freq = get_top_n_words(lines,10)
    words = [words_freq[i][0] for i in range(10)]

    print("Most Frequent words")
    print(words)
    print("\n")

    #Cleans Data corpus to a new Corpus
    new_lines = get_cleansed_corpus(lines)

    print("First 2 vectors are")
    #Convert abstracts to vectors
    X,vectorizer = convert_to_vectors(new_lines)
    
    print(X[0])
    print(X[1])
    print("\n") 

    print("Clusters preperation")
    make_clusters(X,vectorizer,6)

