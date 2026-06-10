# վերահսկիչլ

> Վերահսկող, հաճախորդ/սերվեր համակարգ, որն իր օգտատերերին թույլ է տալիս կառավարել մի շարք գործընթացներ UNIX-ի նման օպերացիոն համակարգերում:.
> Supervisorctl-ը ղեկավարի հրամանի տող-հաճախորդի կտորն է, որն ապահովում է կեղևի նման ինտերֆեյս:.
> Լրացուցիչ տեղեկություններ. <https://supervisord.org/running.html#running-supervisorctl>:.

- Ցույց տալ գործընթացի կարգավիճակը (կամ բոլոր գործընթացները, եթե `process_name` նշված չէ):

`supervisorctl status {{process_name}}`

- Գործընթաց սկսել/դադարեցնել/վերագործարկել.:

`supervisorctl {{start|stop|restart}} {{process_name}}`

- Սկսել / դադարեցնել / վերագործարկել բոլոր գործընթացները խմբում.:

`supervisorctl {{start|stop|restart}} {{group_name}}:*`

- Ցույց տալ գործընթացի վերջին 100 բայթը `stderr`:

`supervisorctl tail -100 {{process_name}} stderr`

- Շարունակեք ցուցադրել գործընթացի `stdout`.:

`supervisorctl tail -f {{process_name}} stdout`

- Վերբեռնեք գործընթացի կազմաձևման ֆայլը՝ անհրաժեշտության դեպքում գործընթացները ավելացնելու/հեռացնելու համար.:

`supervisorctl update`
