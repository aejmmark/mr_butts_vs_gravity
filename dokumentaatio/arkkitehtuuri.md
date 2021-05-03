## Arkkitehtuuri
------------------------------------------------------------------------------------------------------------------
### Rakenne

![](/dokumentaatio/kuvat/structure.png)

* index - käynnistää sovelluksen
* game - sisältää pelin perustoiminnallisuudet kuten peliä pyörittävän silmukan ja sen tärkeimmät osat.
* display - ikkunaan piirtämiseen ja pistetauluun liittyvät toiminnallisuudet.
* stage - kentän liikuttaminen ja olioiden tuottaminen
* effects - poweruppien toiminta ja ajastimet
* sprites - pelaajan hahmo, tasot, viholliset, powerupit
* movement - pelaajan hahmon liikkuminen ja törmäykset
* constants - sisältää luokkien käyttämät vakiot

--------------------------------------------------------------------------------------------------------------------
### Sovelluslogiikka

![](/dokumentaatio/kuvat/packages.png)

Pelin päätoiminnallisuus perustuu silmukkaan, joka pyörittää pelin kolmea päämetodia niin kauan kun peli on käynnissä.
* events() - tarkistaa pelaajan syötteet ja reagoi niihin
* update() - päivittää kaikkien liikkuvien osien sijainnit ja tarkistaa törmäykset
* render() - piirtää taustan, tekstit ja oliot ikkunaan

Pelissä on tulostaulu, joka säilötään tiedostoon highscore.csv. Pelin päätteeksi Display noutaa pisteet ja päivittää uuden tuloksen tiedostoon.

--------------------------------------------------------------------------------------------------------------------
### Pelisilmukka

![](/dokumentaatio/kuvat/events.png)

Sovelluksen eteneminen kun pelaaja on painanut välilyöntiä, mikä on johtanut tasolla olevan hahmon(Mr. Butts) hyppäämiseen. Silmukka käy läpi jokaisen listalla olevan syötteen ja vertaa niitä ehtolauseisiin. Välilyönnin kohdalla syöte täsmää. Tässä kohtaa tarkistetaan vielä onko hahmon kykyyn liittyvä powerup käynnissä. Vastaus on negatiivinen, mutta se ei tässä tapauksessa vaikuta. Peli kutsuu metodia ability(), joka taas hahmon perusteella kutsuu metodia jump().

![](/dokumentaatio/kuvat/update.png)

Update()-metodi pelin oletustilassa. Update() kutsuu metodia stagen metodia scroll(), joka liikuttaa kaikkia kentän olioita vasemmalle. Samalla se kutsuu metodia generate(), joka tarkistaa onko taso- ja vihollislistojen koko pienentynyt ja lisää kentän oikeaan reunaan lisää, mikäli näin on tapahtunut. Jokaisen uuden olion kohdalla se kutsuu vielä metodia check_overlap(), joka tarkistaa etteivät oliot ole päällekkäin. Lopuksi generate() vielä lisää kenttään powerupin, mikäli ajastimen arvo täsmää.
Tämän jälkeen update() käy jokaisen all_sprites-listalla olevan olion läpi ja kutsuu metodia update(). Pelaajan kohdalla se kutsuu edelleen movementin metodia move(), mikä laskee ja päivittää pelaajan senhetkisen sijainnin ja nopeuden. Muiden olioiden kohdalla se päivittää niiden sijainnin ja poistaa ne mikäli ne ovat ikkunan vasemmalla puolella.
Platform_collision()-metodilla tarkistetaan pelaajan ja tasojen yhteentörmäykset ja pysäytetään pelaaja näin sattuessa. Tämän jälkeen vielä tarkistetaan törmäykset poweruppien ja vihollisten kanssa. Lopuksi vielä liikutetaan mahdollisen powerupin ajastinta.

![](/dokumentaatio/kuvat/render.png)

Game-luokan metodi render() kutsuu Display-luokan(disp) samannimistä metodia. Tämä täyttää ikkunan valkoisella pygame.displayn metodilla fill(). Sitten se piirtää parametrina saadusta listasta jokaisen olion ikkunaan. Tämän jälkeen se kirjoittaa pistetuloksen ja mahdollisen powerup ajastimen ikkunaan käyttäen draw_text()-metodia. Lopuksi se päivittää muutokset pygame.displayn metodilla update()
