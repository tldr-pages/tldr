# mkdir

> Opprett mapper og angi rettighetene deres.
> Mer informasjon: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Opprett bestemte mapper:

`mkdir {{sti/til/mappe1 sti/til/mappe2 ...}}`

- Opprett bestemte mapper og deres overordnede mapper ved behov:

`mkdir {{[-p|--parents]}} {{sti/til/mappe1 sti/til/mappe2 ...}}`

- Opprett mapper med bestemte rettigheter:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{sti/til/mappe1 sti/til/mappe2 ...}}`

- Opprett flere nøstede mapper rekursivt:

`mkdir {{[-p|--parents]}} {{sti/til/{a,b}/{x,y,z}/{h,i,j}}}`
