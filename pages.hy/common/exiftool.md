# exiftool

> Կարդացեք և գրեք մետա տեղեկատվությունը ֆայլերում:.
> Լրացուցիչ տեղեկություններ. <https://exiftool.org/exiftool_pod.html>:.

- Տպեք EXIF մետատվյալները տվյալ ֆայլի համար.:

`exiftool {{path/to/file}}`

- Հեռացրեք բոլոր EXIF մետատվյալները տվյալ ֆայլերից.:

`exiftool -All= {{path/to/file1 path/to/file2 ...}}`

- Հեռացրեք GPS EXIF մետատվյալները տրված պատկերային ֆայլերից.:

`exiftool "-gps*=" {{path/to/image1 path/to/image2 ...}}`

- Հեռացրեք բոլոր EXIF մետատվյալները տվյալ պատկերային ֆայլերից, այնուհետև նորից ավելացրեք մետատվյալներ գույնի և կողմնորոշման համար.:

`exiftool -All= -tagsfromfile @ -colorspacetags -orientation {{path/to/image1 path/to/image2 ...}}`

- Տեղափոխեք այն ամսաթիվը, երբ գրացուցակի բոլոր լուսանկարներն արվել են 1 ժամ առաջ:

`exiftool "-AllDates+=0:0:0 1:0:0" {{path/to/directory}}`

- Տեղափոխեք ընթացիկ գրացուցակի բոլոր JPEG լուսանկարների արված ամսաթիվը 1 օր և 2 ժամ հետ:

`exiftool "-AllDates-=0:0:1 2:0:0" {{[-ext|-extension]}} jpg`

- Փոխեք `DateTimeOriginal` դաշտը միայն 1,5 ժամ հանելով՝ առանց կրկնօրինակումներ պահելու.:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- Ռեկուրսիվ կերպով վերանվանեք բոլոր JPEG լուսանկարները գրացուցակում՝ հիմնված `DateTimeOriginal` դաշտի վրա.:

`exiftool '-filename<DateTimeOriginal' {{[-d|-dateFormat]}} %Y-%m-%d_%H-%M-%S%%lc.%%e {{path/to/directory}} {{[-r|-recurse]}} {{[-ext|-extension]}} jpg`
