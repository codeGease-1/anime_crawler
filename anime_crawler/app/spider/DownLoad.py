from playwright.sync_api import sync_playwright
import subprocess
import csv
import os

def get_video_url_dynamic(url):
    with sync_playwright() as p:
        # 启动无头浏览器
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0")
        page = context.new_page()

        try:
            # 打开目标网页
            response = page.goto(url, timeout=120000)
            if not response or response.status != 200:
                print(f"页面加载失败，状态码: {response.status if response else '无响应'}")
                return None

            # 等待页面加载完成
            page.wait_for_load_state('networkidle')

            # 检查是否存在 iframe
            iframes = page.frames
            for iframe in iframes:
                video_tag = iframe.query_selector('video')
                if video_tag:
                    video_url = video_tag.get_attribute('src')
                    if video_url:
                        # 获取“下集”按钮的链接
                        next_button = page.query_selector('.myui-player__operate li:last-child a')  # 选择最后一个li元素内的a标签
                        next_url = "https://www.zkk79.com"+next_button.get_attribute('href') if next_button else None
                        return video_url, next_url
            print("未找到视频 URL")
            return None, None
        except Exception as e:
            print(f"获取视频 URL 时出错: {e}")
            return None, None
        finally:
            browser.close()

def download_video(video_url, output_file='output.mp4'):    
    # 调用 ffmpeg 下载视频
    try:
        result = subprocess.run(
            [
                r'C:\FFmpeg\ffmpeg-2025-03-31-git-35c091f4b7-full_build\ffmpeg-2025-03-31-git-35c091f4b7-full_build\bin\ffmpeg.exe',
                '-headers', 'Cookie:history=%5B%7B%22name%22%3A%22%E7%B4%AB%E7%BD%97%E5%85%B0%E6%B0%B8%E6%81%92%E8%8A%B1%E5%9B%AD%E5%89%A7%E5%9C%BA%E7%89%88%22%2C%22pic%22%3A%22https%3A%2F%2Fcdn.yinghuazy.xyz%2Fupload%2Fvod%2F20201125-1%2F027b7507ee45072bc04d12fcc9ca394e.jpg%22%2C%22link%22%3A%22%2Fdongmanplay%2F4862-1-1.html%22%2C%22part%22%3A%22%E5%85%A8%E9%9B%86%22%7D%2C%7B%22name%22%3A%22%E5%85%A8%E4%BF%AE%E3%80%82%22%2C%22pic%22%3A%22https%3A%2F%2Fvip.dytt-img.com%2Fupload%2Fvod%2F20250214-1%2F4bdc3b7589444515bf2d296d5023c7de.jpg%22%2C%22link%22%3A%22%2Fdongmanplay%2F9182-1-1.html%22%2C%22part%22%3A%22%E7%AC%AC01%E9%9B%86%22%7D%2C%7B%22name%22%3A%22%E7%9B%B4%E8%87%B3%E9%AD%94%E5%A5%B3%E6%B6%88%E9%80%9D%22%2C%22pic%22%3A%22https%3A%2F%2Flain.bgm.tv%2Fr%2F400%2Fpic%2Fcover%2Fl%2Fe1%2Fb7%2F501702_VXrd2.jpg%22%2C%22link%22%3A%22%2Fdongmanplay%2F9235-1-1.html%22%2C%22part%22%3A%22%E7%AC%AC01%E9%9B%86%22%7D%2C%7B%22name%22%3A%22%E6%B5%B7%E8%B4%BC%E7%8E%8B%E8%B0%88%E6%81%8B%E7%88%B1%22%2C%22pic%22%3A%22https%3A%2F%2Flain.bgm.tv%2Fr%2F400%2Fpic%2Fcover%2Fl%2F67%2F58%2F546257_SlLZU.jpg%22%2C%22link%22%3A%22%2Fdongmanplay%2F9247-1-1.html%22%2C%22part%22%3A%22%E7%AC%AC01%E9%9B%86%22%7D%2C%7B%22name%22%3A%22%E6%B5%B7%E8%B4%BC%E7%8E%8B%22%2C%22pic%22%3A%22https%3A%2F%2Fimages.weserv.nl%2F%3Furl%3Dhttps%3A%2F%2Flz.sinaimg.cn%2Fmw690%2F0076NW5Ngy1ge3ztw2rdej307i0b90uy.jpg%22%2C%22link%22%3A%22%2Fdongmanplay%2F1805-1-719.html%22%2C%22part%22%3A%22%E7%AC%AC719%E9%9B%86%22%7D%2C%7B%22name%22%3A%22%E5%92%92%E6%9C%AF%E5%9B%9E%E6%88%98%22%2C%22pic%22%3A%22https%3A%2F%2Fcdn.yinghuazy.xyz%2Fjpg%2Fly1gtk4nh67xyj307i0al0tc.jpg%22%2C%22link%22%3A%22%2Fdongmanplay%2F4419-1-1.html%22%2C%22part%22%3A%22%E7%AC%AC01%E9%9B%86%22%7D%2C%7B%22name%22%3A%22%E5%89%91%E6%9D%A5%22%2C%22pic%22%3A%22https%3A%2F%2Fvcover-vt-pic.puui.qpic.cn%2Fvcover_vt_pic%2F0%2Fmzc0020072zgk611721874669799%2F0%22%2C%22link%22%3A%22%2Fdongmanplay%2F8991-1-3.html%22%2C%22part%22%3A%22%E7%AC%AC03%E9%9B%86%22%7D%2C%7B%22name%22%3A%22%E4%BB%99%E9%80%86%22%2C%22pic%22%3A%22https%3A%2F%2Fimage.baidu.com%2Fsearch%2Fdown%3Furl%3Dhttps%3A%2F%2Flz.sinaimg.cn%2Flarge%2F006sgDEegy1h50jutep64j307i0a5779.jpg%22%2C%22link%22%3A%22%2Fdongmanplay%2F8404-1-1.html%22%2C%22part%22%3A%22%E7%AC%AC01%E9%9B%86%22%7D%5D ',
                '-i', video_url,
                '-c', 'copy',
                output_file
            ],
            check=True,  # 如果命令失败，抛出异常
            stdout=subprocess.PIPE,  # 捕获输出
            stderr=subprocess.PIPE
        )
        print(f"视频下载完成: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"下载视频时出错: {e.stderr.decode('utf-8')}")
    except Exception as e:
        print(f"发生未知错误: {e}")

if __name__ == "__main__":
    output_folder=r'D:\桌面\项目\anime_crawler\my_anime'
    os.makedirs(output_folder, exist_ok=True)  

    # 从 CSV 文件中读取链接
    csv_file =r'd:\桌面\项目\anime_crawler\app\spider\results.csv'
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            url = row['链接']  # 从 CSV 中获取链接
            title = row.get('标题')   # 从 CSV 中获取标题
            print(f"正在处理链接: {url}")

            # 为每个标题创建一个单独的文件夹
            title_folder = os.path.join(output_folder, title)
            os.makedirs(title_folder, exist_ok=True)

            episode_number=1
            previous_url=None
            # 提取视频 URL（动态加载）
            while url:
                if url == previous_url:
                    print("已到达最后一集，停止下载")
                    break
                
                if not url:
                    break
                # 提取视频 URL（动态加载）
                video_url, next_url = get_video_url_dynamic(url)
                if video_url:
                    print(f"找到视频 URL: {video_url}")
                    output_file = os.path.join(title_folder, f"{title}_第{episode_number}集.mp4")
                    download_video(video_url, output_file)
                    episode_number += 1
                    previous_url=url
                    url = next_url  # 更新为“下集”的 URL
                else:
                    print("未找到视频 URL")
                    break