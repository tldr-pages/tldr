# մասնիկ

> Փոխազդել մասնիկների սարքերի հետ:.
> Լրացուցիչ տեղեկություններ. <https://docs.particle.io/tutorials/developer-tools/cli/>:.

- Մուտք գործեք կամ ստեղծեք հաշիվ Particle CLI-ի համար.:

`particle setup`

- Ցուցադրել սարքերի ցանկը.:

`particle list`

- Ստեղծեք նոր մասնիկների նախագիծ ինտերակտիվ կերպով.:

`particle project create`

- Կազմել մասնիկների նախագիծ.:

`particle compile {{device_type}} {{path/to/source_code.ino}}`

- Թարմացրեք սարքը՝ որոշակի հավելված հեռակա կարգով օգտագործելու համար.:

`particle flash {{device_name}} {{path/to/program.bin}}`

- Թարմացրեք սարքը՝ սերիալների միջոցով վերջին որոնվածն օգտագործելու համար.:

`particle flash --serial {{path/to/firmware.bin}}`

- Կատարել գործառույթ սարքի վրա.:

`particle call {{device_name}} {{function_name}} {{function_arguments}}`
