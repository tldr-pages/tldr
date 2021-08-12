# ffuf

> Subdomeniu și instrument de descoperire director.
> Mai multe informaţii: <https://github.com/ffuf/ffuf>

- Descoperiți directoare folosind un [w] ordlist pe o țintă [u] rl cu [c] olorizat și [v] erbose ouput:

`ffuf -w {{path/to/wordlist}} -u {{https://target/FUZZ}} -c -v`

- Fuzz- [H] eaders cu un fișier gazdă pe un site traget și [m] atch HTTP 200 [c] răspunsuri ode:

`ffuf -w {{hosts.txt}} -u {{https://example.org}} -H "{{Host: FUZZ}}" -mc {{200}}`

- Descoperiți directoarele folosind un [w] Ordlist pe un site web țintă cu un timp de lucru maxim individual de 60 de secunde și adâncimea de descoperire recursivă de 2 nivele:

`ffuf -w {{path/to/wordlist}} -u {{https://target/FUZZ}} -maxtime-job {{60}} -recursion -recursion-depth {{2}}`

- Fuzz GET parametru pe un site țintă și [f] ilter out mesaj [s] ize răspuns de 4242 octeți:

`ffuf -w {{path/to/param_names.txt}} -u {{https://target/script.php?FUZZ=test_value}} -fs {{4242}}`

- Metoda Fuzz POST cu POST [d] ata parolei pe un site țintă și [f] ilter out răspuns HTTP [c] ode 401:

`ffuf -w {{path/to/postdata.txt}} -X {{POST}} -d "{{username=admin\&password=FUZZ}}" -u {{https://target/login.php}} -fc {{401}}`

- Descoperă subdomenii folosind o listă de subdoomain pe un site web țintă:

`ffuf -w {{subdomains.txt}} -u {{https://website.com}} -H "{{Host: FUZZ.website.com}}"`
