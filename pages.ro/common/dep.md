# dep

> Un instrument CLI pentru implementarea aplicaţiilor PHP.
> Notă: Comanda Go `dep` cu același nume este învechită și arhivată.
> Mai multe informaţii: <https://deployer.org>

- Iniţializarea interactivă a implementatorului în calea locală (utilizaţi un şablon cadru cu `—template= {{template}} `):

`dep init`

- Implementați o aplicație la o gazdă la distanță:

`dep deploy {{hostname}}`

- Revenirea la versiunea anterioară de lucru:

`dep rollback`

- Conectați-vă la o gazdă la distanță prin ssh:

`dep ssh {{hostname}}`

- Lista comenzilor:

`dep list`

- Rulați orice comandă arbitrară pe gazdele de la distanță:

`dep run "{{command}}"`

- Afișează ajutor pentru o comandă:

`dep help {{command}}`
