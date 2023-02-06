# tee

> Olvasás a standard bemenetről és írás a standard kimenetre és fájlokra (vagy parancsokra). További információ: <https://www.gnu.org/software/coreutils/tee>.

- A szabványos bemenet másolása minden egyes fájlba, valamint a szabványos kimenetre:

`echo "example" | tee {{path/to/file}}`

- Függessze fel a megadott fájlokhoz, ne írja felül:

`echo "example" | tee -a {{path/to/file}}`

- Standard bemenet kiírása a terminálra, és egy másik programba is átvezetheti további feldolgozásra:

`echo "example" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- Hozzon létre egy "example" nevű könyvtárat, számolja meg a "example" könyvtárban lévő karakterek számát, és írja ki a "example" könyvtárat a terminálba:

`echo "example" | tee >(xargs mkdir) >(wc -c)`
