# docker container stats

> Toon een livestream van statistieken over het gebruik van bronnen voor containers.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/container/stats/>.

- Toon een livestream van de statistieken van alle draaiende containers:

`docker {{[stats|container stats]}}`

- Toon een livestream van statistieken voor één of meer containers:

`docker {{[stats|container stats]}} {{container1 container2 ...}}`

- Wijzig het kolommenformaat om het CPU-gebruikspercentage van de container te tonen:

`docker {{[stats|container stats]}} --format "{{.Name}}:\t{{.CPUPerc}}"`

- Toon statistieken voor alle containers (zowel draaiende als gestopte):

`docker {{[stats|container stats]}} {{[-a|--all]}}`

- Schakel streaming statistieken uit en haal alleen de huidige statistieken op:

`docker {{[stats|container stats]}} --no-stream`
