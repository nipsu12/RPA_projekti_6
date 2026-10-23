#Tässä tiedostossa tarkistetaan saadut hinnat ja verrataan niitä annettuun hintarajaan

#Funktio tarkistaa uudet hinnat Excelistä ja vertaa niitä hintarajaan
def tarkista_hinnat(tuote, hintaraja, hinnat):
    """Vertaa kauppojen hintoja annettuun hintarajaan."""
    tulokset = []

    for kauppa, hinta in hinnat.items():
        print(f"\nTarkistetaan {tuote}: {kauppa}")

        #Jos hintaa ei löydy, ilmoitetaan se ajossa
        if hinta is None:
            print("Hintaa ei saatu haettua.")
            continue

        alitti_rajan = hinta < hintaraja

        #Hintaraja Excelistä
        print(f"  Hinta: {hinta:.2f} €")
        print(f"  Hintaraja: {hintaraja:.2f} €")

        #Hintarajan alittuessa:
        if alitti_rajan:
            ilmoitus = "Hintaraja alittui"
            print("Hintaraja alittui")

        #Hintarajan ylittyessä:
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