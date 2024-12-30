# bdfr

> Reddit 的批量下载器。
> 更多信息： <https://github.com/Serene-Arc/bulk-downloader-for-reddit>。

- 从指定的 [l]inks 下载视频/图片到帖子的网址或 ID：

`bdfr download {{path/to/output_directory}} -l {{post_url}}`

- 从指定的 [u]ser 下载最大可能数量（大约 1000）的视频/图片：

`bdfr download {{path/to/output_directory}} -u {{reddit_user}} --submitted`

- 下载提交数据（文本、赞、评论等）[L]imited 每个 [s]ubreddit 限制为 10 个提交（总共 30 个）：

`bdfr archive {{path/to/output_directory}} -s '{{Python, all, mindustry}}' -L 10`

- 从 [s]ubreddit r/Python 下载视频/图片 [S]orted by top（默认是热门），使用 [t]ime filter all，限制为 10 个提交：

`bdfr download {{path/to/output_directory}} -s Python -S top -t all -L 10`

- 从 [s]ubreddit r/Python 下载最大可能数量的提交数据和视频/图片，跳过扩展名为 mp4 或 gif 的提交，并为重复文件创建硬链接：

`bdfr clone {{path/to/output_directory}} -s Python --skip mp4 --skip gif --make-hard-links`

- 下载已认证用户的保存帖子，按照指定格式命名每个文件。避免下载重复以及已存在于输出目录中的帖子：

`bdfr download {{path/to/output_directory}} --user me --saved --authenticate --file-scheme '{{ {POSTID}_{TITLE}_{UPVOTES} }}' --no-dupes --search-existing`