# Sic Mundus Creatus Est

(Titel geklaut von der Netflix Serie "Dark")

Zuerst muss ich beim Lesen der Aufgabe schmunzeln, und frage mich, ob ihr Flask tatsächlich im Einsatz habt, oder ob ihr das gewählt habt, weil es in meinem Lebenslauf /nicht/ auftaucht ;)

Vom Namen her habe ich es allerdings schon mal kurz gehört. Ein kurzes googeln ergibt dann auch gleich: ein "pythonic Frontwnd Framework". Frontend? Hm, na gut, wahrscheinlich werdet ihr Flask zur Implementierung von http-fähigen Aufruf-Endpunkten (gerne ja auch "Webservice" oder "REST API" genannt) verwenden.

Als nächstes frage ich mich, was ihr konkret mit "nicht blockierend" meint. Einfach nur multi-threaded, so dass ein laufender Request den nächsten nicht blockiert? Oder tatsächlich so, dass die Request-Bearbeitung asynchron in einem eigenen Thread erfolgt? Normalerweise würde ich jetzt erstmal die Diskussion suchen, um herauszufinden, ob die erheblich höhere Komplexität (sowohl bei der Implementierung wie auch beim Aufrufer) das wert ist. Häufig habe ich unnötige Verwendung von Asynchronität gesehen, und dabei kommt gewöhnlich nichts Gutes heraus.

Da aber vielleicht ein multithreaded Webservice für die Bearbeitungszeit von 1-2h etwas wenig ist (allerdings die Implementierung eines asynchronen Service etwas viel), entscheide ich mich, "nonblocking" als "asynchron" zu verstehen.

Zur Sprache gab es keine Vorgaben. Da für mich Softwareentwicklung aber irgendwie naturgegeben englisch ist, entscheide ich mich dafür, grösstenteils dabei zu bleiben. Also für alles zu verwenden, außer der Aufgabenstellung und diesem "MakingOf" (oh, ein kleines Paradox ;) ).

Ich denke mir ein Problem aus: Es soll einen "Zoo Webservice" geben. Als Argument kann man ein Tierart angeben, und der Webservice sagt einem nach einer geissen "Ermittlungsphase", was die Tiere gerade tun. Das Beispiel ist vielleicht simpel genug, so dass ich nicht zu viel Zeit in unnötigen Dateils vergeude. Die Dauer für die Ermittlung der Tätigkeit wird künstlich auf 10-20 Sekunden festgelegt. Man will später ja auch Stoff zum Testen haben.

Dann schaue ich gleich mal nach Testbarkeit und entdecke direkt `pytest-flask`. Keine große Überraschung, Flask ist ja auch recht verbreitet.

Ein einfaches "Gerüst" für das Projekt habe ich schon angelegt, und zur Entwicklung werde ich VScode verwenden, weil es so schön praktisch ist (Respekt Microsoft, obwohl ich euch misstraue ;) ).
