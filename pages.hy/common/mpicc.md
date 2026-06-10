# mpicc

> Բացեք MPI C wrapper կոմպիլյատորը:.
> Լրացուցիչ տեղեկություններ. <https://www.mpich.org/static/docs/latest/www1/mpicc.html>:.

- Կազմել աղբյուրի կոդը ֆայլ օբյեկտի ֆայլի մեջ.:

`mpicc -c {{path/to/file}}.c`

- Կապեք օբյեկտի ֆայլը և կատարեք.:

`mpicc -o {{executable}} {{path/to/object_file}}.o`

- Կազմել և կապել աղբյուրի կոդը մեկ հրամանով.:

`mpicc -o {{executable}} {{path/to/file}}.c`
