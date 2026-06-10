#քրոնիկ

> Ցուցադրել `stdout` և `stderr` հրամանը, եթե և միայն այն ձախողվելու դեպքում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/chronic>:.

- Ցուցադրել նշված հրամանի `stdout` և `stderr`-ը, եթե և միայն այն դեպքում, եթե այն արտադրում է ոչ զրոյական ելքի կոդ կամ խափանում է.:

`chronic {{command}} {{option1 option2 ...}}`

- Ցուցադրել նշված հրամանի `stdout` և `stderr`, եթե և միայն այն դեպքում, եթե այն արտադրում է ոչ դատարկ `stderr`:

`chronic -e {{command}} {{option1 option2 ...}}`

- Միացնել [v]erbose ռեժիմը.:

`chronic -v {{command}} {{option1 option2 ...}}`
