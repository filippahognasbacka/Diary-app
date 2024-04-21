Käytä tätä versiota!

Branch main - vanha versio, käyttää sqlalchemy flasks

Ohjeet sovelluksen testaamiseen:

kloonaa repositorio omalle koneellesi, ja luo kansioon .env tiedosto ja määritä sen sisältö seuraavanlaiseksi:
SECRET_KEY=salainen_avain
DATABASE_URL=tietokannan-paikallinen-osoite

Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

$ python3 -m venv venv 
$ source venv/bin/activate 
$ pip install -r ./requirements.txt

tietokannan skeema tulee määrittää komennolla: psql < schema.sql

mene sen jälkeen main.py ja aja koodi
