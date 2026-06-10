#թռչել

> Գործիք concourse-ci-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://concourse-ci.org/fly.html>:.

- Նույնականացրե՛ք և պահպանե՛ք համախմբման թիրախը.:

`fly {{[-t|--target]}} {{target_name}} login {{[-n|--team-name]}} {{team_name}} {{[-c|--concourse-url]}} {{https://ci.example.com}}`

- Նշեք թիրախները.:

`fly targets`

- Ցուցակ խողովակաշարեր.:

`fly {{[-t|--target]}} {{target_name}} pipelines`

- Վերբեռնեք կամ թարմացրեք խողովակաշարը.:

`fly {{[-t|--target]}} {{target_name}} set-pipeline {{[-c|--config]}} {{pipeline.yml}} {{[-p|--pipeline]}} {{pipeline_name}}`

- Չեղարկել խողովակաշարը.:

`fly {{[-t|--target]}} {{target_name}} unpause-pipeline {{[-p|--pipeline]}} {{pipeline_name}}`

- Ցուցադրել խողովակաշարի կոնֆիգուրացիան.:

`fly {{[-t|--target]}} {{target_name}} get-pipeline {{[-p|--pipeline]}} {{pipeline_name}}`

- Թարմացրեք թռչելու տեղական պատճենը.:

`fly {{[-t|--target]}} {{target_name}} sync`

- Խողովակաշարի ոչնչացում.:

`fly {{[-t|--target]}} {{target_name}} destroy-pipeline {{[-p|--pipeline]}} {{pipeline_name}}`
