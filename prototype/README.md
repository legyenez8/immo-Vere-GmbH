# Schlafzeit.de – kattintható ajánlati prototípus

Önálló, statikus demó a „Schlafzeit.de” panzió (Fürth) ajánlatához. Egyetlen HTML-fájl, build-lépés nélkül.

- **Weboldal** (DE/EN): hero foglalósávval, szobák, „Für wen”, reggeli (Der Beck szemben), elhelyezkedés valós távolságokkal és térképpel, GYIK, kapcsolat, Impressum helyőrzőkkel.
- **Foglalási folyamat** 4 lépésben: dátumok (ár naptár), szobák (több szoba, ágytípus, flexibilis vagy spartarifa), vendégadatok, fizetés (PayPal, kártya Stripe-on, Apple Pay, Google Pay), azonnali visszaigazolás.
- **Admin (Verwaltung)**: foglaltsági terv 13 szobára, foglaláslista, árak és szabályok (élőben frissítik a weboldalt), telefonos foglalás felvétele, check-in, sztornó.

Az új online foglalás azonnal megjelenik az adminban: ez a bemutató csúcspontja.

## Indítás

```bash
cd prototype
python3 -m http.server 8000
# http://localhost:8000
```

Közvetlen linkek: `#buchen` (foglalás), `#verwaltung` (admin).

## Ami demó / helyőrző

- **Fotók:** Unsplash-helyőrzők, lásd `assets/CREDITS.md`.
- **Árak:** EZ 55 €, DZ 65 € éjszakánként. A referencia (central-hbf.de) ára EZ 57 €-tól, DZ 66 €-tól, és ott van reggeli.
- **Foglalások:** minta-adatok, minden csak a böngészőben él, nincs valódi fizetés és e-mail.
- **Ágyak:** a 10 DZ-ből 5 franciaágyas és 5 kétágyas (demó-felosztás).
- **Check-in és lemondás:** 14:00 / 11:00, illetve 48 órás ingyenes lemondás. Ezek javaslatok.
- **Cégadatok:** az Impressumban és a telefonszámnál a hiányzó adatok „folgt” jelöléssel állnak.

## Valós adatok

- **Cím:** Hans-Vogel-Str. 45, 90765 Fürth (Poppenreuth).
- **Pékség:** Der Beck, Hans-Vogel-Str. 30. Forrás: OpenStreetMap.
- **Buszmegálló:** Strudelweg, kb. 200 m.
- **Távolságok és autós menetidők:** OSRM-útvonaltervezés alapján, felfelé kerekítve.
