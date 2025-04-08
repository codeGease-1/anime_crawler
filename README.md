# Anime Crawler

这是一个用于自动搜索和下载动漫的 Python 项目。用户可以输入动漫名称，程序将自动搜索并下载该动漫的所有集数，并将其保存到指定目录。

## 项目结构

```
anime_crawler
├── app
│   └── app.py          # 应用程序入口点
├── spider
│   ├── DownLoad.py     # 动态获取视频 URL 和下载视频的功能
│   └── find_obj.py     # 搜索动漫资源的功能
├── requirements.txt     # 项目所需的 Python 库
└── README.md            # 项目文档
```

## 使用说明

1. **安装依赖**  
   在项目根目录下运行以下命令以安装所需的库：
   ```
   pip install -r requirements.txt
   ```

2. **运行程序**  
   使用以下命令运行应用程序：
   ```
   python app/app.py
   ```

3. **输入动漫名称**  
   程序启动后，输入您想要下载的动漫名称，程序将自动搜索并下载所有集数。

4. **下载位置**  
   所有下载的动漫集数将保存在 `D:\桌面\项目\anime_crawler\my_anime` 目录中。

## 依赖库

- requests
- beautifulsoup4
- pandas
- playwright
- ffmpeg

## 注意事项

- 请确保您的计算机上已安装 FFmpeg，并且其路径已添加到系统环境变量中。
- 该项目依赖于网络连接，确保在运行程序时可以访问互联网。
