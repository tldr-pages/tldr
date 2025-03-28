# patator

> A multi-purpose brute-forcer, with a modular design and a flexible usage.
> More information: <https://github.com/lanjelot/patator/wiki/Usage>.

- Brute force ssh login with rate limit and timeout options (successful login will show login banner or something similar):

`patator ssh_login host={{ip_or_host}} user=FILE0 0={{path/to/users.txt}} password=FILE1 1={{path/to/passwords.txt}} --rate_limit={{seconds}} --timeout={{seconds}}`

- Brute force encrypted zip file:

`patator unzip_pass zipfile={{path/to/file.zip}} password=FILE0 0={{path/to/passwords.txt}} -x ignore:code!=0`

- List all available modules:

`patator --help`

- Show help for a particular module:

`patator {{module_name}} --help`
