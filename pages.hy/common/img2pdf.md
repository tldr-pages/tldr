# img2pdf

> Անկորուստ փոխակերպեք ռաստերային պատկերները PDF ֆայլի:.
> Որոշ աջակցվող պատկերի ձևաչափերն են՝ GIF, JPEG, JPEG2000, PNG, GIF և TIFF:.
> Լրացուցիչ տեղեկություններ. <https://gitlab.mister-muffin.de/josch/img2pdf>:.

- Փոխակերպեք մեկ կամ մի քանի պատկեր մեկ PDF-ի, յուրաքանչյուր պատկեր գտնվում է իր էջում.:

`img2pdf {{path/to/image1.ext path/to/image2.ext ...}} --output {{path/to/file.pdf}}`

- Փոխարկեք միայն բազմաֆունկցիոնալ պատկերի առաջին շրջանակը PDF.:

`img2pdf {{path/to/file.gif}} --first-frame-only --output {{path/to/file.pdf}}`

- Ավտոմատ կողմնորոշեք պատկերը, օգտագործեք էջի որոշակի չափ լանդշաֆտային ռեժիմում և սահմանեք որոշակի չափերի սահման՝ հորիզոնական և ուղղահայաց.:

`img2pdf {{path/to/image.ext}} --auto-orient --pagesize {{A4^T}} --border {{2cm}}:{{5.1cm}} --output {{path/to/file.pdf}}`

- Փոքրացրեք միայն ավելի մեծ պատկերները որոշակի չափսերով էջի ներսում նշված չափերի ուղղանկյունի.:

`img2pdf {{path/to/image.ext}} --pagesize {{30cm}}x{{20cm}} --imgsize {{10cm}}x{{15cm}} --fit {{shrink}} --output {{path/to/file.pdf}}`

- Փոխակերպեք պատկերը PDF-ի և նշեք ստացված ֆայլի մետատվյալները.:

`img2pdf {{path/to/image.ext}} --title {{title}} --author {{author}} --creationdate {{1970-01-31}} --keywords {{keyword1 keyword2}} --subject {{subject}} --output {{path/to/file.pdf}}`
