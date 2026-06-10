# pamtowinicon

> Փոխարկել PAM պատկերը Windows ICO ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamtowinicon.html>:.

- Փոխակերպեք PAM պատկերի ֆայլը ICO ֆայլի.:

`pamtowinicon {{path/to/input_file.pam}} > {{path/to/output.ico}}`

- Կոդավորեք պատկերները `t`-ից փոքր լուծաչափերով BMP ձևաչափով և բոլոր մյուս պատկերները PNG ձևաչափով.:

`pamtowinicon {{[-pn|-pngthreshold]}} {{t}} {{path/to/input_file.pam}} > {{path/to/output.ico}}`

- Ոչ անթափանց տարածքից դուրս բոլոր պիքսելները սև դարձրեք.:

`pamtowinicon {{[-t|-truetransparent]}} {{path/to/input_file.pam}} > {{path/to/output.ico}}`
