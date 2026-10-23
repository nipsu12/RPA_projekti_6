# HUOM: Kaikki toiminnot on tehty omiin tiedostoihinsa modules-kansioon.
# Täällä main.py:ssä vain käytetään niitä from xx import xx -komennoilla.

from modules.excel import lue_tuotteet
from modules.hinnan_haku import hae_kauppojen_hinnat
from modules.hinnan_tarkastus import tarkista_hinnat
from modules.email_lahetys import laheta_sahkoposti

print("Robotti käynnistyy!")

# 1. NETTE TEKEE: Luetaan tuotteet ja hintarajat Excelistä
tuotteet = lue_tuotteet()
kaikki_tulokset = []

# Käydään läpi jokainen Excelistä löytyvä tuote
for tuote_tieto in tuotteet:
    tuote_nimi = tuote_tieto[0]   # Tuotteen nimi
    hintaraja = float(tuote_tieto[2])  # Hintaraja sarakkeesta

    print(f"\nSeurattava tuote: {tuote_nimi}")
    print(f"Hintaraja: {hintaraja} €")

    # 2. NITA TEKEE: Haetaan kauppojen hinnat ja tarkistetaan ne hintarajaa vasten
    hinnat = hae_kauppojen_hinnat()
    tulokset = tarkista_hinnat(tuote_nimi, hintaraja, hinnat)
    
    # Kerätään tämän tuotteen tulokset talteen yhteiseen listaan
    kaikki_tulokset.extend(tulokset)

# Lähettää sähköpostin hintatuloksen perusteella 
if kaikki_tulokset:
    laheta_sahkoposti(kaikki_tulokset)

print("\nRobotti valmis!")