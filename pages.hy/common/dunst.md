#փոշի

> Թեթև և կարգավորելի ծանուցման դևոն X11-ի և Wayland-ի համար:.
> Եթե ձեռքով չգործարկվի, D-Bus-ը ավտոմատ կերպով կգործարկվի `dunst`, երբ ծանուցում ուղարկվի:.
> Լրացուցիչ տեղեկություններ. <https://dunst-project.org/documentation/dunst/>:.

- Սկսել `dunst`:

`dunst`

- Ցուցադրել ծանուցում գործարկման մասին.:

`dunst -startup_notification`

- Տպել մուտքային ծանուցումները `stdout`-ում՝:

`dunst -print`

- Օգտագործեք նշված կազմաձևման ֆայլը (կանխադրված՝ `$XDG_CONFIG_HOME/dunst/dunstrc`):

`dunst {{[-conf|-config]}} {{path/to/file}}`
