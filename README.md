# money_controller
### El objetivo del proyecto es basicamente controlar los gastos de cada usuario, manejando presupuestos y gastos dentro de cada presupuesto.

******************
## Cosas a tener en cuenta para la instalacion del proyecto:
  *instalar virtualenv en la maquina e inicializar dentro del proyecto donde se clonaron la repo
  *Instalar las dependencias desde el archivo requirements.txt con este comando pip install -r requirements.txt ya estando en el entorno virtual del proyecto
  
## OBSERVACIONES IMPORTANTES:
Para el correcto funcionamiento del proyecto es necesario realizar estos cambios:
*cambiar esta linea de codigo en el archivo propio de django money_controller\venv\Lib\site-packages\django\contrib\auth\forms.py

    class Meta:
        model = User
        #fields = "__all__"
        fields = ["username","first_name","last_name"]
        field_classes = {"username": UsernameField}
        labels = {
            'username': _('Nombre de usuario'),
            'first_name': _('Primer Nombre'),
            'last_name': _('Segundo Nombre'),
        } 
![image](https://user-images.githubusercontent.com/67200281/217678904-c4669cca-1465-457e-8d4d-ad9a915b7cda.png)

El admin creado hasta el momento tiene este User: damian Pass: damian123
