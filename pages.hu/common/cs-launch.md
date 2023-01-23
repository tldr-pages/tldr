# cs launch

> Indítson el egy alkalmazást a névből közvetlenül egy vagy több Maven függőségből, anélkül, hogy telepítenie kellene. További információ: <https://get-coursier.io/docs/cli-launch>.

- Egy adott alkalmazás indítása argumentumokkal:

`cs launch {{application_name}} -- {{arg1 arg2 ...}}`

- Egy adott alkalmazásváltozat indítása argumentumokkal:

`cs launch {{application_name}}:{{application_version}} -- {{arg1 arg2 ...}}`

- Az alkalmazás egy adott verziójának elindítása, megadva, hogy melyik a fő fájl:

`cs launch {{group_id}}:{{artifact_id}}:{{artifact_version}} --main-class {{path/to/main_class_file}}`

- Egy alkalmazás indítása meghatározott java opciókkal és egy jvm memóriával:

`cs launch --java-opt {{-Doption_name1:option_value1 -Doption_name2:option_value2 ...}} --java-opt {{-Xjvm_option1 -Xjvm_option2 ...}} {{application_name}}`
