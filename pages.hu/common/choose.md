# choose

> Emberbarát és gyors alternatívája a cut-nak és (néha) az awk-nak. További információ: <https://github.com/theryangeary/choose>.

- A sor 5. elemének kiírása (0-tól kezdve):

`choose {{4}}`

- Az első, a 3. és az 5. elem kiírása egy sorból, ahol az elemeket szóköz helyett ':' választja el:

`choose --field-separator '{{:}}' {{0}} {{2}} {{4}}`

- A sor 2. és 5. elemétől az 5. elemet is beleértve mindent kiír a sorból:

`choose {{1}}:{{4}}`

- A sor 2. és 5. elemétől az 5. elem kivételével mindent kiír a sorból:

`choose --exclusive {{1}}:{{4}}`

- A sor elejétől a 3. tételig nyomtatja ki a sort:

`choose :{{2}}`

- A sor elejétől a 3. tételig minden elemet kinyomtat (kizárólag):

`choose --exclusive :{{2}}`

- A 3. tételtől a sor végéig minden elemet kinyomtat:

`choose {{2}}:`

- A sor utolsó elemének nyomtatása:

`choose {{-1}}`
