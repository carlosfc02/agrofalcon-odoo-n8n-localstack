from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    customer_type = fields.Selection(
        [
            ("restaurant", "Restaurant"),
            ("shop", "Shop"),
            ("wholesaler", "Wholesaler"),
        ],
        string="Customer Type",
    )
    crop_interest = fields.Char(string="Crop Interest")
    expected_order_volume_kg = fields.Float(string="Expected Order Volume (kg)")
    external_event_status = fields.Char(string="External Event Status")
    s3_document_key = fields.Char(string="S3 Document Key")
