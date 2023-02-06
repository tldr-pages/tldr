# ffuf

> Aldomain- és könyvtárkereső eszköz. További információ: <https://github.com/ffuf/ffuf>.

- Könyvtárak felfedezése egy \[w\]ordlist segítségével egy cél \[u\]rl-en, \[c\]olorizált és \[v\]erbose kimenettel:

`ffuf -w {{path/to/wordlist}} -u {{https://target/FUZZ}} -c -v`

- Fuzz host-\[H\]eaders egy host-fájl segítségével egy célwebhelyen, és \[m\]atch HTTP 200 \[c\]ode válaszok:

`ffuf -w {{hosts.txt}} -u {{https://example.org}} -H "{{Host: FUZZ}}" -mc {{200}}`

- Könyvtárak felfedezése egy \[w\]ordlist segítségével egy célweboldalon, 60 másodperces maximális egyéni munkaidővel és 2 szintű rekurziós felfedezési mélységgel:

`ffuf -w {{path/to/wordlist}} -u {{https://target/FUZZ}} -maxtime-job {{60}} -recursion -recursion-depth {{2}}`

- Fuzz GET paraméter egy célweboldalon és \[f\]ilter out message \[s\]ize response of 4242 bytes:

`ffuf -w {{path/to/param_names.txt}} -u {{https://target/script.php?FUZZ=test_value}} -fs {{4242}}`

- Fuzz POST módszer POST \[d\]ata jelszóval egy célweboldalon és \[f\]ilter out HTTP válasz \[c\]ode 401:

`ffuf -w {{path/to/postdata.txt}} -X {{POST}} -d "{{username=admin\&password=FUZZ}}" -u {{https://target/login.php}} -fc {{401}}`

- Aldomainek felfedezése egy aldomain-lista segítségével egy célweboldalon:

`ffuf -w {{subdomains.txt}} -u {{https://website.com}} -H "{{Host: FUZZ.website.com}}"`
