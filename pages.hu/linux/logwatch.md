# logwatch

> A gyakori szolgáltatások (pl. apache, pam_unix, sshd, stb.) sok különböző naplófájlját foglalja össze egyetlen jelentésben. További információ: <https://manned.org/logwatch>.

- Naplófájlok elemzése egy bizonyos részletességű dátumtartományra vonatkozóan:

`logwatch --range {{yesterday|today|all|help}} --detail {{low|medium|others}}'`

- A jelentés korlátozása, hogy csak egy kiválasztott szolgáltatásra vonatkozó információkat tartalmazzon:

`logwatch --range {{all}} --service {{apache|pam_unix|etc}}`
