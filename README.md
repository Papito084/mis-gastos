# Mis Gastos Mensuales

Herramienta de seguimiento financiero optimizada para la gestión de presupuestos mensuales, categorización de transacciones y análisis de flujo de caja.

## 🏗️ Arquitectura y Funcionamiento Interno
- **Client-Side Rendering (CSR):** La interfaz se construye y actualiza dinámicamente en el cliente mediante Vanilla JavaScript, asegurando un acoplamiento bajo y alta cohesión en las funciones de manipulación del DOM.
- **Gestión del Estado:** El estado global de las transacciones se mantiene en memoria y se sincroniza asíncronamente con el `localStorage` del navegador para garantizar la persistencia de sesión sin backend externo.
- **Pipeline de Construcción (Build Step):** Incluye un script en Python (`_build.py`) que actúa como generador estático para compilar e inyectar configuraciones (diccionario de categorías, metadatos) directamente en el HTML final antes del despliegue.

## 📂 Estructura del Proyecto

```text
mis-gastos/
├── gastos-mensuales.html   # Core de la aplicación (UI y Lógica acoplada)
├── _build.py               # Script de automatización y pre-procesamiento
├── misgastos.ico           # Binario de iconografía
└── README.md
```

## 🚀 Instalación y Puesta en Marcha
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Papito084/mis-gastos.git
   ```
2. Ejecutar `python _build.py` únicamente si se desea recompilar el HTML con nuevas categorías base.
3. Abrir `gastos-mensuales.html` en un navegador web compatible para visualizar la aplicación.
