# խեժ

> Արխիվացման կոմունալ:.
> Հաճախ զուգորդվում է սեղմման մեթոդի հետ, ինչպիսիք են `gzip` կամ `bzip2`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/tar/manual/tar.html>:.

- [c]ստեղծեք արխիվ և գրեք այն [f] ֆայլում՝:

`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}`

- [c]ստեղծեք g[z]ipped արխիվ և գրեք այն [f]ile-ում.:

`tar czf {{path/to/target.tar.gz}} {{path/to/file1 path/to/file2 ...}}`

- [c]ստեղծել g[z]ipped (սեղմված) արխիվ գրացուցակից՝ օգտագործելով հարաբերական ուղիները.:

`tar czf {{path/to/target.tar.gz}} {{[-C|--directory]}} {{path/to/directory}} .`

- E[x] տարեք (սեղմված) արխիվը [f]ի ընթացիկ գրացուցակ [v]erbosely:

`tar xvf {{path/to/source.tar[.gz|.bz2|.xz]}}`

- E[x] տեղափոխեք (սեղմված) արխիվը [f] ֆայլ թիրախային գրացուցակում.:

`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}} {{[-C|--directory]}} {{path/to/directory}}`

- [c]ստեղծեք սեղմված արխիվ և գրեք այն [f] ֆայլում՝ օգտագործելով ֆայլի ընդլայնումը, սեղմման ծրագիրը ավտոմատ կերպով որոշելու համար.:

`tar caf {{path/to/target.tar.xz}} {{path/to/file1 path/to/file2 ...}}`

- Հստակորեն նշեք tar [f]ile [v] բովանդակությունը.:

`tar tvf {{path/to/source.tar}}`

- E[x]tract ֆայլեր, որոնք համապատասխանում են արխիվի [f]ile օրինակին.:

`tar xf {{path/to/source.tar}} --wildcards "{{*.html}}"`
