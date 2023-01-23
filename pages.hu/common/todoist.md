# todoist

> A Todoist elérése a parancssorból. További információ: <https://github.com/sachaos/todoist>.

- Feladat hozzáadása:

`todoist add "{{task_name}}"`

- Adjon hozzá egy magas prioritású feladatot címkével, projekttel és esedékességgel:

`todoist add "{{task_name}}" --priority {{1}} --label-ids "{{label_id}}" --project-name "{{project_name}}" --date "{{tmr 9am}}"`

- Nagy prioritású feladat hozzáadása címkével, projekttel és esedékességi dátummal gyors módban:

`todoist quick '#{{project_name}} "{{tmr 9am}}" p{{1}} {{task_name}} @{{label_name}}'`

- Az összes feladat listázása fejléccel és színnel:

`todoist --header --color list`

- Az összes magas prioritású feladat listázása:

`todoist list --filter p{{1}}`

- A megadott címkével rendelkező mai magas prioritású feladatok listázása:

`todoist list --filter '(@{{label_name}} | {{today}}) & p{{1}}'`
