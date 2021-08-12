# powerstat

> Măsoară consumul de energie al unui computer care are o sursă de alimentare a bateriei sau acceptă interfața RAPL.
> Mai multe informaţii: <http://manpages.ubuntu.com/manpages/bionic/man8/powerstat.8.html>

- Măsurați puterea cu valoarea implicită a 10 eșantioane cu un interval de 10 secunde:

`powerstat`

- Măsurați puterea cu numărul personalizat de eșantioane și durata intervalului:

`powerstat {{interval}} {{number_of_samples}}`

- Măsuraţi puterea utilizând interfaţa RAPL de la Intel:

`powerstat -R {{interval}} {{number_of_samples}}`

- Afișați o histogramă a măsurătorilor de putere:

`powerstat -H {{interval}} {{number_of_samples}}`

- Activați toate opțiunile de colectare a statisticilor:

`powerstat -a {{interval}} {{number_of_samples}}`
