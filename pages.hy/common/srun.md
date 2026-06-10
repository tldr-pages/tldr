# srun

> Գործարկեք հրաման Slurm աշխատանքային ծանրաբեռնվածության կառավարչի տակ:.
> Լրացուցիչ տեղեկություններ. <https://slurm.schedmd.com/srun.html>:.

- Ինտերակտիվ կերպով գործարկեք պարզ հրաման.:

`srun hostname`

- Գործարկել աշխատանք 4 առաջադրանքով (CPU).:

`srun {{[-n|--ntasks]}} 4 {{path/to/program}}`

- հատկացնել 8 ԳԲ հիշողություն.:

`srun --mem 8G {{path/to/program}}`

- Գործարկել աշխատանք կոնկրետ բաժանման վրա.:

`srun {{[-p|--partition]}} gpu {{path/to/program}}`

- Գործարկեք աշխատանք և պահեք արդյունքը ֆայլում՝:

`srun {{path/to/program}} > {{path/to/output}}`
