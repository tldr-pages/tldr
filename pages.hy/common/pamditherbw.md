# pamditherbw

> Կիրառեք շեղումը մոխրագույն մասշտաբի պատկերի վրա, այսինքն՝ վերածեք այն սև և սպիտակ պիքսելների օրինակի, որոնք նույն տեսքն ունեն, ինչ սկզբնական մոխրագույն սանդղակը:.
> Տես նաև՝ `pbmreduce`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamditherbw.html>:.

- Կարդացեք PGM պատկերը, կիրառեք dithering և պահեք այն ֆայլում.:

`pamditherbw {{path/to/image.pgm}} > {{path/to/file.pgm}}`

- Օգտագործեք նշված քվանտավորման մեթոդը.:

`pamditherbw -{{floyd|fs|atkinson|threshold|hilbert|...}} {{path/to/image.pgm}} > {{path/to/file.pgm}}`

- Օգտագործեք ատկինսոնի քվանտացման մեթոդը և նշված սերմը կեղծ պատահական թվերի գեներատորի համար.:

`pamditherbw {{[-a|-atkinson]}} {{[-r|-randomseed]}} {{1337}} {{path/to/image.pgm}} > {{path/to/file.pgm}}`

- Նշեք շեմային արժեքը քվանտավորման մեթոդների համար, որոնք կատարում են որոշակի շեմեր.:

`pamditherbw -{{fs|atkinson|thresholding}} {{[-va|-value]}} {{0.3}} {{path/to/image.pgm}} > {{path/to/file.pgm}}`
