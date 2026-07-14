from .database import SessionLocal, engine, Base
from . import models

db = SessionLocal()

nuevo = models.Product(
    title="Smartphone",
    description="Smartphone con cámara de 108MP.",
    image="http://10.0.2.2:8000/static/images/smartphone.jpg",
    price=1299.90,
    category="Sin categoría"
)

db.add(nuevo)
db.commit()
db.refresh(nuevo)

print(f"Producto agregado: ID={nuevo.id}, title='{nuevo.title}'")

db.close()

# python -m app.add_product