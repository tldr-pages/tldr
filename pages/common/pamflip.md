# pamflip

> Flip or aotate a PAM or PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pamflip.html>.

- Rotate the input image counter-clockwise by 90/180/270 degrees:

`pamflip -rotate{{90|180|270}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Flip left for right:

`pamflip -leftright {{path/to/input.pam}} > {{path/to/output.pam}}`

- Flip top for bottom:

`pamflip -topbottom {{path/to/input.pam}} > {{path/to/output.pam}}`

- Flip the input image on the main diagonal:

`pamflip -transpose {{path/to/input.pam}} > {{path/to/output.pam}}`
