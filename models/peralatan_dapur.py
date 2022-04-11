from odoo import api, fields, models


class peralatan4(models.Model):
    _name = 'it.dapur'
    _description = 'Daftar untuk Jenis Peralatan Elektronik Dapur'

    name   = fields.Char(string='Name', required=True)
    brand  = fields.Selection(
        string   ='Nama Merek',
        selection=[('samsung', 'Samsung'), ('philips', 'Philips'), ('polytron', 'Polytron'), 
                   ('xiaomi', 'Xiaomi'), ('oxone', 'Oxone'), ('cosmos', 'Cosmos'), 
                   ('strogen', 'Strogen'), ('lainnya', 'Lainnya')])
    type    = fields.Char(string='Tipe Barang')
    harga   = fields.Integer(string='Harga Barang')
    kondisi = fields.Selection(string='Kondisi Barang', 
                               selection=[('tersedia', 'Tersedia'), ('tidak tersedia', 'Tidak Tersedia'),])
    foto = fields.Image(string='Foto Barang', max_width=400, max_height=400)   
    deskripsi = fields.Html(string='Spesifikasi Barang')