# tqdm

> Ցույց տալ առաջընթացը հրամանի ժամանակի ընթացքում:.
> Լրացուցիչ տեղեկություններ. <https://tqdm.github.io/docs/cli/>:.

- Ցույց տալ կրկնությունները վայրկյանում և օգտագործել `stdout` այնուհետև՝:

`{{seq 10000000}} | tqdm | {{command}}`

- Ստեղծեք առաջընթացի գոտի.:

`{{seq 10000000}} | tqdm --total {{10000000}} | {{command}}`

- Ստեղծեք արխիվ գրացուցակից և օգտագործեք այդ գրացուցակի ֆայլերի քանակը՝ առաջընթացի տող ստեղծելու համար.:

`zip {{[-r|--recurse-paths]}} {{path/to/archive.zip}} {{path/to/directory}} | tqdm --total $(find {{path/to/directory}} | wc {{[-l|--lines]}}) --unit files --null`

- Ստեղծեք արխիվ tar-ով և ստեղծեք առաջընթացի տող (համակարգի ագնոստիկ, GNU tar-ն օգտագործում է `stdout`, իսկ BSD tar-ը՝ `stderr`):

`tar vzcf {{path/to/archive.tar.gz}} {{path/to/directory}} 2>&1 | tqdm --total $(find {{path/to/directory}} | wc {{[-l|--lines]}}) --unit files --null`
