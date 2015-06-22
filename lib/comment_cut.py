#encoding=utf-8
import csv
import jieba
jieba.set_dictionary('dict.txt.big')
import sys
import operator
reload(sys)
sys.setdefaultencoding('utf-8')
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  


corpus = []
stopwords = {}.fromkeys(['一律', '潜水','00','001','06','07','08','089','10','100','100rmb','104','11','12','1200','125cc','15','150','17','18','19','193','1937','197','1987','1hr','20','200','2000','2001','2003','2011','2013','2015','20150503','20k','20mins','22','24','24hr','281530','30','3000','31','32','320','37c','38','3d','3k','40','43','45','50','5000','5k','70','77','80','agreatplaceforcyclingandjogging','bbq','bike','chaikou','confuse','dabaisha','diy','free','freetickets','fu','google','greenland','ilovelanyu','image','lifesuckswithouttruelove','luck','murmur','nanliao','niceview','nt','n年','ok','opening','pizza','pub','sapasapa','schedule','share','shilang','shopping','sika','sosurprise','spa','tour','unforgettable','wifi','xd','yelloworred','youtube'])   
with open('sight_modified.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sentence = row['comment']
        words = jieba.cut(sentence, cut_all=False)
        final = []
        for w in words:
            w = w.encode('utf8')
            if w not in stopwords:
                final.append(w)
        corpus.append(" ".join(final))
        # for word in words:
        #     print word

vectorizer = CountVectorizer()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
word = vectorizer.get_feature_names()
weight = tfidf.toarray()

document = []
with open('tfidf_for_cluster.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([','.join(word)])
    for w in weight:
        new_ele = []
        for ele in w:
            new_ele.append(str(ele))
        spamwriter.writerow([','.join(new_ele)])



# for i in range(len(weight)):
#     # print u"-------这里输出第",i,u"类文本的词语tf-idf权重------"
#     # document.append([])
#     aa = {}
#     for j in range(len(word)):  
#         aa[word[j]] = weight[i][j]
#     document.append(aa)

# sorted_result = []
# for d in document:
#     sorte = sorted(d.items(), key = operator.itemgetter(1))
#     sorted_result.append(sorte[-20:])

# # for s in sorted_result:
# #     print ' '
# #     for term in s:
# #         print term[0]
# i = 0
# with open('top_terms.csv', 'wb') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
#     for d in sorted_result:
#         d.reverse()
#         i += 1

#         terms = []
#         # spamwriter.writerow([i, d])
#         for term in d:
#             bb = term[0].encode('utf8')
#             terms.append(bb)
#         spamwriter.writerow(terms)
