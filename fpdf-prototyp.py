from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.image("Bild_png.png", x=-4, y=-8, w=217, h=313)

# Prototyp
#pdf.set_xy(x=0, y=0)
pdf.set_font('Arial', style='B', size=16)
pdf.set_text_color(r=178, g=34, b=34)
pdf.multi_cell(w=0, h=0, txt="Prototyp", border=0, fill=False)

# Arbeitsstelle/Arbeitsort
pdf.set_text_color(r=0, g=0, b=0)
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=49, y=100.9)
pdf.multi_cell(w=0, h=0, txt=u"Fürth", border=0, fill=False)

# Datum
pdf.set_xy(x=117.5, y=100.9)
pdf.multi_cell(w=0, h=0, txt="05.06.2020", border=0, fill=False)

# Uhrzeit
pdf.set_xy(x=161, y=100.9)
pdf.multi_cell(w=0, h=0, txt="10:00", border=0, fill=False)

# Anlagenverantwortlchen
pdf.set_xy(x=49, y=107.5)
pdf.multi_cell(w=0, h=0, txt="Herr Mustermann", border=0, fill=False)

# Arbeitsverantwortlcher
pdf.set_xy(x=141, y=107.5)
pdf.multi_cell(w=0, h=0, txt="Herr Mustermann", border=0, fill=False)

# Arbeitsausführenden
pdf.set_xy(x=44.5, y=114.5)
pdf.multi_cell(w=0, h=0, txt="Herr Max Mustermann", border=0, fill=False)

# PSA gegen elektrischen schlag

print(u"""PSA
a: gegen elektischen schlag
b: Störlichtbogen""")

option = input("> ")

if option == "a":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=104.8, y=121.5)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
else:
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=147.2, y=121.5)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

# Unterschrift
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=35, y=127.5)
pdf.multi_cell(w=0, h=0, txt="Herr Mustermann", border=0, fill=False)

#--------------------------------------------------------------------------------------------#

# NH Sicherung
pdf.set_xy(x=102.5, y=149)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)

# NH Lastschaltleiste
pdf.set_xy(x=102.5, y=154)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)

# Bezeichnungen
pdf.set_xy(x=158, y=154.5)
pdf.multi_cell(w=0, h=0, txt="N/A", border=0, fill=False)

# Leistungsschalter
pdf.set_xy(x=102.5, y=158)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)

# Umspannwerk UW
pdf.set_xy(x=165, y=159)
pdf.multi_cell(w=0, h=0, txt="N/A", border=0, fill=False)

# Trafo Ausser Betrib genommen?

print("Ist die Trafo Schaltanlage Freigeschaltet? j = JA, n = Nein\n")
option = input("> ")

if option == "n":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=114.8, y=164)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
else:
    print("Abfrage durchgefuehrt")

# Kabbelverteilschrank
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=174, y=163.5)
pdf.multi_cell(w=0, h=0, txt="N/A", border=0, fill=False)

#--------------------------------------------------------------------------------------------#

# Gegen Wiedereinschalten gesichert

print("Ist der Schalter gegen Wiedereinschalten gesichert? j = JA, n = Nein\n")
option = input("> ")

if option == "n":
    print("""Wie ist eine Warnung angebracht worden?
    a: durch ein aufgehangenes Schild
    b: durch ein geklebter Zetel oder Schild"
    c: durch ein Maktetisches Schild""")

    option = input("> ")

    if option == "a":
        pdf.set_font('Arial', style='B', size=12)
        pdf.set_xy(x=122.7, y=177.3)
        pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
    elif option == "b":
        pdf.set_font('Arial', style='B', size=12)
        pdf.set_xy(x=148, y=177.3)
        pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
    elif option == "c":
        pdf.set_font('Arial', style='B', size=12)
        pdf.set_xy(x=175.5, y=177.3)
        pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
    else:
        print("Abfrage abgeschlossen\n")

else:
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=148, y=172.65)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
    print("Abfrage abgeschlossen\n")

# ------------------------------------------------------------------------------------------#

# Zweipoliger Spannungsprüfer Nierderspanung Hersteller
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=64, y=194.5)
pdf.multi_cell(w=0, h=0, txt="Siemens / Typ MK III", border=0, fill=False)

# Einpoliger Spannungsprüfer Nierderspanung Hersteller
pdf.set_xy(x=64, y=203)
pdf.multi_cell(w=0, h=0, txt="Siemens / Typ MK XI", border=0, fill=False)

#-------------------------------------------------------------------------------------------#

# Geerdet und kurzgeschlossen

print("""Wo ist ein EuK verbaut?
a: in der NH-Sicherungsunterteile
b: an der Sammelschine
c: am Trafo (Niederspannung)
d: am Terfo (Mittelspannung)""")

option = input("> ")

if option == "a":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=146.6, y=212.55)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif option == "b":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=96, y=217)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif option == "c":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=142, y=217.3)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif option == "d":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=186.2, y=217)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
else:
    print("Bitte geben sie ein grund an")
    text = input("")
    pdf.set_font('Arial', style='B', size=9)
    pdf.set_xy(x=63, y=225)
    pdf.multi_cell(w=0, h=0, txt=f"{text}", border=0, fill=False)

#-------------------------------------------------------------------------------------------#

# Benachbarte unter Spanung stehende Teile abgedeckt

print(u"""Mit der abdekung soll erichet werden:
a: Fingersicherheit
b: Handrückensicherheit
c: vollstaendige Berürungsschutz""")

option = input("> ")

if option == "a":
    pdf.set_xy(x=86.5, y=239.3)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif option == "b":
    pdf.set_xy(x=128, y=239.3)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif option == "c":
    pdf.set_xy(x=181.6, y=239.3)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
else:
    print("auswahl beendet")

print("""Dazu soll benutzt werden:
a: isolierende Tücher
b: isolierende Formteile""")

option = input("> ")

if option == "a":
    pdf.set_xy(x=113.3, y=243.7)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif option == "b":
    pdf.set_xy(x=154.3, y=243.7)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
else:
    print("Auswahl beendet")

# Keine Abdeckung

pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=161.6, y=247.9)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)

# Kennzeichnung mit Bändern oder Ketten gesichert?

print(u"Gefahrenbereich mit Bändern oder Ketten gesicher? j = JA, n = NEIN")

option = input("> ")

if option == "j":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=168.3, y=253)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

pdf.output("Prototyp.pdf")