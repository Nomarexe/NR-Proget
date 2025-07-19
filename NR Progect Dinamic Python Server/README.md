# NR Progetto Dinamic Python Server

Questo progetto è un server web Python dinamico, sviluppato con Flask, che gestisce un sito web che presenta articoli, una galleria e informazioni di contatto. Il marchio "NR Progect Dinamic Python Server" è presente in tutte le pagine.

## Caratteristiche

- Elenco dinamico degli articoli: l'endpoint `/api/articles` fornisce un elenco JSON degli articoli trovati nella directory `Article`.
- Navigazione articoli: la pagina `articles.html` carica e visualizza dinamicamente tutti gli articoli con link alle singole pagine degli articoli.
- Pagine singole degli articoli: ogni pagina dell'articolo include link di navigazione ad altre pagine principali.
- Layout predefinito coerente: tutte le pagine condividono un layout coerente per intestazione, navigazione e piè di pagina, che enfatizza il nome del progetto.
- Controllo del server: il server Flask viene eseguito in un thread e può essere arrestato in modo corretto digitando `stop` nel terminale in cui è in esecuzione il server.
- Galleria dinamica: la pagina `gallery.html` carica automaticamente le immagini e i video dalla cartella `Galleria` tramite un endpoint API dedicato.

## Struttura del progetto

- `app.py`: l'applicazione Flask principale che gestisce il sito web e l'API.
- `articles.html`: La pagina di navigazione degli articoli che elenca tutti gli articoli.
- `Article/`: Directory contenente i file HTML dei singoli articoli.
- `index.html`, `contact.html`, `gallery.html`: Altre pagine principali del sito web.
- `src/assets/`: Contiene gli stili CSS e le icone utilizzate dalle pagine.
- `Galleria/`: Cartella contenente le immagini e i video della galleria.
- `src/assets/js/gallery.js`: Script JavaScript per caricare dinamicamente la galleria e gestire la visualizzazione modale.
- `setup_instructions.sh`: Script per installare le dipendenze necessarie su Windows, Linux e macOS.

## Esecuzione del server

1. Assicurati di aver installato Python 3.
2. Esegui lo script di setup per installare Flask:

```bash
bash setup_instructions.sh
```

3. Avvia il server con:

```bash
python3 app.py
```

4. Per impostazione predefinita, il server verrà avviato su `http://127.0.0.1:8080`.
5. Per arrestare il server in modo corretto, digitare `stop` nel terminale e premere Invio. Verrà visualizzato un messaggio di conferma dell'arresto del server.

## Accesso al sito web

- Apri il browser e vai su `http://127.0.0.1:8080`.
- Utilizza i link di navigazione per sfogliare le pagine Informazioni, Articoli, Contatti e Galleria.
- Nella pagina Articoli, clicca sui titoli degli articoli per leggere i singoli articoli.
- Nella pagina Galleria, le immagini e i video vengono caricati automaticamente dalla cartella `Galleria`.

## Note

- Il server legge dinamicamente i titoli degli articoli dai file HTML nella directory `Article`.
- La galleria supporta i formati immagine comuni: PNG, JPG, JPEG, GIF, BMP, WEBP.
- La galleria supporta i formati video comuni: MP4, WEBM, OGG.
- La pagina galleria include una visualizzazione modale con navigazione tramite tastiera per le immagini; i video sono riprodotti con controlli nativi.
- Il progetto utilizza un layout preimpostato coerente per enfatizzare il marchio "NR Progect Dinamic Python Server".

## Autore

Realizzato da [Nomar.exe](https://github.com/Nomarexe) - 2025
