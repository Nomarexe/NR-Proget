# NR Progetto Dinamic Python Server

Questo progetto è un server web Python dinamico, sviluppato con Flask, che gestisce un sito web che presenta articoli, una galleria e informazioni di contatto. Il marchio "NR Progect Dinamic Python Server" è presente in tutte le pagine.

## Caratteristiche

- Elenco dinamico degli articoli: l'endpoint `/api/articles` fornisce un elenco JSON degli articoli trovati nella directory `Article`.
- Navigazione articoli: la pagina `articles.html` carica e visualizza dinamicamente tutti gli articoli con link alle singole pagine degli articoli.
- Pagine singole degli articoli: ogni pagina dell'articolo include link di navigazione ad altre pagine principali.
- Layout predefinito coerente: tutte le pagine condividono un layout coerente per intestazione, navigazione e piè di pagina, che enfatizza il nome del progetto.
- Controllo del server: il server Flask viene eseguito in un thread e può essere arrestato in modo corretto digitando `stop` nel terminale in cui è in esecuzione il server.

## Struttura del progetto

- `app.py`: l'applicazione Flask principale che gestisce il sito web e l'API.
- `articles.html`: La pagina di navigazione degli articoli che elenca tutti gli articoli.
- `Article/`: Directory contenente i file HTML dei singoli articoli.
- `index.html`, `contact.html`, `gallery.html`: Altre pagine principali del sito web.
- `src/assets/`: Contiene gli stili CSS e le icone utilizzate dalle pagine.

## Esecuzione del server

1. Assicurati di aver installato Python e Flask.
2. Eseguire il server con:

```bash
applicazione python.py
```

3. Per impostazione predefinita, il server verrà avviato su `http://127.0.0.1:8080`.
4. Per arrestare il server in modo corretto, digitare `stop` nel terminale e premere Invio. Verrà visualizzato un messaggio di conferma dell'arresto del server.

## Accesso al sito web

- Apri il browser e vai su `http://127.0.0.1:8080`.
- Utilizzare i link di navigazione per sfogliare le pagine Informazioni, Articoli, Contatti e Galleria.
- Nella pagina Articoli, clicca sui titoli degli articoli per leggere i singoli articoli.

## Note

- Il server legge dinamicamente i titoli degli articoli dai file HTML nella directory `Article`.
- Il progetto utilizza un layout preimpostato coerente per enfatizzare il marchio "NR Progect Dinamic Python Server".

## Gestione server
- Il server viene eseguito in un thread e può essere arrestato in modo corretto digitando `stop` nel terminale in cui è in esecuzione il server.
- Il server gestisce l'endpoint `/api/articles` per fornire un elenco JSON degli articoli. Questo endpoint può essere utilizzato per integrare il sito web con altre applicazioni o servizi.
- Il progetto utilizza Flask per creare un server web dinamico e gestire le richieste HTTP. Flask è un framework Python popolare e facile da utilizzare per sviluppare applicazioni web.

## Autore

Realizzato da [Nomar.exe](https://github.com/Nomarexe) - 2025
