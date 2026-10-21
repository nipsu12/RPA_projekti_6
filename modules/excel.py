#Tämä file lukee ja päivittää Exceliä
from openpyxl import load_workbook
def lue_tuotteet():
    tiedosto = load_workbook("tuotteet.xlsx")
    taulukko = tiedosto.active
    tuotteet = []
    for rivi in taulukko.iter_rows(min_row=2, values_only=True):
        if rivi[0] is not None:
            tuotteet.append(rivi)

    return tuotteet