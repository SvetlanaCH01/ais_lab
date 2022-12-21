from django.db import models
from django.db.models import *
from django.utils import timezone

# Create your models here.
class Reception(Model):
    """ Таблица приемов (пациент, врач, дата приема, цель визита, диагноз, клинические рекомендации"""
    id = AutoField(primary_key=True)     # объявление первичного ключа с автоикрементом
    purpose_of_visit = CharField(max_length=255, null=False)
    # связь полей patient, doctor и diagnosis через внешние ключи
    patient = ForeignKey('Patient', null=False, on_delete=CASCADE)
    doctor = ForeignKey('Doctor', null=False, on_delete=CASCADE)
    diagnosis = ForeignKey('Diagnosis', null=False, on_delete=CASCADE)

    clinical_guid = TextField(null=False)
    created_on = DateTimeField(auto_now_add=True)   # в поле автоматически генерируется метка времени при создании записи
    updated_on = DateTimeField(auto_now=True)       # в поле автоматически генерируется метка времени при создании записи, метка обновляется при каждой операции UPDATE

    class Meta:
        """ Установка названия таблицы """
        db_table = 'reception'


    def __str__(self):
        """ Метод определяет строковое представление модели """
        return str({'purpose_of_visit': self.purpose_of_visit, 'patient': self.patient,
                    'doctor': self.doctor, 'diagnosis': self.diagnosis, 'clinical_guid': self.clinical_guid,'created_on': self.created_on, 'updated_on': self.updated_on})


class Doctor(Model):
    """ Таблица врачей (ФИО, логин, пароль, телефон) """
    id = AutoField(primary_key=True)
    surname= CharField(max_length=255, null=False)
    name= CharField(max_length=255, null=False)
    patronymic= CharField(max_length=255, null=False)
    login= CharField(max_length=255, null=False, unique=True)
    password= CharField(max_length=255, null=False, unique=True)
    phone_number= CharField(max_length=11, null=False, unique=True)
    class Meta:
        db_table = 'doctor'

    def __str__(self):
        return str({'id': self.id, 'surname': self.surname, 'name': self.name, 'patronymic': self.patronymic})

class Diagnosis(Model):
    """ Таблица с диагнозами (название) """
    id = AutoField(primary_key=True)
    name= CharField(max_length=255, null=False, unique=True)
    class Meta:
        db_table = 'diagnosis'

    def __str__(self):
        return str({'id': self.id, 'name': self.name})

class Patient(Model):
    """ Таблица с пациентами (ФИО, дата рождения, паспорт, адрес, телефон) """
    id = AutoField(primary_key=True)
    surname= CharField(max_length=255, null=False)
    name= CharField(max_length=255, null=False)
    patronymic= CharField(max_length=255, null=False)
    date_of_birth = DateField(null=False)
    passport_ID = CharField(max_length=10, null=False, unique=True)
    address= CharField(max_length=255, null=False)
    phone_number= CharField(max_length=11, null=False, unique=True)

    class Meta:
        db_table = 'patient'

    def __str__(self):
        return str({'id': self.id, 'surname': self.surname, 'name': self.name, 'patronymic': self.patronymic})