# pamstack

> Բազմաթիվ PAM պատկերների հարթությունները դրեք մեկ PAM պատկերի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamstack.html>:.

- Նշված PAM պատկերների հարթությունները դրեք նշված կարգով.:

`pamstack {{path/to/image1.pam path/to/image2.pam ...}} > {{path/to/output.pam}}`

- Նշեք ելքային PAM ֆայլի կրկնակի տիպի անունը (առավելագույնը 255 նիշ).:

`pamstack {{[-t|-tupletype]}} {{tuple_type}} {{path/to/image1.pam path/to/image2.pam ...}} > {{path/to/output.pam}}`
