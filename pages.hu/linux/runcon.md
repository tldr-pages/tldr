# runcon

> Egy program futtatása egy másik SELinux biztonsági környezetben. Ha nincs sem kontextus, sem parancs, akkor kiírja az aktuális biztonsági környezetet. További információ: <https://www.gnu.org/software/coreutils/runcon>.

- Az aktuális tartomány meghatározása:

`runcon`

- Adja meg a tartományt, amelyben egy parancsot futtat:

`runcon -t {{domain}}_t {{command}}`

- Adja meg a kontextus szerepét, amellyel a parancsot futtatni kívánja:

`runcon -r {{role}}_r {{command}}`

- A teljes környezet megadása a parancs futtatásához:

`runcon {{user}}_u:{{role}}_r:{{domain}}_t {{command}}`
