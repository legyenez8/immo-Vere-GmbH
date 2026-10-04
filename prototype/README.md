# Schlafzeit.de – kattintható ajánlati prototípus (V2)

Önálló, statikus demó a „Schlafzeit.de” panzió (Fürth) ajánlatához. Egyetlen HTML-fájl, build-lépés nélkül.

- **Weboldal** (DE/EN): hero foglalósávval, szobák élő szabad-szoba-jelzéssel a kiválasztott időszakra, „Für wen”, reggeli (Der Beck szemben), elhelyezkedés valós távolságokkal és térképpel, GYIK, kapcsolat, Impressum helyőrzőkkel.
- **Foglalás** 5 lépésben + visszaigazolás:
  1. Dátumok: érkezés és távozás külön szerkeszthető, a naptár a kiválasztott hónapnál nyílik.
  2. Vendégek és szobák: ágytípusonként, elérhetőség szerint korlátozva.
  3. Tarifa.
  4. Adatok.
  5. Fizetés-szimuláció.

  Visszalépéskor minden adat megmarad.
- **Verwaltung (admin)**:
  - Mai foglaltság, érkezők és távozók, új online foglalások.
  - Foglaltsági terv: csoportosított több szobás foglalások, keresés, hetes lapozás.
  - Foglaláslista szűrőkkel.
  - Árak és szabályok: csak az új ajánlatokra hatnak.
  - Telefonos foglalás, check-in/out, sztornó visszatérítés-számítással.
- **Demo-sáv és Präsentation-panel**: 5 lépéses bemutatási útvonal, „Zurücksetzen” ismert kiinduló állapotra.

A weboldal és az admin közös demo-állapotot használ (böngésző `localStorage`, kulcs: `sz-v2-state`). Az állapot naponta automatikusan újraindul.

## Indítás

```bash
cd prototype
python3 -m http.server 8000
# http://localhost:8000
```

Közvetlen linkek: `#buchen` (foglalás), `#verwaltung` (admin), `#praesentation` (bemutató-panel).

## Egyfájlos változat (továbbküldéshez)

```bash
python3 prototype/tools/standalone.py schlafzeit-demo-v2.html
```

A fotók és a betűtípusok beágyazva, így internet nélkül is működik, kb. 2 MB. Ha a betűtípusok letöltése a build közben nem sikerül, a fájl a Google Fonts-linket tartja meg.

## Ami demó / helyőrző

- **Fotók:** Unsplash-helyőrzők, lásd `assets/CREDITS.md`.
- **Árak:** EZ 55 €, DZ 65 € szobánként és éjszakánként. A referencia (central-hbf.de) ára EZ 57 €-tól, DZ 66 €-tól, és ott van reggeli.
- **Foglalások:** minta-adatok. A fizetés, az e-mail és a számla csak szimuláció („Rechnung · MUSTER”).
- **Ágyak:** a 10 DZ-ből 5 franciaágyas és 5 kétágyas (demó-felosztás).
- **Feltételek:** 48 órás ingyenes lemondás, 14:00 / 11:00 és a 10 %-os kedvezmények mind javaslatok, a felületen „Beispielkonditionen” jelöléssel. A vendégoldal nem állít be- és kijelentkezési időt.
- **Cégadatok:** az Impressumban, a telefonszámnál és az adószámoknál a hiányzó adatok „folgt” jelöléssel állnak.

## Valós adatok

- **Cím:** Hans-Vogel-Str. 45, 90765 Fürth (Poppenreuth).
- **Pékség:** Der Beck, Hans-Vogel-Str. 30. Forrás: OpenStreetMap.
- **Buszmegálló:** Strudelweg, kb. 200 m.
- **Távolságok és autós menetidők:** OSRM-útvonaltervezés alapján, felfelé kerekítve.
