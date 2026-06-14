# դոպլեր վազք

> Գործարկեք հրաման՝ դոպլերային գաղտնիքներով, որոնք ներարկվում են շրջակա միջավայր:.
> Լրացուցիչ տեղեկություններ. <https://docs.doppler.com/docs/cli#run-a-command-with-secrets-populated-in-environment>:.

- Գործարկել հրամանը.:

`doppler run --command {{command}}`

- Գործարկել բազմաթիվ հրամաններ.:

`doppler run --command {{command1 && command2}}`

- Գործարկել սցենար.:

`doppler run {{path/to/command.sh}}`

- Գործարկել հրամանը նշված նախագծով և կազմաձևով.:

`doppler run -p {{project_name}} -c {{config_name}} -- {{command}}`

- Ավտոմատ կերպով վերագործարկեք գործընթացը, երբ գաղտնիքները փոխվում են.:

`doppler run --watch {{command}}`
