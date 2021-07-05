# Sic Mundus Creatus Est

(Titel geklaut von der Netflix Serie "Dark")

Zuerst muss ich beim Lesen der Aufgabe schmunzeln, und frage mich, ob ihr Flask tatsächlich im Einsatz habt, oder ob ihr das gewählt habt, weil es in meinem Lebenslauf /nicht/ auftaucht ;)

Vom Namen her habe ich es allerdings schon mal kurz gehört. Ein kurzes googeln ergibt dann auch gleich: ein "pythonic Frontwnd Framework". Frontend? Hm, na gut, wahrscheinlich werdet ihr Flask zur Implementierung von http-fähigen Aufruf-Endpunkten (gerne ja auch "Webservice" oder "REST API" genannt) verwenden.

Als nächstes frage ich mich, was ihr konkret mit "nicht blockierend" meint. Einfach nur multi-threaded, so dass ein laufender Request den nächsten nicht blockiert? Oder tatsächlich so, dass die Request-Bearbeitung asynchron in einem eigenen Thread erfolgt? Normalerweise würde ich jetzt erstmal die Diskussion suchen, um herauszufinden, ob die erheblich höhere Komplexität (sowohl bei der Implementierung wie auch beim Aufrufer) das wert ist. Häufig habe ich unnötige Verwendung von Asynchronität gesehen, und dabei kommt gewöhnlich nichts Gutes heraus.

Da aber vielleicht ein multithreaded Webservice für die Bearbeitungszeit von 1-2h etwas wenig ist (allerdings die Implementierung eines asynchronen Service etwas viel), entscheide ich mich, "nonblockinh" als "asynchron" zu verstehen.

Zur Sprache gab es keine Vorgaben. Da für mich Softwareentwicklung aber irgendwie naturgegeben englisch ist, entscheide ich mich dafür, grösstenteils dabei zu bleiben. Also für alles zu verwenden, außer der Aufgabenstellung und diesem "MakingOf" (oh, ein kleines Paradox ;) ).
