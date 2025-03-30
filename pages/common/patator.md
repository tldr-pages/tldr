# patator

> A multi-purpose brute-forcer, with a modular design and a flexible usage.
> More information: <https://github.com/lanjelot/patator/wiki/Usage>.

- Brute force ssh login with rate limit and timeout options (successful login will show login banner or something similar):

`patator ssh_login host={{ip_or_host}} user=FILE0 password=FILE1 0={{path/to/users.txt}} 1={{path/to/passwords.txt}} --rate_limit={{seconds}} --timeout={{seconds}} -x ignore:mesg='Authentication failed.'`

- Brute force encrypted zip file:

`patator unzip_pass zipfile={{path/to/file.zip}} password=FILE0 0={{path/to/passwords.txt}} -x ignore:code!=0`

- Brute force http basic auth (payload file `userpass.txt` should be in the format `username:password`):

`patator http_fuzz url={{http://host:port}} auth_type=basic user_pass=COMBO00:COMBO01 0={{path/to/userpass.txt}} -x ignore:code=401`

- Brute force FTP/FTPS login:

`patator ftp_login host={{ip_or_host}} user=FILE0 password=FILE1 0={{path/to/users.txt}} 1={{path/to/passwords.txt}} tls={{0|1}} -x ignore:mesg='Login incorrect.' -x ignore,reset,retry:code=500`

- List all available modules:

`patator --help`

- Show help for a particular module:

`patator {{module_name}} --help`
