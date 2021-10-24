# cewl

> Custom word list generator based on the expressions found on designated website
> Best run with elevated priviledges.
> More information: <https://github.com/digininja/CeWL>.

- Crawl target website in verbose mode: 

`cewl -v {{website_url}}`

- Crawl target website in verbose mode and generate alpha-numberic wordlist: 

`cewl -v {{website_url}} --with-numbers`

- Crawl target website and log to file with a minimum word character length of 3 and spider depth of 1:

`cewl {{website_url}} -w {{path/to/log_file}} -m {{3}} -d {{1}}` 

- Crawl target website, hide discovered words and only log discovered [e]mails to file:

`cewl {{website_url}} -n -e -w {{path/to/log_file}}`
