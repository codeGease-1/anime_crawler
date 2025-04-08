import os
from spider.find_obj import search_resource
from spider.DownLoad import get_video_url_dynamic, download_video

OUTPUT_FOLDER = r'D:\桌面\项目\anime_crawler\my_anime'

def main():
    keyword = input("请输入要搜索的动漫名称：")
    results = search_resource(keyword)
    
    if results:
        for result in results:
            title = result['标题']
            url = result['链接']
            print(f"正在处理动漫: {title}")

            # 为每个标题创建一个单独的文件夹
            title_folder = os.path.join(OUTPUT_FOLDER, title)
            os.makedirs(title_folder, exist_ok=True)

            episode_number = 1
            previous_url = None
            
            # 提取视频 URL（动态加载）
            while url:
                if url == previous_url:
                    print("已到达最后一集，停止下载")
                    break
                
                video_url, next_url = get_video_url_dynamic(url)
                if video_url:
                    print(f"找到视频 URL: {video_url}")
                    output_file = os.path.join(title_folder, f"{title}_第{episode_number}集.mp4")
                    download_video(video_url, output_file)
                    episode_number += 1
                    previous_url = url
                    url = next_url  # 更新为“下集”的 URL
                else:
                    print("未找到视频 URL")
                    break
    else:
        print("未找到相关资源")

if __name__ == "__main__":
    main()