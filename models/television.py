from odoo import api, fields, models


class Peralatan3(models.Model):
    _name = 'it.television'
    _description = 'Daftar untuk jenis Televisi(TV)'

    name  = fields.Char(string='Nama Barang', required=True)
    brand = fields.Selection(
        string='Nama Merek',
        selection=[('samsung', 'Samsung'), ('panasonic', 'Panasonic'), 
                   ('xiaomi', 'Xiaomi'), ('lg', 'LG'), ('polytron', 'Polytron'), 
                   ('sony', 'Sony'), ('sharp', 'Sharp'), ('lainnya', 'Lainnya')])
    type  = fields.Char(string='Tipe Barang')
    harga = fields.Integer(string='Harga Barang')
    kondisi = fields.Selection(string='Kondisi Barang', 
                               selection=[('tersedia', 'Tersedia'), ('tidak tersedia', 'Tidak Tersedia'),])
    foto = fields.Image(string='Foto Barang', max_width=500, max_height=500)
    deskripsi = fields.Html(string='Spesifikasi Barang')
