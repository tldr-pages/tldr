# docker կոնտեյների թարմացում

> Թարմացրեք Docker բեռնարկղերի կոնֆիգուրացիան:.
> Նշում. այս հրամանը չի աջակցվում Windows կոնտեյներների համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/container/update/>:.

- Թարմացրեք վերագործարկման քաղաքականությունը՝ կիրառելու համար, երբ որոշակի կոնտեյներ դուրս է գալիս.:

`docker {{[update|container update]}} --restart {{always|no|on-failure|unless-stopped}} {{container_name}}`

- Թարմացրեք քաղաքականությունը՝ կոնկրետ կոնտեյները մինչև երեք անգամ վերագործարկելու համար, երբ այն դուրս է գալիս ելքի ոչ զրոյական կարգավիճակով.:

`docker {{[update|container update]}} --restart on-failure:3 {{container_name}}`

- Թարմացրեք որոշակի կոնտեյների համար հասանելի պրոցեսորների քանակը.:

`docker {{[update|container update]}} --cpus {{count}} {{container_name}}`

- Թարմացրեք հիշողության սահմանաչափը [M] մեգաբայթով կոնկրետ կոնտեյների համար.:

`docker {{[update|container update]}} {{[-m|--memory]}} {{limit}}M {{container_name}}`

- Թարմացրեք գործընթացի ID-ների առավելագույն քանակը, որոնք թույլատրվում են որոշակի կոնտեյների ներսում (օգտագործեք `-1` անսահմանափակ համար).:

`docker {{[update|container update]}} --pids-limit {{count}} {{container_name}}`

- Թարմացրեք հիշողության քանակը [M] մեգաբայթում, որը որոշակի կոնտեյներ կարող է փոխարինել սկավառակի վրա (օգտագործեք `-1` անսահմանափակ համար):

`docker {{[update|container update]}} --memory-swap {{limit}}M {{container_name}}`
