# elasticsearch-keystore

> Կառավարեք Elasticsearch-ի կողմից օգտագործվող անվտանգ կարգավորումները (օրինակ՝ գաղտնաբառերը, նշանները և հավատարմագրերը):.
> Լրացուցիչ տեղեկություններ. <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/elasticsearch-keystore>:.

- Ստեղծեք նոր բանալիների պահեստ (գաղտնաբառով չպաշտպանված).:

`elasticsearch-keystore create`

- Ստեղծեք նոր գաղտնաբառով պաշտպանված բանալիների պահեստ.:

`elasticsearch-keystore create -p`

- Ինտերակտիվ կերպով ավելացրեք կարգավորում.:

`elasticsearch-keystore add {{setting_name}}`

- Ավելացրեք պարամետր `stdin`-ից՝:

`echo "{{setting_value}}" | elasticsearch-keystore add --stdin {{setting_name}}`

- Հեռացրեք կարգավորումները բանալիների պահեստից.:

`elasticsearch-keystore remove {{setting_name}}`

- Փոխել keystore գաղտնաբառը:

`elasticsearch-keystore passwd`

- Թվարկեք keystore-ում պահված բոլոր կարգավորումները.:

`elasticsearch-keystore list`

- Թարմացրեք keystore ձևաչափը (Elasticsearch-ի թարմացումից հետո).:

`elasticsearch-keystore upgrade`
