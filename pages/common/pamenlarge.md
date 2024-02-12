# pamenlarge

> Enlarge a PAM image by duplicating pixels.
> See also: `pbmreduce`, `pamditherbw`, `pbmpscale`.
> More information: <https://netpbm.sourceforge.net/doc/pamenlarge.html>.

- Enlarge the specified image by the specified factor:

`pamenlarge -scale {{N}} {{path/to/image.pam}} > {{path/to/output.pam}}`

- Enlarge the specified image by the specified factors horizontally and vertically:

`pamenlarge -xscale {{XN}} -yscale {{YN}} {{path/to/image.pam}} > {{path/to/output.pam}}`
