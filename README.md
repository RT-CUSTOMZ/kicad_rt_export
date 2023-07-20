# KiCad manufactoring data exporter

Kleines Script um alle im Labor notwendigen Produktionsdaten zu erzeugen.
Für das Erstellen weiterer Dokumentation bitte mit
[InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom) verwenden.

Basiert auf dem InteractiveHtmlBom Projekt.

## KiCad 5

Das Plugin funktioniert unter KiCad 7.0 sowie KiCad 6.0, für KiCad 5 muss die mit dem *Tag* `kicad-5.x` versehene Version verwendet werden.

(im Dropdown unter *tags* `kicad-5.x`, anstatt `master`, auswählen  )

## Installation

### Installationspfad finden

Der Ordner ist je nach Betriebssystem / Installationsmethode unterschiedlich. In KiCad "PCB Editor" öffnen, unter Tools/Werkzeuge -> Externe Plugins -> Ordner öffnen.

Beispielpfade:

* Windows

  * %APPDATA%/kicad/6.0/scripting/plugins

* Linux

  * ~/.local/share/kicad/6.0/scripting/plugins

* MacOS

  * ~/Library/Application Support/kicad/6.0/scripting/plugins 

### Installation

Repository in entsprechende Ordner clonen/entpacken.

Danach in KiCad unter Tools/Werkzeuge -> Externe Plugins -> Plugins aktualisieren.

In der Toolbar sollte ein Icon erscheinen.
