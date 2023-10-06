# extrepo 

> manage external Debian repositories 
> The extrepo tool is used to manage external repositories in Debian.  Before extrepo, users 
> who wished to use software not packaged for Debian had to manually write the apt 
> configuration files, run an unsigned script as root, or install an unsigned .deb package
> More information: <https://manpages.ubuntu.com/manpages/focal/man1/extrepo.1p.html> 
> use apt to install the package after enabling the repository
- Search for a given package:

`extrepo search {{key}}`

- Enable the repository named {{repository_name}} 

`sudo extrepo enable {{repository_name}}`

- Disable the repository named {{repository_name}} 

`sudo extrepo disable {{repository_name}}`

- Update the repository named {{repository_name}} 

`sudo extrepo update {{repository_name}}`


