import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)
        self.maksukortti_konkurssi = Maksukortti(100)

    def test_kassassa_oikea_aloitussumma(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_alkuun_0_edulliset(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassassa_alkuun_0_maukkaat(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kateisella_lisaa_kassaan_oikean_summan_jos_rahat_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_lisaa_maukkaiden_maaraa_jos_rahat_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_vaihtoraha_oikein_jos_rahat_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_syo_maukkaasti_kateisella_ei_lisaa_kassaan_oikean_summan_jos_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_ei_lisaa_maukkaiden_maaraa_jos_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kateisella_kaikki_palautetaan_vaihtorahana_jos_rahat_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_syo_edullisesti_kateisella_lisaa_kassaan_oikean_summan_jos_rahat_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_lisaa_maukkaiden_maaraa_jos_rahat_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_vaihtoraha_oikein_jos_rahat_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_syo_edullisesti_kateisella_ei_lisaa_kassaan_oikean_summan_jos_rahat_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_ei_lisaa_maukkaiden_maaraa_jos_rahat_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_kateisella_kaikki_palautetaan_vaihtorahana_jos_rahat_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_syo_maukkaasti_kortilla_veloittaa_jos_rahat_riittaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_syo_maukkaasti_kortilla_palauttaa_true_jos_rahat_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_maukkaasti_kortilla_lisaa_maukkaiden_maaraa_jos_rahat_riittaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_ei_veloita_jos_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_konkurssi)
        self.assertEqual(self.maksukortti_konkurssi.saldo, 100)

    def test_syo_maukkaasti_kortilla_palauttaa_false_jos_rahat_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_konkurssi), False)

    def test_syo_maukkaasti_kortilla_ei_lisaa_maukkaiden_maaraa_jos_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_konkurssi)
        self.assertEqual(self.kassapaate.maukkaat, 0)  

    def test_syo_maukkaasti_kortilla_ei_vaikuta_kassaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)      

    def test_syo_edullisesti_kortilla_veloittaa_jos_rahat_riittaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 260)

    def test_syo_edullisesti_kortilla_palauttaa_true_jos_rahat_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_edullisesti_kortilla_lisaa_maukkaiden_maaraa_jos_rahat_riittaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_ei_veloita_jos_rahat_ei_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_konkurssi)
        self.assertEqual(self.maksukortti_konkurssi.saldo, 100)

    def test_syo_edullisesti_kortilla_palauttaa_false_jos_rahat_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_konkurssi), False)

    def test_syo_edullisesti_kortilla_ei_lisaa_maukkaiden_maaraa_jos_rahat_ei_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_konkurssi)
        self.assertEqual(self.kassapaate.edulliset, 0)        

    def test_syo_edullisesti_kortilla_ei_vaikuta_kassaan(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_kortille_lisaa_kassaan_oikean_summan(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_kortille_ei_voi_ladata_negatiivista(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 500)

