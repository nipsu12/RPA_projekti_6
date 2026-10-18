#Tämä file hakee hinnan verkkosivulta


from urllib.request import Request, urlopen
import re


KAUPAT = {
    "Gigantti": (
        "https://www.gigantti.fi/product/tietokoneet-ja-toimistotarvikkeet/"
        "tietokoneet/kannettavat-tietokoneet/"
        "macbook-air-13-m5-16512gb-keskiyo/1056068"
    ),
    "Power": (
        "https://www.power.fi/tietotekniikka/tietokoneet/"
        "kannettavat-tietokoneet/"
        "apple-macbook-air-13-2026-m5-16512-gt-keskiyo/"
        "p-4253519/o-1217023/"
    )
}


def hae_hinta(url):
    """Hakee verkkosivun ja yrittää löytää hinnan HTML-sisällöstä."""

    try:
        pyynto = Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urlopen(pyynto, timeout=20) as vastaus:
            html = vastaus.read().decode(
                "utf-8", errors="ignore"
            )

        # Etsitään esimerkiksi 1 299,00 € tai 1299,00 €
        loyto = re.search(
            r"(\d[\d\s\u00a0.]*,\d{2})\s*(?:&nbsp;|€)",
            html
        )

        if loyto:
            hinta = loyto.group(1)
            hinta = hinta.replace(" ", "")
            hinta = hinta.replace("\u00a0", "")
            hinta = hinta.replace(".", "")
            hinta = hinta.replace(",", ".")
            return float(hinta)

        print("Hintaa ei löytynyt sivulta.")
        return None

    except Exception as virhe:
        print(f"Hinnan haku epäonnistui: {virhe}")
        return None


def hae_kauppojen_hinnat():
    """Palauttaa molempien kauppojen hinnat sanakirjana."""

    hinnat = {}

    for kauppa, url in KAUPAT.items():
        print(f"Haetaan hintaa: {kauppa}")
        hinnat[kauppa] = hae_hinta(url)

    return hinnat
