# git flow

> A Git kiterjesztések gyűjteménye, amely magas szintű tárolóműveleteket biztosít. További információ: <https://github.com/nvie/gitflow>.

- Inicializálja egy meglévő Git-tárházon belül:

`git flow init`

- Kezdje el a fejlesztést egy funkció ágon a `develop` alapján:

`git flow feature start {{feature}}`

- Fejezze be a fejlesztést egy feature branch-en, egyesítve azt a `develop` branch-be és törölve azt:

`git flow feature finish {{feature}}`

- Egy funkció közzététele a távoli kiszolgálóra:

`git flow feature publish {{feature}}`

- Egy másik felhasználó által közzétett funkció megszerzése:

`git flow feature pull origin {{feature}}`
