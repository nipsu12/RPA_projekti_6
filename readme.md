# RPA-projekti – Tuotteiden hintaseuranta

## 1. Projektin kuvaus

Projektin tavoitteena on automatisoida tuotteiden hintojen seuranta verkkokaupoissa. Robotti lukee seurattavan tuotteen tiedot Excel-tiedostosta, hakee tuotteen hinnat Gigantilta ja Powerilta, vertaa hintoja asetettuihin hintarajoihin ja tallentaa tulokset Exceliin.

Jos tuotteen hinta alittaa asetetun hintarajan, robotti voi lähettää käyttäjälle sähköposti-ilmoituksen.

## 2. Käytetyt työkalut

- Python – ohjelman toiminnallisuus.
- Robot Framework – automaation suorittaminen projektin toteutuksen mukaisesti.
- Excel – tuotteiden tietojen ja hintatulosten tallentaminen.
- Git – projektin versionhallinta.

## 3. Projektin rakenne

- `main.py` – robotin käynnistys ja toimintojen yhdistäminen.
- `modules/hinnan_haku.py` – tuotteiden hintojen hakeminen verkkokaupoista.
- `modules/hinnan_tarkastus.py` – hintojen vertaaminen hintarajoihin.
- `modules/excel.py` – Excel-tiedostojen käsittely.
- `modules/email_lahetys.py` – sähköposti-ilmoitusten lähettäminen.
- `tuotteet.xlsx` – seurattavien tuotteiden tiedot.
- `logs/robot.log` – robotin tapahtumaloki.

## 4. Hintojen seuranta

Robotti seuraa Apple MacBook Air M5 -kannettavan hintoja seuraavissa verkkokaupoissa:

- Gigantti: https://www.gigantti.fi/
- Power: https://www.power.fi/

Tuotteen hinnat haetaan verkkokauppojen tuotesivuilta. Hintoja verrataan Excelissä määritettyyn hintarajaan.

## 5. Hintarajan tarkistus

Hintarajan tarkistus toimii seuraavasti:

1. Robotti hakee tuotteen hinnan.
2. Hintaa verrataan asetettuun hintarajaan.
3. Jos hinta on hintarajaa pienempi, tulokseen merkitään, että hintaraja alittui.
4. Muussa tapauksessa ilmoitusta ei merkitä lähetettäväksi.
5. Hintatulokset tallennetaan Exceliin myöhempää käsittelyä varten.

## 6. Asennus

Pythonin tulee olla asennettuna tietokoneelle.

Excel-tiedostojen käsittelyyn tarvittava kirjasto asennetaan komennolla:

```bash
python -m pip install openpyxl
```

## 7. Käynnistäminen

Projekti käynnistetään projektin toteutuksen mukaisesti esimerkiksi suorittamalla `main.py` tai Robot Frameworkin `.robot`-tiedosto.

## 8. Huomioitavaa

Verkkokauppojen sivurakenne voi muuttua, ja hinnan automaattinen hakeminen riippuu siitä, miten sivusto tarjoaa tuotteen hinnan. Hinnanhaun oikeellisuus tulee testata ennen robotin käyttöä.

Projektin lopullinen toiminta riippuu kaikkien moduulien yhdistämisestä ja testaamisesta.