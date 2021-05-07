import requests
from bs4 import BeautifulSoup


class BaiDuWenKu(object):
    def __init__(self):
        # 初始化操作
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"
        }
        self.session = requests.Session()
        self.session.headers.update(headers)

    def setBduss(self, bduss):
        '''
        设置cookie,将作为解析下载时的身份验证
        '''
        cookies = {"BDUSS": "hRa1RIOXBQdHppUkV2blJwdGQtQzBFM1VQcVR-OEVTWHppfmRrS0lNZW1SNHBnRVFBQUFBJCQAAAAAAAAAAAEAAAC8JucpZ3JlYXS5wrbAwcG9owAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKa6YmCmumJgN1"}
        self.session.cookies.update(cookies)

    def parserFileInfo(self, file_url):
        '''
        根据文档url解析文档信息
        '''
        res = self.session.get(file_url)
        soup = BeautifulSoup(res.text, "html.parser")
        file_info_options = [
            "ct", "doc_id", "retType", "sns_type", "storage", "useTicket",
            "target_uticket_num", "downloadToken", "sz", "v_code", "v_input"
        ]
        data = {}
        try:
            for option in file_info_options:
                value = soup.find(
                    "input", attrs={
                        "name": option
                    }).get("value") or ""
                data[option] = value
        except BaseException as e:
            raise Exception("文档信息解析失败！")
        data["req_vip_free_doc"] = "1"
        return data

    def download(self, data):
        '''
        根据解析的数据下载文档
        '''
        url = "https://wenku.baidu.com/view/caaea0bd68eae009581b6bd97f1922791788becc?ivk_sa=1023194j"
        params = {"doc_id": data["doc_id"]}
        jRes = self.session.get(url, params=params).json()
        if not jRes["data"]["is_vip_free_doc"]:
            raise Exception("只能下载vip免费文档哦")
        url = "https://wenku.baidu.com/user/submit/download"
        res = self.session.post(url, data=data, allow_redirects=False)
        if res.status_code == 302:
            return res.headers.get("Location")
        else:
            raise Exception("下载失败，请稍后再试！")


def main():
    '''
    负责逻辑调度
    '''
    bduss = "Vx*************81djg2WDgtUU5pMkE5UnhmRV*********AAAAAAEAAABlTk4wbnZwZW5neW91amlnZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIBo9V6AaPVeWG"
    bdwk = BaiDuWenKu()
    bdwk.setBduss(bduss)
    # url=input("请输入要下载的文档url：")
    url = "https://wenku.baidu.com/view/96fec4f4f321dd36a32d7375a417866fb94ac074.html?fr=search-income2"
    file_info = bdwk.parserFileInfo(url)
    download_url = bdwk.download(file_info)
    input("文档下载地址为：{}\n请及时下载".format(download_url))


if __name__ == "__main__":
    try:
        main()
    except BaseException as e:
        input(e)