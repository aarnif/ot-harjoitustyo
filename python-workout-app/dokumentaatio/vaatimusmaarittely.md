# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi pitää kirjaa omista treeneistään ja asettaa treeni-tavoitteita sekä seurata edistymistään.

## Käyttäjät

Sovelluksessa on vain yhdenlaisia käyttäjiä, jotka ovat rekisteröityneitä käyttäjiä.
Myöhemmin mahdollisesti ylläpitäjä-roolin käyttäjä.

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

- Käyttäjä näkee päänäkymän, jossa on listattuna käyttäjän viikottainen treenitavoite ja kuinka lähellä käyttäjä on tavoitettaan
- Käyttäjä voi asettaa uuden viikottaisen treenitavoitteen
  - Tavoitteelle annetaan nimi ja tavoiteltava treenimäärä
- Käyttäjä voi lisätä uuden treenin
  - Treenille määritetään ainakin tyyppi (esim. lihaskunto tai aerobinen) ja kesto.
- Käyttäjä voi tarkastella treenihistoriaansa
  - Treenihistoriasta näkee treenin tyypin, keston ja päivämäärän
- [x] Käyttäjä voi kirjautua ulos järjestelmästä
