from odoo import api, fields, models


class Peralatan5(models.Model):
    _name = 'it.rumahtangga'
    _description = 'Daftar untuk Jenis Peralatan Elektronik Rumah Tangga'

    name = fields.Char(string='Name', required=True)
    brand  = fields.Selection(
        string   ='Nama Merek',
        selection=[('samsung', 'Samsung'), ('philips', 'Philips'), ('polytron', 'Polytron'), 
                   ('xiaomi', 'Xiaomi'), ('lainnya', 'Lainnya')])
    type    = fields.Char(string='Tipe Barang')
    harga   = fields.Integer(string='Harga Barang')
    kondisi = fields.Selection(string='Kondisi Barang', 
                               selection=[('tersedia', 'Tersedia'), ('tidak tersedia', 'Tidak Tersedia'),]) 
    foto = fields.Image(string='Foto Barang', max_width=400, max_height=400)
    deskripsi = fields.Html(string='Spesifikasi Barang')
