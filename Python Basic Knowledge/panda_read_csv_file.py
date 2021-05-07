import pandas as pd

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
print(search_info)
for item in search_info:
    print(item["search_term"])
    print(item["paper_counts"])
