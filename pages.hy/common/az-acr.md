# ազ ակր

> Կառավարեք մասնավոր ռեգիստրները Azure Container Registries-ով:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/acr>:.

- Ստեղծեք կառավարվող կոնտեյների ռեեստր.:

`az acr create {{[-n|--name]}} {{registry_name}} {{[-g|--resource-group]}} {{resource_group}} --sku {{sku}}`

- Մուտք գործեք ռեեստր.:

`az acr login {{[-n|--name]}} {{registry_name}}`

- Նշեք տեղական պատկեր ACR-ի համար.:

`docker tag {{image_name}} {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- Պատկերը տեղափոխեք ռեեստր.:

`docker push {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- Քաշեք պատկեր ռեեստրից.:

`docker pull {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- Ջնջել պատկերը գրանցամատյանից.:

`az acr repository delete {{[-n|--name]}} {{registry_name}} --repository {{image_name}}:{{tag}}`

- Ջնջել կառավարվող կոնտեյների ռեեստրը.:

`az acr delete {{[-n|--name]}} {{registry_name}} {{[-g|--resource-group]}} {{resource_group}} {{[-y|--yes]}}`

- Ցուցակեք պատկերները ռեեստրի ներսում.:

`az acr repository list {{[-n|--name]}} {{registry_name}} --output table`
