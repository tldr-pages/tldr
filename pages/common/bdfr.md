# bdfr

> Bulk downloader for Reddit.
> More information: <https://github.com/Serene-Arc/bulk-downloader-for-reddit>.

- Download videos/images from the specified [l]inks to URL or ID's of posts:

`bdfr download {{path/to/output_directory}} -l {{post_url}}`

- Download the maximum possible number (roughly 1000) of videos/images from a specified [u]ser:

`bdfr download {{path/to/output_directory}} -u {{reddit_user}} --submitted`

- Download submission data (text, upvotes, comments, etc.) [L]imited to 10 submissions for each [s]ubreddit (30 total):

`bdfr archive {{path/to/output_directory}} -s '{{Python, all, mindustry}}' -L 10`

- Download videos/images from the [s]ubreddit r/Python [S]orted by top (default is hot) using [t]ime filter all, [L]imited to 10 submissions:

`bdfr download {{path/to/output_directory}} -s Python -S top -t all -L 10`

- Download the maximum possible number of both submission data and videos/images from [s]ubreddit r/Python skipping over submissions with mp4 or gif file extensions and creating hard links for duplicate files:

`bdfr clone {{path/to/output_directory}} -s Python --skip mp4 --skip gif --make-hard-links`

- Download saved posts of the authenticated user, naming each file according to a specified format. Avoid downloading duplicates and posts already present in the output directory:

`bdfr download {{path/to/output_directory}} --user me --saved --authenticate --file-scheme '{{ {POSTID}_{TITLE}_{UPVOTES} }}' --no-dupes --search-existing`
