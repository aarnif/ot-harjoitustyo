import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_myytyja_lounaita_nolla_kappaletta(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_toimii_kateisella_jos_rahaa_riittavasti(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(380)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(vaihtoraha, 140)

    def test_syo_maukkaasti_toimii_kateisella_jos_rahaa_riittavasti(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(540)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(vaihtoraha, 140)

    def test_syo_edullisesti_ei_toimi_jos_rahaa_ei_ole_riittävästi(self):
        maksu = 200
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(vaihtoraha, maksu)

    def test_syo_maukkaasti_ei_toimi_jos_rahaa_ei_ole_riittävästi(self):
        maksu = 300
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(vaihtoraha, maksu)

    def test_korttiosto_toimii_edullisen_lounaan_osalta_jos_rahaa_riittavasti(self):
        self.maksukortti = Maksukortti(1000)
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_maukkaan_lounaan_osalta_jos_rahaa_riittavasti(self):
        self.maksukortti = Maksukortti(1000)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_ei_toimi_edullisen_lounaan_osalta_jos_rahaa_ei_ole_riittavasti(self):
        self.maksukortti = Maksukortti(200)
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(tulos, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_ei_toimi_maukkaan_lounaan_osalta_jos_rahaa_ei_ole_riittavasti(self):
        self.maksukortti = Maksukortti(300)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(tulos, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladattaessa_kortin_ja_kassan_saldo_muuttuu_ladatulla_summalla(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    