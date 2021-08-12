# ab

> Apache HTTP instrument de benchmarking server.
> Mai multe informaţii: <https://httpd.apache.org/docs/current/programs/ab.html>

- Executați 100 de cereri HTTP GET la un anumit URL:

`ab -n {{100}} {{url}}`

- Executați 100 de cereri HTTP GET, în loturi simultane de 10, la un URL:

`ab -n {{100}} -c {{10}} {{url}}`

- Executați 100 de cereri HTTP POST la un URL, folosind o sarcină utilă JSON dintr-un fișier:

`ab -n {{100}} -T {{application/json}} -p {{path/to/file.json}} {{url}}`

- Utilizați HTTP [K] eep Alive, adică efectuați mai multe solicitări în cadrul unei sesiuni HTTP:

`ab -k {{url}}`

- Setați numărul maxim de secunde pentru a petrece pentru benchmarking:

`ab -t {{60}} {{url}}`
