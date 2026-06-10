# npm sbom

> Ստեղծեք ծրագրային ապահովման օրինագիծ (SBOM) ձեր Node.js նախագծի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-sbom/>:.

- Արտադրեք ձեր նախագծի բոլոր կախվածությունների ցանկը.:

`npm sbom`

- Բացառել `dev` և `optional` կախվածությունները՝:

`npm sbom --omit dev --omit optional`

- Ստեղծեք SBOM՝ հիմնված միայն `package-lock.json`-ի վրա՝:

`npm sbom --package-lock-only`
