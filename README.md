# Flask Service

## Aufgabe

Erläutern Sie die Erstellung eines non-blocking Flask Services. Hierbei können alle Tools und libraries der GNU/Linux oder Python Welt benutzt werden. Beachten Sie bitte auch Sicherheitsaspekte.

Zur Abnahme sollte eine kurze Erklärung der eingesetzten Tools, die oberflächliche Zusammenarbeit dieser Tools und eine Route des Flasks als Programmcode vorliegen, der ausführbar ist. (KISS)

## Rahmenbedingungen

- Bitte die Aufgabe selbstständig und allein lösen, natürlich darf dabei Literatur und / oder das Internet benutzt werden.
- Bitte teilen Sie uns Ihre Bearbeitungszeit mit.
- Die Lösung hätten wir gern als GitHub Projekt.
- Die Programmiersprache ist Python.
- Das Resultat muss von uns gebaut und ausgeführt werden können. Bitte entsprechende build-scripte oder Makefiles bereitstellen.
- Eigene Annahmen und wichtige Implementierungsdetails bitte klar kommentieren.
- Eventuelle sinnvolle Zwischenergebnisse dürfen gern als separater Git commit vorliegen.

Genauso wichtig wie das lauffähige Programm ist die Dokumentation (readme und code comments) der Lösungsidee und der einzelnen Programmteile und Tests. Das Hauptziel ist es, dass wir erleben, wie Sie Software in einem professionellen Umfeld entwickeln. Die gesamte Bearbeitungsdauer sollte max. 1-2 Stunden sein.

## Install

python3 -m venv venv
. venv/bin/activate

## Tests

Simple unit tests as well as algorithm-correctness tests are performed using pytest. To run

  1. `pip install pytest`
  1. `pytest -v`
