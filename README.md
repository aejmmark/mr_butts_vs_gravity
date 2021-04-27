#### README

## Mr. Butts vs Gravity

Mr. Butts vs Gravity on yksinkertainen loputtomiin jatkuva tasohyppelypeli, joka tuottaa jatkuvasti lisää tasoja ja vaaratekijöitä. Pelaaja voi liikkua oikealle tai vasemmalle painamalla nuolinäppäimiä. Lisäksi pelaaja voi hypätä painamalla välilyöntiä. Tämä on mahdollista toistaa kerran ennen kuin hahmo osuu maahan. Peli muuttuu edetessään haastavammaksi ja päättyy lopulta kun pelaajan hahmo osuu piikkeihin.

--------------------------------------------------------------------------------------------------------------------

[Release](https://github.com/aejmmark/ot-harjoitustyo/releases/tag/viikko5)

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