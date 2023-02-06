# replace

> Fájlok cseréje Lásd még: `robocopy`, `move`, `copy` és `del`. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/replace>.

- A célfájl cseréje a forráskönyvtárból származó fájlra:

`replace {{path/to/file_or_directory}} {{path/to/destination}}`

- Fájlok hozzáadása a célkönyvtárhoz a meglévő fájlok cseréje helyett:

`replace {{path/to/file_or_directory}} {{path/to/destination}} /a`

- Több fájl interaktív másolása, a célfájl cseréje vagy hozzáadása előtt kérdezősködéssel:

`replace {{path/to/file_or_directory}} {{path/to/destination}} /p`

- Még a csak olvasható fájlok cseréje is:

`replace {{path/to/file_or_directory}} {{path/to/destination}} /r`

- Várja meg, hogy behelyezzen egy lemezt, mielőtt kicseréli a fájlokat (eredetileg azért, hogy lehetővé tegye a floppylemez behelyezését):

`replace {{path/to/file_or_directory}} {{path/to/destination}} /w`

- A célkönyvtár alkönyvtáraiban lévő összes fájl cseréje:

`replace {{path/to/file_or_directory}} {{path/to/destination}} /s`

- Csak a célkönyvtárban lévő, a forráskönyvtárban lévő fájloknál régebbi fájlok cseréje:

`replace {{path/to/file_or_directory}} {{path/to/destination}} /u`

- Részletes használati információk megjelenítése:

`replace /?`
