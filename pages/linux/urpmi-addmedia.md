# urpmi.addmedia

> Add media in Mageia.
> NOTE: Mageia documentation uses medium and repository as synonymous.
> See also: `urpmi`, `urpmi.update`, `urpme`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> More information: <https://wiki.mageia.org/en/URPMI#urpme>.

- Add a medium:

`sudo urpmi.addmedia {{medium}} {{ftp://ftp.site.com/path/to/Mageia/RPMS}}`

- Add a medium from a hard drive (run `genhdlist2` in the directory first):

`sudo urpmi.addmedia --distrib HD file:/{{/path/to/repo}}`

- Add important media from a chosen mirror:

`sudo urpmi.addmedia --distrib ftp://{{mirror_website}/mirror/mageia/distrib/{{version}}/{{arch}}`

- Automatically select mirrors from a mirror list:

`sudo urpmi.addmedia --distrib --mirrorlist {{mirrorlist}}`
