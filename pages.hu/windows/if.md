# if

> Feltételes feldolgozást végez kötegelt szkriptekben. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/if>.

- A megadott parancsok végrehajtása, ha a feltétel igaz:

`if {{condition}} ({{echo Condition is true}})`

- A megadott parancsok végrehajtása, ha a feltétel hamis:

`if not {{condition}} ({{echo Condition is true}})`

- Az első megadott parancsok végrehajtása, ha a feltétel igaz, különben a második megadott parancsok végrehajtása:

`if {{condition}} ({{echo Condition is true}}) else ({{echo Condition is false}})`

- Ellenőrizze, hogy a `%errorlevel%` nagyobb vagy egyenlő-e a megadott kilépési kóddal:

`if errorlevel {{exit_code}} ({{echo Condition is true}})`

- Ellenőrizze, hogy két karakterlánc egyenlő-e:

`if %{{variable}}% == {{string}} ({{echo Condition is true}})`

- Ellenőrizze, hogy két karakterlánc egyenlő-e, a betűk nagy- és kisbetűinek figyelembevétele nélkül:

`if /i %{{variable}}% == {{string}} ({{echo Condition is true}})`

- Ellenőrizze, hogy létezik-e fájl:

`if exist {{path/to/file}} ({{echo Condition is true}})`
