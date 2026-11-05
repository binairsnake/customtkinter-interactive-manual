[readme.md](https://github.com/user-attachments/files/34439867/readme.md)
# customtkinter-interactive-manual
Eerste release van de CustomTkinter Interactive Manual


# CustomTkinter Interactive Manual 🚀

Een interactieve handleiding en live code-tester voor **CustomTkinter**, gebouwd in Python met behulp van CustomTkinter zelf en `CTkListbox`.

Met deze applicatie kun je snel de belangrijkste widgets, globale stijlen en core logica van CustomTkinter opzoeken, de documentatie bekijken én de voorbeeldcode direct live testen in een apart pop-upvenster—zonder dat je bestanden hoeft op te slaan!
![CustomTkinter Manual in actie](docs/CTK_Interactive Manual.png)
---

## ✨ Kenmerken

* **Overzichtelijk & Gestructureerd:** Gecategoriseerd in *Globale Stijlen*, *Core & Logica* en *Widgets*.
* **Live Code Uitvoeren:** Pas code direct aan in het scherm en klik op **▶ Run Code** om het resultaat onmiddellijk te zien.
* **Geen Rommel:** Voorbeelden openen netjes als geïsoleerde pop-ups (`CTkToplevel`) boven je applicatie (`-topmost`), zonder tijdelijke bestanden aan te maken.
* **Grote & Leesbare Fonts:** Geoptimaliseerd met comfortabele lettergroottes voor zowel beschrijvingen als codeblokken.

---

## 📦 Vereisten

Voordat je de code kunt starten, heb je Python nodig samen met de volgende bibliotheken:

```bash
pip install customtkinter CTkListbox Pillow

```

---

## 🚀 Aan de slag

1. Clone deze repository of download de broncode:
```bash
git clone https://github.com/binairsnake/customtkinter-interactive-manual.git
cd customtkinter-interactive-manual

```


2. Start de applicatie:
```bash
python main.py

```



---

## 🛠️ Inbegrepen Onderwerpen

* **Globale Stijlen:** Thema's (`Dark`, `Light`, `System`), accentkleuren en schaling.
* **Core & Logica:** Layout managers (`pack`, `grid`, `place`), Variabelen (`StringVar`), Event Binding (`.bind`) en Timers (`.after`).
* **Widgets & Componenten:**
* `CTkButton`, `CTkLabel`, `CTkEntry`, `CTkTextbox`
* `CTkCheckBox`, `CTkRadioButton`, `CTkSwitch`, `CTkSlider`, `CTkSegmentedButton`
* `CTkOptionMenu`, `CTkComboBox`, `CTkProgressBar`
* `CTkFrame`, `CTkScrollableFrame`, `CTkTabview`


* **Geavanceerd:** `CTkToplevel`, `CTkImage`, `CTkFont`.

---

## 🤝 Bijdragen (Contributing)

Heb je een verbetering, zie je een bug, of wil je een ontbrekend widget-voorbeeld toevoegen? Pull requests zijn van harte welkom!

1. Fork het project
2. Maak je eigen feature branch (`git checkout -b feature/NieuweWidget`)
3. Commit je wijzigingen (`git commit -m 'Voeg CTkScrollbar voorbeeld toe'`)
4. Push naar de branch (`git push origin feature/NieuweWidget`)
5. Open een Pull Request

---

## 📄 Licentie

Dit project is open-source en beschikbaar onder de [MIT License](https://www.google.com/search?q=LICENSE).

---
