from passlib.context import CryptContext
from .database import SessionLocal, engine, Base
from . import models

Base.metadata.create_all(bind=engine)
db = SessionLocal()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

if db.query(models.Product).count() == 0:
    productos = [
        models.Product(
            title="Laptop",
            description="Laptop con pantalla de 15 pulgadas.",
            image="http://10.0.2.2:8000/static/images/laptop.png",
            price=3499.90,
            category="Sin categoría"
        ),
        models.Product(
            title="Mouse",
            description="Mouse gamer con RGB.",
            image="http://10.0.2.2:8000/static/images/mouse.png",
            price=99.90,
            category="Sin categoría"
        ),
        models.Product(
            title="Teclado",
            description="Teclado gamer con RGB.",
            image="http://10.0.2.2:8000/static/images/keyboard.png",
            price=129.90,
            category="Sin categoría"
        ),
        models.Product(
            title="Monitor",
            description="Monitor de 24 pulgadas.",
            image="http://10.0.2.2:8000/static/images/monitor.png",
            price=499.90,
            category="Sin categoría"
        ),
        models.Product(
            title="Audífonos",
            description="Audífonos inalámbricos.",
            image="http://10.0.2.2:8000/static/images/headphones.png",
            price=159.90,
            category="Sin categoría"
        ),
        models.Product(
            title="Tablet",
            description="Tablet para tareas generales.",
            image="http://10.0.2.2:8000/static/images/tablet.png",
            price=1999.90,
            category="Sin categoría"
        ),
        models.Product(
            title="Mouse-pad",
            description="Mouse-pad bonito.",
            image="http://10.0.2.2:8000/static/images/mouse_pad.png",
            price=29.90,
            category="Sin categoría"
        ),
    ]
    db.add_all(productos)
    db.commit()
    print(f"Seed completado: {len(productos)} productos insertados.")
else:
    print("Ya existen productos, no se insertó nada.")

if db.query(models.User).count() == 0:
    usuarios = [
        models.User(
            username="marco",
            hashed_password=pwd_context.hash("password123")
        ),
        models.User(
            username="antonio",
            hashed_password=pwd_context.hash("password456")
        )
    ]
    db.add_all(usuarios)
    db.commit()
    print(f"Usuarios insertados: {len(usuarios)}")
else:
    print("Ya existen usuarios, no se insertó nada.")

db.close()