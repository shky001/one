# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models



class Candidate(models.Model):
    userid = models.IntegerField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=135)
    city = models.CharField(max_length=135)
    phone = models.CharField(max_length=135)
    email = models.CharField(max_length=135)
    apply_position = models.CharField(max_length=135)
    born_address = models.CharField(max_length=135)
    gender = models.CharField(max_length=135)
    candidate_remark = models.CharField(max_length=135)
    bachelor_school = models.CharField(max_length=135)
    master_school = models.CharField(max_length=135)
    doctor_school = models.CharField(max_length=135)
    major = models.CharField(max_length=135)
    degree = models.CharField(max_length=135)
    test_score_of_general_ability = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    paper_score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    first_score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    first_learning_ability = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    first_professional_competency = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    first_advantage = models.TextField()
    first_disadvantage = models.TextField()
    first_result = models.CharField(max_length=256)
    first_recommend_position = models.CharField(max_length=256)
    first_remark = models.CharField(max_length=135)
    second_score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    second_learning_ability = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    second_professional_competency = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    second_pursue_of_excellence = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    second_communication_ability = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    second_pressure_score = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    second_advantage = models.TextField()
    second_disadvantage = models.TextField()
    second_result = models.CharField(max_length=256)
    second_recommend_position = models.CharField(max_length=256)
    second_remark = models.CharField(max_length=135)
    hr_score = models.CharField(max_length=10)
    hr_responsibility = models.CharField(max_length=10)
    hr_communication_ability = models.CharField(max_length=10)
    hr_logic_ability = models.CharField(max_length=10)
    hr_potential = models.CharField(max_length=10)
    hr_stability = models.CharField(max_length=10)
    hr_advantage = models.TextField()
    hr_disadvantage = models.TextField()
    hr_result = models.CharField(max_length=256)
    hr_remark = models.CharField(max_length=256)
    creator = models.CharField(max_length=256)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    last_editor = models.CharField(max_length=256)
    first_interviewer_user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='first_interviewer_user')
    hr_interviewer_user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='hr_interviewer_user')
    second_interviewer_user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='second_interviewer_user')

    class Meta:
        managed = False
        db_table = 'candidate'


class JobsJob(models.Model):
    job_type = models.SmallIntegerField()
    job_name = models.CharField(max_length=250)
    job_city = models.SmallIntegerField()
    job_responsibility = models.TextField()
    job_requirement = models.TextField()
    created_date = models.DateTimeField()
    creator = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jobs_job'


class JobsResume(models.Model):
    username = models.CharField(max_length=135)
    city = models.CharField(max_length=135)
    phone = models.CharField(max_length=135)
    email = models.CharField(max_length=135)
    apply_position = models.CharField(max_length=135)
    born_address = models.CharField(max_length=135)
    gender = models.CharField(max_length=135)
    picture = models.CharField(max_length=100)
    attachment = models.CharField(max_length=100)
    bachelor_school = models.CharField(max_length=135)
    master_school = models.CharField(max_length=135)
    doctor_school = models.CharField(max_length=135)
    major = models.CharField(max_length=135)
    degree = models.CharField(max_length=135)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    candidate_introduction = models.TextField()
    work_experience = models.TextField()
    project_experience = models.TextField()
    applicant = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs_resume'

