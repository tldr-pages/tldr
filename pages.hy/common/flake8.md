#փաթիլ8

> Ստուգեք Python կոդի ոճն ու որակը:.
> Լրացուցիչ տեղեկություններ. <https://flake8.pycqa.org/en/latest/user/options.html>:.

- Ֆայլը կամ գրացուցակը ռեկուրսիվ կերպով տեղադրեք.:

`flake8 {{path/to/file_or_directory}}`

- Վերադարձեք ֆայլը կամ գրացուցակը և ցույց տվեք այն տողը, որի վրա տեղի է ունեցել յուրաքանչյուր սխալ.:

`flake8 --show-source {{path/to/file_or_directory}}`

- Վերադարձեք ֆայլը կամ գրացուցակը և անտեսեք կանոնների ցանկը: (Բոլոր առկա կանոնները կարելի է գտնել <https://www.flake8rules.com/> կայքում):

`flake8 --ignore {{rule1,rule2,...}} {{path/to/file_or_directory}}`

- Փակեք ֆայլը կամ գրացուցակը ռեկուրսիվորեն, բայց բացառեք տվյալ գլոբուսներին կամ ենթատողերին համապատասխանող ֆայլերը.:

`flake8 --exclude {{substring1,glob2}} {{path/to/file_or_directory}}`
