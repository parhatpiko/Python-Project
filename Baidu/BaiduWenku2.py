
import requests
import re

# 设置会话列表
session = requests.session()
# 请求网址
def get_content_url(url):
    return session.get(url).content.decode('utf-8')

def get_content_type(content):
    return re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]

def get_content_doc(content):
    result = ''
    url_list = re.findall('(https.*?0.json.*?)\\\\x22}', content)
    # print(url_list)
    url_list = [addr.replace("\\\\\\/", "/") for addr in url_list]
    for url in url_list[:-5]:
        content = fetch_url(url)
        y = 0
        txtlists = re.findall('"c":"(.*?)".*?"y":(.*?),', content)
        for item in txtlists:
            if not y == item[1]:
                y = item[1]
                n = '\n'
            else:
                n = ''
            result += n
            result += item[0].encode('utf-8').decode('unicode_escape', 'ignore')
    return result

def main():
    url = input('请输入你要付费下载百度文库的url网址：')
    content = get_content_url(url)
    print(content)

if __name__ == "__main__":
    main()