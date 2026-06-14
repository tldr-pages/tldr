# perlbrew

> Կառավարեք Perl-ի տեղադրումները հիմնական գրացուցակում:.
> Տես նաև՝ `asdf`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/gugod/App-perlbrew>:.

- Նախաձեռնել `perlbrew` միջավայրը՝:

`perlbrew init`

- Ցուցակեք հասանելի Perl տարբերակները.:

`perlbrew available`

- Տեղադրեք/տեղահանեք Perl տարբերակը.:

`perlbrew {{install|uninstall}} {{version}}`

- Թվարկեք perl տեղադրումները.:

`perlbrew list`

- Անցեք տեղադրման և սահմանեք այն որպես լռելյայն.:

`perlbrew switch perl-{{version}}`

- Կրկին օգտագործեք Perl համակարգը.:

`perlbrew off`

- Ցուցակե՛ք տեղադրված CPAN մոդուլները՝ օգտագործվող տեղադրման համար.:

`perlbrew list-modules`

- Կլոնավորեք CPAN մոդուլները մեկ տեղադրումից մյուսը.:

`perlbrew clone-modules {{source_installation}} {{destination_installation}}`
