# cgexec

> Limita, mede e controla recursos usados pelos processos.
> Há vários tipos de cgroup (conhecidos como controladores), tal como `cpu`, `memory`, etc.
> Mais informações: <https://manned.org/cgexec>.

- Executa um processo em um cgroup e controlador providos pelo usuário:

`cgexec -g {{controlador}}:{{nome_cgroup}} {{nome_processo}}`
