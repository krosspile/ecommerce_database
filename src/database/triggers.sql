CREATE TRIGGER IF NOT EXISTS update_total
AFTER
INSERT
    ON ContenutoOrdine BEGIN
UPDATE
    Ordine
SET
    totale = (
        SELECT
            SUM(prezzo * quantità)
        FROM
            ContenutoOrdine CO,
            Prodotto P
        WHERE
            CO.id_prodotto = P.id
            AND CO.id_ordine = new.id_ordine
    )
WHERE
    Ordine.id = new.id_ordine;

END;

--
CREATE TRIGGER IF NOT EXISTS insert_refund
AFTER
INSERT
    ON SegnalazioneGestita
    WHEN new.descrizione like '%rimborso acconsentito%' BEGIN
INSERT INTO
    Rimborso(
        id_cliente,
        id_dipendente,
        importo,
        data_versamento
    )
VALUES
    (
        (
            SELECT
                id_cliente
            FROM
                Ordine O
            WHERE
                O.id = new.id_segnalazione
        ),
        new.id_dipendente,
        (
            SELECT
                totale
            FROM
                Ordine O
            WHERE
                O.id = new.id_segnalazione
        ),
        DATETIME('now')
    );

END;

--
CREATE TRIGGER IF NOT EXISTS insert_data_order
AFTER
INSERT
    ON Ordine BEGIN
UPDATE
    Ordine
SET
    data = DATETIME('now')
WHERE
    Ordine.id = new.id;

END;

--
CREATE TRIGGER IF NOT EXISTS insert_date_report
AFTER
INSERT
    ON Segnalazione BEGIN
UPDATE
    Segnalazione
SET
    data_apertura = DATETIME('now')
WHERE
    Segnalazione.id_ordine = new.id_ordine;

END;

--
CREATE TRIGGER IF NOT EXISTS insert_date_review
AFTER
INSERT
    ON Recensione BEGIN
UPDATE
    Recensione
SET
    data = DATETIME('now')
WHERE
    Recensione.id_cliente = new.id_cliente
    AND Recensione.id_prodotto = new.id_prodotto;

END;

--
CREATE TRIGGER IF NOT EXISTS insert_date_closed_report
AFTER
INSERT
    ON SegnalazioneGestita BEGIN
UPDATE
    SegnalazioneGestita
SET
    data = DATETIME('now')
WHERE
    SegnalazioneGestita.id_segnalazione = new.id_segnalazione
    AND SegnalazioneGestita.id_dipendente = new.id_dipendente;

END;

--
CREATE TRIGGER IF NOT EXISTS update_articoli_totali
AFTER
INSERT
    ON Prodotto BEGIN
UPDATE
    Categoria
SET
    articoli_totali = (
        SELECT
            COUNT(*)
        FROM
            Prodotto P
        WHERE
            P.id_categoria = Categoria.id
    )
WHERE
    Categoria.id = new.id_categoria;

END;

--
CREATE TRIGGER IF NOT EXISTS update_segnalazioni_gestite
AFTER
INSERT
    ON SegnalazioneGestita BEGIN
UPDATE
    Dipendente
SET
    segnalazioni_gestite = (
        SELECT
            COUNT(*)
        FROM
            SegnalazioneGestita SG
        WHERE
            SG.id_dipendente = new.id_dipendente
    )
WHERE
    Dipendente.id = new.id_dipendente;

END;

--
CREATE TRIGGER IF NOT EXISTS update_rating
AFTER
INSERT
    ON Recensione BEGIN
UPDATE
    Prodotto
SET
    rating = (
        SELECT
            AVG(rating)
        FROM
            Recensione R
        WHERE
            R.id_prodotto = new.id_prodotto
    )
WHERE
    Prodotto.id = new.id_prodotto;

END;

--