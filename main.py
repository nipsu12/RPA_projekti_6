#HUOM kaikki toiminnot kirjataan jokaisen omaan osioon
#modules kansiossa. Täällä vain käytetään
#from xx import xx komentoja

##NETTE TEKEE
##Robotti käynnistyy
##→ Lukee products.xlsx
##→ Löytää esimerkiksi 3 seurattavaa tuotetta

##NITA TEKEE
##→ Hakee tuotteen 1 hinnan
   ##Hinta: 89,90 €
   ##Hintaraja: 100 €
   ##✓ Hintaraja alittui
##→ Hakee tuotteen 2 hinnan
   ##Hinta: 549 €
   ##Hintaraja: 500 €
   ##- Ei ilmoitusta
##→ Tallentaa uudet hinnat Exceliin

from modules.hinnan_haku import hae_kauppojen_hinnat
from modules.hinnan_tarkastus import tarkista_hinnat

tuote = "MacBook Air M5 13 tuumaa, keskiyö"
hintaraja = 1000.00

hinnat = hae_kauppojen_hinnat()

tulokset = tarkista_hinnat(
    tuote,
    hintaraja,
    hinnat
)

print(tulokset)

##SILJA TEKEE
##→ Lähettää sähköpostin:
   ##"Tuote 1 maksaa nyt 89,90 €"
##→ Robotti valmis