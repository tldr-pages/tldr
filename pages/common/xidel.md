# xidel

> A command line tool to download and extract data from HTML/XML pages as well as JSON APIs.
> More information: <https://www.videlibri.de/xidel.html>.

- Print all URLs found by a google search:

`xidel https://www.google.de/search?q=test --extract "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"`

- Print the title of all pages found by a google search and download them:

`xidel https://www.google.de/search?q=test --follow "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']" --extract //title --download '{$host}/'`

- Follow all links on a page and print the titles, With XPath:

`xidel https://example.org -f //a -e //title`

- Follow all links on a page and print the titles, With CSS selectors:

`xidel https://example.org -f "css('a')" --css title`

- Follow all links on a page and print the titles, With pattern matching:

`xidel https://example.org -f "<a>{.}</a>*" -e "<title>{.}</title>"`

- If you have an example.xml file, you can read the important part like (which will also check, if the element containing "ood" is there, and fail otherwise):

`xidel example.xml -e "<x><foo>ood</foo><bar>{.}</bar></x>"`

- Print all newest Stackoverflow questions with title and url using pattern matching on their RSS feed:

`xidel http://stackoverflow.com/feeds -e "<entry><title>{title:=.}</title><link>{uri:=@href}</link></entry>+"`

- Check if you have Reddit mail, Webscraping, combining CSS, XPath, JSONiq, and automatically form evaluation:

`xidel https://reddit.com -f "form(css('form.login-form')[1], {'user': '$your_username', 'passwd': '$your_password'})" -e "css('#mail')/@title"`
