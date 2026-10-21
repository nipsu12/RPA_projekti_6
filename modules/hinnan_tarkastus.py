#Tämä file vertaa hinnan asetettuun hintarajaan

from hinnan_haku import hae_kauppojen_hinnat
from email_lahetys import laheta_sahkoposti


def tarkista_hinnat(tuote, hintaraja, hinnat):
    """Vertaa kauppojen hintoja annettuun hintarajaan."""
    tulokset = []

    for kauppa, hinta in hinnat.items():
        print(f"\nTarkistetaan {tuote}: {kauppa}")

        if hinta is None:
            print("Hintaa ei saatu haettua.")
            continue

        alitti_rajan = hinta < hintaraja

        print(f"  Hinta: {hinta:.2f} €")
        print(f"  Hintaraja: {hintaraja:.2f} €")

        if alitti_rajan:
            ilmoitus = "Hintaraja alittui"
            print("Hintaraja alittui")
        else:
            ilmoitus = "Ei ilmoitusta"
            print("Ei ilmoitusta")

        tulokset.append(
            {
                "tuote": tuote,
                "kauppa": kauppa,
                "hinta": hinta,
                "hintaraja": hintaraja,
                "alitti_rajan": alitti_rajan,
                "ilmoitus": ilmoitus,
            }
        )

    return tulokset


# Suoritetaan tarkistus
if __name__ == "__main__":
    tuote = "MacBook Air 13 M5"
    hintaraja = 1000.00  # Hintaraja asetettu 1000 euroon

    # Haetaan hinnat ensimmäisestä tiedostosta
    hinnat = hae_kauppojen_hinnat()

    # Tarkistetaan hinnat
    tulos = tarkista_hinnat(tuote, hintaraja, hinnat)

    #Lähetä säpo
    laheta_sahkoposti(tulokset)