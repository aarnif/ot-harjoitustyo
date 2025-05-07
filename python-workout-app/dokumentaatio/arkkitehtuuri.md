# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen rakenne koostuu kolmesta eri kerroksesta, joilla jokaisella on oma vastuunsa. Näistä ui-pakkaus vastaa käyttöliittymästä, services-pakkaus sovelluslogiikasta ja repositories-pakkaus tiedon pysyväistallentamisesta tietokantaan.

## Käyttöliittymä

Sovelluksen käyttöliittymä sisältää seuraavat näkymät:

- Kirjautuminen
- Käyttäjän luonti
- Päänäkymä
- Treenitavoitteen muokkaus
- Viikon treenihistoria
- Treenin luonti
- Treenin muokkaus
- Treenin poiston vahvistus

Käyttöliittymä on eristetty muusta sovelluslogiikasta ja sen tehtävänä on kutsua UserService- ja WorkoutService-luokkien metodeja riippuen käyttäjän toiminnasta sovelluksessa.

## Sovelluslogiikka

Alla olevassa pakkauskaavioissa on kuvattu sovelluksen eri osien suhteet toisiinsa.

![Pakkauskaavio](kuvat/pakkauskaavio.png)

Sovelluslogiikan kannalta olennaisimmat luokat ovat UserService ja WorkoutService, jotka vastaavat sovelluksen toiminnallisuuksista.
Sovelluksen looginen tietomalli muodostuu User- ja Workout-luokista, jotka kuvaavat käyttäjiä ja niiden treenejä. Käyttäjä voi lisätä useita treenejä, mutta jokainen treeni kuuluu vain yhdelle käyttäjälle.

```mermaid
 classDiagram
      User "1" --> "*" Workout
      class Workout{
          id
          username
          type
          duration
          created_at
      }
      class User{
          username
          password
          weekly_training_goal_in_minutes
      }
```

## Tietojen pysyväistallennus

Pakkauksen repositories luokkien UserRepository ja WorkoutRepository tehtävinä on vastata tietojen tallentamisesta.
Tietojen tallentaminen tapahtuu kummassakin tapauksessa hyödyntämällä SQLite-tietokantaa. Käyttäjätiedot tallennetaan tietokanta tauluun `users` ja treenitiedot tauluun `workouts`.

## Päätoiminnallisuudet

Alla on esitelty sovelluksen päätoiminnallisuuksia sekvenssikaavioiden avulla.

### Käyttäjän luonti

```mermaid
sequenceDiagram
  participant User
  participant UI
  participant UserService
  participant UserRepository
  participant test
  User->>UI: click "Create User" button
  UI->>UserService: create_user("test", "password", "password")
  UserService->>UserRepository: find_by_username("test")
  UserRepository-->>UserService: None
  UserService->>test: User("test", "password", weekly_training_goal_in_minutes=0)
  UserService->>UserRepository: create(test)
  UserRepository-->>UserService: user
  UserService-->>UI: user
  UI->>UI: _show_main_view()
```

### Käyttäjän kirjautuminen

```mermaid
sequenceDiagram
  participant User
  participant UI
  participant UserService
  participant UserRepository
  participant test
  User->>UI: click "Login" button
  UI->>UserService: login_user("test", "password")
  UserService->>UserRepository: find_by_username("test")
  UserRepository-->>UserService: user
  UserService-->>UI: user
  UI->>UI: _show_main_view()
```

### Uuden treenin luonti

```mermaid
sequenceDiagram
  participant User
  participant UI
  participant WorkoutService
  participant WorkoutRepository
  participant workout
  User->>UI: click "Add Workout" button
  UI->>WorkoutService: create_workout("test", "cardio", 60)
  WorkoutService->>workout: Workout("test", "cardio", 60)
  WorkoutService->>WorkoutRepository: create(workout)
  WorkoutRepository-->>WorkoutService: workout
  WorkoutService-->>UI: workout
  UI->>UI: _show_main_view()
```

### Muut toiminnallisuudet

Sovelluksen muut toiminnallisuudet, kuten treenitavoitteen asetus sekä treenin muokkaus ja poisto, toimivat samalla tavalla. Käyttöliittymä kutsuu sovelluslogiikan metodeja, jotka puolestaan tekevät operaatioita tietokantaan ja palauttavat näiden operaatioiden tulokset käyttöliittymään, joka tarvittaessa päivittää näkymän käyttäjälle.
