import customtkinter as ctk
from CTkListbox import CTkListbox

# Stel het standaard thema en uiterlijk in
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Database met categorie-scheidingen, widgets, stijlen en core logica
WIDGET_DATA = {
    "--- GLOBALE STIJLEN ---": {
        "description": (
            "Globale instellingen gelden voor de hele applicatie en bepalen het uiterlijk.\n\n"
            "Belangrijke functies:\n"
            "- ctk.set_appearance_mode('Dark' / 'Light' / 'System'): Bepaalt of de app een donker of licht thema gebruikt.\n"
            "- ctk.set_default_color_theme('blue' / 'green' / 'dark-blue'): Verandert de accentkleur.\n"
            "- ctk.set_widget_scaling(1.2): Vergroot of verkleint alle widgets proportioneel."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "ctk.set_appearance_mode('Dark')\n"
            "ctk.set_default_color_theme('green')\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x250')\n"
            "app.title('Stijlen Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "label = ctk.CTkLabel(app, text='Dark thema en groene accenten!', wraplength=300)\n"
            "label.pack(padx=20, pady=40)\n"
        )
    },
    "--- CORE & LOGICA ---": {
        "description": (
            "De motor achter elke app: fundamentele Tkinter-mechanismen die je ook in CustomTkinter continu gebruikt.\n\n"
            "1. Layout (.pack / .grid / .place): Hoe zet je elementen op het scherm?\n"
            "2. Variabelen (StringVar / IntVar): Om live data te koppelen aan widgets.\n"
            "3. Event Binding (.bind): Om te luisteren naar toetsen en muiskliks.\n"
            "4. Timers (.after): Om acties uit te voeren na een vertraging."
        ),
        "code": (
            "# Dit is een informatief hoofdcategorie-overzicht.\n"
            "# Selecteer een van de specifieke onderwerpen hieronder\n"
            "# in de lijst (Layout, Variabelen, Bind of After)\n"
            "# om een werkend codevoorbeeld te bekijken!"
        )
    },
    "Layout (pack, grid, place)": {
        "description": (
            "Layout managers bepalen waar widgets op het scherm komen te staan.\n\n"
            "- .pack(): Zet elementen automatisch onder of naast elkaar.\n"
            "- .grid(): Werkt in een raster van rijen (row) en kolommen (column), ideaal voor formulieren.\n"
            "- .place(): Plaatst elementen op exacte X- en Y-coördinaten in pixels."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x250')\n"
            "app.title('Grid Layout Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "# Grid gebruiken voor een formulier-indeling\n"
            "lbl_naam = ctk.CTkLabel(app, text='Naam:')\n"
            "lbl_naam.grid(row=0, column=0, padx=10, pady=10, sticky='w')\n\n"
            "entry_naam = ctk.CTkEntry(app)\n"
            "entry_naam.grid(row=0, column=1, padx=10, pady=10)\n\n"
            "lbl_wnd = ctk.CTkLabel(app, text='Wachtwoord:')\n"
            "lbl_wnd.grid(row=1, column=0, padx=10, pady=10, sticky='w')\n\n"
            "entry_wnd = ctk.CTkEntry(app, show='*')\n"
            "entry_wnd.grid(row=1, column=1, padx=10, pady=10)\n"
        )
    },
    "Variabelen (StringVar, etc.)": {
        "description": (
            "Tkinter-variabelen (zoals ctk.StringVar en ctk.IntVar) bewaken data.\n"
            "Als de waarde verandert, past de gekoppelde widget (zoals een Label of Entry) zich automatisch aan, "
            "en vice versa."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('StringVar Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "# Maak een StringVar aan\n"
            "mijn_tekst = ctk.StringVar(value='Typ hieronder...')\n\n"
            "label = ctk.CTkLabel(app, textvariable=mijn_tekst, font=('Helvetica', 16))\n"
            "label.pack(padx=20, pady=20)\n\n"
            "entry = ctk.CTkEntry(app, textvariable=mijn_tekst)\n"
            "entry.pack(padx=20, pady=10)\n"
        )
    },
    "Event Binding (.bind)": {
        "description": (
            "Met .bind() kun je specifieke acties (events) afvangen, zoals het indrukken van een "
            "bepaalde toets op het toetsenbord of dubbelklikken met de muis."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('Bind Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "def handle_enter(event):\n"
            "    print('Enter toets ingedrukt! Invoer:', entry.get())\n\n"
            "entry = ctk.CTkEntry(app, placeholder_text='Typ iets en druk op Enter')\n"
            "entry.pack(padx=20, pady=40)\n\n"
            "# Koppel de Enter-toets aan het invoerveld\n"
            "entry.bind('<Return>', handle_enter)\n"
        )
    },
    "Timers & Delays (.after)": {
        "description": (
            "Met .after(milliseconden, functie) kun je een timer instellen om code pas na een "
            "specifieke vertraging uit te voeren, of om taken periodiek te herhalen."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('Timer Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "label = ctk.CTkLabel(app, text='Wacht op update...')\n"
            "label.pack(padx=20, pady=40)\n\n"
            "def update_tekst():\n"
            "    label.configure(text='Dit bericht verscheen na 2 seconden!')\n\n"
            "# Voer update_tekst uit na 2000 milliseconden (2 seconden)\n"
            "app.after(2000, update_tekst)\n"
        )
    },
    "--- WIDGETS ---": {
        "description": (
            "Hier beginnen de visuele bouwstenen (widgets) van CustomTkinter.\n\n"
            "Met deze componenten bouw je de gebruikersinterface van je applicatie op. "
            "Elke widget heeft zijn eigen specifieke eigenschappen en functies."
        ),
        "code": (
            "# Dit is het startpunt van de visuele widgets.\n"
            "# Selecteer een widget hieronder in de lijst (zoals CTkButton of CTkLabel)\n"
            "# om de beschrijving en een werkend voorbeeld te bekijken!"
        )
    },
    "CTkButton": {
        "description": (
            "CTkButton is een aanpasbare knop die acties activeert wanneer er op geklikt wordt.\n\n"
            "Belangrijkste eigenschappen:\n"
            "- text: De tekst op de knop.\n"
            "- command: De functie die wordt aangeroepen bij een klik.\n"
            "- corner_radius: Ronding van de hoeken.\n"
            "- fg_color / hover_color: Achtergrondkleur en kleur bij hover."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkButton Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "def button_click():\n"
            "    print('Knop is geklikt!')\n\n"
            "button = ctk.CTkButton(app, text='Klik Hier', command=button_click, corner_radius=8)\n"
            "button.pack(padx=20, pady=20)\n"
        )
    },
    "CTkLabel": {
        "description": (
            "CTkLabel wordt gebruikt om tekst of afbeeldingen op het scherm weer te geven.\n\n"
            "Belangrijkste eigenschappen:\n"
            "- text: De weer te geven tekst.\n"
            "- font: Lettertype en grootte, bijv. ('Arial', 16).\n"
            "- text_color: Kleur van de tekst."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkLabel Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "label = ctk.CTkLabel(app, text='Hallo, CustomTkinter!', font=('Helvetica', 18, 'bold'))\n"
            "label.pack(padx=20, pady=20)\n"
        )
    },
    "CTkEntry": {
        "description": (
            "CTkEntry is een invoerveld voor een enkele regel tekst.\n\n"
            "Belangrijkste eigenschappen:\n"
            "- placeholder_text: Tijdelijke tekst wanneer het veld leeg is.\n"
            "- get(): Haalt de ingevoerde tekst op.\n"
            "- show: Gebruik show='*' voor wachtwoordinvoer."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkEntry Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "entry = ctk.CTkEntry(app, placeholder_text='Typ hier...')\n"
            "entry.pack(padx=20, pady=20)\n\n"
            "def show_input():\n"
            "    print('Ingevoerd:', entry.get())\n\n"
            "btn = ctk.CTkButton(app, text='Verstuur', command=show_input)\n"
            "btn.pack(padx=20, pady=10)\n"
        )
    },
    "CTkCheckBox": {
        "description": (
            "CTkCheckBox is een selectievakje waarmee de gebruiker een optie in- of uitschakelt.\n\n"
            "Belangrijkste eigenschappen:\n"
            "- text: Beschrijving naast het vinkje.\n"
            "- get(): Geeft 1 (Aan) of 0 (Uit) terug."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkCheckBox Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "checkbox = ctk.CTkCheckBox(app, text='Accepteer voorwaarden')\n"
            "checkbox.pack(padx=20, pady=20)\n"
        )
    },
    "CTkRadioButton": {
        "description": (
            "CTkRadioButton laat de gebruiker één optie kiezen uit een groep.\n\n"
            "Belangrijkste eigenschappen:\n"
            "- variable: Houdt de gekozen waarde bij (bijv. ctk.StringVar).\n"
            "- value: De unieke waarde van deze knop."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x250')\n"
            "app.title('CTkRadioButton Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "var = ctk.StringVar(value='Optie 1')\n"
            "r1 = ctk.CTkRadioButton(app, text='Optie 1', value='Optie 1', variable=var)\n"
            "r2 = ctk.CTkRadioButton(app, text='Optie 2', value='Optie 2', variable=var)\n"
            "r1.pack(padx=20, pady=10)\n"
            "r2.pack(padx=20, pady=10)\n"
        )
    },
    "CTkSwitch": {
        "description": (
            "CTkSwitch is een tuimelschakelaar (toggle switch) voor een aan/uit instelling."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkSwitch Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "switch = ctk.CTkSwitch(app, text='Donkere modus')\n"
            "switch.pack(padx=20, pady=20)\n"
        )
    },
    "CTkSlider": {
        "description": (
            "CTkSlider is een schuifbalk om een numerieke waarde te selecteren binnen een bereik."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkSlider Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "slider = ctk.CTkSlider(app, from_=0, to=100)\n"
            "slider.pack(padx=20, pady=40)\n"
            "slider.set(50)\n"
        )
    },
    "CTkSegmentedButton": {
        "description": (
            "CTkSegmentedButton is een moderne reeks knoppen die werkt als een horizontale optiekiezer "
            "(vergelijkbaar met tabs of radiobuttons in knopvorm)."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkSegmentedButton Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "def seg_callback(value):\n"
            "    print('Gekozen:', value)\n\n"
            "seg_btn = ctk.CTkSegmentedButton(app, values=['Waarde 1', 'Waarde 2', 'Waarde 3'], command=seg_callback)\n"
            "seg_btn.pack(padx=20, pady=30)\n"
            "seg_btn.set('Waarde 1')\n"
        )
    },
    "CTkOptionMenu": {
        "description": (
            "CTkOptionMenu is een keuzemenu (dropdown menu) waarmee de gebruiker één optie kan kiezen uit een lijst."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkOptionMenu Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "optionmenu = ctk.CTkOptionMenu(app, values=['Optie 1', 'Optie 2', 'Optie 3'])\n"
            "optionmenu.pack(padx=20, pady=20)\n"
        )
    },
    "CTkComboBox": {
        "description": (
            "CTkComboBox combineert een invoerveld en een dropdown menu, zodat de gebruiker kan typen of kiezen."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkComboBox Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "combobox = ctk.CTkComboBox(app, values=['Python', 'JavaScript', 'C++'])\n"
            "combobox.pack(padx=20, pady=20)\n"
        )
    },
    "CTkProgressBar": {
        "description": (
            "CTkProgressBar geeft de voortgang van een proces visueel weer (0.0 tot 1.0)."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkProgressBar Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "progress = ctk.CTkProgressBar(app)\n"
            "progress.pack(padx=20, pady=30)\n"
            "progress.set(0.7)\n"
        )
    },
    "CTkTextbox": {
        "description": (
            "CTkTextbox is een tekstveld voor meerdere regels."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x300')\n"
            "app.title('CTkTextbox Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "textbox = ctk.CTkTextbox(app, width=300, height=150)\n"
            "textbox.pack(padx=20, pady=20)\n"
            "textbox.insert('1.0', 'Meeregelige tekst hier...')\n"
        )
    },
    "CTkFrame": {
        "description": (
            "CTkFrame is een container om andere widgets in te groeperen."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x300')\n"
            "app.title('CTkFrame Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "frame = ctk.CTkFrame(app, corner_radius=15)\n"
            "frame.pack(padx=20, pady=20, fill='both', expand=True)\n"
            "label = ctk.CTkLabel(frame, text='In het frame')\n"
            "label.pack(padx=10, pady=10)\n"
        )
    },
    "CTkScrollableFrame": {
        "description": (
            "CTkScrollableFrame is een container met een ingebouwde verticale schuifbalk."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x300')\n"
            "app.title('CTkScrollableFrame Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "sf = ctk.CTkScrollableFrame(app, label_text='Lijst')\n"
            "sf.pack(padx=20, pady=20, fill='both', expand=True)\n"
            "for i in range(15):\n"
            "    ctk.CTkButton(sf, text=f'Item {i+1}').pack(pady=5)\n"
        )
    },
    "CTkTabview": {
        "description": (
            "CTkTabview biedt een interface met tabbladen."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x300')\n"
            "app.title('CTkTabview Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "tv = ctk.CTkTabview(app)\n"
            "tv.pack(padx=20, pady=20, fill='both', expand=True)\n"
            "t1 = tv.add('Tab 1')\n"
            "t2 = tv.add('Tab 2')\n"
            "ctk.CTkLabel(t1, text='Inhoud Tab 1').pack(padx=10, pady=10)\n"
        )
    },
    "CTkToplevel": {
        "description": (
            "CTkToplevel wordt gebruikt om extra, losse pop-up vensters te openen naast je hoofdvenster.\n\n"
            "Belangrijkste eigenschappen:\n"
            "- geometry('WxH'): Bepaalt de afmetingen van het venster.\n"
            "- title('Titel'): Titelbalk tekst."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('300x150')\n"
            "app.title('Pop-up Venster')\n"
            "app.attributes('-topmost', True)\n\n"
            "lbl = ctk.CTkLabel(app, text='Dit is een apart toplevel-venster!')\n"
            "lbl.pack(padx=20, pady=30)\n"
        )
    },
    "CTkImage": {
        "description": (
            "CTkImage is speciaal ontworpen voor CustomTkinter om afbeeldingen (PNG/JPG) "
            "scherp weer te geven op schermen met hoge resolutie (Retina/DPI) én om automatisch "
            "te wisselen tussen een lichte en donkere variant."
        ),
        "code": (
            "import customtkinter as ctk\nfrom PIL import Image, ImageTk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x300')\n"
            "app.title('CTkImage Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "# Let op: vervang 'pad/naar/afbeelding.png' door een echt lokaal bestand\n"
            "try:\n"
            "    my_image = ctk.CTkImage(light_image=Image.open('afbeelding.png'), size=(100, 100))\n"
            "    lbl = ctk.CTkLabel(app, text='', image=my_image)\n"
            "    lbl.pack(padx=20, pady=20)\n"
            "except:\n"
            "    lbl = ctk.CTkLabel(app, text='Plaats een afbeelding.png in je map\\nom dit te testen.')\n"
            "    lbl.pack(padx=20, pady=20)\n"
        )
    },
    "CTkFont": {
        "description": (
            "CTkFont maakt het mogelijk om herbruikbare lettertype-objecten te maken. "
            "Handig als je de stijl op meerdere plekken wilt hergebruiken of later in één keer wilt aanpassen.\n\n"
            "Belangrijkste eigenschappen:\n"
            "- family: Naam van het lettertype (bijv. 'Arial', 'Helvetica').\n"
            "- size: Tekstgrootte in punten.\n"
            "- weight: 'normal' of 'bold'."
        ),
        "code": (
            "import customtkinter as ctk\n\n"
            "app = ctk.CTkToplevel()\n"
            "app.geometry('400x200')\n"
            "app.title('CTkFont Voorbeeld')\n"
            "app.attributes('-topmost', True)\n\n"
            "mijn_font = ctk.CTkFont(family='Helvetica', size=16, weight='bold')\n\n"
            "lbl = ctk.CTkLabel(app, text='Dit gebruikt een CTkFont object!', font=mijn_font)\n"
            "lbl.pack(padx=20, pady=40)\n"
        )
    }
}

# Hoofdapplicatie (hoogte op 800)
app = ctk.CTk()
app.title("CustomTkinter Interactive Manual")
app.geometry("1100x800")

# Structuur: Links menu (breder gemaakt op 320), Rechts details
left_frame = ctk.CTkFrame(app, width=320)
left_frame.pack(side="left", fill="y", padx=10, pady=10)
left_frame.pack_propagate(False)  # Zorgt ervoor dat de breedte van 320 vast blijft staan

title_label = ctk.CTkLabel(left_frame, text="Onderwerpen", font=("Helvetica", 16, "bold"))
title_label.pack(padx=10, pady=(10, 5))


# Functie om de beschrijving en code bij te werken bij selectie
def update_details(selected_function):
    data = WIDGET_DATA.get(selected_function, {
        "description": f"Geen beschrijving beschikbaar voor {selected_function}.",
        "code": f"# Geen voorbeeldcode beschikbaar voor {selected_function}."
    })

    header_label.configure(text=selected_function)

    # Scherm 1 (Beschrijving) bijwerken
    description_text.configure(state="normal")
    description_text.delete("1.0", "end")
    description_text.insert("end", data["description"])
    description_text.configure(state="disabled")

    # Scherm 2 (Code voorbeeld) bijwerken
    code_text.configure(state="normal")
    code_text.delete("1.0", "end")
    code_text.insert("end", data["code"])


# Functie om de code uit het tekstvak dynamisch uit te voeren
def run_custom_code():
    code_to_run = code_text.get("1.0", "end")
    try:
        exec(code_to_run, {"ctk": ctk})
    except Exception as e:
        print(f"Fout bij uitvoeren van de code:\n{e}")


# Listbox links voor navigatie (met fontgrootte 14 ingesteld)
function_list = CTkListbox(left_frame, command=update_details, font=("Helvetica", 14))
function_list.pack(fill="both", expand=True, padx=5, pady=5)

for func_name in WIDGET_DATA.keys():
    function_list.insert("end", func_name)

# Detail frame rechts
right_frame = ctk.CTkFrame(app)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

header_label = ctk.CTkLabel(right_frame, text="Selecteer een onderwerp", font=("Helvetica", 20, "bold"))
header_label.pack(anchor="w", padx=15, pady=(15, 5))

# Tabview voor Scherm 1 (Beschrijving) en Scherm 2 (Code voorbeeld)
detail_tabs = ctk.CTkTabview(right_frame)
detail_tabs.pack(fill="both", expand=True, padx=10, pady=10)

tab_desc = detail_tabs.add("Beschrijving (Scherm 1)")
tab_code = detail_tabs.add("Werkend Code Voorbeeld (Scherm 2)")

# Scherm 1: Beschrijving (Fontgrootte 18)
description_text = ctk.CTkTextbox(tab_desc, font=("Helvetica", 18), wrap="word")
description_text.pack(fill="both", expand=True, padx=5, pady=5)

# Scherm 2: Code voorbeeld (Fontgrootte 18)
code_text = ctk.CTkTextbox(tab_code, font=("Consolas", 18), wrap="none")
code_text.pack(fill="both", expand=True, padx=5, pady=(5, 10))

run_button = ctk.CTkButton(tab_code, text="▶ Run Code", fg_color="#2fa572", hover_color="#227a53",
                           command=run_custom_code)
run_button.pack(anchor="e", padx=5, pady=5)

# Selecteer standaard het eerste item
function_list.select(0)
update_details(list(WIDGET_DATA.keys())[0])

app.mainloop()