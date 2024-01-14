# Scraping y Limpieza de Datos - Buenos Aires Compras: Penas y Sanciones

## Porqué

En la actualidad, el portal de compras y contrataciones de la Ciudad de Buenos Aires no proporciona un listado descargable de penas y sanciones. Este repositorio presenta dos scripts diseñados para automatizar la obtención de este listado de manera eficiente y su posterior limpieza para su reutilización. 

## Cómo

### Requisitos Previos
- Python 3.11+
- Bibliotecas necesarias: selenium, pandas.

### Instalación de Librerías
```bash
pip install selenium pandas
```

### Configuración del Entorno Virtual (Opcional pero Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Para sistemas Unix
venv\Scripts\activate  # Para sistemas Windows
```

### Ejecución de los Scripts
1. Descargar el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repo.git
    cd tu_repo
    ```

2. Ejecutar el primer script (01_scrap.py):
    ```bash
    python 01_scrap.py
    ```

3. Ejecutar el segundo script (02_clean.py):
    ```bash
    python 02_clean.py
    ```

## To-Do's

### Posibles Mejoras

1. **Optimización de Descarga:**
    - Evaluar la posibilidad de correcciones directas desde Selenium al descargar datos, reduciendo la necesidad de procesos posteriores.

2. **Simplificación del Proceso de Limpieza:**
    - Explorar alternativas para simplificar el proceso de limpieza de datos, considerando métodos más eficientes o bibliotecas especializadas.

3. **Manejo de Errores Mejorado:**
    - Implementar un manejo de errores más robusto en ambos scripts para garantizar una ejecución sin interrupciones.

4. **Documentación Adicional:**
    - Ampliar la documentación en el código fuente para facilitar la comprensión y mantenimiento del código en el futuro.

Recuerda revisar y adaptar los scripts según tus necesidades específicas antes de ejecutarlos.

¡Esperamos que estos scripts te sean de utilidad! Si tienes sugerencias o encuentras áreas de mejora, no dudes en contribuir o compartir tus ideas. ¡Gracias por utilizar este recurso!