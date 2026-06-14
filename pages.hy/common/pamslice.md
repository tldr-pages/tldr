# թմբուկ

> PAM պատկերից հանեք արժեքների մեկ տող:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamslice.html>:.

- Տպեք աղյուսակի n-րդ շարքի պիքսելների արժեքները.:

`pamslice {{[-r|-row]}} {{n}} {{path/to/image.pam}}`

- Տպեք աղյուսակի n-րդ սյունակի պիքսելների արժեքները.:

`pamslice {{[-c|-column]}} {{n}} {{path/to/image.pam}}`

- Հաշվի առեք միայն մուտքային պատկերի m' հարթությունը.:

`pamslice {{[-r|-row]}} {{n}} -plane {{m}} {{path/to/image.pam}}`

- Արտադրեք ելք այնպիսի ձևաչափով, որը հարմար է տեսողականացման համար `xmgr` մուտքագրման համար.:

`pamslice {{[-r|-row]}} {{n}} {{[-x|-xmgr]}} {{path/to/image.pam}}`
