# from flask import Flask

# class Customer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(50), nullable=False)
#     invoices = db.relationship('Invoice', backref='customer', lazy=True)

# class Invoice(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     amount = db.Column(db.Float, nullable=False)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

# class InvoiceItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
