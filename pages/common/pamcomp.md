# pamcomp

> Overlay two PAM images.
> More information: <https://netpbm.sourceforge.net/doc/pamcomp.html>.

- Overlay two images such with the overlay blocking parts of the underlay:

`pamcomp {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- Set the horizontal alignment of the overlay:

`pamcomp -align {{left|center|right|beyondleft|beyondright}} -xoff {{x_offset}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- Set the vertical alignment of the overlay:

`pamcomp -valign {{top|middle|bottom|above|below}} -yoff {{y_offset}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- Set the opacity of the overlay:

`pamcomp -opacity {{0.7}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`
