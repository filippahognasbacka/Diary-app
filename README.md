Käytä tätä versiota!

Sovelluksen idea: Päiväkirja

Uusi käyttäjä pystyy luoda käyttäjän ja kirjautua sisään. Sovelluksessa sisällä käyttäjä pystyy lisätä päiväkirjan päivän aiheen (esimerkiksi päivämäärän) otsikoksi. Sen jälkeen aihetta pystyy painaa ja seuraavalla sivulla on mahdollista kirjoittaa pidempi julkaisu päiväkirjaan.

Kotisivulla on myös mahdollista poistaa päiväkirjan julkaisu sekä kirjautua ulos sovelluksesta.





Miten testata sovellusta:

Kloonaa repositorio omalle koneellesi. Luo kansioon .env tiedosto ja määritä sen sisältö seuraavanlaiseksi:

SECRET_KEY=<salainen-avain>

DB_NAME=<tietokannan-paikallinen-osoite>


Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt


$ flask run


