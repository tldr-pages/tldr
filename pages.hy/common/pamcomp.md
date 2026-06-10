# pamcomp

> Ծածկեք երկու PAM պատկերներ:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamcomp.html>:.

- Ծածկեք երկու պատկեր, ինչպիսիք են ներքևի ծածկույթի արգելափակման մասերը.:

`pamcomp {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- Սահմանեք ծածկույթի հորիզոնական հավասարեցումը.:

`pamcomp {{[-ali|-align]}} {{left|center|right|beyondleft|beyondright}} {{[-x|-xoff]}} {{x_offset}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- Սահմանեք ծածկույթի ուղղահայաց հավասարեցումը.:

`pamcomp {{[-va|-valign]}} {{top|middle|bottom|above|below}} {{[-y|-yoff]}} {{y_offset}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- Սահմանեք ծածկույթի անթափանցիկությունը.:

`pamcomp {{[-o|-opacity]}} {{0.7}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`
