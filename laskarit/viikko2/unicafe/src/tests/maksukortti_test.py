import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahan_lataus_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_kortin_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_kortin_saldo_ei_muutu_jos_rahaa_ei_riittavasti(self):
        tulos = self.maksukortti.ota_rahaa(1200)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(tulos, False)
    
    def test_kortin_saldo_muuttuu_jos_rahaa_on_riittavasti(self):
        tulos = self.maksukortti.ota_rahaa(800)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(tulos, True)