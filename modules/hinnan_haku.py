#Täällä haetaan hintatiedot valituilta verkkosivuilta

from urllib.request import Request, urlopen
import re

#Määrittelyt verkkosivujen URL-osoitteet
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

#Funktio tuotteen hinnan hakemiseen verkkosivulta
def hae_hinta(url):
    """Hakee tuotteen hinnan verkkosivun HTML-koodista."""

    #Yritys hakea hintaa verkkosivulta
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

        # Etsintä JSON-muotoisista hinnoista jos tarvitaan
        loyto = re.search(
            r'"price"\s*:\s*([\d.]+)',
            html
        )

        if loyto:
            return float(loyto.group(1))

        print(f"Hintaa ei löytynyt sivulta: {url}")
        return None

    #Virheilmoitus jos hintaa ei saatu haettua (esim. verkkosivu ei vastaa)
    except Exception as virhe:
        print(f"Hinnan haku epäonnistui: {virhe}")
        return None

#Funktiolla haetaan kauppojen hinnat ja palautetaan ne Excel-tiedostoon
def hae_kauppojen_hinnat():
    """Palauttaa kauppojen hinnat sanakirjana."""

    hinnat = {}

    for kauppa, url in KAUPAT.items():
        print(f"Haetaan hintaa: {kauppa}")
        hinnat[kauppa] = hae_hinta(url)

    return hinnat
