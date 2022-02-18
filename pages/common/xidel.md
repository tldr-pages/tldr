# xidel

> Download and extract data from HTML/XML pages as well as JSON APIs.
> More information: <https://www.videlibri.de/xidel.html>.

- Print all URLs found by a Google search:

`xidel {{https://www.google.com/search?q=test}} --extract "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"`

- Print the title of all pages found by a Google search and download them:

`xidel {{https://www.google.com/search?q=test}} --follow "{{//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']}}" --extract {{//title}} --download {{'{$host}/'}}`

- Follow all links on a page and print the titles, with XPath:

`xidel {{https://example.org}} --follow {{//a}} --extract {{//title}}`

- Follow all links on a page and print the titles, with CSS selectors:

`xidel {{https://example.org}} --follow "{{css('a')}}" --css {{title}}`

- Follow all links on a page and print the titles, with pattern matching:

`xidel {{https://example.org}} --follow "{{<a>{.}</a>*}}" --extract "{{<title>{.}</title>}}"`

- Read the pattern from example.xml (which will also check if the element containing "ood" is there, and fail otherwise):

`xidel {{path/to/example.xml}} --extract "{{<x><foo>ood</foo><bar>{.}</bar></x>}}"`

- Print all newest Stack Overflow questions with title and URL using pattern matching on their RSS feed:

`xidel {{http://stackoverflow.com/feeds}} --extract "{{<entry><title>{title:=.}</title><link>{uri:=@href}</link></entry>+}}"`

- Check for unread Reddit mail, Webscraping, combining CSS, XPath, JSONiq, and automatically form evaluation:

`xidel {{https://reddit.com}} --follow "{{form(css('form.login-form')[1], {'user': '$your_username', 'passwd': '$your_password'})}}" --extract "{{css('#mail')/@title}}"`
