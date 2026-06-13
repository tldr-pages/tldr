# pdfimages

> Narzędzie do wyodrębniania obrazów z plików PDF.
> Więcej informacji: <https://manned.org/pdfimages>.

- Wyodrębnij wszystkie obrazy z pliku PDF i zapisz je jako pliki PNG:

`pdfimages -png {{ścieżka/do/pliku.pdf}} {{przedrostek_nazwy_pliku}}`

- Wyodrębnij obrazy ze stron 3 do 5:

`pdfimages -f {{3}} -l {{5}} {{ścieżka/do/pliku.pdf}} {{przedrostek_nazwy_pliku}}`

- Wyodrębnij obrazy z pliku PDF oraz zawrzyj numer strony w nazwach wyjściowych:

`pdfimages -p {{ścieżka/do/pliku.pdf}} {{przedrostek_nazwy_pliku}}`

- Wyświetl listę informacji o każdym obrazie w pliku PDF:

`pdfimages -list {{ścieżka/do/pliku.pdf}}`
