## Monopoli, alustava luokkakaavio

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Ruutu "1" -- "1" Vankila
    Vankila "1" -- "1" Monopolipeli
    Ruutu "1" -- "1" Aloitusruutu
    Aloitusruutu "1" -- "1" Monopolipeli
    Ruutu "1" -- "1" Sattuma
    Ruutu "1" -- "1" Yhteismaa
    Ruutu "1" -- "1" Katu
    Katu "1" -- "1" Nimi
    Ruutu "1" -- "*" Toiminto
    Pelaaja "1" -- "1" Katu
    Katu "1" -- "4" Talo
    Katu "1" -- "1" Hotelli
    Pelaaja "1" -- "*" Raha
```

## Monopoli, alustava luokkakaavio

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    class Ruutu {
        toiminto
    }

    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma
    Ruutu <|-- Yhteismaa
    Ruutu <|-- Asema
    Ruutu <|-- Laitos
    Ruutu <|-- Katu

    Aloitusruutu "1" -- "1" Monopolipeli
    Vankila "1" -- "1" Monopolipeli

    Sattuma "1" -- "1" Kortti
    Yhteismaa "1" -- "1" Kortti

    class Katu {
        nimi
    }

    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli

    class Pelaaja {
        rahaa
    }

    Pelaaja "1" -- "1" Katu
    Talo "4" -- "1" Katu
    Hotelli "1" -- "1" Katu
```
