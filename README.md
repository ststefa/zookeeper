# Flask Service

<!-- TOC depthfrom:2 depthto:4 -->

- [Aufgabse](#aufgabse)
- [Rahmenbedingungen](#rahmenbedingungen)
- [Notes](#notes)
- [Solution](#solution)
  - [Installation](#installation)
  - [Tests](#tests)
  - [Implementation](#implementation)
    - [Overview](#overview)
    - [Usage](#usage)
    - [Example](#example)
  - [Simplifications](#simplifications)

<!-- /TOC -->

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

## Notes

See <MakingOf.md> for additional thoughts on the exercise (german)

## Solution

### Installation

- (recommended) Create a python virtual environment for better separation:

      python3 -m venv venv
      . venv/bin/activate

- Install required python dependencies

      pip3 install -r requirements.txt

### Tests

Make sure you already set up the runtime requirements. To run test cases

- (recommended) Activate the python virtual environment (see above)

      . venv/bin/activate

- Install additional python development-time dependencies

      pip3 install -r requirements-dev.txt

Run the tests

    pytest

### Implementation

#### Overview

This implements a fictive "zookeeper service". It consists of a configurable list of animals with arbitrary "status" compiled from a list of - also configurable - words (see zookeeper.conf).

The purpose is to simulate an asynchronuous (aka non-blocking) processing of a workload. Animals can be listed - which returns information about available animals - and queried - which returns an approximation of their current status. Note that any query will result in a discrete status, even when invoked for the same animal multiple times.

#### Usage

The implementation runs as a foreground server process and is invoked by

    ./zookeper.py

There are not arguments. There is also no separate logfile, everything is written to regular unixen streams.

The endpoints of the service can be invoked by `curl` or any other HTTP request generator.

The "API" implements the following endpoints

`/animals`

  Return a list of available animals in the "zoo".

`/animals/<animal_name>`

Start a new and asynchronous query about the animals status. The endpoint will immediately return a UUID which can be used for querying the state of the computation. The "workload" will (deterministically) take 10-20 seconds to complete. A separate thread will be spawned for every invocation of this endpoint, regardless of animal. That is, the endpoint is intentionally *not* idempotent. However, the query is.

`/query/<uuid>`

If the "computation" is still in progress then the query will return "..." as the status. As soon as the computation is complete, the animals status will be shown instead.

#### Example

This shows an example use of the zookeeper service. Some output has been omitted for clarity.

```bash
$ ./zookeeperd.py &
[1] 76104

$ zkc() { curl http://localhost:5000${1} ; }

$ zkc /animals
["aardvarks","alpacas","bisons","crocodiles","elks","gorillas","hippos","koalas","kangaroos","lions","pandas","tigers","unicorns","zebras"]

$ zkc /animals/hippos
"424d60a6-f21a-4089-b828-23d123a62565"

$ zkc /query/424d60a6-f21a-4089-b828-23d123a62565
"..."

$ zkc /query/424d60a6-f21a-4089-b828-23d123a62565
"..."

$ zkc /query/424d60a6-f21a-4089-b828-23d123a62565
"Sleepy hippos eat wildly"
```

### Simplifications

For the sake of brevity, the implementation makes several simplifications which would probably be considered indispensable for a real world application:

- Threads are "managed" in a simple dictionary. A real implementation would implement some kind of thread management which allows for more control and observability of the runtime state.

- The use of `threading` would not be appropriate for compute-bound activities due to Pythons Global Interpreter Lock (GIL).

- There is no persistence.

- Logging would be pimped. Also, overall configurability (e.g. server port, config file) would be improved using argparse.

- Security is deemed irrelevant for this example. In a real-world implementation this would probably be added best by e.g.

  - Some kind of clever additional flask annotations (very likely such exists already)
  - Outsourcing the topic entirely to the embedding system, e.g. the invoking webserver which would act as a reverse proxy

- JSON structures would be used for HTTP responses consequently.

- Timing information would be added in several places.

- The wording of the implemented "REST API" did not receive much consideration time. I would usually consider this wording an important subject to spend a lot of time and discussion on with the goal to make it intuitive to use.

- Proper HTTP response code handling is not implemented
