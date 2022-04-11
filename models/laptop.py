from odoo import api, fields, models


class Peralatan2(models.Model):
    _name = 'it.laptop'
    _description = 'Daftar untuk jenis PC/Laptop'

    name = fields.Char(string='Nama Barang', required=True)
    brand = fields.Selection(
        string='Nama Merek',
        selection=[('apple', 'Apple'), ('samsung', 'Samsung'), ('acer', 'Acer'), 
                   ('lenovo', 'Lenovo'), ('hp', 'HP'), ('asus', 'Asus'), ('dell', 'Dell'), 
                   ('msi', 'MSI'), ('lainnya', 'Lainnya')])
    jenis = fields.Selection(
        string='Jenis Laptop/PC',
        selection=[('notebook', 'Notebook'), ('gaming', 'Gaming'), ('business', 'Business'), ('desktop', 'Desktop'),
                   ('all in one', 'All in One'), ('lainnya', 'Lainnya')])
    type = fields.Char(string='Tipe Barang')
    harga = fields.Integer(string='Harga Barang')
    kondisi = fields.Selection(string='Kondisi Barang', 
                               selection=[('tersedia', 'Tersedia'), ('tidak tersedia', 'Tidak Tersedia'),])
    foto = fields.Image(string='Foto Barang', max_width=500, max_height=500)
    deskripsi = fields.Html(string='Spesifikasi Barang')
    
    
    

    
