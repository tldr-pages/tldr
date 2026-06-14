# mkvmerge

> Միավորել և հանել մուլտիմեդիա հոսքերը:.
> Լրացուցիչ տեղեկություններ. <https://mkvtoolnix.download/doc/mkvmerge.html>:.

- Ցուցադրել Matroska ֆայլի մասին տեղեկատվություն.:

`mkvmerge --identify {{path/to/file.mkv}}`

- Աուդիո հանեք որոշակի ֆայլի 1-ին ուղուց.:

`mkvextract tracks {{path/to/file.mkv}} {{1}}:{{path/to/output.webm}}`

- Քաղեք ենթագրերը կոնկրետ ֆայլի 3-րդ ուղուց.:

`mkvextract tracks {{path/to/file.mkv}} {{3}}:{{path/to/subs.srt}}`

- Ավելացնել ենթավերնագիր ֆայլին.:

`mkvmerge --output {{path/to/output.mkv}} {{path/to/file.mkv}} {{path/to/subs.srt}}`
