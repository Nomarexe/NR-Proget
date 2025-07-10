# nr proget

Benvenuto/a in **nr proget**!

## Descrizione

**nr proget** è un progetto web che consiste in un server dinamico Python basato su Flask che serve una raccolta di articoli in formato HTML. Il server fornisce una semplice API per elencare gli articoli disponibili e serve le pagine HTML degli articoli stessi. È ideale per la pubblicazione e la visualizzazione di contenuti statici con un backend leggero.

## Tecnologie utilizzate

- Python 3
- Flask
- HTML, CSS, JavaScript (per il frontend)

## Installazione

1. Clona il repository:
   ```bash
   git clone https://github.com/TUO-USERNAME/nr-proget.git
   ```
2. Accedi alla cartella del progetto:
   ```bash
   cd nr-proget/NR\ Progect\ Dinamic\ Python\ Server
   ```
3. (Opzionale) Crea un ambiente virtuale Python:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Installa le dipendenze:
   ```bash
   pip install Flask
   ```

## Utilizzo

Per avviare il server Flask, esegui:

```bash
python app.py [porta]
```

- `porta` è opzionale, il valore predefinito è 8080.
- Esempio per avviare sulla porta 5000:
  ```bash
  python app.py 5000
  ```

Una volta avviato, apri il browser e visita:

- `http://127.0.0.1:porta/` per visualizzare la pagina principale con gli articoli.
- `http://127.0.0.1:porta/api/articles` per ottenere la lista degli articoli in formato JSON.
- `http://127.0.0.1:porta/Article/<nomefile>` per visualizzare un articolo specifico.

## Struttura del progetto

```
NR Progect Dinamic Python Server/
├── app.py                  # Server Flask principale
├── articles.html           # Pagina principale degli articoli
├── Article/                # Cartella contenente gli articoli HTML
│   ├── article1.html
│   ├── article2.html
│   └── ...
├── contact.html            # Pagina di contatto
├── gallery.html            # Pagina galleria
├── index.html              # Pagina principale statica
├── src/                    # Risorse statiche (CSS, JS, immagini, ecc.)
```

## Contribuire

1. Fai un fork del progetto
2. Crea una branch: `git checkout -b feature/NuovaFunzionalita`
3. Fai commit delle tue modifiche: `git commit -m 'Aggiunta nuova funzionalità'`
4. Fai push sul branch: `git push origin feature/NuovaFunzionalita`
5. Invia una Pull Request

## Licenza

Questo progetto è rilasciato sotto la licenza Creative Commons.

## Autori

- [Nomar Reyes](https://github.com/Nomarexe)
