import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import csv

BASE_URL = "https://www.zkk79.com"

def search_resource(keyword):
    """在 zkk79.com 上搜索指定资源"""
    search_url = f"{BASE_URL}/search/-------------.html?wd={keyword}&submit="
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
               "accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
               "referer":"https://www.zkk79.com/search/-------------.html?wd=%E6%B5%B7%E8%B4%BC%E7%8E%8B&submit="}
    
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print("请求失败，请检查网络或网站状态")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    results = []
    
    for item in soup.select("#searchList li"):
        title = item.select_one(".detail .title a").text
        play_link = item.select_one(".detail a.btn.btn-warm")["href"]
        

        print(f"Title: {title}")
        print(f"Play Link: {play_link}")
        print("-" * 40)
        
        results.append({"标题": title,  "链接": BASE_URL+play_link})
        break  # 只获取第一个结果
    return results

def save_results(results, filename="d:\\桌面\\项目\\anime_crawler\\app\\spider\\results.csv"):
    ##将搜索结果保存为 CSV
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"数据已保存至 {filename}")

if __name__ == "__main__":
    keyword = input("请输入要搜索的资源名称：")
    results = search_resource(keyword)
    if results:
        save_results(results)
    else:
        print("未找到相关资源")
