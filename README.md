**DESPLEGANDO MODELO PROPIO EN EL SERVIDOR RAILWAY Y UTILIZANDO EL MODELO DESDE LA API HUGGING FACE**

El modelo se utiliza a través de la API de Hugging Face para optimizar el uso de recursos. Esto se debe a que, al desplegarlo directamente en Railway con una cuenta gratuita, los recursos son limitados. Por esta razón, se optó por alojar el modelo en Hugging Face, permitiendo un uso más eficiente desde su infraestructura.

**Cómo usar la API de Hugging Face**

En este ejemplo de backend, el modelo se encuentra alojado en Hugging Face. El procesamiento se realiza directamente a través de su API, lo que requiere únicamente el token de autenticación de la API para acceder al modelo y utilizarlo.

**PASO 1. MODELO ALOJADO HUGGING FACE** 

![image](https://github.com/user-attachments/assets/cc635c8f-ba44-4f95-adc6-e50956d486b4)

**PASO 2. CREAR UN TOKEN DE LECTURA** 

![image](https://github.com/user-attachments/assets/c8b6fa67-22a4-4269-ae85-55eda5a9b942)

**PASO 3. DESPLIEGUE DEL MODELO** 

Antes de hacer el despliegue en Railway , alojar el backend en github.

![image](https://github.com/user-attachments/assets/2bac847f-0101-4faf-84b2-33e7ee219e7c)

Algunas configuraciones , para crear la URL del backend

![image](https://github.com/user-attachments/assets/3e334ca7-1db1-4a63-bc74-30ca90a5ab10)

Establecer el comando para el despliegue: **gunicorn -w 1 -b 0.0.0.0:8080 app:app --timeout 30** 

![image](https://github.com/user-attachments/assets/519654c1-83e0-41ef-bfdf-053c7725483c)

**TESTEANDO LA API**

![image](https://github.com/user-attachments/assets/78a6c8d4-0936-4c13-9944-8f45dccecac4)

**VERIFICANDO EL FUNCIONAMIENTO DEL SERVIDOR RAILWAY**

![image](https://github.com/user-attachments/assets/3e23a8ad-5220-4605-aa2f-8d3f274a50f1)


