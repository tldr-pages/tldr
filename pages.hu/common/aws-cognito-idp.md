# aws cognito-idp

> Az Amazon Cognito felhasználói készlet, valamint a felhasználók és csoportok kezelése a CLI segítségével. További információk: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>.

- Hozzon létre egy új Cognito felhasználói csoportot:

`aws cognito-idp create-user-pool --pool-name {{name}}`

- Az összes felhasználói pool listázása:

`aws cognito-idp list-user-pools --max-results {{10}}`

- Egy adott felhasználói csoport törlése:

`aws cognito-idp delete-user-pool --user-pool-id {{user_pool_id}}`

- Felhasználó létrehozása egy adott poolban:

`aws cognito-idp admin-create-user --username {{username}} --user-pool-id {{user_pool_id}}`

- Egy adott pool felhasználóinak listázása:

`aws cognito-idp list-users --user-pool-id {{user_pool_id}}`

- Felhasználó törlése egy adott csoportból:

`aws cognito-idp admin-delete-user --username {{username}} --user-pool-id {{user_pool_id}}`
