# bundletool dump

> Instrument de linie de comandă pentru a manipula pachetele de aplicații Android.
> Mai multe informaţii: <https://developer.android.com/studio/command-line/bundletool>

- Afișează `AndroidManifest.xml` a modulului de bază:

`bundletool dump manifest --bundle={{path/to/bundle.aab}}`

- Afișează o anumită valoare din `AndroidManifest.xml` folosind XPath:

`bundletool dump manifest --bundle={{path/to/bundle.aab}} --xpath={{/manifest/@android:versionCode}}`

- Afișează `AndroidManifest.xml` a unui anumit modul:

`bundletool dump manifest --bundle={{path/to/bundle.aab}} --module={{name}}`

- Afișează toate resursele din pachetul de aplicații:

`bundletool dump resources --bundle={{path/to/bundle.aab}}`

- Afișați configurația pentru o anumită resursă:

`bundletool dump resources --bundle={{path/to/bundle.aab}} --resource={{type/name}}`

- Afișați configurația și valorile pentru o anumită resursă utilizând ID-ul:

`bundletool dump resources --bundle={{path/to/bundle.aab}} --resource={{0x7f0e013a}} --values`

- Afișează conținutul fișierului de configurare a pachetului:

`bundletool dump config --bundle={{path/to/bundle.aab}}`
