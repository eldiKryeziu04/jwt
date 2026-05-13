JWT Authentication Console Application

Përshkrimi
Ky projekt është një implementim i sistemit të autentikimit duke përdorur JSON Web Tokens (JWT) në një model klient-server përmes Socket-ave. Serveri autentikon kredencialet dhe lëshon një token të nënshkruar me RSA (Asymmetric Encryption), i cili përdoret nga klienti për të aksesuar burime të mbrojtura.

Arkitektura Teknike
Gjuha: Python 3.x

Libraritë:

PyJWT: Për krijimin dhe verifikimin e tokeneve.

cryptography: Për gjenerimin e çelësave RSA.

socket: Për komunikimin në rrjet.

Kërkesat e Sistemit
Para ekzekutimit, duhet të instaloni libraritë e nevojshme:

Bash
pip install PyJWT cryptography
Udhëzimet për Ekzekutim
1. Startimi i Serverit
Hapni një terminal (CMD ose PowerShell) dhe lundroni te folderi i projektit:

Bash
python server.py
Serveri do të gjenerojë çelësat RSA automatikisht dhe do të presë për lidhje në portin 5000.

2. Startimi i Klientit
Hapni një terminal të dytë dhe ekzekutoni:

Bash
python client.py
Përdorimi i Aplikacionit
Login: Kur klienti kërkon kredencialet, përdorni:

Username: jane_doe

Password: password123

Access Protected Data: Pasi të jeni identifikuar me sukses dhe të keni marrë token-in, shkruani komandën:

Plaintext
request_data
Serveri do të verifikojë nënshkrimin e token-it me çelësin publik dhe do të kthejë të dhënat nëse token-i është valid.

Logout: Shkruani komandën logout për të fshirë token-in nga memoria e klientit dhe për të mbyllur sesionin.

Siguria
Algoritmi: RS256 (RSA Signature me SHA-256).

Validiteti: Token-i skadon automatikisht pas 10 minutave (exp claim).

Asymmetric Keys: Serveri mban çelësin privat për nënshkrim, ndërsa verifikimi bëhet përmes çelësit publik.
