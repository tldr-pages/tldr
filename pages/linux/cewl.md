# CeWL

> URL spidering tool for making a cracking wordlist from Web content.

- Create a wordlist file from the given URL up to 2 links depth:

`cewl --depth 2 --write {{wordlist}} {{url}}`

- Output an alpha-numeric wordlist from the given URL with words of minimum 5 characters:

`cewl --with-numbers --min_word_length 5 {{url}}`

- Output a wordlist from the given URL in debug mode including email addresses:

`cewl --debug --email {{url}}`

- Output a wordlist from the given URL using HTTP Basic authentication:

`cewl --auth_type basic --auth_user admin --auth_pass password1 {{url}}`

- Output a wordlist from the given URL through a proxy:

`cewl --proxy_host 10.10.1.5 --proxy_port 3128 {{url}}`
