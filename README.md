# Django Tutorial

Willkommen zu deinem Django-Tutorial! Dieses Repository dient als Basis für unseren Einstieg in Django. In diesem Repository ist eine Entwicklungsumgebung vorkonfiguriert, damit Du Dich voll auf das Lernen von Django konzentrieren kannst.

---

## 🚀 Schnellstart

Folge diesen Schritten, um deine eigene Arbeitsumgebung zu erstellen:

### 1. Repository kopieren
Klicke oben rechts auf auf den grünen Button:
<br>
<a href="#" style="background-color: #2ea44f; color: white; padding: 6px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block; pointer-events: none;">Use this template</a>
<br>
*(Wähle "Create a new repository" und gib ihm einen Namen, z. B. `django-tutorial-01`.)*

### 2. Codespace starten
In deinem **neuen** Repository klickst Du auf den grünen **Code**-Button, wechselst zum Reiter **Codespaces** und klickst auf:

<a href="#" style="background-color: #2ea44f; color: white; padding: 6px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block; pointer-events: none;">Create codespace on main</a>
<br>
*Der Aufbau dauert ca. 1–2 Minuten. Sobald das Terminal bereit ist, kannst Du loslegen.*

## 🛠️ Enthaltene Werkzeuge

* **[uv](https://astral.sh/uv)**: Unser moderner Paketmanager. Er erstellt automatisch deine virtuelle Umgebung (`.venv`) und hält alle Abhängigkeiten aktuell.
* **[SQLite IntelliView](https://marketplace.visualstudio.com/items?itemName=bowlerr.sqlite-intelliview-vscode)**: Klicke links im Explorer einfach auf `db.sqlite3`. Es öffnet sich eine grafische Ansicht, in der Du deine Daten (wie Tabellen und Einträge) direkt einsehen kannst.
* **[Ruff](https://astral.sh/ruff)**: Ein extrem schneller Linter und Formatter. Er korrigiert Deinen Code automatisch beim Speichern, damit wir nicht über Einrückungen o.ä. diskutieren müssen.

---

## 📖 Wichtige Befehle (ab Kapitel 3)

| Aktion | Befehl |
| :--- | :--- |
| **Server starten** | `uv run python manage.py runserver` |
| **Migrationen erstellen** | `uv run python manage.py makemigrations` |
| **Migrationen anwenden** | `uv run python manage.py migrate` |
| **Superuser (Admin) anlegen** | `uv run python manage.py createsuperuser` |
| **Pakete synchronisieren** | `uv sync` |

---

## 🛠️ Fehlersuche (Troubleshooting)

### 1. "Mein Kontingent ist erschöpft" (GitHub Quota)
GitHub bietet ein monatliches Gratis-Limit für Codespaces. Wenn dieses voll ist, kannst Du keinen neuen Container starten.
* **Lösung:** Lösche ungenutzte Codespaces unter [github.com/codespaces](https://github.com/codespaces).
* **Tipp:** Beende Deinen Codespace immer über das blaue Menü unten links (*Stop Current Codespace*), wenn Du fertig bist.

### 2. "Port 8000 wird bereits verwendet"
Das passiert, wenn ein alter Server-Prozess nicht richtig beendet wurde.
* **Lösung:** Drücke `Strg + C` im Terminal. Falls das nicht hilft, nutze `fuser -k 8000/tcp` oder starte Django auf einem anderen Port:
    `uv run python manage.py runserver 8080`

### 3. Keine Anzeige in SQLite IntelliView
Du hast Daten geändert, aber die Tabelle in VS Code sieht leer aus oder zeigt alte Werte.
* **Lösung:** Klicke in der IntelliView-Tab-Leiste oben auf den **Refresh-Button** (das Kreispfeil-Symbol). Die Ansicht aktualisiert sich nicht automatisch bei jedem Datenbank-Schreibvorgang.

### 4. Rote Wellenlinien im Code
Manchmal verliert VS Code die VerbinDung zur virtuellen Umgebung.
* **Lösung:** Drücke `Strg + Shift + P`, tippe `Developer: Reload Window` und bestätige. Meistens erkennt Pylance den Interpreter danach sofort wieder korrekt.

### 5. "Command not found: uv"
Sollte `uv` im Terminal nicht erkannt werden, ist der Container noch im Setup-Prozess oder wurde fehlerhaft erstellt.
* **Lösung:** Warte kurz ab. Wenn es nach 2 Minuten nicht geht, erstelle den Codespace neu (über den "Code"-Button -> drei Punkte -> *New with options*).

---

> [!IMPORTANT]
> Arbeite immer innerhalb des Terminals, in dem am Zeilenanfang `(django-intro)` steht. Nur dann sind alle installierten Pakete für Python sichtbar!
