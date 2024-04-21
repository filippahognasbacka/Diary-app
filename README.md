Käytä tätä versiota!

Branch main - vanha versio, käyttää sqlalchemy flasks

Ohjeet sovelluksen testaamiseen:

kloonaa repositorio omalle koneellesi, ja luo kansioon .env tiedosto ja määritä sen sisältö seuraavanlaiseksi:
SECRET_KEY=
DB_NAME=

Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

$ python3 -m venv venv 
$ source venv/bin/activate 
$ pip install -r ./requirements.txt
ja mene sen jälkeen main.py ja aja koodi
