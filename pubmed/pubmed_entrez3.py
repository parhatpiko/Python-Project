from Bio import Entrez
from Bio import Medline
from collections import Counter
import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
# 参数设置
Entrez.email = "parhatpiko@zju.edu.cn"
Entrez.max_tries=10
Entrez.api_key="1620334c97028769f1779fa9078fac18f108"

# 搜索
head_esearch = Entrez.esearch(db="pubmed", term="cervical cancer",retmax=1000, usehistory="y")
result_esearch = Entrez.read(head_esearch)
head_esearch.close()
# result_esearch 为{'Count': '4226980', 'RetMax': '2', 'RetStart': '0', 'QueryKey': '1', 'WebEnv': 'MCID_5fefd388a34a3f4de62f5521', 'IdList': ['33383587', '33383577'], 'TranslationSet': [{'From': 'cancer', 'To': '"neoplasms"[MeSH Terms] OR "neoplasms"[All Fields] OR "cancer"[All Fields]'}], 'TranslationStack': [{'Term': '"neoplasms"[MeSH Terms]', 'Field': 'MeSH Terms', 'Count': '3399263', 'Explode': 'Y'}, {'Term': '"neoplasms"[All Fields]', 'Field': 'All Fields', 'Count': '2729563', 'Explode': 'N'}, 'OR', {'Term': '"cancer"[All Fields]', 'Field': 'All Fields', 'Count': '2399765', 'Explode': 'N'}, 'OR', 'GROUP'], 'QueryTranslation': '"neoplasms"[MeSH Terms] OR "neoplasms"[All Fields] OR "cancer"[All Fields]'}

result_esearch_ids = result_esearch["IdList"]
# result_esearch_ids 为 ['33383587', '33383577']
print(result_esearch_ids)
result_esearch_total = 1000
result_esearch_webenv = result_esearch["WebEnv"]
result_esearch_query_key = result_esearch["QueryKey"]
result_fetch_step=5

# print("Result items: ","WebEnv","QueryKey", result_esearch_total,result_esearch_webenv,result_esearch_query_key)
Entrez.sleep_between_tries = 9000
head_efetch = Entrez.efetch(db="pubmed", id=result_esearch_ids,rettype="medline", retmode="text",retstart=5,retmax=30)
records = Medline.parse(head_efetch)
records = list(records)
for record in records:
     print("title:", record.get("TI", "?"))
     # print("authors:", record.get("AU", "?"))
     # print("source:", record.get("SO", "?"))

# efetch_retmax = 30
# for efetch_start in range(0, result_esearch_total, result_fetch_step):
#     # print("Download record %i to %i" % efetch_start + 1, int(efetch_start+result_fetch_step))
#     head_efetch = Entrez.efetch(db="pubmed", id=result_esearch_ids,retstart=efetch_start, retmax=efetch_retmax, rettype="medline", retmode="text")
#     # head_efetch为 < _io.TextIOWrapperencoding = 'UTF-8' >
#     # head_efetch.read()为读取txt文本
#     result_efetch = Medline.parse(head_efetch)
#     # Medline.parse(head_efetch)为< generatorobjectparseat0x0000027CF2BF2190 >
#     result_efetch = list(result_efetch)
#     # list(result_efetch)为[{'PMID': '33383548', 'OWN': 'NLM', 'STAT': 'Publisher', 'LR'....]
#     # print("title:", result_efetch.get("TI", "?"))
#     # print("Pubmid\t"+str(result_efetch[0].get("PMID")))
#     print("Title\t" + str(result_efetch[0].get("TI")))
#     # print("Abstract\t" + str(result_efetch[0].get("AB")))
