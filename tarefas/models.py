from django.db import models

# Create your models here.


# class Usuario(models.Model):
#     pes_cod = models.AutoField(primary_key=True)
#     pes_nome = models.CharField("Nome", max_length=100)
#     pes_email = models.EmailField("E-mail", unique=True)
#     senha = models.CharField("Senha", max_length=100)
#     data_criacao = models.DateTimeField("Data de Criação", auto_now_add=True)

#     def __str__(self):
#         return self.nome
    

class Tarefas(models.Model):
    id = models.AutoField( primary_key=True) 
    titulo = models.CharField(("nome"), max_length=250)
    prioridade = models.CharField(("prioridade"), max_length=1)
    area = models.CharField(("area"), max_length=50)
    status = models.CharField(("status"), max_length=50)
    data_prazo = models.DateField()
    # pes_cod = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    