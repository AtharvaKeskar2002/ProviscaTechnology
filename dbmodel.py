from connection import *

class Contact(db.Model):
    __tablename__ = "contact"
    id = db.Column("id", db.Integer, primary_key=True)
    firstname = db.Column("firstname", db.String(100), nullable=False)
    lasttname = db.Column("lastname", db.String(100), nullable=False)
    email = db.Column("email", db.String(100), nullable=False)
    phone = db.Column("phone", db.BigInteger, nullable=False)
    message = db.Column("message", db.String(1000), nullable=False)

    def __str__(self):
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        return str(self)
#
# db.create_all()