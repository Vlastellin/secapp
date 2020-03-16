from django.db import models

class Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    employee_login=models.CharField(max_length=255)
    employee_password=models.CharField(max_length=255)
    employee_fio=models.CharField(max_length=255)
    employee_f=models.CharField(max_length=255)
    employee_i=models.CharField(max_length=255)
    employee_o=models.CharField(max_length=255)
    employee_phone_number=models.CharField(max_length=255)
    employee_home_adress=models.CharField(max_length=255)
    employee_voice_example=models.CharField(max_length=255)
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        
        
# Create your models here.
class Object(models.Model):
    object_id=models.AutoField(primary_key=True)
    object_name=models.CharField(max_length=255)
    object_adress=models.CharField(max_length=255)
    object_positions_number=models.IntegerField()
    class Meta:
        verbose_name = "Object"
        verbose_name_plural = "Objects"

    def __unicode__(self):
        return self.object_name
    
class Position(models.Model):
    position_id=models.AutoField(primary_key=True)
    position_object = models.ForeignKey(Object, on_delete = models.PROTECT)
    position_phone_number=models.CharField(max_length=255)
    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"
    
class Mode(models.Model):
    mode_id = models.AutoField(primary_key=True)
    mode_value = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Mode"
        verbose_name_plural = "Modes"
    
class Call_Status(models.Model):
    call_status_id = models.AutoField(primary_key=True)
    call_status_value = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Call_Status"
        verbose_name_plural = "Call_Statuses"
    
class Call_Type(models.Model):
    type_call_id = models.AutoField(primary_key=True)
    type_call_value = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Call_Type"
        verbose_name_plural = "Call_Types"
    
class Type_ChP(models.Model):
    type_chp_id = models.AutoField(primary_key=True)
    type_chp_value = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Type_ChP"
        verbose_name_plural = "Type_ChPes"

class Status_ChP(models.Model):
    status_chp_id = models.AutoField(primary_key=True)
    status_chp_value = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Status_ChP"
        verbose_name_plural = "Status_ChPes"
    
class Period(models.Model):
    period_id = models.AutoField(primary_key=True)
    period_value = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Period"
        verbose_name_plural = "Periods"
    
class Plan(models.Model):
    plan_id=models.AutoField(primary_key=True)
    plan_day = models.CharField(max_length=255)
    plan_position = models.ForeignKey(Position, on_delete = models.PROTECT)
    plan_mode = models.ForeignKey(Mode, on_delete = models.PROTECT)
    plan_time_from = models.TimeField()
    plan_time_to = models.TimeField()
    plan_date = models.DateField(auto_now=True)
    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"
    
class Plan_raw(models.Model):
    plan_raw_id = models.AutoField(primary_key=True)
    plan_raw_plan = models.ForeignKey(Plan, on_delete = models.PROTECT)
    plan_raw_period = models.ForeignKey(Period, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Plan_raw"
        verbose_name_plural = "Plan_raws"

class Tick_ChP(models.Model):
    tick_chp_id=models.AutoField(primary_key=True)
    tick_chp_date = models.DateField()
    tick_chp_time = models.TimeField()
    tick_chp_position = models.ForeignKey(Position, on_delete = models.PROTECT)
    tick_chp_type = models.ForeignKey(Type_ChP, on_delete = models.PROTECT)
    tick_chp_record_path= models.CharField(max_length=255)
    tick_chp_app_path = models.CharField(max_length=255)
    tick_chp_employee = models.ForeignKey(Employee, on_delete = models.PROTECT)
    tick_chp_status = models.ForeignKey(Status_ChP, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Tick_ChP"
        verbose_name_plural = "Tick_ChPes"
    
    
    
class Close_ChP(models.Model):
    close_chp_id=models.AutoField(primary_key=True)
    close_chp_date = models.DateField()
    close_chp_time = models.TimeField()
    close_chp_employee = models.ForeignKey(Employee, on_delete = models.PROTECT)
    close_chp_is = models.ForeignKey(Tick_ChP, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Close_ChP"
        verbose_name_plural = "Close_ChPes"
    
class Call(models.Model):
    call_id=models.AutoField(primary_key=True)
    call_date = models.DateField()
    call_time = models.TimeField()
    call_position = models.ForeignKey(Position, on_delete = models.PROTECT)
    call_employee = models.ForeignKey(Employee, on_delete = models.PROTECT)
    call_type = models.ForeignKey(Call_Type, on_delete = models.PROTECT)
    call_status = models.ForeignKey(Call_Status, on_delete = models.PROTECT)
    call_path = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Call"
        verbose_name_plural = "Calls"
    
