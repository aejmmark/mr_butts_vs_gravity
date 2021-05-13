
## Testausdokumentti

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

### Yksikkö- ja integraatiotestaus

Testit on osittain toteutettu hyödyntämällä Game-luokkaan lisättyjä metodeja set_stage(), add_event() ja play_event(). Lisäksi pelisilmukassa on parametrinä ajastin, jonka avulla voidaan säätää kuinka kauan peli on kerrallaan käynnissä. Metodi set_stage() mahdollistaa kentän ja hahmon vaihtamisen. Metodi add_event() avulla voidaan peliin lisätä etukäteen syötteitä, joita play_event() aktivoi pelin pyöriessä. Kokonaisuus mahdollistaa eri tilanteiden ja syötteiden nopean automaattisen testauksen.

Testauksen haarautumiskattavuus on 75%

![](/dokumentaatio/kuvat/coverage.png)

Testaamatta jäi Display-luokan metodit ja niihin liittyvät Game-luokan metodit. Nämä keskittyvät pääosin ruudulle piirtämiseen, joten niiden testaaminen on tapahtunut manuaalisesti.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Järjestelmätestaus

Järjestelmätestaus on toteutettu manuaalisesti. Tähän on sisältynyt muun muassa käyttöliittymien toiminnallisuuksien ja visuaalisten osioiden testaus sekä pelin tasapainotus. Kaikki vaatimusmäärittelyssä ja käyttöohjeessa mainitut toiminallisuudet on testattu ja todettu toimiviksi. Testaus on tapahtunut Linux-ympäristössä.