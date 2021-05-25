# gobuster

> Brute-forces hidden paths on web servers and more.
> More information: <https://github.com/OJ/gobuster>.

- Discover directories and files that match in the wordlist:

`gobuster dir --url {{https://example.com/}} --wordlist {{path/to/file}}`

- Discover subdomains:

`gobuster dns --domain {{example.com}} --wordlist {{path/to/file}}`

- Discover Amazon S3 buckets:

`gobuster s3 --wordlist {{path/to/file}}`

- Discover other virtual hosts on the server:

`gobuster vhost --url {{https://example.com/}} --wordlist {{path/to/file}}`

- Fuzz the value of a parameter:

`gobuster fuzz --url {{https://example.com/?parameter=FUZZ}} --wordlist {{path/to/file}}`

- Fuzz the name of a parameter:

`gobuster fuzz --url {{https://example.com/?FUZZ=value}} --wordlist {{path/to/file}}`
