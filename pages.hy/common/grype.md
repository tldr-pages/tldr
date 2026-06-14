#բողոք

> Կոնտեյների պատկերների և ֆայլային համակարգերի խոցելիության սկաներ:.
> Լրացուցիչ տեղեկություններ. <https://oss.anchore.com/docs/reference/grype/cli>:.

- Սկանավորեք կոնտեյների պատկերը.:

`grype {{image:tag}}`

- Սկանավորեք պատկերը և ցուցադրեք արդյունքները որոշակի ձևաչափով.:

`grype {{image:tag}} {{[-o|--output]}} {{json|table|cyclonedx|cyclonedx-json|sarif|template}}`

- Սկանավորեք պատկերը՝ անտեսելով չֆիքսված խոցելիությունները.:

`grype {{image:tag}} --only-fixed`

- Սկանավորեք պատկերը և ձախողեք խոցելիությունը տվյալ մակարդակից կամ ավելի բարձր ծանրությամբ.:

`grype {{image:tag}} {{[-f|--fail-on]}} {{negligible|low|medium|high|critical}}`

- Սկանավորեք տեղական գրացուցակը և պահեք հաշվետվությունը ֆայլում.:

`grype {{path/to/directory}} --file {{path/to/report}}`

- Թարմացրեք խոցելիության տվյալների բազան.:

`grype db update`

- Ցուցադրել տվյալների բազայի ընթացիկ կարգավիճակը.:

`grype db status`

- Ցուցադրել օգնությունը.:

`grype {{[-h|--help]}}`
