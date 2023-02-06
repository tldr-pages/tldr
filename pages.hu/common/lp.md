# lp

> További információ: <https://manned.org/lp>.

- Egy parancs kimeneteinek kinyomtatása az alapértelmezett nyomtatóra (lásd `lpstat` parancs):

`echo "test" | lp`

- Egy fájl nyomtatása az alapértelmezett nyomtatóra:

`lp {{path/to/filename}}`

- Fájl nyomtatása egy megnevezett nyomtatóra (lásd `lpstat` parancs):

`lp -d {{printer_name}} {{path/to/filename}}`

- A fájl N példányának nyomtatása az alapértelmezett nyomtatóra (az N helyett a kívánt példányszámot kell beírni):

`lp -n {{N}} {{path/to/filename}}`

- Csak bizonyos oldalak nyomtatása az alapértelmezett nyomtatóra (az 1., 3-5. és 16. oldal nyomtatása):

`lp -P 1,3-5,16 {{path/to/filename}}`

- Egy munka nyomtatásának folytatása:

`lp -i {{job_id}} -H resume`
