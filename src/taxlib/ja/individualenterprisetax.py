# -*- coding: utf-8 -*-
u"""Individual Enterprise Tax

事業所得又は（及び）不動産所得
(1)
＋
所得税の事業専従者給与（控除）額
－
個人の事業税の事業専従者給与（控除）額
(2)
＋
青色申告特別控除額
(3)
－
各種控除額
(4)
）×
税率
＝
税額

（1）事業所得又は（及び）不動産所得
　前年の１月1日から１２月３１日までの１年間の事業から生じた事業所得又は（及び）不動産所得で、事業の総収入金額から必要経費、青色申告特別控除額等を控除して計算します。所得税の確定申告書第1表及び青色申告決算書、収支内訳書の所得金額欄の金額が当該所得です。（ただし、雑所得が課税の対象となる場合もあります。）

（2）個人の事業税の事業専従者給与(控除)額
　事業主と生計を一にする親族の方が専らその事業に従事するときは、一定額を必要経費として控除できます。
・青色申告の場合･････その給与支払額（所得税の事業専従者給与）
・白色申告の場合･････配偶者の場合は８６万円、その他の方の場合は１人５０万円が限度

（3）青色申告特別控除額
　個人の事業税には青色申告特別控除の適用はありませんので、所得金額に加算します。

（4）各種控除額
① 繰越控除
　次の控除を受けるには、原則として、所得税、住民税、事業税のいずれかの申告を一定の期限内に毎年行っていることが必要です。
（ア）損失の繰越控除
　青色申告者で、事業の所得が赤字（損失）となったときは、翌年以降３年間、繰越控除ができます。

（イ）被災事業用資産の損失の繰越控除
　白色申告者で、震災、風水害、火災などによって生じた事業用資産の損失の金額があるときは、翌年以降３年間、繰越控除ができます。

（ウ）譲渡損失の控除と繰越控除
　直接事業の用に供する資産（機械、装置、車両等。ただし、土地、家屋等を除く。）を譲渡したために生じた損失額については、事業の所得の計算上、控除することができます。青色申告をした方は、翌年以降３年間、繰越控除ができます。

② 事業主控除
　控除額は、年間２９０万円（営業期間が１年未満の場合は月割額）です。


（単位：　円）
事業を行った
月　　数1ヶ月2ヶ月3ヶ月4ヶ月5ヶ月6ヶ月7ヶ月8ヶ月9ヶ月10ヶ月11ヶ月12ヶ月
事業主控除額242,000484,000725,000967,0001,209,0001,450,0001,692,0001,934,0002,175,0002,417,0002,659,0002,900,000



deduction: 控除
"""
import datetime
from decimal import Decimal
from enum import (
    Enum,
    unique,
    )
from zope.interface import Interface


class KindRate(Enum):
    first = Decimal('0.05')  # 第1種事業 (5%)
    second = Decimal('0.04')  # 第2種事業 (4%)
    third_a = Decimal('0.05')  # 第3種事業 (5%)
    third_b = Decimal('0.03')  # 第3種事業 (3%)
    default = Decimal('0.05')  # 当てはまらないものはとりあえず5%w


class BussinessType(Enum):
    # First
    buppin_hanbai = KindRate.first  # 物品販売業
    unso_toriatsukai = KindRate.first  # 運送取扱業
    ryoriten = KindRate.first  # 理店業
    yuranjo = KindRate.first  # 覧所業
    hoken = KindRate.first  # 険業
    senpaku_teikeijou = KindRate.first  # 舶ていけい場業
    inshokuten = KindRate.first  # 食店業
    shouhin_torihiki = KindRate.first  # 品取引業
    kinsen_kashitsuke = KindRate.first  # 銭貸付業
    souko = KindRate.first  # 庫業
    shuusen = KindRate.first  # 旋業
    hudousan_hanbai = KindRate.first  # 動産売買業
    buppin_kashitsuke = KindRate.first  # 品貸付業
    chuushajou = KindRate.first  # 車場業
    dairi = KindRate.first  # 理業
    koukoku = KindRate.first  # 告業
    hudousan_kashitsuke = KindRate.first  # 動産貸付業
    ukeoi = KindRate.first  # 負業
    nakadachi = KindRate.first  # 立業
    koushinjo = KindRate.first  # 信所業
    seizou = KindRate.first  # 造業
    insatshu = KindRate.first  # 刷業
    tonya = KindRate.first  # 屋業
    annai = KindRate.first  # 内業
    denki_kyoukyuu = KindRate.first  # 気供給業
    shuppan = KindRate.first  # 版業
    ryougae = KindRate.first  # 替業
    kankonsousai = KindRate.first  # 婚葬祭業
    doseki_saikutsu = KindRate.first  # 石採取業
    shashin = KindRate.first  # 真業
    koushu_yokujou_mushiburo = KindRate.first  # 衆浴場業（むし風呂等）
    denki_tsuushin = KindRate.first  # 気通信事業
    sekigasi = KindRate.first  # 貸業
    engeki_kougyou = KindRate.first  # 劇興行業
    unsou = KindRate.first  # 送業
    ryokan = KindRate.first  # 館業
    yuugijou = KindRate.first  # 技場業

    # Second
    chikusan = KindRate.second  # 産業
    suisan = KindRate.second  # 産業
    shintan_seizou = KindRate.second  # 炭製造業

    # Third A
    iryou = KindRate.third_a  # 業
    koushounin = KindRate.third_a  # 証人業
    sekkeikantoku = KindRate.third_a  # 計監督者業
    koushuuyokujou_sentou = KindRate.third_a  # 衆浴場業（銭湯）
    shikai = KindRate.third_a  # 科医業
    benrishi = KindRate.third_a  # 理士業
    hudousan_kantei = KindRate.third_a  # 動産鑑定業
    shikaeiseishi = KindRate.third_a  # 科衛生士業
    yakuzaishi = KindRate.third_a  # 剤師業
    zeirishi = KindRate.third_a  # 理士業
    design = KindRate.third_a  # ザイン業
    shikagikoushi = KindRate.third_a  # 科技工士業
    juui = KindRate.third_a  # 医業
    kouninkaikeishi = KindRate.third_a  # 認会計士業
    shogeisishou = KindRate.third_a  # 芸師匠業
    sokuryoushi = KindRate.third_a  # 量士業
    bengoshi = KindRate.third_a  # 護士業
    keirishi = KindRate.third_a  # 理士業
    riyoushi = KindRate.third_a  # 容業
    tochikaouchousashi = KindRate.third_a  # 地家屋調査士業
    shihoushoshi = KindRate.third_a  # 法書士業
    shakaihokenroumushi = KindRate.third_a  # 会保険労務士業
    biyoushi = KindRate.third_a  # 容業
    kaijidairishi = KindRate.third_a  # 事代理士業
    gyouseishoshi = KindRate.third_a  # 政書士業
    consultant = KindRate.third_a  # ンサルタント業
    clearing = KindRate.third_a  # リーニング業
    insatsuseihan = KindRate.third_a  # 刷製版業

    # Third B
    anma = KindRate.third_b  # んま・マッサージ又は指圧・はり・きゅう・柔道整復
    medical_other = KindRate.third_b  # の他の医業に類する事業装蹄師業


def callable_or_raise(target, default, exception):
    if callable(target):
        return target
    elif target is None:
        return default
    else:
        raise exception

def default_value(target, default):
    return default if target is None else target


@unique
class FinalReturnColor(Enum):
    blue = 1
    white = 2


class ProfitHistory(object):
    year = None
    value = Decimal('0')


def calc_rate(bussiness_type=None, types=None):
    types = types or BussinessType
    type_ = getattr(types, bussiness_type, None)
    if type_:
        return type_.value.value
    else:
        return KindRate.default.value


def calc_family_deduction(amount, final_return_color, is_partner=False):
    u"""個人の事業税の事業専従者給与(控除)額の算出

    事業主と生計を一にする親族の方が専らその事業に従事するときは、一定額を必要経費として控除できます。
    - 青色申告の場合･････その給与支払額（所得税の事業専従者給与）
    - 白色申告の場合･････配偶者の場合は８６万円、その他の方の場合は１人５０万円が限度
    """
    if final_return_color == FinalReturnColor.blue.name:
        return amount
    elif final_return_color == FinalReturnColor.white.name:
        max_amount = Decimal('860000') if is_partner else Decimal('500000')
        return max(max_amount, amount)
    else:
        raise ValueError('Invalid final return color: {}: Expected {}'.format(
            final_return_color, [elm.name for elm in FinalReturnColor]))


class BussinessOwnerDetection(object):
    _default = Decimal('2900000')
    _term_amount = {
        0: Decimal('0'),
        1: Decimal('242000'),
        2: Decimal('484000'),
        3: Decimal('725000'),
        4: Decimal('967000'),
        5: Decimal('1209000'),
        6: Decimal('1450000'),
        7: Decimal('1692000'),
        8: Decimal('1934000'),
        9: Decimal('2175000'),
        10: Decimal('2417000'),
        11: Decimal('2659000'),
        12: _default,
        }

    def __call__(self, start_on, fiscal=None):
        u"""

        fiscal: 年度
        """
        fiscal = datetime.date.today().year() if fiscal is None else fiscal
        last_day = datetime.date(year, 12, 31)
        return ((last_day.year - start_on.year) * 12) + (last_day.month - start_on.month)

calc_bussiness_owner_deduction = BussinessOwnerDetection()


class ProfitHistory(object):
    def __init__(self, amount, fiscal):
        self.amount = amount
        self.fiscal = fiscal


class FamilyDeduction(object):
    def __init__(self, amount, final_return_color, is_partner=False, calc=None):
        self._amount = amount
        self._finaly_return_corlo = final_return_color
        self._is_pertner = is_pertner
        self._calc = callable_or_raise(calc, calc_family_deduction, ValueError('Invalid value: {}'.format(calc)))


    def __call__(self):
        return self._calc(
            amount=self._amount,
            final_return_color=self._final_return_color,
            is_pertner=self._is_pertner,
            )


def calc_individual_enterprize_tax(
        income_amount,  # 事業所得
        real_estate_income_amount,  # 不動産所得
        family_deduction_amount,  # 個人の事業税の事業専従者給与(控除)額
        final_return_color,  # 青色申告 or 白色申告
        blue_special_deduction,  # 青色申告特別控除額(個人事業者には使わない)
        lost_carry_over_amount,  # 繰越控除額
        lost_hazard_carry_over_amount,  # 被災事業用資産の損失の繰越控除
        lost_transfer_carry_over_amount,  # 譲渡損失の控除と繰越控除
        bussiness_owner_detection_amount,  # 事業主控除
        rate,  # 税率
        ):
    blue_special_deduction = Decimal('0')  # 青色申告特別控除額(個人事業者には使わない)
    total_profit = (income_amount + real_estate_income_amount) \
                   - family_deduction_amount \
                   - lost_transfer_carry_over_amount \
                   - bussiness_owner_detection_amount

    if final_return_color == FinalReturnColor.blue.name:
        total_profit -= (
            blue_special_deduction + \
            lost_carry_over_amount + \
            )
    elif final_return_color == FinalReturnColor.white.name:
        total_profit -= lost_hazard_carry_over_amount
    if total_profit < 0:
        total_profit = Decimal('0')
    return total_profit * rate


class IndividualEnterpriseTax(object):
    def __init__(self, get_rate=None, bissiness_types=None,
                 get_individual_enterprize_tax=None,
                 get_bussiness_owner_detection=None):
        self._get_rate = callable_or_raise(
            get_rate, calc_rate, ValueError('Invalid rate calc function:'.format(rate)))
        self._bussiness_types = bissiness_types
        self._get_bussiness_owner_detection = callable_or_raise(
            get_bussiness_owner_detection, calc_bussiness_owner_detection,
            ValueError('Invalid rate calc function:'.format(bussiness_owner_detection)))
        self._get_individual_enterprize_tax = callable_or_raise(
            get_individual_enterprize_tax, calc_individual_enterprize_tax,
            ValueError('Invalid rate calc function:'.format(get_individual_enterprize_tax)))

    def get_rate(self, bussiness_type):
        return self._get_rate(bussiness_type, self._bissiness_types)

    def get_bussiness_onwer_deduction_amount(self, start_on, fiscal):
        return self._get_rate(start_on=start_on, fiscal=fiscal)

    def __call__(
            self,
            bussiness_type,
            final_return_color,  # 青色申告 or 白色申告
            start_on,  # 開業日時
            income_amount=Decimal('0'),  # 事業所得
            real_estate_income_amount=Decimal('0'),  # 不動産所得
            family_deductions=[],  # 個人の事業税の事業専従者給与(控除)額
            blue_special_deduction_amount=Decimal('0'),  # 青色申告特別控除額(個人事業者には使わない)
            lost_carry_over_amount=Decimal('0'),  # 繰越控除額
            lost_hazard_carry_over_amount=Decimal('0'),  # 被災事業用資産の損失の繰越控除
            lost_transfer_carry_over_amount=Decimal('0'),  # 譲渡損失の控除と繰越控除
            fiscal=None,  # 年度
            ):
        rate = self.get_rate(bussiness_type)
        family_deduction_amount = sum(family_deduction() for family_deduction in family_deductions)
        bussiness_owner_detection_amount = self.get_bussiness_owner_detection_amount(start_on, fiscal)
        return self._get_individual_enterprize_tax(
            income_amount=income_amount,
            real_estate_income_amount=real_estate_income_amount,
            family_deduction_amount=family_deduction_amount,
            final_return_color=final_return_color,
            blue_special_deduction_amount==blue_special_deduction_amount,
            lost_carry_over_amount=lost_carry_over_amount,
            lost_hazard_carry_over_amount=lost_hazard_carry_over_amount,
            lost_transfer_carry_over_amount=lost_transfer_carry_over_amount,
            bussiness_owner_detection_amount=bussiness_owner_detection_amount,
            rate=rate,
            )
