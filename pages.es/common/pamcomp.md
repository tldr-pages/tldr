# pamcomp

> Superpone dos imágenes PAM.
> Más información: <https://netpbm.sourceforge.net/doc/pamcomp.html>.

- Superpone dos imágenes de tal forma que la superposición bloquee partes de la imagen subyacente:

`pamcomp {{ruta/a/overlay.pam}} {{ruta/a/underlay.pam}} > {{ruta/a/output.pam}}`

- Establece la alineación horizontal de la superposición:

`pamcomp {{[-ali|-align]}} {{left|center|right|beyondleft|beyondright}} {{[-x|-xoff]}} {{x_offset}} {{ruta/a/overlay.pam}} {{ruta/a/underlay.pam}} > {{ruta/a/output.pam}}`

- Establece la alineación vertical de la superposición:

`pamcomp {{[-va|-valign]}} {{top|middle|bottom|above|below}} {{[-y|-yoff]}} {{y_offset}} {{ruta/a/overlay.pam}} {{ruta/a/underlay.pam}} > {{ruta/a/output.pam}}`

- Establece la opacidad de la superposición:

`pamcomp {{[-o|-opacity]}} {{0.7}} {{ruta/a/overlay.pam}} {{ruta/a/underlay.pam}} > {{ruta/a/output.pam}}`
