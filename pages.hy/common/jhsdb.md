# jhsdb

> Կցեք Java գործընթացին կամ գործարկեք հետմահու վրիպազերծիչ՝ վթարված Java վիրտուալ մեքենայի հիմնական աղբավայրը վերլուծելու համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/jhsdb>:.

- Տպել կույտ և կողպել Java գործընթացի տեղեկատվությունը.:

`jhsdb jstack --pid {{pid}}`

- Բացեք հիմնական աղբավայրը ինտերակտիվ կարգաբերման ռեժիմում.:

`jhsdb clhsdb --core {{path/to/core_dump}} --exe {{path/to/jdk_or_bin_or_java}}`

- Սկսեք հեռակա կարգաբերման սերվեր.:

`jhsdb debugd --pid {{pid}} --serverid {{optional_unique_id}}`

- Միացեք գործընթացին ինտերակտիվ կարգաբերման ռեժիմում.:

`jhsdb clhsdb --pid {{pid}}`
