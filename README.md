# Ohjelmistotekniikka, harjoitustyö

## Treeni-sovellus

Harjoitustyön aiheena on **treeni-sovellus**, mihin käyttäjä voi asettaa _treenitavoitteita_, _kirjata treeninsä_ ja _seurata edistymistään_.

## Python versio

Sovellus vaatii vähintään Python-versio 3.10. Se ei välttämättä toimi sitä vanhemmilla versioilla.

## Dokumentaatio

- [Vaatimusmäärittely](./python-workout-app/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./python-workout-app/dokumentaatio/tuntikirjanpito.md)
- [Changelog](./python-workout-app/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](./python-workout-app/dokumentaatio/arkkitehtuuri.md)

## Asennus

1.  Siirry harjoitustyön-hakemistoon:

        cd python-workout-app

2.  Asenna sovelluksen vaatimat riippuvuudet:

        poetry install

3.  Alusta sovelluksen käyttämä tietokanta:

        poetry run invoke build

4.  Käynnistä sovellus:

        poetry run invoke start

## Muut komentorivikomennot

Sovelluksen testaus

    poetry run invoke test

Testiraportin luonti

    poetry run invoke coverage-report

Sovelluksen koodin tarkistus

    poetry run invoke lint

Sovelluksen koodin muotoilu

    poetry run invoke format
