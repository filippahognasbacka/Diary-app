Miten testata sovellusta:

Kloonaa repositorio omalle koneellesi. Luo kansioon .env tiedosto ja määritä sen sisältö seuraavanlaiseksi:

SECRET_KEY=<salainen-avain>

DB_NAME=<tietokannan-paikallinen-osoite>


Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt


$ flask run


Sovelluksen tilanne:

Tällä hetkellä pystyy luoda uuden käyttäjätunnuksen sekä kirjautua sisään. Käyttäjä pystyy kirjoittamaan arvostelun sekä kirjautua ulos.