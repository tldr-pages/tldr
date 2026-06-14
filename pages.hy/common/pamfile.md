# pamfile

> Նկարագրեք Netpbm (PAM կամ PNM) ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamfile.html>:.

- Նկարագրեք նշված Netpbm ֆայլերը.:

`pamfile {{path/to/file1 path/to/file2 ...}}`

- Նկարագրեք յուրաքանչյուր պատկեր յուրաքանչյուր մուտքային ֆայլում (ի տարբերություն յուրաքանչյուր ֆայլի միայն առաջին պատկերի) մեքենայական ընթեռնելի ձևաչափով.:

`pamfile {{[-a|-allimages]}} -machine {{path/to/file}}`

- Ցուցադրել հաշվարկ, թե քանի պատկեր են պարունակում մուտքագրված ֆայլերը.:

`pamfile {{[-cou|-count]}} {{path/to/file}}`
