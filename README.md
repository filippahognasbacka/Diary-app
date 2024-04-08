# Kahvilasovellus1

Sovelluksen perusidea on kerätä Helsingin tietyltä kartta-alueelta kahvilat. Käyttäjät voivat tarkistaa kahvilan aukioloajat sekä kirjoittaa yritykselle arvion. 

Jotta käyttäjä pystyy antamaan kirjallisen arvion sekä tähdet kahvilalle, hänen on oltava kirjautuneena sisään nettisivuille. Sisäänkirjautuneena käyttäjä pystyy myös etsimään tiettyä kahvilaa avainsanalla.

Käyttäjät voivat etsiä ravintoloita annetulla sanalla kuvauskentästä. Mahdollisesti myös mahdollisuus luokitella kahviloita esimerkiksi ketjuiksi, paikoiksi, joissa on suolaista syötävää yms.

Sovelluksessa on tähän mennessä toiminnot luoda käyttäjätunnus sekä kirjautua sovellukseen. Home sivulla on vielä ainoastaan mahdollisuus kirjoittaa arvostelu, mutta en ole ehtinyt lisätä karttaa paikoista vielä. 


Miten testata sovellusta:
kloonaa repositorio omalle koneellesi, ja luo kansioon .env tiedosto ja määritä sen siältö seuraavanlaiseksi:

SECRET_KEY=<salainen-avain>
DB_NAME=<tietokannan-paikallinen-osoite>

Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt


$ flask run

hox! kun itse kokeilin herjaa että __init__.py tiedoston dotenv ei ole asennettu, asensin sen mutta virhe ei kadonnut (voi siis olla ettei toimi)
