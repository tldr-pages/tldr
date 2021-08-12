# subfinder

> Un instrument de descoperire subdomeniu care descoperă subdomenii valide pentru site-uri web.
> Proiectat ca un cadru pasiv pentru a fi util pentru recompensele de bug-uri și sigur pentru testarea penetrării.
> Mai multe informaţii: <https://github.com/subfinder/subfinder>

- Găsiți subdomenii pentru un anumit domeniu:

`subfinder -d {{example.com}}`

- Arată doar subdomeniile găsite:

`subfinder --silent -d {{example.com}}`

- Utilizați un atac brute-force pentru a găsi subdomenii:

`subfinder -d {{example.com}} -b`

- Elimină subdomeniile metacaractere:

`subfinder -nW -d {{example.com}}`

- Utilizaţi o listă de rezolvatori separate prin virgulă:

`subfinder -r {{8.8.8.8}},{{1.1.1.1}} -d {{example.com}}`
