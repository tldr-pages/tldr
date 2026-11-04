# cut

> Standart girdiden (`stdin`) veya dosyalardan alanları kes.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>.

- Satırların beşinci karakterini yazdır:

`{{komut}} | cut {{[-c|--characters]}} 5`

- Belirtilen dosyadaki satırların beşinci ile onuncu arasındaki karakterlerini yazdır:

`cut {{[-c|--characters]}} 5-10 {{dosya/yolu}}`

- Bir dosyadaki satırları bir ayırıcıya göre alanlara böl ve ikinci ile altıncı alanları yazdır (varsayılan ayırıcı `TAB`'dır):

`cut {{[-f|--fields]}} 2,6 {{dosya/yolu}}`

- Satırları belirtilen ayırıcıya göre böl ve ikinci alandan itibaren hepsini yazdır:

`{{komut}} | cut {{[-d|--delimiter]}} "{{ayırıcı}}" {{[-f|--fields]}} 2-`

- Ayırıcı olarak boşluk kullan ve yalnızca ilk 3 alanı yazdır:

`{{komut}} | cut {{[-d|--delimiter]}} " " {{[-f|--fields]}} -3`

- Yalnızca ayırıcıyı içeren satırları yazdır:

`{{komut}} | cut {{[-d|--delimiter]}} "{{:}}" {{[-f|--fields]}} {{1}} {{[-s|--only-delimited]}}`

- Satır sonu olarak yeni satır yerine `NUL` kullanan satırların belirli alanlarını yazdır:

`{{find . -print0}} | cut {{[-z|--zero-terminated]}} {{[-d|--delimiter]}} "{{/}}" {{[-f|--fields]}} {{2}}`
