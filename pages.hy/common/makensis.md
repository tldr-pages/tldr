# makensis

> NSIS տեղադրողների համար միջպլատֆորմային կոմպիլյատոր:.
> Այն կազմում է NSIS սկրիպտը Windows-ի տեղադրիչի գործարկվող սարքի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://nsis.sourceforge.io/Docs/Chapter3.html>:.

- Կազմեք NSIS սցենար.:

`makensis {{path/to/file.nsi}}`

- Կազմեք NSIS սցենար խիստ ռեժիմով (նախազգուշացումները վերաբերվեք որպես սխալներ).:

`makensis -WX {{path/to/file.nsi}}`

- Ցուցադրել օգնություն կոնկրետ հրամանի համար.:

`makensis -CMDHELP {{command}}`
