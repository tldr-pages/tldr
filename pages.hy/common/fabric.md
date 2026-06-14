#գործվածք

> Բաց կոդով շրջանակ՝ AI-ի միջոցով մարդկանց մեծացնելու համար:.
> Ապահովում է մոդուլային շրջանակ՝ կոնկրետ խնդիրներ լուծելու համար՝ օգտագործելով AI-ի հրահանգների ամբոխային փաթեթը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/danielmiessler/fabric#usage>:.

- Գործարկեք կարգավորումը՝ գործվածքը կարգավորելու համար.:

`fabric {{[-S|--setup]}}`

- Թվարկեք բոլոր առկա նախշերը.:

`fabric {{[-l|--listpatterns]}}`

- Գործարկեք օրինաչափություն ֆայլից մուտքագրմամբ.:

`fabric < {{path/to/input_file}} {{[-p|--pattern]}} {{pattern_name}}`

- Գործարկեք օրինակ YouTube տեսանյութի URL-ում.:

`fabric {{[-y|--youtube]}} "{{https://www.youtube.com/watch?v=video_id}}" {{[-p|--pattern]}} {{pattern_name}}`

- Շղթայական նախշերը միասին՝ խողովակաշարերի ելքով մեկից մյուսը.:

`fabric {{[-p|--pattern]}} {{pattern1}} | fabric {{[-p|--pattern]}} {{pattern2}}`

- Գործարկեք օգտագործողի կողմից սահմանված օրինաչափություն.:

`fabric {{[-p|--pattern]}} {{custom_pattern_name}}`

- Գործարկեք օրինաչափություն և պահեք արդյունքը ֆայլում.:

`fabric {{[-p|--pattern]}} {{pattern_name}} {{[-o|--output]}} {{path/to/output_file}}`

- Գործարկեք օրինաչափություն նշված փոփոխականներով.:

`fabric {{[-p|--pattern]}} {{pattern_name}} {{[-v|--variable]}} "{{variable_name}}:{{value}}"`
