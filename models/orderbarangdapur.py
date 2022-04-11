from odoo import api, fields, models


class OrderBarangDapur(models.Model):
    _name = 'it.orderdapur'
    _description = 'Proses Order Peralatan Elektronik Dapur'

    orderdetail_dapur_ids = fields.One2many(
        comodel_name=('it.order_detaildapur'), 
        inverse_name=('order_dapur_id'), 
        string='Order Detail')
    name = fields.Char(
        string='Kode Order', 
        required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pesanan', default=fields.Datetime.now, readonly=True)
    total = fields.Integer(compute='_compute_total', string='Total Harga Keseluruhan', store=True)

    @api.depends('orderdetail_dapur_ids')
    def _compute_total(self):
        for record in self:
            total_penjualan = sum(self.env['it.order_detaildapur'].search([('order_dapur_id', '=', record.id)]).mapped('harga'))
            record.total    = total_penjualan


class OrderDetailDapur(models.Model):
    _name = 'it.order_detaildapur'
    _description = 'Detail Order Peralatan Elektronik Dapur'

    order_dapur_id = fields.Many2one(comodel_name='it.orderdapur', string='Order')
    
    dapur_id = fields.Many2one(comodel_name='it.dapur', string='Eletronik Dapur')
    
    hrg_satuan = fields.Integer(compute='_compute_hrg_satuan', string='Harga Satuan')
    
    @api.depends('dapur_id')
    def _compute_hrg_satuan(self):
        for record in self:
            record.hrg_satuan = record.dapur_id.harga
    
    harga = fields.Integer(compute='_compute_harga', string='Harga Total')
    kuantitas = fields.Integer(string='Quantity')
    
    @api.depends('kuantitas', 'hrg_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.dapur_id.harga * record.kuantitas
    
    foto = fields.Image(compute='_compute_foto', string='Foto Produk', max_width=250, max_height=250)
    
    @api.depends('dapur_id')
    def _compute_foto(self):
        for record in self:
            record.foto = record.dapur_id.foto
            



