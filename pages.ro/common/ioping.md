# ioping

> Monitorizați latența I/O în timp real.
> Mai multe informaţii: <https://github.com/koct9i/ioping>

- Afișează latența I/O pe disc utilizând valorile implicite și directorul curent:

`ioping .`

- Măsuraţi latenţa pe /tmp utilizând 10 cereri de câte 1 megabyte fiecare:

`ioping -c 10 -s 1M /tmp`

- Măsura disc caută rata pe `/dev/sdx`:

`ioping -R {{/dev/sdX}}`

- Măsurați viteza secvențială a discului pe `/dev/sdx`:

`ioping -RL {{/dev/sdX}}`
