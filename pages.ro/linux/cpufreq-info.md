# cpufreq-info

> Un instrument pentru a afișa informații despre frecvența procesorului.
> Mai multe informaţii: <https://manned.org/cpufreq-info>

- Afișează informații de frecvență CPU pentru toate procesoarele:

`cpufreq-info`

- Afișați informațiile de frecvență CPU pentru procesorul specificat:

`cpufreq-info -c {{cpu_number}}`

- Afișați frecvența minimă și maximă admisă CPU:

`cpufreq-info -l`

- Afișați frecvența minimă și maximă curentă a procesorului și politica în format tabel:

`cpufreq-info -o`

- Afișați politicile de frecvență disponibile ale procesorului:

`cpufreq-info -g`

- Afișează frecvența curentă de lucru a procesorului într-un format care poate fi citit de om, în conformitate cu modulul kernel cpufreq:

`cpufreq-info -f -m`

- Afișează frecvența curentă de lucru a procesorului într-un format ușor de citit de om, citindu-l din hardware (disponibil numai pentru root):

`sudo cpufreq-info -w -m`
