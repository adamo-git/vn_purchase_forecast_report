# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#
# Please note that these reports are not multi-currency !!!
#

from odoo import api, fields, models, tools


class purchase_requisition_report(models.Model):
    _name = "purchase.requisition.report"
    _description = "Purchase Requisition Report"
    _auto = False
    _order = 'ordering_date desc'

    ordering_date = fields.Datetime('Order Date', readonly=True, help="Date on which this document has been created")
    state = fields.Selection([
        ('draft', 'Draft RFQ'),
        ('ongoing', 'RFQ Sent'),
        ('in_progress', 'To Approve'),
        ('open', 'Purchase Order'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], 'Order Status', readonly=True)
    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    vendor_id = fields.Many2one('res.partner', 'Vendor', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', readonly=True)
    currency_id = fields.Many2one('res.currency', 'Currency', readonly=True)
    user_id = fields.Many2one('res.users', 'Purchase Representative', readonly=True)
    requisition_id = fields.Many2one('purchase.requisition', 'Requisition', readonly=True)
    account_analytic_id = fields.Many2one('account.analytic.account', 'Analytic Account', readonly=True)
    price_unit =  fields.Float('Price Unit', readonly=True)
    product_qty =  fields.Float('Quantity Product', readonly=True)
    sum_price =  fields.Float('Sum', readonly=True)
    date_end = fields.Datetime('Date end', readonly=True)
    schedule_date = fields.Datetime('Schedule date', readonly=True)
    type_id = fields.Many2one('purchase.requisition.type', 'Type Contract', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr,'purchase_requisition_report')
        self.env.cr.execute("""create or replace view purchase_requisition_report as (
                    SELECT 
			            min(l.id) as id,
                        pr.id as requisition_id,
                        pr.type_id,
                        pr.ordering_date as ordering_date,
                        pr.state,
                        pr.date_end,
                        pr.schedule_date,
                        l.product_id,
                        pr.vendor_id,
                        l.account_analytic_id,
                        pr.company_id,
                        pr.currency_id,
                        pr.user_id as user_id,
                        l.price_unit,
                        l.product_qty,
                        sum(l.price_unit*product_qty) as sum_price
                    FROM
                        purchase_requisition_line l,
                        purchase_requisition pr,
                        product_product p
                    WHERE 
                        l.requisition_id=pr.id and
                        l.product_id=p.id 
                    group by
                        pr.id,
                        pr.type_id,
                        pr.ordering_date,
                        pr.state,
                        pr.date_end,
                        pr.schedule_date,
                        l.product_id,
                        pr.vendor_id,
                        l.account_analytic_id,
                        pr.company_id,
                        pr.currency_id,
                        pr.user_id,
                        l.price_unit,
                        l.product_qty
                    )""")
        
