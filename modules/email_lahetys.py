#Tämä tiedosto lähettää sähköposti-ilmoituksen

import os 
import smtplib
from email.message import EmailMessage

def laheta_sahkoposti(tulokset): 

    # Kerätään tuote, jonka hinta alitti hintarajan
    ilmoitukset = []

    for tulos in tulokset:
        if tulos["alitti_rajan"]:
            ilmoitukset.append(tulos)

    # Jos hinta ei alittunut, ei lähetetä sähköpostia
    if not ilmoitukset:
        print("Ei uusia hintailmoituksia. ")
        return
    
    # Haetaan sähköpostiasetukset ympäristömuuttujista
    lahettaja = os.getenv("EMAIL_LAHETTAJA")
    salasana = os.getenv("EMAIL_SOVELLUSSALASANA")
    vastaanottaja = os.getenv("EMAIL_VASTAANOTTAJA")

    # Tarkistetaan, että tarvittavat tiedot löytyvät
    if not lahettaja or not salasana or not vastaanottaja:
        print("Sähköpostiasetukset puuttuvat.")
        return
    
    # Luodaan sähköpostiviesti ja lsätään siihen tarvittavat tiedot
    viesti = EmailMessage()
    viesti["Subject"] = "Hintavahti: hintaraja alittui"
    viesti["From"] = lahettaja
    viesti["To"] = vastaanottaja

    # Muodostetaan viestin sisältö 
    teksti = ""

    for tulos in ilmoitukset:
        teksti += (
            f"Tuote: {tulos['tuote']} maksaa nyt "
            f"{tulos['hinta']:.2f} €\n"
            f"Kauppa: {tulos['kauppa']}\n"
            f"Hintaraja: {tulos['hintaraja']:.2f} €\n\n"
        )

    # Lisätään teksti sähköpostiviestiin.
    viesti.set_content(teksti)

    # Muodostetaan yhteys Gmailiin ja lähetetään viesti
    try:
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, timeout=20
        ) as palvelin:
            palvelin.login(lahettaja, salasana)
            palvelin.send_message(viesti)

        # Tulostetaan ilmoitus, jos lähetys onnistui
        print("Sähköposti lähetetty!")

    # Jos tapahtui virhe, tulostetaan virheilmoitus
    except Exception as virhe:
        print(f"Sähköpostin lähetys epäonnistui: {virhe}")


        