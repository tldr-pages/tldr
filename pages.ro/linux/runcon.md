# runcon

> Executați un program într-un context de securitate SELinux diferit.
> Cu nici context, nici comandă, imprimați contextul de securitate curent.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/runcon>

- Determinați domeniul curent:

`runcon`

- Specificați domeniul pentru a rula o comandă în:

`runcon -t {{domain}}_t {{command}}`

- Specificați rolul contextual pentru a rula o comandă cu:

`runcon -r {{role}}_r {{command}}`

- Specificați întregul context pentru a rula o comandă cu:

`runcon {{user}}_u:{{role}}_r:{{domain}}_t {{command}}`
