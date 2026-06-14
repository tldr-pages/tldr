# podman ներմուծում

> Ներմուծեք tarball և պահպանեք այն որպես ֆայլային համակարգի պատկեր:.
> Տես նաև՝ `podman export`, `podman save`:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-import.1.html>:.

- Ներմուծեք tarball տեղական ֆայլից և ստեղծեք պատկեր.:

`podman import {{path/to/tarball.tar}} {{image:tag}}`

- Ներմուծեք tarball URL-ից.:

`podman import {{https://example.com/image.tar}} {{image:tag}}`

- Ներմուծեք tarball և ավելացրեք commit հաղորդագրություն.:

`podman import {{[-m|--message]}} "{{commit_message}}" {{path/to/tarball.tar}} {{image:tag}}`

- Ներմուծեք tarball և սահմանեք լռելյայն հրաման (պահանջվում է բեռնարկղը գործարկելու համար).:

`podman import {{[-c|--change]}} CMD={{/bin/bash}} {{path/to/tarball.tar}} {{image:tag}}`
