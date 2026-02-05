# MyWallet API

API de gestión de finanzas personales construida con Django, Django REST Framework, JWT y PostgreSQL.

## Descripción
Permite a los usuarios registrarse, iniciar sesión y gestionar sus ingresos y gastos personales. Cada usuario solo puede ver y editar sus propios datos.

## Instalación

1. Clona el repositorio:
	```
	git clone <URL-del-repo>
	cd My-Wallet
	```
2. Crea y activa un entorno virtual:
	```
	python -m venv venv
	# En Windows:
	venv\Scripts\activate
	# En Mac/Linux:
	source venv/bin/activate
	```
3. Instala las dependencias:
	```
	pip install -r requirements.txt
	```
4. Configura la base de datos PostgreSQL en `mywallet/settings.py`.
5. Aplica las migraciones:
	```
	python manage.py makemigrations
	python manage.py migrate
	```
6. Crea un superusuario:
	```
	python manage.py createsuperuser
	```
7. Ejecuta el servidor:
	```
	python manage.py runserver
	```

## Endpoints principales

- `POST /api/register/` — Registro de usuario
- `POST /api/token/` — Login (obtener JWT)
- `POST /api/token/refresh/` — Refrescar JWT
- `GET/POST/PUT/DELETE /api/categories/` — CRUD de categorías
- `GET/POST/PUT/DELETE /api/transactions/` — CRUD de transacciones
- `GET /api/dashboard/` — Resumen financiero (ingresos, gastos, balance)

## Pruebas con Insomnia

1. Abre Insomnia y selecciona `Import`.
2. Elige el archivo de colección incluido (`MyWallet_API.yaml` en la raíz del proyecto).
3. Prueba los endpoints:
	- Regístrate con `/api/register/`.
	- Haz login con `/api/token/` y copia el `access token`.
	- En los endpoints protegidos, agrega el header:
	  ```
	  Authorization: Bearer <access_token>
	  ```
	- Prueba crear, listar, editar y borrar categorías y transacciones.
	- Consulta el dashboard con `/api/dashboard/`.

## Notas
- Asegúrate de tener PostgreSQL corriendo y la base de datos creada.
- El archivo de colección de Insomnia está en la raíz o en la carpeta `/docs`.
- El proyecto está protegido con JWT: necesitas el token para acceder a la mayoría de los endpoints.

## Autor
- Alejandro Ramirez

---
¡Gracias por usar MyWallet API!
