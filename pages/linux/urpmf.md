# urpmf

> Mageia's command for finding files in packages and querying information about them.
> NOTE: Mageia documentation uses medium and repository as synonymous.
> See also: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmi.update`, `urpmq`.
> More information: <https://wiki.mageia.org/en/URPMI#urpmi.removemedia>.

- Search for packages that contain a file:

`urpmf {{filename}}`

- Search for packages that contain both a keyword [a]nd another in their summaries:

`urpmf --summary {{keyword1}} -a {{keyword2}}`

- Search for packages that contain a keyword [o]r another in their descriptions:

`urpmf --description {{keyword1}} -o {{keyword2}}`

- Search for packages that not contain a keyword in their name ignoring case distinction using "|" as the [F]ield separator (":" by default):

`urpmf --description ! {{keyword}} -F'|'`
