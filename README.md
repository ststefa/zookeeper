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

- (recommended) Create a python virtual environment for better separation:

      python3 -m venv venv
      . venv/bin/activate

- Install required python dependencies

      pip3 install -r requirements.txt

## Tests

Make sure you already set up the runtime requirements. To run test cases

- (recommended) Activate the python virtual environment (see above)

      . venv/bin/activate

- Install additional python development-time dependencies

      pip3 install -r requirements-dev.txt

Run the tests

    `pytest -v`

## Simplification

For the sake of brevity, the implementation makes several simplifications which would probably be considered indispensable for a real world application:

- Threads are managed in a simple dictionary. A real implementation would implement some kind of thread management which allows for more control and observability of the runtime state

- The use of `threading` is not appropriate for compute-bound activities due to Pythons Global Interpreter Lock (GIL).

- There is no persistence

- Logging would be pimped. Also, overall configurability would be increased (e.g. server port)

- Security is deemed irrelevant for this example. In a real-world implementation this would probably be added best by e.g.

  - Some kind of clever code annotations
  - Outsourced entirely to the embedding system, e.g. the invoking webserver
