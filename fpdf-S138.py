# Inports
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.image("S138.png", x=-4, y=-8, w=217, h=313)

#--------------------------------------------------------Kopf---------------------------------------------------------#

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

print(u"""
PSA?
a: gegen elektischen schlag
b: Störlichtbogen""")

option = input("> ")

if option == "a":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=104.8, y=121.5)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
    print("")
else:
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=147.2, y=121.5)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
    print("")

# Unterschrift
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=35, y=127.5)
pdf.multi_cell(w=0, h=0, txt="Herr Mustermann", border=0, fill=False)

#---------------------------------------------Die fünf Sicherheitsregeln---------------------------------------------#

#1a

# NH-Sicherungen
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=102, y=149.5)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)

# NH-Leischaltleiste
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=102, y=154)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)

# Leistungsschalter
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=102, y=158.5)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)

# Kabelverteilerschrank
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=157.5, y=154)
pdf.multi_cell(w=0, h=0, txt="N/A", border=0, fill=False)

# Trafostation
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=157.5, y=163)
pdf.multi_cell(w=0, h=0, txt="N/A", border=0, fill=False)

# Kompacktstation
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=157.5, y=171.7)
pdf.multi_cell(w=0, h=0, txt="N/A", border=0, fill=False)

# Zusätzlich im HK

print("(1a) Zusätlich im HAK? 'j' JA 'n' Nein")

output = input("> ")

if output == "j":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=166.5, y=181.7)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
    print("")
else:
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=166.5, y=181.7)
    pdf.multi_cell(w=0, h=0, txt="", border=0, fill=False)
    print("")

# 1b

# NH-Sicherungen
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=102, y=189)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)

# NH-Leischaltleiste
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=102, y=194)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)

# Leistungsschalter
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=102, y=198.2)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)

# Kabelverteilerschrank
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=157.5, y=193.7)
pdf.multi_cell(w=0, h=0, txt="N/A", border=0, fill=False)

# Trafostation
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=157.5, y=202.7)
pdf.multi_cell(w=0, h=0, txt="N/A", border=0, fill=False)

# Kompacktstation
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=157.5, y=211.5)
pdf.multi_cell(w=0, h=0, txt="N/A", border=0, fill=False)

# Zusätzlich im HK
print("(1b) Zusätlich im HAK? 'j' JA 'n' Nein")

output = input("> ")

if output == "j":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=166.5, y=221.7)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
    print("")
else:
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=166.5, y=221.7)
    pdf.multi_cell(w=0, h=0, txt="", border=0, fill=False)
    print("")


# 2a Gegen wiedereinschalten gesichert an der Aussenschale 1

print("""(2a) Ist ein Schloss an (Leistungs-) Schalter eingehangt und abgeschlossen? 
'j' JA 'n' Nein""")

output = input("> ")

if output == "j":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=166, y=230.3)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

    print("""Wie ist das Schild angebracht?
    a = Schuld angehängt
    b = Schild geglebt
    c = Schild magnetisch
    """)

    output = input("> ")

    if output == "a":
        pdf.set_font('Arial', style='B', size=12)
        pdf.set_xy(x=122.5, y=235)
        pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

    elif output == "b":
        pdf.set_font('Arial', style='B', size=12)
        pdf.set_xy(x=146, y=235)
        pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

    elif output == "c":
        pdf.set_font('Arial', style='B', size=12)
        pdf.set_xy(x=175.5, y=235)
        pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

else:
    print("Nichts vom dem trift zu\n")

# 2b Gegen wiedereinschalten gesichert an der Aussenschale 1

print("""(2b) Ist ein Schloss an (Leistungs-) Schalter eingehangt und abgeschlossen? 
'j' JA 'n' Nein""")

output = input("> ")

if output == "j":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=166, y=252.7)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

    print("""Wie ist das Schild angebracht?
    a = Schuld angehängt
    b = Schild geglebt
    c = Schild magnetisch
    """)

    output = input("> ")

    if output == "a":
        pdf.set_font('Arial', style='B', size=12)
        pdf.set_xy(x=122.5, y=257.3)
        pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

    elif output == "b":
        pdf.set_font('Arial', style='B', size=12)
        pdf.set_xy(x=146, y=257.2)
        pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

    elif output == "c":
        pdf.set_font('Arial', style='B', size=12)
        pdf.set_xy(x=175.5, y=257.2)
        pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

else:
    print("Nichts vom dem trift zu\n")



#----------------------------------------------------Zweite Seite----------------------------------------------------#

pdf.add_page()

pdf.image("S138b.png", x=-4, y=-8, w=217, h=313)

#---------------------------------------------Die fünf Sicherheitsregeln---------------------------------------------#

# 3a Spannungsfreiheit allpolig festgesltelt an der Aussenschale 1
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=125.5, y=47)
pdf.multi_cell(w=0, h=0, txt="Siemens MKI", border=0, fill=False)

# 3b Spannungsfreiheit allpolig festgesltelt an der Aussenschale 1
pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=125.5, y=81.5)
pdf.multi_cell(w=0, h=0, txt="Siemens MKII", border=0, fill=False)

# 3c Spannungsfreiheit allpoling festgestelt an der Arbeitsstelle

print("""(3c) Welche Spannungsfreiheit haben Sie an der Arbeitsstelle festgestellt?
a = Kabel geschnitten
b = Kabeln mit Beschussgerät beschossen
c = Spanung gebpüft
d = Mit kabelmesser isoliert
e = Andere Methode
""")

output = input("> ")

if output == "a":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=129.5, y=104)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif output == "b":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=116.3, y=108.5)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif output == "c":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=99.7, y=117.3)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif output == "d":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=170.8, y=121.7)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
else:
    text = input("")
    pdf.set_font('Arial', style='B', size=9)
    pdf.set_xy(x=89, y=126)
    pdf.multi_cell(w=0, h=0, txt=f"{text}", border=0, fill=False)

# 4 Geerdet und kurzgeschlossen
print("""Ist eine EuK-Gamintur eingebaut?
a = an der aussenschale I
b = an der Aussenschale II
c = bei beiden
d = Nicht geerder, weil...""")

output = input("> ")

if output == "a":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=92.5, y=139.5)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif output =="b":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=92.5, y=144.3)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif output == "c":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=92.5, y=139.5)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=92.5, y=144.3)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
else:
    text = input("")
    pdf.set_font('Arial', style='B', size=9)
    pdf.set_xy(x=119.5, y=148.5)
    pdf.multi_cell(w=0, h=0, txt=f"{text}", border=0, fill=False)

# 5 Benachtbare, unter Spannung stehende Teile abgedeckt
print("""was wuede genutzt?
a = isolierte Tücher
b = isolierende Formteile""")

output = input("> ")

if output == "a":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=113.4, y=161.6)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)
elif output == "b":
    pdf.set_font('Arial', style='B', size=12)
    pdf.set_xy(x=154.5, y=161.6)
    pdf.multi_cell(w=0, h=0, txt="X", border=0, fill=False)

pdf.set_font('Arial', style='B', size=9)
pdf.set_xy(x=158.5, y=166)
pdf.multi_cell(w=0, h=0, txt="10", border=0, fill=False)



pdf.output("S138.pdf")