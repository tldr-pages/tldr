# sstat

> Vizualizați informații despre executarea de lucrări.
> Mai multe informaţii: <https://slurm.schedmd.com/sstat.html>

- Afișează informații despre starea unei liste separate prin virgulă de locuri de muncă:

`sstat --jobs={{job_id}}`

- Afișați ID-ul de locuri de muncă, CPU mediu și dimensiunea medie a memoriei virtuale a unei liste separate prin virgulă de locuri de muncă, cu țevi ca delimitatoare de coloană:

`sstat --parsable --jobs={{job_id}} --format={{JobID}},{{AveCPU}},{{AveVMSize}}`

- Afișează lista de câmpuri disponibile:

`sstat --helpformat`
