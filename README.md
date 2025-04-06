# Esercizi di Programmazione Python

Questa repository contiene due esercizi di programmazione implementati in Python:

## 1. FooBar

### Descrizione
Un programma che stampa i numeri da 1 a 100 seguendo queste regole:
- Per i multipli di 3, stampa "Foo"
- Per i multipli di 5, stampa "Bar"
- Per i numeri che sono multipli sia di 3 che di 5, stampa "FooBar"
- Per tutti gli altri numeri, stampa il numero stesso

### Struttura
```
foobar/
├── foobar.py         # Implementazione principale
└── test_foobar.py    # Test unitari
```

## 2. Rock Paper Scissors (Carta, Forbice, Sasso)

### Descrizione
Un'implementazione del classico gioco "Carta, Forbice, Sasso" con le seguenti caratteristiche:
- Supporto per modalità Umano vs Computer
- Supporto per modalità Computer vs Computer
- Possibilità di giocare più partite consecutive
- Design estendibile per future varianti (es. Rock, Paper, Scissors, Lizard, Spock)

### Struttura
```
rock_paper_scissors/
├── game.py           # Implementazione del gioco
└── test_game.py      # Test unitari
```

### Caratteristiche Tecniche
- Implementazione in Python puro senza dipendenze esterne (eccetto per i test)
- Codice scritto seguendo le best practice dell'industry (clean code principles, docstrings, unit testing, error handling, ecc...)
- Design modulare ed estendibile
- Approccio MVP (Minimum Viable Product) con focus su eleganza e semplicità

## Come Eseguire i Progetti

### FooBar
```bash
cd foobar
python foobar.py
```

### Rock Paper Scissors
```bash
cd rock_paper_scissors
python game.py
```

## Test
Entrambi i progetti includono test unitari che possono essere eseguiti usando:
```bash
python test_foobar.py    # Per FooBar
python test_game.py      # Per Rock Paper Scissors
``` 

## CI/CD Pipeline
Il progetto include una semplice pipeline di Continuous Integration implementata con GitHub Actions che:
- Si attiva automaticamente ad ogni push su main o pull request
- Esegue il linting del codice con flake8
- Lancia i test unitari per verificare che tutto funzioni correttamente

Per vedere lo stato dei test, controlla la tab "Actions" su GitHub. 