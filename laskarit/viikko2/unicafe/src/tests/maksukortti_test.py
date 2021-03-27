import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortin_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2)
        self.assertEqual(str(self.maksukortti), "saldo: 0.12")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(str(self.maksukortti), "saldo: 0.08")

    def test_saldo_ei_muutu_jos_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(12)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_palauttaa_true_jos_rahat_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2), True)

    def test_palauttaa_false_jos_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(12), False)