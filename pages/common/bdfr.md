# bdfr

> Bulk downloader for Reddit.
> More information: <https://github.com/Serene-Arc/bulk-downloader-for-reddit>.

- Download videos/images from the specified links to URL or ID's of posts:

`bdfr download {{path/to/output_directory}} {{[-l|--link]}} {{post_url}}`

- Download the maximum possible number (roughly 1000) of videos/images from a specified user:

`bdfr download {{path/to/output_directory}} {{[-u|--user]}} {{reddit_user}} --submitted`

- Download submission data (text, upvotes, comments, etc.) limited to 10 submissions for each subreddit (30 total):

`bdfr archive {{path/to/output_directory}} {{[-s|--subreddit]}} '{{Python, all, mindustry}}' {{[-L|--limit]}} 10`

- Download videos/images from the subreddit r/Python sorted by top (default is hot) using time filter all, limited to 10 submissions:

`bdfr download {{path/to/output_directory}} {{[-s|--subreddit]}} Python {{[-S|--sort]}} top {{[-t|--time]}} all {{[-L|--limit]}} 10`

- Download the maximum possible number of both submission data and videos/images from subreddit r/Python skipping over submissions with mp4 or gif file extensions and creating hard links for duplicate files:

`bdfr clone {{path/to/output_directory}} {{[-s|--subreddit]}} Python --skip mp4 --skip gif --make-hard-links`

- Download saved posts of the authenticated user, naming each file according to a specified format. Avoid downloading duplicates and posts already present in the output directory:

`bdfr download {{path/to/output_directory}} {{[-u|--user]}} me --saved --authenticate --file-scheme '{{ {POSTID}_{TITLE}_{UPVOTES} }}' --no-dupes --search-existing`
