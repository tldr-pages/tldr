# cs գործարկում

> Գործարկեք հավելված անունից անմիջապես Maven-ի կախվածություններից՝ առանց այն տեղադրելու:.
> Լրացուցիչ տեղեկություններ. <https://get-coursier.io/docs/cli-launch>:.

- Գործարկեք հատուկ հավելված փաստարկներով.:

`cs launch {{application_name}} -- {{argument1 argument2 ...}}`

- Գործարկեք հատուկ հավելվածի տարբերակը փաստարկներով.:

`cs launch {{application_name}}:{{application_version}} -- {{argument1 argument2 ...}}`

- Գործարկեք հավելվածի հատուկ տարբերակը՝ նշելով, թե որն է հիմնական ֆայլը.:

`cs launch {{group_id}}:{{artifact_id}}:{{artifact_version}} --main-class {{path/to/main_class_file}}`

- Գործարկեք հավելված հատուկ Java ընտրանքներով և JVM հիշողության տարբերակներով.:

`cs launch --java-opt {{-Doption_name1:option_value1 -Doption_name2:option_value2 ...}} --java-opt {{-Xjvm_option1 -Xjvm_option2 ...}} {{application_name}}`
