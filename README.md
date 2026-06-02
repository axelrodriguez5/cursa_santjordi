# 🌹 Cursa de Sant Jordi - Institut Sa Palomera

Aplicació web desenvolupada amb **Django** per gestionar la cursa de Sant Jordi de l'institut.

## 📋 Funcionalitats

- Gestió de **participants** (CRUD complet: crear, llistar, editar, eliminar)
- Gestió de **categories** per edat
- **Filtre** de participants per categoria
- **Classificació** de resultats ordenada per temps
- Panell d'**administració** de Django
- **Missatges del sistema** quan es realitzen accions
- Interfície responsiva amb **Bootstrap 5**

## 🛠️ Tecnologies

- Python 3
- Django 5.2
- SQLite
- Bootstrap 5

## 🚀 Instal·lació

```bash
# 1. Clonar el repositori
git clone <URL_DEL_REPO>
cd cursa_santjordi

# 2. Crear i activar el virtualenv
python3 -m venv env
source env/bin/activate

# 3. Instal·lar dependències
pip install -r requirements.txt

# 4. Aplicar migracions
python manage.py migrate

# 5. (Opcional) Crear un superusuari per l'admin
python manage.py createsuperuser

# 6. (Opcional) Carregar dades de prova
python manage.py shell < carregar_dades.py

# 7. Executar el servidor
python manage.py runserver
```

Obre el navegador a: http://localhost:8000/

## 🗂️ Estructura del projecte

```
cursa_santjordi/
├── manage.py
├── requirements.txt
├── .gitignore
├── carregar_dades.py        # Script opcional de dades de prova
├── cursa_santjordi/         # Configuració del projecte
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── cursa/                   # App principal
    ├── models.py            # Models: Categoria, Participant
    ├── views.py             # Vistes amb consultes ORM
    ├── forms.py             # ModelForms
    ├── urls.py              # Rutes de l'app
    ├── admin.py             # Configuració del panell admin
    └── templates/cursa/     # Plantilles HTML
```

## 🗄️ Model de dades

**Categoria**
- `nom` (CharField)
- `edat_minima` (IntegerField)
- `edat_maxima` (IntegerField)
- `distancia_km` (DecimalField)

**Participant**
- `nom`, `cognoms` (CharField)
- `dorsal` (IntegerField, unique)
- `email` (EmailField)
- `data_naixement` (DateField)
- `categoria` (ForeignKey → Categoria)
- `temps_segons` (IntegerField, nullable)

**Relació:** Una `Categoria` pot tenir molts `Participants` (1:N).

## 📍 Rutes principals

| URL | Descripció |
|-----|------------|
| `/` | Pàgina d'inici amb estadístiques |
| `/participants/` | Llistat de participants (amb filtre) |
| `/participants/afegir/` | Afegir un nou participant |
| `/participants/<id>/editar/` | Editar un participant |
| `/participants/<id>/eliminar/` | Eliminar un participant |
| `/categories/` | Llistat de categories |
| `/categories/afegir/` | Afegir una categoria |
| `/resultats/` | Classificació general |
| `/admin/` | Panell d'administració |

## 👤 Autor

Projecte realitzat per al mòdul **M0376 - Implantació d'Aplicacions Web**  
2n CFGS ASIX - Curs 2025-2026  
Institut Sa Palomera
