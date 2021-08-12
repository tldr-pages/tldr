# Xephyr

> Un server X imbricate care rulează ca o aplicație X.

- Creați o fereastră neagră cu ID-ul de afișare „:2":

`Xephyr -br -ac -noreset -screen {{800x600}} {{:2}}`

- Porniți o aplicație X pe noul ecran:

`DISPLAY=:2 {{command_name}}`
