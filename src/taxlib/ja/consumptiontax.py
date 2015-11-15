# -*- coding: utf-8 -*-
import math
from enum import Enum
from decimal import Decimal
from datetime import datetime
from zope.interface import (
    Interface,
    implementer,
    )

POINT_TAKESHITA = datetime(1989, 4, 1, 0, 0, 0)  # Takeshita, Takeshita
POINT_HASHIMOTO = datetime(1997, 4, 1, 0, 0, 0)  # Murayama, Hashimoto
POINT_ABE = datetime(2014, 4, 1, 0, 0, 0)  # Noda, Abe


class ConsumptionTaxRate(object):
    def __init__(self, now_=None, now_factory=datetime.now):
        self._now = now_ if now_ is not None else now_factory()

    def __call__(self, now_=None):
        u"""Return consumption tax rate"""
        _now = self._now if now_ is None else now_
        if _now < POINT_TAKESHITA:
            return Decimal('0')
        elif POINT_TAKESHITA <= _now < POINT_HASHIMOTO:
            return Decimal('0.03')
        elif POINT_HASHIMOTO <= _now < POINT_ABE:
            return Decimal('0.05')
        elif POINT_ABE <= _now:
            return Decimal('0.08')
        else:
            assert False, 'Invalid datetime: {}'.format(self._datetime)  # noqa


class IRoundMode(Interface):
    def __call__(self, price):
        return Decimal()


@implementer(IRoundMode)
class RoundDownMode(object):
    def __call__(self, price):
        return Decimal(math.floor(price))


@implementer(IRoundMode)
class RoundOffMode(object):
    def __call__(self, price):
        return Decimal(round(price))


@implementer(IRoundMode)
class RoundUpMode(object):
    def __call__(self, price):
        return Decimal(math.ceil(price))


class RoundMode(Enum):
    down = RoundDownMode
    off = RoundOffMode
    up = RoundUpMode


class ConsumptionTax(object):
    def __init__(self, datetime=None, mode=None):
        self._get_rate = ConsumptionTaxRate(datetime)
        self._mode = mode() if mode is not None else RoundMode.down.value()

    def rate(self, now_=None):
        return self._get_rate(now_)

    def __call__(self, price, now_=None):
        return self._mode(price * self.rate(now_))

    def total(self, price, *args, **kwds):
        return price + self(price)


def includem(config):
    reg = config.registry
    for mode in RoundMode:
        reg.registerUtility(mode.value(), IRoundMode, mode.name)
