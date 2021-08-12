# multipass

> CLI pentru a gestiona mașinile virtuale Ubuntu folosind hipervizoare native.
> Mai multe informaţii: <https://multipass.run/>

- Listați aliasurile care pot fi utilizate pentru a lansa o instanță:

`multipass find`

- Lansați o instanță nouă, setați numele și utilizați un fișier de configurare în cloud:

`multipass launch -n {{instance_name}} --cloud-init {{configuration_file}}`

- Listați toate instanțele create și unele dintre proprietățile lor:

`multipass list`

- Începeți o anumită instanță după nume:

`multipass start {{instance_name}}`

- Afișează proprietățile unei instanțe:

`multipass info {{instance_name}}`

- Deschideți un prompt shell pe o anumită instanță după nume:

`multipass shell {{instance_name}}`

- Ștergeți o instanță după nume:

`multipass delete {{instance_name}}`

- Montați un director într-o anumită instanță:

`multipass mount {{path/to/local/directory}} {{instance_name}}:{{path/to/target/directory}}`
