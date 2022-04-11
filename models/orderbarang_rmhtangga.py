from odoo import api, fields, models


class OrderBarangRumahTangga(models.Model):
    _name = 'it.orderrt'
    _description = 'Proses Order Peralatan Elektronik Rumah Tangga'

    orderdetail_rt_ids = fields.One2many(
        comodel_name=('it.order_detailrt'), 
        inverse_name=('order_rt_id'), 
        string='Order Detail')
    name = fields.Char(
        string='Kode Order', 
        required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pesanan', default=fields.Datetime.now, readonly=True)
    total = fields.Integer(compute='_compute_total', string='Total Harga Keseluruhan', store=True)

    @api.depends('orderdetail_rt_ids')
    def _compute_total(self):
        for record in self:
            total_penjualan = sum(self.env['it.order_detailrt'].search([('order_rt_id', '=', record.id)]).mapped('harga'))
            record.total    = total_penjualan


class OrderDetailRumahTangga(models.Model):
    _name = 'it.order_detailrt'
    _description = 'Detail Order Peralatan Elektronik Rumah Tangga'

    order_rt_id = fields.Many2one(comodel_name='it.orderrt', string='Order')
    
    rt_id = fields.Many2one(comodel_name='it.rumahtangga', string='Elektronik Rumah Tangga')
    
    hrg_satuan = fields.Integer(compute='_compute_hrg_satuan', string='Harga Satuan')
    
    @api.depends('rt_id')
    def _compute_hrg_satuan(self):
        for record in self:
            record.hrg_satuan = record.rt_id.harga
    
    harga = fields.Integer(compute='_compute_harga', string='Harga Total')
    kuantitas = fields.Integer(string='Quantity')
    
    @api.depends('kuantitas', 'hrg_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.rt_id.harga * record.kuantitas
    
    foto = fields.Image(compute='_compute_foto', string='Foto Produk', max_width=250, max_height=250)
    
    @api.depends('rt_id')
    def _compute_foto(self):
        for record in self:
            record.foto = record.rt_id.foto
            



