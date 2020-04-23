# wpscan

> Wordpress vulnerability scanner.
> More information: <https://github.com/wpscanteam/wpscan>.

- Update the vulnerability database:

`wpscan --update`

- Scan a Wordpress website:

`wpscan --url {{url}}`

- Scan a Wordpress website, using random user agents and passive detection:

`wpscan --url {{url}} --stealthy`

- Scan a Wordpress website, checking for vulnerable plugins and specifying the path to the `wp-content` directory:

`wpscan --url {{url}} --enumerate {{vp}} --wp-content-dir {{remote/path/to/wp-content}}`

- Scan a Wordpress website through a proxy:

`wpscan --url {{url}} --proxy {{protocol://ip:port}} --proxy-auth {{username:password}}`

- Perform user identifiers enumeration on a Wordpress website:

`wpscan --url {{url}} --enumerate {{u}}`

- Execute a password guessing attack on a Wordpress website:

`wpscan --url {{url}} --usernames {{username|path/to/usernames.txt}} --passwords {{path/to/passwords.txt}} threads {{20}}`

- Scan a Wordpress website, collecting vulnerability data from the WPVulnDB (https://wpvulndb.com/):

`wpscan --url {{url}} --api-token {{token}}`
