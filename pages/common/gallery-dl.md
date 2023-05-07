# gallery-dl

> Download image galleries and collections from several image hosting sites.
> More information: <https://github.com/mikf/gallery-dl>.

- Download images; in this case from danbooru via tag search for 'bonocho':

`gallery-dl "https://danbooru.donmai.us/posts?tags=bonocho"`

- Get the direct URL of an image from a site supporting authentication with username & password:

`gallery-dl -g -u "<username>" -p "<password>" "https://twitter.com/i/web/status/604341487988576256"`

- Filter manga chapters by chapter number and language:

`gallery-dl --chapter-filter "10 <= chapter < 20" -o "lang=fr" "https://mangadex.org/title/59793dd0-a2d8-41a2-9758-8197287a8539"`
