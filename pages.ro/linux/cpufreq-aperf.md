# cpufreq-aperf

> Calculați frecvența medie a procesorului pe o perioadă de timp.
> Necesită privilegii de root.
> Mai multe informaţii: <https://manned.org/cpufreq-aperf>

- Începeți calcularea, implicită la toate nucleele procesorului și intervalul de reîmprospătare 1 secundă:

`sudo cpufreq-aperf`

- Începeți calcularea numai pentru CPU 1:

`sudo cpufreq-aperf -c {{1}}`

- Începeți calcularea cu un interval de reîmprospătare de 3 secunde pentru toate nucleele procesorului:

`sudo cpufreq-aperf -i {{3}}`

- Se calculează o singură dată:

`sudo cpufreq-aperf -o`
