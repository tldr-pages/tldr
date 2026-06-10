# skopeo

> Կոնտեյների պատկերների կառավարման գործիքակազմ:.
> Տրամադրում է տարբեր կոմունալ հրամաններ՝ հեռավոր բեռնարկղերի պատկերները կառավարելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/containers/skopeo/blob/main/docs/skopeo.1.md>:.

- Ստուգեք ռեեստրի հեռավոր պատկերը.:

`skopeo inspect docker://{{registry_hostname}}/{{image:tag}}`

- Ցուցակեք հասանելի պիտակները հեռավոր պատկերի համար.:

`skopeo list-tags docker://{{registry_hostname}}/{{image}}`

- Ներբեռնեք պատկեր ռեեստրից.:

`skopeo copy docker://{{registry_hostname}}/{{image:tag}} dir:{{path/to/directory}}`

- Պատճենեք պատկերը մի ռեեստրից մյուսը.:

`skopeo copy docker://{{source_registry}}/{{image:tag}} docker://{{destination_registry}}/{{image:tag}}`

- Ջնջել պատկերը գրանցամատյանից.:

`skopeo delete docker://{{registry_hostname}}/{{image:tag}}`

- Մուտք գործեք գրանցամատյան.:

`skopeo login --username {{username}} {{registry_hostname}}`
