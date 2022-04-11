from odoo import api, fields, models


class Peralatan(models.Model):
    _name = 'it.handphone'
    _description = 'Daftar untuk jenis Handphones'

    name = fields.Char(string='Nama Barang', required=True)
    brand = fields.Selection(
        string='Nama Merek',
        selection=[('apple', 'Apple'), ('samsung', 'Samsung'), ('sony', 'Sony'), 
                   ('huawei', 'Huawei'), ('lg', 'LG'), ('nokia', 'Nokia'), ('oppo', 'OPPO'), 
                   ('vivo', 'ViVO'), ('lainnya', 'Lainnya')])
    type = fields.Char(string='Tipe Barang')
    harga = fields.Integer(string='Harga Barang')
    kondisi = fields.Selection(string='Kondisi Barang', 
                               selection=[('tersedia', 'Tersedia'), ('tidak tersedia', 'Tidak Tersedia'),])
    foto = fields.Image(string='Foto Barang', max_width=550, max_height=550)
    deskripsi = fields.Html(string='Spesifikasi Barang')
    

    
