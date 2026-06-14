# xwininfo

> Ցուցադրել տեղեկություններ պատուհանների մասին:.
> Տես նաև՝ `xprop`, `xkill`:.
> Լրացուցիչ տեղեկություններ. <https://www.x.org/releases/current/doc/man/man1/xwininfo.1.xhtml>:.

- Ցուցադրել կուրսորը՝ պատուհան ընտրելու համար՝ դրա հատկանիշները (id, անուն, չափ, դիրք, ...):

`xwininfo`

- Ցուցադրել բոլոր պատուհանների ծառը.:

`xwininfo -tree -root`

- Ցուցադրել հատուկ ID-ով պատուհանի ատրիբուտները.:

`xwininfo -id {{id}}`

- Ցուցադրել հատուկ անունով պատուհանի ատրիբուտները.:

`xwininfo -name {{name}}`

- Ցուցադրել անունով որոնող պատուհանի ID-ն.:

`xwininfo -tree -root | grep {{keyword}} | head -1 | perl -ne 'print $1 if /(0x[\da-f]+)/ig;'`
