# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi pitää kirjaa omista treeneistään ja asettaa viikottaisen treenitavoitteen sekä seurata sen edistymistä.

## Käyttäjät

Sovelluksessa on vain yhdenlaisia käyttäjiä, jotka ovat rekisteröityneitä käyttäjiä.

## Sovelluksen tarjoama toiminnallisuus

### Ennen kirjautumista

- [x] Käyttäjä voi luoda järjestelmään uuden käyttäjätunnuksen

  - [x] Käyttäjätunnuksen tulee olla uniikki
  - [x] Käyttäjätunnuksen tulee olla pituudeltaan vähintään 3 merkkiä
  - [x] Salasanan tulee olla pituudeltaan vähintään 6 merkkiä

- [x] Käyttäjä voi kirjautua järjestelmään
  - [x] Kirjautuminen tapahtuu syöttämällä käyttäjätunnus ja salasana lomakkeelle
    - [x] Jos käyttäjätunnus tai salasana on väärin, käyttäjälle ilmoitetaan tästä

### Kirjautumisen jälkeen

- [x] Käyttäjä näkee päänäkymän, jossa on listattuna käyttäjän viikottainen treenitavoite ja kuinka lähellä käyttäjä on tavoitettaan
- [x] Käyttäjä voi asettaa uuden viikottaisen treenitavoitteen
- [x] Käyttäjä voi lisätä uuden treenin
  - [x] Treenille määritetään ainakin tyyppi (esim. lihaskunto tai aerobinen) ja kesto.
- [x] Käyttäjä voi tarkastella käynnissä olevan viikon treenihistoriaa
  - [x] Treenihistoriasta näkee treenin tyypin, keston ja päivämäärän
- [x] Käyttäjä voi muokata lisättyjä treenejä
- [x] Käyttäjä voi poistaa lisättyjä treenejä
- [x] Käyttäjä voi kirjautua ulos järjestelmästä
