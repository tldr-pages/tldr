# black

> Formatteer Python-code automatisch.
> Meer informatie: <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>.

- Formatteer een bestand of hele map automatisch:

`black {{pad/naar/bestand_of_map}}`

- Formatteer de code die is opgegeven als een string:

`black {{[-c|--code]}} "{{code}}"`

- Toon of een bestand of map wijzigingen zou ondergaan als deze geformatteerd zou worden:

`black --check {{pad/naar/bestand_of_map}}`

- Toon wijzigingen die in een bestand of map zouden worden aangebracht zonder ze daadwerkelijk toe te passen (dry-run):

`black --diff {{pad/naar/bestand_of_map}}`

- Formatteer een bestand of map automatisch, waarbij foutmeldingen uitsluitend naar `stderr` worden verstuurd:

`black {{[-q|--quiet]}} {{pad/naar/bestand_of_map}}`

- Formatteer een bestand of map automatisch zonder enkele aanhalingstekens te vervangen door dubbele aanhalingstekens (adoptiehulp, vermijd dit voor nieuwe projecten):

`black {{[-S|--skip-string-normalization]}} {{pad/naar/bestand_of_map}}`
