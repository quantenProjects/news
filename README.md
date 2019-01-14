# news
random german news sources. Get out of your filterbubble

Man ruft https://quantenprojects.github.io/news/index.html auf und wird eine zufällige Nachrrichtenseite weitergeleitet.

## Kontrolle über die Nachrichtenseiten
Man kann mit einem Fragment-Identifier (das Ding nach dem #) einstellen, welche Kategorien in den Lostopf geschmissen werden sollen.

Dabei stehen aktuell zur Verfügung.

| Id | Kategorie                             |
|----|---------------------------------------|
| tr | regionale Tageszeitungen              |
| tu | überregionale Tageszeitungen          |
| wr | regionale Wochenzeitungen             |
| wu | überregionale Wochenzeitungen         |
| m  | "Magazine", aktuell Spiegel und Stern |

Dabei wurden alle Daten bis auf die letzte Kategorie von [Wikipedia](https://de.wikipedia.org/w/index.php?title=Liste_deutscher_Zeitungen&oldid=183702454) übernommen.

Man kann mehrere Kateogrien auswählen und auch einzelne mehrfach in den Lostopf werfen.

Die formale Syntax sieht so aus:

`https://quantenprojects.github.io/news/index.html#(Id[:n],)*`

Wobei `Id` der Identifier aus der oberen Tabelle ist und `n` die Anzahl wie häufig es in den Lostop geworfen wird.

### Beispiele

* alle überregionalen Zeitungen und die Magazine (aktuell Standard, wenn nicht angegeben wird)
https://quantenprojects.github.io/news/index.html#tu,wu,m
* alle überregionalen Wochenzeitungen und die Magazine mit 10-facher Chance https://quantenprojects.github.io/news/index.html#wu,m:10
* nur regionale Tageszeitungen https://quantenprojects.github.io/news/index.html#tr 