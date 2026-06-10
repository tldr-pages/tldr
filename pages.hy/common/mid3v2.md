# mid3v2

> Խմբագրել աուդիո պիտակները:.
> Տես նաև՝ `id3v2`:.
> Լրացուցիչ տեղեկություններ. <https://mutagen.readthedocs.io/en/latest/man/mid3v2.html>:.

- Թվարկեք բոլոր աջակցվող ID3v2.3 կամ ID3v2.4 շրջանակները և դրանց իմաստները.:

`mid3v2 --list-frames {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Թվարկեք բոլոր աջակցվող ID3v1 թվային ժանրերը.:

`mid3v2 --list-genres {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Նշեք բոլոր պիտակները հատուկ ֆայլերում.:

`mid3v2 --list {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Սահմանեք կոնկրետ նկարչի, ալբոմի կամ երգի տեղեկատվություն.:

`mid3v2 {{--artist|--album|--song}}={{string}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Սահմանեք պատկերի հատուկ տեղեկատվություն.:

`mid3v2 --picture={{filename:description:image_type:mime_type}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Սահմանել կոնկրետ տարվա տեղեկատվություն.:

`mid3v2 --year={{YYYY}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Սահմանեք կոնկրետ ամսաթվի մասին տեղեկատվություն.:

`mid3v2 --date={{YYYY-MM-DD}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`
