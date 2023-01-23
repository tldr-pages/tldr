# repair-bde

> Kísérlet a sérült BitLocker titkosított kötet javítására vagy visszafejtésére. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/repair-bde>.

- Kísérlet egy megadott kötet javítására:

`repair-bde {{C:}}`

- Kísérlet egy megadott kötet javítására és egy másik kötetre történő kimenetre:

`repair-bde {{C:}} {{D:}}`

- Megpróbálja megjavítani a megadott kötetet a megadott helyreállítási kulcsfájl használatával:

`repair-bde {{C:}} -RecoveryKey {{path/to/file.bek}}`

- Megadott kötet javításának kísérlete a megadott numerikus helyreállítási jelszó használatával:

`repair-bde {{C:}} -RecoveryPassword {{password}}`

- Megadott kötet javításának kísérlete a megadott jelszó használatával:

`repair-bde {{C:}} -Password {{password}}`

- Megadott kötet javításának kísérlete a megadott kulcscsomag használatával:

`repair-bde {{C:}} -KeyPackage {{path/to/directory}}`

- Az összes kimenet naplózása egy adott fájlba:

`repair-bde {{C:}} -LogFile {{path/to/file}}`

- Az összes rendelkezésre álló opció megjelenítése:

`repair-bde /?`
