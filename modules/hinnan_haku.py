#Tämä file hakee hinnan verkkosivulta


from urllib.request import Request, urlopen
import re


KAUPAT = {
    "Gigantti": (
        "https://www.gigantti.fi/product/tietokoneet-ja-toimistotarvikkeet/tietokoneet/kannettavat-tietokoneet/macbook-air-13-m5-16512gb-keskiyo/1056068?qid=a33f187d3ef1fe52e247bbf238fb82b2"
    ),
    "Power": (
        "https://www.power.fi/tietotekniikka/tietokoneet/kannettavat-tietokoneet/apple-macbook-air-13-2026-m5-16512-gt-keskiyo/p-4253519/?q=apple-macbook-air-13-2026-m5-16512-gt-keskiyo"
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

        # TESTI: tulostetaan HTML:n ensimmäiset 1000 merkkiä
        print(html[:1000])

                # Etsitään HTML:stä kaikki kohdat, joissa mainitaan hinta
        for osuma in re.finditer(
            r"(?i).{0,80}(?:price|hinta|1499|1500).{0,120}",
            html
        ):
            print("MAHDOLLINEN HINTAKOHTA:", osuma.group(0))

        # Etsitään esimerkiksi hintoja, jotka voivat olla muodossa "89,90 €" tai "1 299,00 €"
        loyto = re.search(
            r"(\d[\d\s\u00a0.]*,\d{2})\s*(?:&nbsp;|€)",
            html
        )

        if loyto:
            # Poistetaan kaikki muut merkit paitsi numerot ja pilkku,
            # -> muutetaan pilkku pisteeksi float-muunnosta varten.
            puhdas_hinta = re.sub(r"[^\d,]", "", loyto.group(1)).replace(",", ".")
            return float(puhdas_hinta)

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
