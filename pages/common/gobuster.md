# gobuster

> Brute-forces hidden paths on web servers and more.
> More information: <https://github.com/OJ/gobuster#modes>.

- Discover directories and files that match in the wordlist:

`gobuster dir {{[-u|--url]}} {{https://example.com/}} {{[-w|--wordlist]}} {{path/to/file}}`

- Discover subdomains:

`gobuster dns {{[-d|--domain]}} {{example.com}} {{[-w|--wordlist]}} {{path/to/file}}`

- Discover Amazon S3 buckets:

`gobuster s3 {{[-w|--wordlist]}} {{path/to/file}}`

- Discover other virtual hosts on the server:

`gobuster vhost {{[-u|--url]}} {{https://example.com/}} {{[-w|--wordlist]}} {{path/to/file}}`

- Fuzz the value of a parameter:

`gobuster fuzz {{[-u|--url]}} {{https://example.com/?parameter=FUZZ}} {{[-w|--wordlist]}} {{path/to/file}}`

- Fuzz the name of a parameter:

`gobuster fuzz {{[-u|--url]}} {{https://example.com/?FUZZ=value}} {{[-w|--wordlist]}} {{path/to/file}}`
