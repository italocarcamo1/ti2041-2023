from ninja import Schema
from typing import List

# Este es el esquema utilizado para la creación de posts exclusivamente
class MessageSchema(Schema):
    message: str

class ServiceInputSchema(Schema):
    nom: str
    descrip: str
    provi: int
    valor: int
    from_date: str
    thru_date: str

class ProviderOutputSchema(Schema):
    fantasy: str
    tax_nom: str
    tax_id: str
    permitir: bool

class AddressOutputSchema(Schema):
    provi: int
    type: str
    direcc1: str
    direcc2: str
    codigopost: str
    ciud: str
    region: str
    pais: str

class ContactOutputSchema(Schema):
    provi: int
    type: str
    first_nom: str
    last_nom: str
    email: str
    telefono: str
    mobile: str

class ServiceOutputSchema(Schema):
    nom: str
    descrip: str
    provi: ProviderOutputSchema
    valor: int
    from_date: str
    thru_date: str
    contacto: List[ContactOutputSchema]
    direcc: AddressOutputSchema






