# Sic Mundus Creatus Est

(Titel geklaut von der Netflix Serie "Dark")

Zuerst muss ich beim Lesen der Aufgabe schmunzeln, und frage mich, ob ihr Flask tatsächlich im Einsatz habt, oder ob ihr das gewählt habt, weil es in meinem Lebenslauf *nicht* auftaucht ;)

Vom Namen her habe ich es allerdings schon mal kurz gehört. Ein kurzes googeln ergibt dann auch gleich: ein "pythonic Frontend Framework". Frontend? Hm, na gut, wahrscheinlich werdet ihr Flask zur Implementierung von http-fähigen Aufruf-Endpunkten (aka "Webservice" oder "REST API") verwenden.

Als nächstes frage ich mich, was ihr konkret mit "nicht blockierend" meint. Einfach nur multi-threaded, so dass ein laufender Request den nächsten nicht blockiert? Oder tatsächlich so, dass die Request-Bearbeitung asynchron in einem eigenen Thread erfolgt? Normalerweise würde ich jetzt erstmal die Diskussion suchen, um herauszufinden, ob die sich aus Asynchronität ergebende, erheblich höhere Komplexität (sowohl beim Service wie auch beim Aufrufer) für den Usecase erforderlich ist. Häufig habe ich unnötige Verwendung von Asynchronität gesehen, und dabei kommt gewöhnlich nichts Gutes heraus.

Da aber vielleicht ein multithreaded Webservice für die Bearbeitungszeit von 1-2h etwas wenig ist (allerdings die Implementierung eines asynchronen Service etwas viel), entscheide ich mich, "nonblocking" als "asynchron" zu verstehen.

Zur (natürlichen) Sprache gab es keine Vorgaben. Da für mich Softwareentwicklung aber irgendwie naturgegeben englisch ist, entscheide ich mich dafür, grösstenteils dabei zu bleiben. Also für alles zu verwenden, außer der Aufgabenstellung und diesem "MakingOf" (oh, ein kleines Paradox ;) ).

Ich denke mir ein Problem aus: Es soll einen "Zoo Webservice" geben. Als Argument kann man ein Tierart angeben, und der Webservice sagt einem nach einer gewissen "Ermittlungsphase", wie diese Tiere gerade drauf sind. Das Beispiel ist vielleicht simpel genug, so dass ich nicht zu viel Zeit in unnötigen Details vergeude. Meinen Fokus lege ich nicht so sehr auf die möglichst optimale Verwendung von Flask, was ich unter "echten" Umständen erstmal ausführlich erforschen würde. Das ist 1-2 Stunden nicht machbar. Eher möchte ich den Fokus auf die Implementierung eines pragmatischen, lehrbuchartigen Beispiels für asynchrone Programmierung legen.

Dann schaue ich gleich mal nach Testbarkeit und entdecke direkt `pytest-flask`. Keine große Überraschung, Flask ist ja auch recht verbreitet.

Ein einfaches "Gerüst" für das Projekt habe ich schon angelegt, und zur Entwicklung werde ich VScode verwenden, weil es so schön praktisch ist (Respekt Microsoft, obwohl ich euch misstraue ;) ).

Nebenher lasse ich ein Script mitlaufen, welches alle 30 Minuten den aktuellen Stand committed. Vielleicht kann man ja daraus ein bisschen den zeitlichen Verlauf meiner Herangehensweise sehen.

Meine insgesamte Bearbeitungszeit würde ich (nach Abzug großzügiger Pausen, ich habe ja Urlaub ;) ) auf 3-4 Stunden schätzen.

Umfangreiche - und in einem echten Projekt unverzichtbare - `pytest-flask` Tests habe ich aus Zeitgründen vernachlässigt, da seine Verwendung sich mir nicht unmittelbar erschlossen hat.

Nachtrag: Ich habe heute (2021-07-08) aus reinem Selbstinteresse und als Notiz für mein zukünftiges Ich noch einige `pytest-flask` Tests ergänzt. Flask scheint mir ein sehr gutes Konzept zu sein, welches mir in Zukunft sicher wieder begegnen wird.
