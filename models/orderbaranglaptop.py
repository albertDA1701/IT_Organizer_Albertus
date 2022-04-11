from odoo import api, fields, models


class OrderBarangLaptop(models.Model):
    _name = 'it.orderlaptop'
    _description = 'Proses Order Laptop'

    orderdetail_laptop_ids = fields.One2many(
        comodel_name=('it.order_detaillaptop'), 
        inverse_name=('order_laptop_id'), 
        string='Order Detail')
    name = fields.Char(
        string='Kode Order', 
        required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pesanan', default=fields.Datetime.now, readonly=True)
    total = fields.Integer(compute='_compute_total', string='Total Harga Keseluruhan', store=True)

    @api.depends('orderdetail_laptop_ids')
    def _compute_total(self):
        for record in self:
            total_penjualan = sum(self.env['it.order_detaillaptop'].search([('order_laptop_id', '=', record.id)]).mapped('harga'))
            record.total    = total_penjualan


class OrderDetailLaptop(models.Model):
    _name = 'it.order_detaillaptop'
    _description = 'Detail Order Laptop'

    order_laptop_id = fields.Many2one(comodel_name='it.orderlaptop', string='Order')
    
    laptop_id = fields.Many2one(comodel_name='it.laptop', string='Handphone')
    
    hrg_satuan = fields.Integer(compute='_compute_hrg_satuan', string='Harga Satuan')
    
    @api.depends('laptop_id')
    def _compute_hrg_satuan(self):
        for record in self:
            record.hrg_satuan = record.laptop_id.harga
    
    harga = fields.Integer(compute='_compute_harga', string='Harga Total')
    kuantitas = fields.Integer(string='Quantity')
    
    @api.depends('kuantitas', 'hrg_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.laptop_id.harga * record.kuantitas
    
    foto = fields.Image(compute='_compute_foto', string='Foto Produk', max_width=250, max_height=250)
    
    @api.depends('laptop_id')
    def _compute_foto(self):
        for record in self:
            record.foto = record.laptop_id.foto
            



