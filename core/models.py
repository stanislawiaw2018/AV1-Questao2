from django.db import models

# Create your models here.

class Turma(models.Model):
    nome = models.CharField("Nome", max_length=10, default='')
    #num = models.IntegerField("Número da Turma",null=True,blank=True)
    datai= models.DateField("Data Inicio",null=False,blank=False)
    dataf= models.DateField("Data Termino" , null=False, blank=False)
    horai= models.TimeField("Horario Inicial", null=False, blank=False)
    horaf= models.TimeField("Horario Termino", null=False,blank=False)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

    def __str__(self):
        return self.nome


class Professor(models.Model):
    turma = models.ForeignKey( Turma,on_delete=models.CASCADE)
    nome = models.CharField("Nome", max_length=50, null=False,blank=False)
    carga = models.IntegerField("Carga Horaria", null=False,blank=False)
    telefone = models.CharField("Telefone", max_length=12 ,null=False, blank=False)
    valor = models.DecimalField("Hora/aula", null=False, blank=False, max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"

    def __str__(self):
        return self.nome

class Curso(models.Model):
    turma = models.ForeignKey(Turma,on_delete=models.CASCADE)
    nome = models.CharField("Nome", max_length=50,null=False,blank=False)
    carga_horaria = models.IntegerField("Carga_Horaria",null=False,blank=False)
    ementa = models.TextField("Ementa", null=False , blank=False)
    valor = models.DecimalField("Valor_curso", max_digits=6,decimal_places=2)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return str(self.nome)

