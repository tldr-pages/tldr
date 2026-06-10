# մոծակների_փաբ

> Պարզ MQTT տարբերակ 3.1.1 հաճախորդ, որը կհրապարակի մեկ հաղորդագրություն թեմայի վերաբերյալ և դուրս կգա:.
> Լրացուցիչ տեղեկություններ. <https://mosquitto.org/man/mosquitto_pub-1.html>:.

- Հրապարակեք 32 ջերմաստիճանի արժեքը `sensors/temperature`-ից մինչև 192.168.1.1 (կանխադրված՝ `localhost`) թեմայի շուրջ՝ ծառայության որակը (`QoS`) սահմանված է 1:

`mosquitto_pub {{[-h|--host]}} {{192.168.1.1}} {{[-t|--topic]}} {{sensors/temperature}} {{[-m|--message]}} {{32}} {{[-q|--qos]}} {{1}}`

- Հրապարակեք ժամանակի դրոշմակնիքի և ջերմաստիճանի տվյալները `sensors/temperature` թեմայի վերաբերյալ ոչ ստանդարտ պորտի վրա գտնվող հեռավոր հոսթին.:

`mosquitto_pub {{[-h|--host]}} {{192.168.1.1}} {{[-p|--port]}} {{1885}} {{[-t|--topic]}} {{sensors/temperature}} {{[-m|--message]}} "{{1266193804 32}}"`

- Հրապարակեք լույսի անջատիչի կարգավիճակը և պահեք `switches/kitchen_lights/status` թեմայի վերաբերյալ հաղորդագրությունը հեռավոր հաղորդավարին, քանի որ լույսի անջատիչի իրադարձությունների միջև կարող է երկար ժամանակ լինել.:

`mosquitto_pub {{[-r|--retain]}} {{[-h|--host]}} "{{iot.eclipse.org}}" {{[-t|--topic]}} {{switches/kitchen_lights/status}} {{[-m|--message]}} "{{on}}"`

- Ուղարկեք ֆայլի բովանդակությունը (`data.txt`) որպես հաղորդագրություն և հրապարակեք այն `sensors/temperature` թեմային.:

`mosquitto_pub {{[-t|--topic]}} {{sensors/temperature}} {{[-f|--file]}} {{data.txt}}`

- Ուղարկեք ֆայլի բովանդակությունը (`data.txt`), կարդալով `stdin`-ից և ուղարկեք ամբողջ մուտքագրումը որպես հաղորդագրություն և հրապարակեք այն `sensors/temperature` թեմայում.:

`mosquitto_pub < {{data.txt}} {{[-t|--topic]}} {{sensors/temperature}} {{[-s|--stdin-file]}}`

- Կարդացեք նոր տողով սահմանազատված տվյալները `stdin`-ից որպես հաղորդագրություն և հրապարակեք դրանք `sensors/temperature` թեմայում.:

`{{echo data.txt}} | mosquitto_pub {{[-t|--topic]}} {{sensors/temperature}} {{[-l|--stdin-line]}}`
