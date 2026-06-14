# aws cognito-idp

> Կազմաձևեք Amazon Cognito օգտատերերի լողավազանը և դրա օգտատերերն ու խմբերը և վավերացրեք դրանք:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/>:.

- Ստեղծեք նոր Cognito օգտվողների լողավազան.:

`aws cognito-idp create-user-pool --pool-name {{name}}`

- Թվարկեք բոլոր օգտվողների լողավազանները.:

`aws cognito-idp list-user-pools --max-results {{10}}`

- Ջնջել որոշակի օգտվողների լողավազան.:

`aws cognito-idp delete-user-pool --user-pool-id {{user_pool_id}}`

- Ստեղծեք օգտվող կոնկրետ լողավազանում.:

`aws cognito-idp admin-create-user --username {{username}} --user-pool-id {{user_pool_id}}`

- Թվարկեք կոնկրետ լողավազանի օգտվողներին.:

`aws cognito-idp list-users --user-pool-id {{user_pool_id}}`

- Ջնջել օգտվողին որոշակի լողավազանից.:

`aws cognito-idp admin-delete-user --username {{username}} --user-pool-id {{user_pool_id}}`
