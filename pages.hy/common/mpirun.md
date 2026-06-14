#մպիրուն

> Կատարեք սերիական և զուգահեռ աշխատանքներ Open MPI-ում:.
> Տես նաև՝ `mpic++`:.
> Լրացուցիչ տեղեկություններ. <https://docs.open-mpi.org/en/main/man-openmpi/man1/mpirun.1.html>:.

- Գործարկել Open MPI ծրագիր.:

`mpirun {{path/to/executable}}`

- Իրականացրեք Open MPI ծրագիր `n` զուգահեռ գործընթացներով.:

`mpirun -n {{n}} {{path/to/executable}}`

- Թույլատրել ավելի շատ գործընթացներ, քան առկա ֆիզիկական միջուկները.:

`mpirun -oversubscribe {{path/to/executable}}`
