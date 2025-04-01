# bdfr

> Reddit 批量下载器。
> 更多信息：<https://github.com/Serene-Arc/bulk-downloader-for-reddit>.

- 从指定的链接或帖子的 URL 或 ID 下载视频/图片：

`bdfr download {{path/to/output_directory}} {{[-l|--link]}} {{post_url}}`

- 从指定用户下载尽可能多的（大约 1000 个）视频/图片：

`bdfr download {{path/to/output_directory}} {{[-u|--user]}} {{reddit_user}} --submitted`

- 下载提交数据（文本、点赞、评论等），每个子版块限制为 10 个提交（总共 30 个）：

`bdfr archive {{path/to/output_directory}} {{[-s|--subreddit]}} '{{Python, all, mindustry}}' {{[-L|--limit]}} 10`

- 从 r/Python 子版块下载视频/图片，按“最热”排序（默认为“热门”），使用“全部时间”筛选器，限制为 10 个提交：

`bdfr download {{path/to/output_directory}} {{[-s|--subreddit]}} Python {{[-S|--sort]}} top {{[-t|--time]}} all {{[-L|--limit]}} 10`

- 从 r/Python 子版块下载尽可能多的提交数据和视频/图片，跳过扩展名为 mp4 或 gif 的提交，并为重复文件创建硬链接：

`bdfr clone {{path/to/output_directory}} {{[-s|--subreddit]}} Python --skip mp4 --skip gif --make-hard-links`

- 下载已验证用户的已保存帖子，根据指定格式命名每个文件。避免下载重复的帖子和已存在于输出目录中的帖子：

`bdfr download {{path/to/output_directory}} {{[-u|--user]}} me --saved --authenticate --file-scheme '{{ {POSTID}_{TITLE}_{UPVOTES} }}' --no-dupes --search-existing`
