CREATE TABLE IF NOT EXISTS Cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(20) NOT NULL,
    cognome VARCHAR(20) NOT NULL,
    email VARCHAR(20) NOT NULL,
    password_hash VARCHAR(64) NOT NULL,
    UNIQUE(email)
);

CREATE TABLE IF NOT EXISTS Categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(20) NOT NULL,
    articoli_totali INTEGER NULL
);

CREATE TABLE IF NOT EXISTS Ordine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    data DATE NOT NULL,
    totale INTEGER NOT NULL,
    indirizzo_spedizione VARCHAR(30) NOT NULL,
    FOREIGN KEY(id_cliente) REFERENCES Cliente(id)
);

CREATE TABLE IF NOT EXISTS Segnalazione (
    id_ordine INTEGER NOT NULL,
    data_apertura DATE NOT NULL,
    descrizione VARCHAR(200),
    FOREIGN KEY(id_ordine) REFERENCES Ordine(id),
    PRIMARY KEY(id_ordine)
);

CREATE TABLE IF NOT EXISTS Dipendente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_assunzione DATE NOT NULL,
    nome VARCHAR(20),
    cognome VARCHAR(20),
    segnalazioni_gestite INTEGER NULL
);

CREATE TABLE IF NOT EXISTS Prodotto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_categoria INTEGER NOT NULL,
    marca VARCHAR(20),
    modello VARCHAR(20),
    taglia VARCHAR(6),
    colore VARCHAR(20),
    prezzo INTEGER NOT NULL,
    rating integer NULL,
    genere VARCHAR(20),
    UNIQUE(marca, modello, taglia, colore, genere),
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id)
);

CREATE TABLE IF NOT EXISTS ContenutoOrdine (
    id_ordine INTEGER NOT NULL,
    id_prodotto INTEGER NOT NULL,
    quantità INTEGER NOT NULL,
    FOREIGN KEY (id_ordine) REFERENCES Ordine(id),
    FOREIGN KEY (id_prodotto) REFERENCES Prodotto(id),
    PRIMARY KEY (id_ordine, id_prodotto)
);

CREATE TABLE IF NOT EXISTS Recensione (
    id_cliente INTEGER NOT NULL,
    id_prodotto INTEGER NOT NULL,
    data DATE NOT NULL,
    rating INTEGER NOT NULL,
    commento TEXT NULL,
    PRIMARY KEY(id_cliente, id_prodotto),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
    FOREIGN KEY (id_prodotto) REFERENCES Prodotto(id)
);

CREATE TABLE IF NOT EXISTS Rimborso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    id_dipendente INTEGER NOT NULL,
    importo INTEGER NOT NULL,
    data_versamento DATE NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
    FOREIGN KEY (id_dipendente) REFERENCES Dipendente(id)
);

CREATE TABLE IF NOT EXISTS SegnalazioneGestita (
    id_segnalazione INTEGER NOT NULL,
    id_dipendente INTEGER NOT NULL,
    descrizione TEXT NOT NULL,
    data DATE NOT NULL,
    FOREIGN KEY (id_segnalazione) REFERENCES Segnalazione(id_ordine),
    FOREIGN KEY (id_dipendente) REFERENCES Dipendente(id)
);

CREATE TABLE IF NOT EXISTS ProdottoScontato (
    id_prodotto INTEGER NOT NULL,
    data_inizio DATE NOT NULL,
    data_fine DATE NOT NULL,
    prezzo_scontato INTEGER NOT NULL,
    FOREIGN KEY (id_prodotto) REFERENCES Prodotto(id),
    PRIMARY KEY (id_prodotto, data_inizio)
);