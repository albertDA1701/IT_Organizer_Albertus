from odoo import api, fields, models


class OrderBarangTV(models.Model):
    _name = 'it.ordertv'
    _description = 'Proses Order Televisi(TV)'

    orderdetail_tv_ids = fields.One2many(
        comodel_name=('it.order_detailtv'), 
        inverse_name=('order_tv_id'), 
        string='Order Detail')
    name = fields.Char(
        string='Kode Order', 
        required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pesanan', default=fields.Datetime.now, readonly=True)
    total = fields.Integer(compute='_compute_total', string='Total Harga Keseluruhan', store=True)

    @api.depends('orderdetail_tv_ids')
    def _compute_total(self):
        for record in self:
            total_penjualan = sum(self.env['it.order_detailtv'].search([('order_tv_id', '=', record.id)]).mapped('harga'))
            record.total    = total_penjualan


class OrderDetailTV(models.Model):
    _name = 'it.order_detailtv'
    _description = 'Detail Order Televisi(TV)'

    order_tv_id = fields.Many2one(comodel_name='it.ordertv', string='Order')
    
    tv_id = fields.Many2one(comodel_name='it.television', string='Televisi(TV)')
    
    hrg_satuan = fields.Integer(compute='_compute_hrg_satuan', string='Harga Satuan')
    
    @api.depends('tv_id')
    def _compute_hrg_satuan(self):
        for record in self:
            record.hrg_satuan = record.tv_id.harga
    
    harga = fields.Integer(compute='_compute_harga', string='Harga Total')
    kuantitas = fields.Integer(string='Quantity')
    
    @api.depends('kuantitas', 'hrg_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.tv_id.harga * record.kuantitas
    
    foto = fields.Image(compute='_compute_foto', string='Foto Produk', max_width=250, max_height=250)
    
    @api.depends('tv_id')
    def _compute_foto(self):
        for record in self:
            record.foto = record.tv_id.foto
            





