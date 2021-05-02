#### README

## Mr. Butts vs Gravity

Mr. Butts vs Gravity on yksinkertainen loputtomiin jatkuva tasohyppelypeli. Siinä on jatkuvasti liikkuva kenttä, joka tuottaa edetessään lisää tasoja ja vaaratekijöitä. Pelissä on kolme eri hahmoa, joilla on erilaiset tavat liikkua kentässä. Peli muuttuu haastavammaksi ajan myötä ja päättyy lopulta kun pelaajan hahmo osuu viholliseen, jolloin pelaaja näkee kerryttämänsä pisteet.

--------------------------------------------------------------------------------------------------------------------

[Release](https://github.com/aejmmark/ot-harjoitustyo/releases/tag/viikko5)

[Käyttöohje](https://github.com/aejmmark/ot-harjoitustyo/tree/master/dokumentaatio/kaytto-ohje.md)

[Arkkitehtuuri](https://github.com/aejmmark/ot-harjoitustyo/tree/master/dokumentaatio/arkkitehtuuri.md)

[Vaatimusmäärittely](https://github.com/aejmmark/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/aejmmark/ot-harjoitustyo/blob/master/dokumentaatio/tyoaika.md)

--------------------------------------------------------------------------------------------------------------------

Peli edellyttää että [poetry](https://python-poetry.org/docs/#installation) on asennettuna ja Pythonin versio on vähintään 3.6


### riippuvuuksien asentaminen:

    poetry install

### pelin käynnistäminen:

    poetry run invoke

### pelin testaus:

    poetry run invoke test

### pelin testikattavuus:

    poetry run invoke coverage-report

raportin löytää /hmtlcov/index.html

### pylint:

    poetry run invoke lint

tarkistukset määritelty [.pylintrc](https://github.com/aejmmark/ot-harjoitustyo/blob/master/.pylintrc)