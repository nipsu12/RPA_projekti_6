def tarkista_hinnat(tuote, hintaraja, hinnat):
    """Vertaa kauppojen hintoja annettuun hintarajaan."""
    tulokset = []

    for kauppa, hinta in hinnat.items():
        print(f"\nTarkistetaan {tuote}: {kauppa}")

        if hinta is None:
            print("  Hintaa ei saatu haettua.")
            continue

        alitti_rajan = hinta < hintaraja

        print(f"  Hinta: {hinta:.2f} €")
        print(f"  Hintaraja: {hintaraja:.2f} €")

        if alitti_rajan:
            ilmoitus = "Hintaraja alittui"
            print("  ✓ Hintaraja alittui")
        else:
            ilmoitus = "Ei ilmoitusta"
            print("  - Ei ilmoitusta")

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