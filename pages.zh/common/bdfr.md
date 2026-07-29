# bdfr

> Reddit 批量下载器。
> 更多信息：<https://github.com/Serene-Arc/bulk-downloader-for-reddit>。

- 从指定的链接下载视频/图片到 URL 或帖子 ID：

`bdfr download {{路径/到/输出目录}} {{[-l|--link]}} {{帖子_url}}`

- 从指定用户下载最大数量（约 1000）的视频/图片：

`bdfr download {{路径/到/输出目录}} {{[-u|--user]}} {{reddit_用户}} --submitted`

- 下载提交数据（文本、点赞、评论等），每个子版块限制 10 个提交（总共 30 个）：

`bdfr archive {{路径/到/输出目录}} {{[-s|--subreddit]}} '{{Python, all, mindustry}}' {{[-L|--limit]}} 10`

- 从 r/Python 子版块下载视频/图片，按热门排序（默认），使用全部时间过滤，限制 10 个提交：

`bdfr download {{路径/到/输出目录}} {{[-s|--subreddit]}} Python {{[-S|--sort]}} top {{[-t|--time]}} all {{[-L|--limit]}} 10`

- 从 r/Python 子版块下载提交数据和视频/图片，跳过 .mp4 或 .gif 文件扩展名的提交，为重复文件创建硬链接：

`bdfr clone {{路径/到/输出目录}} {{[-s|--subreddit]}} Python --skip mp4 --skip gif --make-hard-links`

- 下载已认证用户的已保存帖子，根据指定格式命名每个文件。避免下载重复项和已存在于输出目录中的帖子：

`bdfr download {{路径/到/输出目录}} {{[-u|--user]}} me --saved --authenticate --file-scheme '{{ {POSTID}_{TITLE}_{UPVOTES} }}' --no-dupes --search-existing`
