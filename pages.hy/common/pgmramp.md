# pgmramp

> Ստեղծեք մոխրագույն մասշտաբի քարտեզ:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pgmramp.html>:.

- Ստեղծեք ձախից աջ մոխրագույն մասշտաբի քարտեզ.:

`pgmramp -lr > {{path/to/output.pgm}}`

- Ստեղծեք վերևից ներքև մոխրագույն մասշտաբի քարտեզ.:

`pgmramp -tb > {{path/to/output.pgm}}`

- Ստեղծեք ուղղանկյուն մոխրագույն մասշտաբի քարտեզ.:

`pgmramp -rectangle > {{path/to/output.pgm}}`

- Ստեղծեք էլիպսաձեւ մոխրագույն մասշտաբի քարտեզ.:

`pgmramp -ellipse {{path/to/image.pgm}} > {{path/to/output.pgm}}`

- Ստեղծեք մոխրագույն քարտեզ վերևի ձախ անկյունից մինչև ներքևի աջ անկյուն.:

`pgmramp -diagonal {{path/to/image.pgm}} > {{path/to/output.pgm}}`
