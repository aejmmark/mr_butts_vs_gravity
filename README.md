#### README

## Escape from Dangerland

Escape from Dangerland on yksinkertainen tasohyppelypeli, jossa on toistaiseksi vain yksi testikenttä. Pelaaja voi liikkua oikealle tai vasemmalle painamalla nuolinäppäimiä. Lisäksi pelaaja voi hypätä painamalla välilyöntiä. Tämä on mahdollista toistaa kerran ennen kuin hahmo osuu maahan. Pelin voittaa saavuttamalla kentän huipulla olevan lipun.

[Vaatimusmäärittely](https://github.com/aejmmark/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/aejmmark/ot-harjoitustyo/blob/master/dokumentaatio/tyoaika.md)

--------------------------------------------------------------------------------------------------------------------

riippuvuuksien asentaminen:

    poetry install

pelin käynnistäminen:

    poetry run invoke

pelin testaus:

    poetry run invoke test

pelin testikattavuus:

    poetry run invoke coverage-report

raportin löytää /hmtlcov/index.html