from Bio import Entrez
from Bio import Medline
import pandas as pd
import csv
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

# define a function that get the pubmed list with parameters passed in from ouside of function
def get_pubmed_article_info(serch_term,paper_counts):

    # 参数设置
    Entrez.email = "parhatpiko@zju.edu.cn"
    Entrez.max_tries = 6
    Entrez.sleep_between_tries = 300
    Entrez.api_key = "1620334c97028769f1779fa9078fac18f108"

    # 搜索
    paper_counts = paper_counts
    serch_term = serch_term
    hd_esearch = Entrez.esearch(db="pubmed", term=serch_term, retmax=paper_counts, usehistory="y")
    read_esearch = Entrez.read(hd_esearch)
    hd_esearch.close()
    eftech_id_list = read_esearch["IdList"]
    efetch_step = 20
    articleInfo = []
    wordcloud_abstract = ""
    wordcloud_keywords = ""
    wordcloud_jounals = ""

    for efetch_start in range(0, paper_counts, efetch_step):
        print("Download records %i to %i" % (efetch_start + 1, int(efetch_start + efetch_step)))
        flag = False
        n = 2
        while (flag != True):
            head_efetch = Entrez.efetch(db="pubmed", id=eftech_id_list, rettype="medline", retmode="text",
                                        retstart=efetch_start, retmax=efetch_step)
            records = Medline.parse(head_efetch)
            records = list(records)
            if ("TI" in records[0]):
                # print(records[0].get("TI"))
                # print("success")
                flag = True
                for record in records:
                    # print(record)
                    # print("title:", record.get("TI", "?"))
                    # print("authors:", record.get("AU", "?"))
                    # print("source:", record.get("SO", "?"))
                    temp_dict = {u'pubmed_id': record.get("PMID", "?"),
                                 u'DOI': record.get("AID", "?"),
                                 u'journal': record.get("JT", "?"),
                                 u'title': record.get("TI", "?"),
                                 u'keywords': str(record.get("OT", "?")).replace(']', '').replace('[', '').replace("'",
                                                                                           ""),
                                 u'abstract': record.get("AB", "?"), }
                    wordcloud_abstract = wordcloud_abstract + "\n" + record.get("AB", "?")
                    wordcloud_keywords = wordcloud_keywords + "\t" + str(record.get("OT", "?")).replace(']', '').replace('[', '').replace( "'", "")
                    wordcloud_jounals = wordcloud_jounals + "\n" + record.get("JT", "?")
                    # print(temp_dict)
                    articleInfo.append(temp_dict.copy())
                    # print(articleInfo)
                    temp_dict.clear()

            else:

                print(" fatal error", "第", n, "次尝试")
            n = n + 1

    # print(articleInfo)
    # print(wordcloud_abstract)

    # journal wordcloud
    text_journal = wordcloud_jounals
    wordcloud_jounals_plt = WordCloud().generate(text_journal)
    plt.figure(figsize=(20, 30))
    plt.imshow(wordcloud_jounals_plt, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(serch_term + "_" + "journals" + ".png", dpi=300, bbox_inches='tight')

    # abstract wordcloud
    text_abstract = wordcloud_abstract
    wordcloud_abstract_plt = WordCloud().generate(text_abstract)
    plt.figure(figsize=(20, 30))
    plt.imshow(wordcloud_abstract_plt, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(serch_term + "_" + "abstract" + ".png", dpi=300, bbox_inches='tight')

    file_name = serch_term + ".csv"
    field_names = ['pubmed_id', 'DOI','title', 'keywords', 'journal', 'abstract']
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(articleInfo)

#define a function that get the search term from the resercher have written into the csv file,and pass them to the get_pubmed_article_info
def get_search_info():
    df = pd.read_excel('test.xlsx', header=0)
    df = pd.DataFrame(df)
    # define a list that collect the search information
    search_info = []
    search_info_dict_temp = {}
    for index, row in df.iterrows():
        search_info_dict_temp["search_term"] = row["search term"]
        search_info_dict_temp["paper_counts"] = row["paper  counts"]
        # print(row["search term"], row["paper  counts"])
        search_info.append(search_info_dict_temp.copy())
        search_info_dict_temp.clear()
    return search_info


# retrieve the detail from the search information list
search_info  = get_search_info()
for item in search_info:
    # segment for getting the article information
    print(item["search_term"], item["paper_counts"])
    get_pubmed_article_info(item["search_term"], item["paper_counts"])
    # print(item["paper_counts"])
























# flag = False
# n=2
# while(flag!=True):
#      head_efetch = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="text", retstart=0, retmax=10)
#      records = Medline.parse(head_efetch)
#      records = list(records)
#      if ("TI" in records[0]):
#           # print(records[0].get("TI"))
#           # print("success")
#           flag = True
#           for record in records:
#                print(record)
#                print("title:", record.get("TI", "?"))
#                # print("authors:", record.get("AU", "?"))
#                # print("source:", record.get("SO", "?"))
#
#      else:
#
#           print("error","第",n,"次尝试")
#      n = n+1
