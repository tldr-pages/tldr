# mimikatz crypto

> Manipola i servizi crittografici di Windows e i certificati, consentendo di elencare ed esportare certificati e chiavi, anche se contrassegnati come non esportabili.
> Richiede in genere privilegi elevati, soprattutto quando si accede a chiavi di sistema.
> Maggiori informazioni: <https://github.com/gentilkiwi/mimikatz>.

- Elenca i provider crittografici (CryptoAPI/CNG) disponibili:

`mimikatz "crypto::providers"`

- Elenca le chiavi in un provider crittografico (e applica patch per rendere esportabili le chiavi non esportabili tramite CryptoAPI):

`mimikatz "crypto::capi"`

- Esporta certificati e chiavi dai negozi certificati:

`mimikatz "crypto::certificates /export"`
