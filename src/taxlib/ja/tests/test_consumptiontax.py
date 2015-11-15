# -*- coding: utf-8 -*-
from unittest import TestCase
from decimal import Decimal


class ConsumptionTaxTest(TestCase):
    def test_tax(self):
        from ..consumptiontax import ConsumptionTax
        tax = ConsumptionTax()
        self.assertEqual(tax(1000), Decimal('80'))

    def test_total(self):
        from ..consumptiontax import ConsumptionTax
        tax = ConsumptionTax()
        self.assertEqual(tax(1000), Decimal(80))
        self.assertEqual(tax.total(1000), Decimal('1080'))
