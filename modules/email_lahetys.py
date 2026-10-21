#Tämä file lähettää sähköposti-ilmoituksen

import os 
import smtplib
from email.message import EmailMessage

def laheta_sahkoposti(tulokset): 
    """Lähettää sähköpostin, jos hintaraja alittuu."""

    ilmoitukset = [
        tulos for tulos in tulokset
        if tulos["alitti_rajan"]
    ]

    if not ilmoitukset:
        print("Ei uusia hintailmoituksia. ")
        return

    lahettaja = os.getenv("EMAIL_LAHETTAJA")
    salasana = os.getenv("EMAIL_SOVELLUSSALASANA")
    vastaanottaja = os.getenv("EMAIL_VASTAANOTTAJA")

    if not all([lahettaja, salasana, vastaanottaja]):
        print("Sähköpostiasetukset puuttuvat.")
        return

    viesti = EmailMessage()
    viesti["Subject"] = "Hintavahti: hintaraja alittui"
    viesti["From"] = lahettaja
    viesti["To"] = vastaanottaja

    teksti = ""

    for tulos in ilmoitukset:
        teksti += (
            f"Tuote: {tulos['tuote']} maksaa nyt "
            f"{tulos['hinta']:.2f} €\n"
            f"Kauppa: {tulos['kauppa']}\n"
            f"Hintaraja: {tulos['hintaraja']:.2f} €\n\n"


        )

    viesti.set_content(teksti)

    try:
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, timeout=20
        ) as palvelin:
            palvelin.login(lahettaja, salasana)
            palvelin.send_message(viesti)

        print("Sähköposti lähetetty!")

    except Exception as virhe:
        print(f"Sähköpostin lähetys epäonnistui: {virhe}")


        