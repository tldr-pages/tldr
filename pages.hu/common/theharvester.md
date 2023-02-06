# theHarvester

> A behatolásvizsgálat korai szakaszában használható eszköz. További információ: <https://github.com/laramies/theHarvester>.

- Információgyűjtés egy tartományról a Google segítségével:

`theHarvester --domain {{domain_name}} --source google`

- Információgyűjtés egy tartományról több forrás felhasználásával:

`theHarvester --domain {{domain_name}} --source {{google,bing,crtsh}}`

- Az eredmények határértékének módosítása a munkavégzéshez:

`theHarvester --domain {{domain_name}} --source {{google}} --limit {{200}}`

- A kimenet mentése két fájlba XML és HTML formátumban:

`theHarvester --domain {{domain_name}} --source {{google}} --file {{output_file_name}}`

- Az összes rendelkezésre álló lehetőség kimenete:

`theHarvester --help`
