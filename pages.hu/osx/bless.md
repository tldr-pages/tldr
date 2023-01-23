# bless

> A kötet indítási képességének és az indítólemez beállítása. További információ: <https://ss64.com/osx/bless.html>.

- Áldjon meg egy kötetet csak Mac OS X vagy Darwin operációs rendszerrel, és hozza létre a BootX és `boot.efi` fájlokat szükség szerint:

`bless --folder {{/Volumes/Mac OS X/System/Library/CoreServices}} --bootinfo --bootefi`

- Állítson be egy olyan kötetet, amely Mac OS 9-et vagy Mac OS X-et tartalmaz, aktív kötetnek:

`bless --mount {{/Volumes/Mac OS}} --setBoot`

- Állítsa a rendszert NetBoot-ra, és sugározzon egy elérhető kiszolgálót:

`bless --netboot --server {{bsdp://255.255.255.255}}`

- Gyűjtsön információt az aktuálisan kiválasztott kötetről (a firmware által meghatározottak szerint), amely alkalmas a Property Lists elemzésére alkalmas programba való továbbításra:

`bless --info --plist`
