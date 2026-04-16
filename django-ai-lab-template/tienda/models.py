from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=1)
    
    def __str__(self):
        return self.nombre
    
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.email}" 
    
class Pedido(models.Model):
    ESTADOS = [
        ("CREADO", "Creado"),
        ("PAGADO", "Pagado"),
        ("ENVIADO", "Enviado"),
        ("CERRADO", "Cerrado"),
    ]
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")
    productos = models.ManyToManyField(Producto, related_name="pedidos")
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default="CREADO")
    
    def __str__(self):
        return f"Pedido #{self.pk} - {self.Cliente.nombre} ({self.estado})"
    