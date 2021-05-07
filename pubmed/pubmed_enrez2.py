from Bio import Entrez
from Bio import Medline
# 参数设置
Entrez.email = "example@163.com"
Entrez.tool  = "exampleScript"

# 搜索
paper_count = 1000
hd_esearch = Entrez.esearch(db="pubmed", term="cancer",retmax=paper_count, reldate=365, ptyp="Review", usehistory="y")
read_esearch = Entrez.read(hd_esearch)
webenv = read_esearch["WebEnv"]
query_key = read_esearch["QueryKey"]

# 这里演示设定total为 10
step = 5
print("Result items: ", paper_count)
for start in range(0, paper_count, step):
    print("Download record %i to %i" % (start + 1, int(start+step)))
    head_efetch = Entrez.efetch(db="pubmed", retstart=start, retmax=step, webenv=webenv, query_key=query_key, rettype="medline", retmode="text")
    records = Medline.parse(head_efetch)
    records = list(records)
    for record in records:
        print("title:", record.get("TI", "?"))
        # print("authors:", record.get("AU", "?"))
        # print("source:", record.get("SO", "?"))