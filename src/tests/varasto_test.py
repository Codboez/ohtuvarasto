import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus_nollataan(self):
        varasto = Varasto(-10)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_virheellinen_saldo_nollataan(self):
        varasto = Varasto(10, -10)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_ylimaarainen_saldo_alussa_poistetaan(self):
        varasto = Varasto(10, 20)

        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisatessa_negatiivista_saldoa_ei_muuteta(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisatessa_liikaa_ylijaama_poistetaan(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaessa_negatiivista_saldoa_ei_muuteta(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ottaminen_palauttaa_kaiken_ottaessa_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(maara, 5)

    def test_ottaessa_liikaa_saldo_nollataan(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varasto_muutetaan_merkkijonoksi_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")