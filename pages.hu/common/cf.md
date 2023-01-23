# cf

> Parancssori eszköz a Cloud Foundry alkalmazások és szolgáltatások kezelésére. További információ: <https://docs.cloudfoundry.org>.

- Jelentkezzen be a Cloud Foundry API-ba:

`cf login -a {{api_url}}`

- Pusholjon egy alkalmazást az alapértelmezett beállításokkal:

`cf push {{app_name}}`

- Tekintse meg a szervezete által elérhető szolgáltatásokat:

`cf marketplace`

- Hozzon létre egy szolgáltatáspéldányt:

`cf create-service {{service}} {{plan}} {{service_name}}`

- Csatlakoztasson egy alkalmazást egy szolgáltatáshoz:

`cf bind-service {{app_name}} {{service_name}}`

- Olyan szkript futtatása, amelynek kódja az alkalmazásban szerepel, de attól függetlenül fut:

`cf run-task {{app_name}} "{{script_command}}" --name {{task_name}}`

- Interaktív SSH-munkamenet indítása egy alkalmazást tároló VM-mel:

`cf ssh {{app_name}}`

- Az alkalmazás legutóbbi naplóinak dumpjainak megtekintése:

`cf logs {{app_name}} --recent`
