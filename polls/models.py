from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    gender = models.CharField('gender', max_length=10, default='-')
    created_date = models.DateTimeField('date created', default=timezone.now)
    age_range = models.CharField(max_length=50, default='-')
    marriage = models.CharField(max_length=50, default='-')
    education = models.CharField(max_length=50, default='-')
    live_with = models.CharField(max_length=50, default='-')
    live_with_detail = models.CharField(max_length=255, default='-')
    guardian = models.CharField(max_length=50, default='-')
    guardian_detail = models.CharField(max_length=255, default='-')
    occupation = models.CharField(max_length=50, default='-')
    income_avg = models.CharField(max_length=50, default='-')
    chronic_dis = models.CharField(max_length=50, default='-')
    chronic_dis_detail = models.CharField(max_length=255, default='-')
    chronic_dis_time = models.CharField(max_length=50, default='-')
    medi_number = models.CharField(max_length=50, default='-')
    medi_detail = models.CharField(max_length=255, default='-')
    hyperventi_medi = models.CharField(max_length=50, default='-')
    hyperventi_detail = models.CharField(max_length=255, default='-')
    fall_hist = models.CharField(max_length=50, default='-')

    def __str__(self):
        return str(self.id)


class AnswerSheetA(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    qa1 = models.IntegerField('การหกล้มอาจทำให้กระดูกหักได้')
    qa2 = models.IntegerField('ถ้าท่านหกล้มศีรษะกระแทกพื้นทำให้ได้รับบาดเจ็บรุนแรงถึงขั้นเสียชีวิตได้')
    qa3 = models.IntegerField('หากท่านไม่จัดการสิ่งกีดขวางเกะกะทางเดินอาจทำให้ท่านพิการจากการหกล้มได้')
    qa4 = models.IntegerField(
        'หากท่านไม่จัดการสิ่งแวดล้อมภายในบ้านจะทำให้ท่านหกล้มเกิดการบาดเจ็บศีรษะกระแทกพื้นและมีโอกาสเสียชีวิตได้')
    qa5 = models.IntegerField(
        'หากท่านไม่ปฏิบัติท่ากายบริหารเพื่อความแข็งแรงของกล้ามเนื้อจะทำให้หกล้มศีรษะกระแทกพื้นเป็นอัมพาตได้ง่าย')
    qa6 = models.IntegerField(
        'หากท่านไม่ปฏิบัติตัวตามคำแนะนำของบุคลากรทางการแพทย์ในการป้องกันการหกล้มจะทำให้ท่านหกล้มกระดูกสะโพกหัก')

    def __str__(self):
        return str(self.user_id)


class AnswerSheetB(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    qb1 = models.IntegerField('ท่านเชื่อว่าการหกล้มเกิดจากการไม่จัดการสิ่งแวดล้อมภายในบ้าน')
    qb2 = models.IntegerField('ท่านเชื่อว่าการหกล้มเกิดจากกล้ามเนื้อไม่แข็งแรงเนื่องจากไม่ปฏิบัติท่ากายบริหาร')
    qb3 = models.IntegerField('พื้นห้องน้ำห้องส้วมที่บ้านเปียกอาจจะทำให้ท่านหกล้มได้ง่าย')
    qb4 = models.IntegerField('แสงสว่างที่บ้านไม่เพียงพอโดยเฉพาะบริเวณบันได ห้องน้ำ ทำให้เสี่ยงต่อการหกล้มได้')
    qb5 = models.IntegerField(
        'การที่บ้านท่านไม่มีการจัดการสิ่งแวดล้อม เช่น ราวจับ ประตู ทางลาด ทำให้เสี่ยงต่อการหกล้มได้ง่าย')
    qb6 = models.IntegerField(
        'การที่ภายในบ้านมีสิ่งกีดขวาง เกะกะทางเดิน เช่น สายไฟ ข้าวของ เครื่องใช้ทำให้เสี่ยงต่อการหกล้มได้ง่าย')


class AnswerSheetC(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    qc1 = models.IntegerField('การปฏิบัติท่ากายบริหารทำให้กล้ามเนื้อแข็งแรงจึงไม่เกิดการหกล้มบาดเจ็บได้')
    qc2 = models.IntegerField(
        'การจัดการภายในบ้านไม่ให้มีสิ่งกีดขวาง เกะกะทางเดิน เช่น สายไฟ ข้าวของ เครื่องใช้จะช่วยป้องกันการหกล้มได้')
    qc3 = models.IntegerField('แสงสว่างที่บ้านเพียงพอโดยเฉพาะบริเวณบันได ห้องน้ำ จะช่วยลดความเสี่ยงต่อการหกล้มได้')
    qc4 = models.IntegerField('การมีราวจับจะช่วยป้องกันการเสียชีวิตจากการหกล้มศีรษะกระแทกพื้นได้')
    qc5 = models.IntegerField('การทรงตัวได้ดีจากการทำท่ากายบริหารเป็นประจำจะช่วยป้องกันการได้รับบาดเจ็บจากการหกล้ม')
    qc6 = models.IntegerField('การปฏิบัติตัวตามคำแนะนำของบุคลากรทางการแพทย์สามารถป้องกันการหกล้มได้')


class AnswerSheetD(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    qd1 = models.IntegerField('ท่านสามารถทำท่ากายบริหารเป็นประจำได้')
    qd2 = models.IntegerField(
        'ท่านสามารถจัดการภายในบ้านไม่ให้มีสิ่งกีดขวาง เกะกะทางเดิน เช่น สายไฟ ข้าวของ เครื่องใช้ได้')
    qd3 = models.IntegerField('ท่านสามารถจัดการให้ที่บ้านมีแสงสว่างเพียงพอได้ โดยเฉพาะบริเวณบันได ห้องน้ำ')
    qd4 = models.IntegerField('ท่านสามารถปฏิบัติพฤติกรรมการป้องกันการพลัดตกหกล้มได้ตามคำแนะนำของบุคลากรทางการแพทย์')
    qd5 = models.IntegerField('ท่านสามารถป้องกันการหกล้มด้วยการจัดการสิ่งแวดล้อมภายในบ้าน เช่น ราวจับ ประตู ทางลาด')


class AnswerSheetE(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    qe1 = models.IntegerField('ท่านตั้งใจทำท่ากายบริหารเป็นประจำได้')
    qe2 = models.IntegerField(
        'ท่านตั้งใจจัดการภายในบ้านไม่ให้มีสิ่งกีดขวาง เกะกะทางเดิน เช่น สายไฟ ข้าวของ เครื่องใช้ได้')
    qe3 = models.IntegerField('ท่านตั้งใจจัดการให้ที่บ้านมีแสงสว่างเพียงพอได้ โดยเฉพาะบริเวณบันได ห้องน้ำ')
    qe4 = models.IntegerField('ท่านตั้งใจปฏิบัติพฤติกรรมการป้องกันการพลัดตกหกล้มได้ตามคำแนะนำของบุคลากรทางการแพทย์')
    qe5 = models.IntegerField('ท่านตั้งใจป้องกันการหกล้มด้วยการจัดการสิ่งแวดล้อมภายในบ้าน เช่น ราวจับ ประตู ทางลาด')


class ScoreCard(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    profile = models.FloatField(default=0)
    quest_A = models.FloatField(default=0)
    quest_B = models.FloatField(default=0)
    quest_C = models.FloatField(default=0)
    quest_D = models.FloatField(default=0)
    quest_E = models.FloatField(default=0)
    finished = models.BooleanField(default=False)


class Risk(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    eye_sight = models.CharField(max_length=50, default='-')
    balancing = models.CharField(max_length=50, default='-')
    medication = models.CharField(max_length=100, default='-')
    falling_in_6_months = models.CharField(max_length=50, default='-')
    home = models.CharField(max_length=50, default='-')
    score = models.IntegerField(default=0)