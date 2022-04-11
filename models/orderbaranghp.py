from odoo import api, fields, models


class OrderBarang(models.Model):
    _name = 'it.order'
    _description = 'Proses Order Barang'

    orderdetail_ids = fields.One2many(
        comodel_name=('it.order_detail'), 
        inverse_name=('order_id'), 
        string='Order Detail')
    name = fields.Char(
        string='Kode Order', 
        required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pesanan', default=fields.Datetime.now, readonly=True)
    total = fields.Integer(compute='_compute_total', string='Total Harga Keseluruhan', store=True)

    @api.depends('orderdetail_ids')
    def _compute_total(self):
        for record in self:
            total_penjualan = sum(self.env['it.order_detail'].search([('order_id', '=', record.id)]).mapped('harga'))
            record.total    = total_penjualan


class OrderDetail(models.Model):
    _name = 'it.order_detail'
    _description = 'Detail Order'

    order_id = fields.Many2one(comodel_name='it.order', string='Order')
    
    hp_id = fields.Many2one(comodel_name='it.handphone', string='Handphone')
    
    name = fields.Selection(
        string='Name',
        selection=[('hp', 'HP'), ('laptop', 'Laptop'), 
                   ('television', 'Television'), ('peralatan_dapur', 'Peralatan_Dapur'),
                   ('peralatan_rumah_tangga', 'Peralatan_Rumah_Tangga')])
    hrg_satuan = fields.Integer(compute='_compute_hrg_satuan', string='Harga Satuan')
    
    @api.depends('hp_id')
    def _compute_hrg_satuan(self):
        for record in self:
            record.hrg_satuan = record.hp_id.harga
    
    harga = fields.Integer(compute='_compute_harga', string='Harga Total')
    kuantitas = fields.Integer(string='Quantity')
    
    @api.depends('kuantitas', 'hrg_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.hp_id.harga * record.kuantitas
    
    foto = fields.Image(compute='_compute_foto', string='Foto Produk', max_width=250, max_height=250)
    
    @api.depends('hp_id')
    def _compute_foto(self):
        for record in self:
            record.foto = record.hp_id.foto
            



