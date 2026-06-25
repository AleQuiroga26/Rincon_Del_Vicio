# 🎮 Rincón del Vicio

¡Bienvenido a **Rincón del Vicio**! Una tienda de videojuegos digital diseñada para que los gamers puedan explorar el catálogo, descubrir sus próximos títulos favoritos y gestionar su propia biblioteca personal.


La aplicación maneja estos aspectos :

*Catálogo Dinámico*: Se puede explorar juegos, filtrar por categorías y usar un buscador  para encontrar algun titulo.
*Sistema de Compras basico:* Los usuarios pueden registrarse, iniciar sesión y comprar juegos. El juego pasa automáticamente a formar parte de su "Biblioteca" y el sistema guarda el precio que pagaste.
*Historial de Usuario:* Cada Usuario tiene su propio panel de "Mis Compras" para ver qué compro, cuándo lo hizo y cuánto lleva gastado en la plataforma.
*Control Avanzado (Para Jefes y Desarrolladores):* La app cuenta con un sistema de roles. Los Jefes pueden administrar las categorías directamente desde la tienda ademas de los juegos y los desarrolladores pueden agregar, editar o eliminar juegos del catálogo.

---

**La base de datos relaciona lo siguiente:*

* **Juegos**, que son el centro de todo.
* **Categorías** y **Plataformas** (PlayStation, PC, Xbox) vinculadas a cada juego.
* **Desarrolladoras** y **Requisitos del Sistema** tambien para cada juego
* **Usuarios Personalizados** (con foto de perfil y con la compra de uno o varios juego).
* **Compras** que muestra al usuario los juegos que tiene.

---

## 🚀 Cómo correr el proyecto

1. **Clona o descarga** este repositorio.
2. Abre una terminal en la carpeta del proyecto (`Rincon_del_vicio2`).
3. Activa tu entorno virtual (si tienes uno) e instala las dependencias necesarias y los requirements.txt
   ```bash
   pip install -r requirements.txt
   ```
4. Aplica las migraciones para preparar la base de datos:
   ```bash
   python manage.py makremigrations
   ```
   ```bash
   python manage.py migrate
   ```
5. ¡Enciende el servidor!
   ```bash
   python manage.py runserver
   ```
6. Entra desde tu navegador web a `http://127.0.0.1:8000/` 

*Para acceder al panel de control total, creas un superusuario con `python manage.py createsuperuser` y luego entras a `/admin`.*

