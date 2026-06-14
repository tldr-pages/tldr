# aws ուժեղանում է

> Մշակման հարթակ՝ անվտանգ, մասշտաբային բջջային և վեբ հավելվածներ ստեղծելու համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/amplify/>:.

- Ստեղծեք նոր Amplify հավելված.:

`aws amplify create-app --name {{app_name}} --description {{description}} --repository {{repo_url}} --platform {{platform}} --environment-variables {{env_vars}} --tags {{tags}}`

- Ջնջել գոյություն ունեցող Amplify հավելվածը.:

`aws amplify delete-app --app-id {{app_id}}`

- Ստացեք կոնկրետ Amplify հավելվածի մանրամասները.:

`aws amplify get-app --app-id {{app_id}}`

- Թվարկեք Amplify-ի բոլոր հավելվածները.:

`aws amplify list-apps`

- Թարմացրեք Amplify հավելվածի կարգավորումները.:

`aws amplify update-app --app-id {{app_id}} --name {{new_name}} --description {{new_description}} --repository {{new_repo_url}} --environment-variables {{new_env_vars}} --tags {{new_tags}}`

- Ավելացնել նոր հետին միջավայր Amplify հավելվածին.:

`aws amplify create-backend-environment --app-id {{app_id}} --environment-name {{env_name}} --deployment-artifacts {{artifacts}}`

- Հեռացրեք հետին միջավայրը Amplify հավելվածից.:

`aws amplify delete-backend-environment --app-id {{app_id}} --environment-name {{env_name}}`

- Թվարկեք բոլոր հետին միջավայրերը Amplify հավելվածում.:

`aws amplify list-backend-environments --app-id {{app_id}}`
