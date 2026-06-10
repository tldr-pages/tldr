# դոկեր կոնտեյներ exec

> Կատարեք հրաման արդեն աշխատող Docker կոնտեյների վրա:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/container/exec/>:.

- Մուտքագրեք ինտերակտիվ կեղևի նստաշրջան արդեն աշխատող կոնտեյների վրա.:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{container_name}} {{/bin/bash}}`

- Գործարկեք հրամանը հետին պլանում (անջատված) աշխատող կոնտեյների վրա.:

`docker {{[exec|container exec]}} {{[-d|--detach]}} {{container_name}} {{command}}`

- Ընտրեք աշխատանքային գրացուցակը տվյալ հրամանի համար, որը պետք է կատարվի հետևյալում.:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{path/to/directory}} {{container_name}} {{command}}`

- Գործարկեք հրամանը ֆոնային ռեժիմում գոյություն ունեցող կոնտեյների վրա, բայց բաց պահեք `stdin`:

`docker {{[exec|container exec]}} {{[-i|--interactive]}} {{[-d|--detach]}} {{container_name}} {{command}}`

- Գործող Bash նիստում սահմանեք շրջակա միջավայրի փոփոխական.:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-e|--env]}} {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`

- Գործարկել հրամանը որպես կոնկրետ օգտվող.:

`docker {{[exec|container exec]}} {{[-u|--user]}} {{user}} {{container_name}} {{command}}`
