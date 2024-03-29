# Generated by Django 2.0.3 on 2018-04-17 13:07
# -*- coding: utf-8 -*-
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerSheetA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qa1', models.IntegerField(verbose_name='การหกล้มอาจทำให้กระดูกหักได้')),
                ('qa2', models.IntegerField(verbose_name='ถ้าท่านหกล้มศีรษะกระแทกพื้นทำให้ได้รับบาดเจ็บรุนแรงถึงขั้นเสียชีวิตได้')),
                ('qa3', models.IntegerField(verbose_name='หากท่านไม่จัดการสิ่งกีดขวางเกะกะทางเดินอาจทำให้ท่านพิการจากการหกล้มได้')),
                ('qa4', models.IntegerField(verbose_name='หากท่านไม่จัดการสิ่งแวดล้อมภายในบ้านจะทำให้ท่านหกล้มเกิดการบาดเจ็บศีรษะกระแทกพื้นและมีโอกาสเสียชีวิตได้')),
                ('qa5', models.IntegerField(verbose_name='หากท่านไม่ปฏิบัติท่ากายบริหารเพื่อความแข็งแรงของกล้ามเนื้อจะทำให้หกล้มศีรษะกระแทกพื้นเป็นอัมพาตได้ง่าย')),
                ('qa6', models.IntegerField(verbose_name='หากท่านไม่ปฏิบัติตัวตามคำแนะนำของบุคลากรทางการแพทย์ในการป้องกันการหกล้มจะทำให้ท่านหกล้มกระดูกสะโพกหัก')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSheetB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qb1', models.IntegerField(verbose_name='ท่านเชื่อว่าการหกล้มเกิดจากการไม่จัดการสิ่งแวดล้อมภายในบ้าน')),
                ('qb2', models.IntegerField(verbose_name='ท่านเชื่อว่าการหกล้มเกิดจากกล้ามเนื้อไม่แข็งแรงเนื่องจากไม่ปฏิบัติท่ากายบริหาร')),
                ('qb3', models.IntegerField(verbose_name='พื้นห้องน้ำห้องส้วมที่บ้านเปียกอาจจะทำให้ท่านหกล้มได้ง่าย')),
                ('qb4', models.IntegerField(verbose_name='แสงสว่างที่บ้านไม่เพียงพอโดยเฉพาะบริเวณบันได ห้องน้ำ ทำให้เสี่ยงต่อการหกล้มได้')),
                ('qb5', models.IntegerField(verbose_name='การที่บ้านท่านไม่มีการจัดการสิ่งแวดล้อม เช่น ราวจับ ประตู ทางลาด ทำให้เสี่ยงต่อการหกล้มได้ง่าย')),
                ('qb6', models.IntegerField(verbose_name='การที่ภายในบ้านมีสิ่งกีดขวาง เกะกะทางเดิน เช่น สายไฟ ข้าวของ เครื่องใช้ทำให้เสี่ยงต่อการหกล้มได้ง่าย')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSheetC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qc1', models.IntegerField(verbose_name='การปฏิบัติท่ากายบริหารทำให้กล้ามเนื้อแข็งแรงจึงไม่เกิดการหกล้มบาดเจ็บได้')),
                ('qc2', models.IntegerField(verbose_name='การจัดการภายในบ้านไม่ให้มีสิ่งกีดขวาง เกะกะทางเดิน เช่น สายไฟ ข้าวของ เครื่องใช้จะช่วยป้องกันการหกล้มได้')),
                ('qc3', models.IntegerField(verbose_name='แสงสว่างที่บ้านเพียงพอโดยเฉพาะบริเวณบันได ห้องน้ำ จะช่วยลดความเสี่ยงต่อการหกล้มได้')),
                ('qc4', models.IntegerField(verbose_name='การมีราวจับจะช่วยป้องกันการเสียชีวิตจากการหกล้มศีรษะกระแทกพื้นได้')),
                ('qc5', models.IntegerField(verbose_name='การทรงตัวได้ดีจากการทำท่ากายบริหารเป็นประจำจะช่วยป้องกันการได้รับบาดเจ็บจากการหกล้ม')),
                ('qc6', models.IntegerField(verbose_name='การปฏิบัติตัวตามคำแนะนำของบุคลากรทางการแพทย์สามารถป้องกันการหกล้มได้')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSheetD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qd1', models.IntegerField(verbose_name='ท่านสามารถทำท่ากายบริหารเป็นประจำได้')),
                ('qd2', models.IntegerField(verbose_name='ท่านสามารถจัดการภายในบ้านไม่ให้มีสิ่งกีดขวาง เกะกะทางเดิน เช่น สายไฟ ข้าวของ เครื่องใช้ได้')),
                ('qd3', models.IntegerField(verbose_name='ท่านสามารถจัดการให้ที่บ้านมีแสงสว่างเพียงพอได้ โดยเฉพาะบริเวณบันได ห้องน้ำ')),
                ('qd4', models.IntegerField(verbose_name='ท่านสามารถปฏิบัติพฤติกรรมการป้องกันการพลัดตกหกล้มได้ตามคำแนะนำของบุคลากรทางการแพทย์')),
                ('qd5', models.IntegerField(verbose_name='ท่านสามารถป้องกันการหกล้มด้วยการจัดการสิ่งแวดล้อมภายในบ้าน เช่น ราวจับ ประตู ทางลาด')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSheetE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qe1', models.IntegerField(verbose_name='ท่านตั้งใจทำท่ากายบริหารเป็นประจำได้')),
                ('qe2', models.IntegerField(verbose_name='ท่านตั้งใจจัดการภายในบ้านไม่ให้มีสิ่งกีดขวาง เกะกะทางเดิน เช่น สายไฟ ข้าวของ เครื่องใช้ได้')),
                ('qe3', models.IntegerField(verbose_name='ท่านตั้งใจจัดการให้ที่บ้านมีแสงสว่างเพียงพอได้ โดยเฉพาะบริเวณบันได ห้องน้ำ')),
                ('qe4', models.IntegerField(verbose_name='ท่านตั้งใจปฏิบัติพฤติกรรมการป้องกันการพลัดตกหกล้มได้ตามคำแนะนำของบุคลากรทางการแพทย์')),
                ('qe5', models.IntegerField(verbose_name='ท่านตั้งใจป้องกันการหกล้มด้วยการจัดการสิ่งแวดล้อมภายในบ้าน เช่น ราวจับ ประตู ทางลาด')),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eye_sight', models.CharField(default='-', max_length=50)),
                ('balancing', models.CharField(default='-', max_length=50)),
                ('medication', models.CharField(default='-', max_length=100)),
                ('falling_in_6_months', models.CharField(default='-', max_length=50)),
                ('home', models.CharField(default='-', max_length=50)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.FloatField(default=0)),
                ('quest_A', models.FloatField(default=0)),
                ('quest_B', models.FloatField(default=0)),
                ('quest_C', models.FloatField(default=0)),
                ('quest_D', models.FloatField(default=0)),
                ('quest_E', models.FloatField(default=0)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='-', max_length=10, verbose_name='gender')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('age_range', models.CharField(default='-', max_length=50)),
                ('marriage', models.CharField(default='-', max_length=50)),
                ('education', models.CharField(default='-', max_length=50)),
                ('live_with', models.CharField(default='-', max_length=50)),
                ('live_with_detail', models.CharField(default='-', max_length=255)),
                ('guardian', models.CharField(default='-', max_length=50)),
                ('guardian_detail', models.CharField(default='-', max_length=255)),
                ('occupation', models.CharField(default='-', max_length=50)),
                ('income_avg', models.CharField(default='-', max_length=50)),
                ('chronic_dis', models.CharField(default='-', max_length=50)),
                ('chronic_dis_detail', models.CharField(default='-', max_length=255)),
                ('chronic_dis_time', models.CharField(default='-', max_length=50)),
                ('medi_number', models.CharField(default='-', max_length=50)),
                ('medi_detail', models.CharField(default='-', max_length=255)),
                ('hyperventi_medi', models.CharField(default='-', max_length=50)),
                ('hyperventi_detail', models.CharField(default='-', max_length=255)),
                ('fall_hist', models.CharField(default='-', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='scorecard',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='risk',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='answersheete',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='answersheetd',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='answersheetc',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='answersheetb',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='answersheeta',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.UserProfile'),
        ),
    ]
