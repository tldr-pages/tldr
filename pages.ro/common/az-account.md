# az account

> Gestionați informațiile de abonament Azure.
> O parte din `az`, clientul de linie de comandă pentru Microsoft Azure.
> Mai multe informaţii: <https://docs.microsoft.com/cli/azure/account>

- Imprimați o listă de abonamente pentru contul conectat:

`az account list`

- Setați un `abonament” pentru a fi abonamentul activ în prezent:

`az account set --subscription {{subscription_id}}`

- Lista regiunilor acceptate pentru abonamentul activ în prezent:

`az account list-locations`

- Imprimați un token de acces pentru a fi utilizat cu „MS Graph API”:

`az account get-access-token --resource-type {{ms-graph}}`

- Detaliile de imprimare ale abonamentului activ în prezent într-un format specific:

`az account show --output {{json|tsv|table|yaml}}`
