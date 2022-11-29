# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from num2words import num2words


class xx_amount2words(models.Model):
    _inherit = 'account.move'

    amount2words = fields.Char(string= "المبلغ كتابتا")

    @api.onchange('invoice_line_ids')
    def onchange_values(self):
         self.amount2words = self.changeamount2words(self.amount_total)

    def changeamount2words(self, amount):
        pre = float(amount)
        if pre:
            text = ''
            entire_num = int((str(pre).split('.'))[0])
            decimal_num = int((str(pre).split('.'))[1])
            if decimal_num < 10:
                decimal_num = decimal_num * 10
            #     ar_001
            text += num2words(entire_num, lang='ar_001').title()
            text += ' ريال '
            if decimal_num:
                text += ' و '
                text += num2words(decimal_num, lang='ar_001').title()
                text += ' هلله '
            if self.type in ('out_invoice', 'in_refund'):
                text = text.replace(',', ' و ')

                amount_text = 'عليكم ' + text.replace('،', ' و ')
                return amount_text
            else:

                if self.type in ('in_invoice', 'out_refund'):
                    text = 'لكم ' + text.replace(',', ' و ')

                    amount_text = 'لكم ' + text.replace('،', ' و ')
                    return amount_text


class xx_amount2words_sale_order(models.Model):
    _inherit = 'sale.order'

    amount2words = fields.Char(string= "المبلغ كتابتا")

    @api.onchange('order_line')
    def onchange_values(self):
         self.amount2words = self.changeamount2words(self.amount_total)

    def changeamount2words(self, amount):
        pre = float(amount)
        if pre:
            text = ''
            entire_num = int((str(pre).split('.'))[0])
            decimal_num = int((str(pre).split('.'))[1])
            if decimal_num < 10:
                decimal_num = decimal_num * 10
            #     ar_001
            text += num2words(entire_num, lang='ar_001').title()
            text += ' ريال '
            if decimal_num:
                text += ' و '
                text += num2words(decimal_num, lang='ar_001').title()
                text += ' هلله '
                text = text.replace(',', ' و ')

                amount_text = 'عليكم ' + text.replace('،', ' و ')
                return amount_text

class xx_amount2words_payment(models.Model):
    _inherit = 'account.payment'

    amount2words = fields.Char(string= "المبلغ كتابتا")

    @api.onchange('amount')
    def onchange_values(self):
         self.amount2words = self.changeamount2words(self.amount)

    def changeamount2words(self, amount):
        pre = float(amount)
        if pre:
            text = ''
            entire_num = int((str(pre).split('.'))[0])
            decimal_num = int((str(pre).split('.'))[1])
            if decimal_num < 10:
                decimal_num = decimal_num * 10
            #     ar_001
            text += num2words(entire_num, lang='ar_001').title()
            text += ' ريال '
            if decimal_num:
                text += ' و '
                text += num2words(decimal_num, lang='ar_001').title()
                text += ' هلله '
            if self.payment_type in ('inbound'):
                text = text.replace(',', ' و ')

                amount_text = 'عليكم ' + text.replace('،', ' و ')
                return amount_text
            else:

                if self.payment_type in ('outbound'):
                    text = 'لكم ' + text.replace(',', ' و ')

                    amount_text = 'لكم ' + text.replace('،', ' و ')
                    return amount_text
