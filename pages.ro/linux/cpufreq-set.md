# cpufreq-set

> Un instrument pentru modificarea setărilor de frecvență ale procesorului.
> Valoarea frecvenței trebuie să se încadreze între ieșirea comenzii `cpufreq-info -l`.
> Mai multe informaţii: <https://manned.org/cpufreq-set>

- Setați politica de frecvență a procesorului 1 la „spațiul de utilizator”:

`sudo cpufreq-set -c {{1}} -g {{userspace}}`

- Setați frecvența procesorului minim curent de CPU 1:

`sudo cpufreq-set -c {{1}} --min {{min_frequency}}`

- Setați frecvența procesorului maxim curent de CPU 1:

`sudo cpufreq-set -c {{1}} --max {{max_frequency}}`

- Setați frecvența curentă de lucru a procesorului 1:

`sudo cpufreq-set -c {{1}} -f {{work_frequency}}`
