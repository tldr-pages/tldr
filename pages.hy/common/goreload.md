# goreload

> Ուղիղ վերբեռնման օգտակար ծրագիր Go ծրագրերի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/acoshift/goreload#basic-usage>:.

- Դիտեք երկուական ֆայլ (կանխադրված է `.goreload`):

`goreload {{[-b|--bin]}} {{path/to/binary}} {{path/to/file.go}}`

- Սահմանեք հատուկ մատյան նախածանց (կանխադրված է `goreload`):

`goreload --logPrefix {{prefix}} {{path/to/file.go}}`

- Վերբեռնեք, երբ որևէ ֆայլ փոխվում է.:

`goreload --all`
