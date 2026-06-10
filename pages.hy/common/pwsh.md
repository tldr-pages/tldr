# pwsh

> Shell և սկրիպտավորման լեզու, որը նախատեսված է հատկապես համակարգի կառավարման համար:.
> Այս հրամանը վերաբերում է PowerShell 6-րդ և ավելի բարձր տարբերակին (նաև հայտնի է որպես PowerShell Core և խաչմերուկային PowerShell):.
> Windows-ի սկզբնական տարբերակը (5.1 և ավելի ցածր, որը նաև հայտնի է որպես հին Windows PowerShell) օգտագործելու համար օգտագործեք `powershell` `pwsh`-ի փոխարեն:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>:.

- Սկսեք ինտերակտիվ shell նստաշրջան.:

`pwsh`

- Սկսեք ինտերակտիվ կեղևի նստաշրջան առանց գործարկման կազմաձևերի բեռնման.:

`pwsh -NoProfile`

- Կատարել հատուկ հրամաններ.:

`pwsh -Command "{{echo 'powershell is executed'}}"`

- Կատարել կոնկրետ սցենար.:

`pwsh -File {{path/to/script.ps1}}`

- Սկսեք նիստ PowerShell-ի հատուկ տարբերակով.:

`pwsh -Version {{version}}`

- Կանխել կեղևի ելքը գործարկման հրամանները գործարկելուց հետո.:

`pwsh -NoExit`

- Նկարագրեք PowerShell-ին ուղարկված տվյալների ձևաչափը.:

`pwsh -InputFormat {{Text|XML}}`

- Որոշեք, թե ինչպես է ֆորմատավորվում PowerShell-ի ելքը.:

`pwsh -OutputFormat {{Text|XML}}`
