# theHarvester

> Un instrument conceput pentru a fi utilizat în stadiile incipiente ale unui test de penetrare.
> Mai multe informaţii: <https://github.com/laramies/theHarvester>

- Adunați informații despre un domeniu utilizând Google:

`theHarvester --domain {{domain_name}} --source google`

- Colectarea de informații despre un domeniu folosind mai multe surse:

`theHarvester --domain {{domain_name}} --source {{google,bing,crtsh}}`

- Modificați limita de rezultate pentru a lucra cu:

`theHarvester --domain {{domain_name}} --source {{google}} --limit {{200}}`

- Salvați ieșirea în două fișiere în format xml și html:

`theHarvester --domain {{domain_name}} --source {{google}} --file {{output_file_name}}`

- Ieșire toate opțiunile disponibile:

`theHarvester --help`
