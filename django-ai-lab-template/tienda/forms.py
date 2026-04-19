from django import forms 
from django.forms import inlineformset_factory
from .models import Producto
from .models import Cliente
from .models import Pedido
from.models import PedidoItem

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ("nombre", "descripcion", "precio", "stock")
        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Nombre del Producto"
            }),
            "descripcion": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Descripcion breve"
            }),
            "precio": forms.NumberInput(attrs={
                "step": "0.01",
                "min": "0"                
            }),
            "stock": forms.NumberInput(attrs={
                "step": "1",
                "min": "0"                
            }),
        }    
            
    def clean_precio(self):
        #Si el precio es negativo o 0 se lanza una exepción 
        precio = self.cleaned_data.get("precio")
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0, Pendejo.")
        return precio
    
    def clean_stock(self):
        #Si el precio es negativo o 0 se lanza una exepción 
        stock = self.cleaned_data.get("stock")
        if stock is not None and stock <= 0:
            raise forms.ValidationError(" ¿Cómo vas a agregarlo si no hay?, Pendejo.")
        return stock
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "email", "activo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre completo"}),
            "email": forms.EmailInput(attrs={"placeholder": "ejemplo@correo.com"}),
        
        }

class PedidoSimpleForm(forms.ModelForm):
    class Meta:
       model = Pedido
       fields = ["Cliente", "estado"]
       
class PedidoItemForm(forms.ModelForm):
    class Meta:
       model = PedidoItem
       fields = ["producto", "cantidad", "precio_unitario"]
       widgets = {
           "cantidad": forms.NumberInput(attrs={"min": "1", "step": "1"}),
            "precio_unitario": forms.NumberInput(attrs={"min": "0", "step": "0.01"}) }
       
PedidoItemFormSet = inlineformset_factory(
    parent_model=Pedido,
    model=PedidoItem,
    form=PedidoItemForm,
    extra=1,
    can_delete=True,
)