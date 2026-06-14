#տես

> Կառավարեք հավելվածներն ու ծառայությունները Cloud Foundry-ում:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloudfoundry.org/cf-cli/getting-started.html>:.

- Մուտք գործեք Cloud Foundry API.:

`cf login -a {{api_url}}`

- Հրել հավելված՝ օգտագործելով լռելյայն կարգավորումները.:

`cf push {{app_name}}`

- Դիտեք ձեր կազմակերպությունից հասանելի ծառայությունները.:

`cf marketplace`

- Ստեղծեք ծառայության օրինակ.:

`cf create-service {{service}} {{plan}} {{service_name}}`

- Միացրեք հավելվածը ծառայությանը.:

`cf bind-service {{app_name}} {{service_name}}`

- Գործարկեք սցենար, որի կոդը ներառված է հավելվածում, բայց աշխատում է ինքնուրույն.:

`cf run-task {{app_name}} "{{script_command}}" --name {{task_name}}`

- Սկսեք ինտերակտիվ SSH նստաշրջան VM-ով, որը հոսթինգում է հավելված.:

`cf ssh {{app_name}}`

- Դիտեք հավելվածների վերջին տեղեկամատյանների աղբանոցը.:

`cf logs {{app_name}} --recent`
