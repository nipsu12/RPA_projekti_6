#Täällä haetaan hintatiedot valituilta verkkosivuilta

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
        "p-4253519/?q=apple-macbook-air-13-2026-m5-16512-gt-keskiyo"
    )
}


def hae_hinta(url):
    """Hakee tuotteen hinnan verkkosivun HTML-koodista."""

    try:
        pyynto = Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urlopen(pyynto, timeout=20) as vastaus:
            html = vastaus.read().decode(
                "utf-8", errors="ignore"
            )

        # Tuotteen hinnan etsintä
        loyto = re.search(
            r'<meta\s+property="product:price:amount"\s+content="([\d.]+)"',
            html
        )

        if loyto:
            return float(loyto.group(1))

        # Tarkistus JSON-muotoisista hinnoista
        loyto = re.search(
            r'"price"\s*:\s*([\d.]+)',
            html
        )

        if loyto:
            return float(loyto.group(1))

        print(f"Hintaa ei löytynyt sivulta: {url}")
        return None

    except Exception as virhe:
        print(f"Hinnan haku epäonnistui: {virhe}")
        return None


def hae_kauppojen_hinnat():
    """Palauttaa kauppojen hinnat sanakirjana."""

    hinnat = {}

    for kauppa, url in KAUPAT.items():
        print(f"Haetaan hintaa: {kauppa}")
        hinnat[kauppa] = hae_hinta(url)

    return hinnat
