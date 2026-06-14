# mpijavac

> Բացեք MPI կոմպիլյատորի փաթաթան Java-ի համար:.
> Տես նաև՝ `mpirun`:.
> Լրացուցիչ տեղեկություններ. <https://docs.open-mpi.org/en/main/features/java.html#building-java-mpi-applications>:.

- Կազմեք Java աղբյուրի ֆայլ.:

`mpijavac {{path/to/source_file}}.java`

- Կոմպիլյատորին փոխանցեք հավելվածին հատուկ դասընթացներ.:

`mpijavac -cp {{path/to/app}}.jar {{path/to/source_file}}.java`

- Ցույց տվեք MPI Java հավելվածներ ստեղծելու համար անհրաժեշտ դրոշները.:

`mpijavac --showme`

- Ցույց տվեք MPI Java հավելվածները կազմելու համար անհրաժեշտ դրոշները.:

`mpijavac --showme:compile`

- Ցուցադրել ամբողջությամբ կանչված Java կոմպիլյատորի հրամանի տողը.:

`mpijavac {{path/to/source_file}}.java --showme`
