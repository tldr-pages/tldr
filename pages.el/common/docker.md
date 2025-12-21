# docker

> Διαχείριση containers και images Docker.
> Μερικές υποεντολές όπως `container` και `image` έχουν τη δική τους τεκμηρίωση χρήσης.
> Περισσότερες πληροφορίες: <https://docs.docker.com/reference/cli/docker/>.

- Λίστα όλων ([a]ll) των Docker containers (εκτελούμενων και σταματημένων):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Εκκίνηση ενός container από ενα image, με προσαρμοσμένο όνομα:

`docker {{[run|container run]}} --name {{container_name}} {{image}}`

- Εκκίνηση ή τερματισμός ενός υπάρχοντος docker:

`docker container {{start|stop}} {{container_name}}`

- Λήψη (pull) ενος image από ένα μητρώο (registry) Docker:

`docker {{[pull|image pull]}} {{image}}`

- Εμφάνιση της λίστας των ήδη ληφθέντων images:

`docker {{[images|image ls]}}`

- Άνοιγμα ενός διαδραστικού κελύφους ([i]nteractive [t]ty) Bourne (`sh`) μέσα σε έναν εκτελούμενο docker:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{container_name}} {{sh}}`

- Αφαίρεση σταματημένων dockers:

`docker {{[rm|container rm]}} {{container1 container2 ...}}`

- Λήψη και παρακολούθηση ([f]ollow) των αρχείων καταγραφής (logs) ενός docker:

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{container_name}}`
