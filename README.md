Käytä tätä versiota!

Sovelluksen idea: Päiväkirja

Toiminnallisuudet:

-Uusi käyttäjä pystyy luoda käyttäjän ja kirjautua sisään.

-Sovelluksessa sisällä käyttäjä pystyy lisätä päiväkirjan päivän aiheen (esimerkiksi päivämäärän) otsikoksi

-Otsikkoa pystyy painaa ja seuraavalla sivulla on mahdollista kirjoittaa pidempi julkaisu päiväkirjaan

-Kotisivulla on myös mahdollista poistaa päiväkirjan julkaisu

-Entry sivulla on mahdollista myös poistaa kirjoitettu note

-User sivulla on mahdollista etsiä kirjoitetuista julkaisuista julkaisua ja sen kautta päästä julkaisuun

-Kirjautua ulos sovelluksesta.

<br />

Disclaimer:

Valitettavasti en saanut toimimaan mahdollisuutta lisätä kuvaa/tiedostoa kun käyttäjä kirjoittaa Noten. Kuvan tallennuksessa (views.py / add_note funktiossa on jotain pielessä), enkä valitettavasti osannut korjata virhettä vaikka katsoinkin sitä kauan. Tietokantataulussa (pictures_files) ei pitäisi olla ongelmaa mutta arvelen polussa olevan jotain mättää. Tarkoitus oli siis saada kuvat ladattua static sisällä olevaan kansioon (uploads). Toivottavasti tämä on OK.


<br />

Miten testata sovellusta:

Kloonaa repositorio omalle koneellesi. Luo kansioon .env tiedosto ja määritä sen sisältö seuraavanlaiseksi:

SECRET_KEY= <salainen-avain>

DB_NAME= <tietokannan-paikallinen-osoite>


Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt


$ flask run


