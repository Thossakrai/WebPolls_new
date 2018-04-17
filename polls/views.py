# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Risk,UserProfile, AnswerSheetA, AnswerSheetE, AnswerSheetC, AnswerSheetD, AnswerSheetB, ScoreCard
from .forms import form_risk ,form_UserProfile, form_AnswerSheetAB, form_AnswerSheetC, form_intermediate, form_AnswerSheetD, \
    form_AnswerSheetE
from django.template import RequestContext
import json


# Create your views here.


def get_UserProfile(request):
    if request.method == 'POST':
        data = form_UserProfile(request.POST).data

        gender = data['gender']
        age_range = data['age']
        education = data['education']
        live_with = data['live_with']
        marriage = data['marriage']
        live_with_detail = data['live_with_detail']
        guardian = data['guardian']
        guardian_detail = data['guardian_detail']
        occupation = data['occupation']
        income_avg = data['income_avg']
        chronic_dis = data['chronic_dis']
        chronic_dis_detail = data['chronic_dis_detail']
        chronic_dis_time = data['chronic_dis_time']
        medi_number = data['medi_number']
        medi_detail = data['medi_detail']
        hyperventi_medi = data['hyperventi_medi']
        hyperventi_detail = data['hyperventi_detial']
        fall_hist = data['fall_hist']

        eye_sight = data['eye_sight']
        balancing = data['balancing']
        medication = data['medication']
        falling = data['falling']
        home = data['home']


        new_user = UserProfile(gender=gender, age_range=age_range, education=education, marriage=marriage,
                               live_with=live_with, live_with_detail=live_with_detail
                               , guardian=guardian, guardian_detail=guardian_detail, occupation=occupation,
                               income_avg=income_avg
                               , chronic_dis=chronic_dis, chronic_dis_detail=chronic_dis_detail,
                               chronic_dis_time=chronic_dis_time,
                               medi_number=medi_number, medi_detail=medi_detail, hyperventi_medi=hyperventi_medi,
                               hyperventi_detail=hyperventi_detail,
                               fall_hist=fall_hist)
        new_user.save()
        user_id = new_user.id




        score = 0
        if gender == 'หญิง' : score += 1
        if eye_sight == 'บกพร่อง' : score += 1
        if balancing == 'บกพร่อง' : score += 2
        if medication == 'บกพร่อง' : score += 1
        if falling == 'มีความเสี่ยง' : score += 5
        if home == 'มีความเสี่ยง' : score += 1

        new_risk = Risk(user_id_id=user_id, eye_sight=eye_sight, balancing=balancing, medication=medication,
                        falling_in_6_months=falling, home=home, score=score)
        new_risk.save()

        new_score = ScoreCard(user_id_id=user_id, profile=score)
        new_score.save()

        content = {'user_id': user_id}
        print(user_id)
        return render(request, 'polls/Quest1.html', content)

    else:
        data = UserProfile()

    return render(request, 'polls/start.html', {'data': data})


def questionnaire_part1(request):
    if request.method == 'POST':
        data = form_AnswerSheetAB(request.POST).data
        # print(data)

        qa1 = data['QA1']
        qa2 = data['QA2']
        qa3 = data['QA3']
        qa4 = data['QA4']
        qa5 = data['QA5']
        qa6 = data['QA6']

        qb1 = data['QB1']
        qb2 = data['QB2']
        qb3 = data['QB3']
        qb4 = data['QB4']
        qb5 = data['QB5']
        qb6 = data['QB6']

        user_id = int(data['id'])

        answerA = AnswerSheetA(user_id_id=user_id, qa1=qa1, qa2=qa2, qa3=qa3, qa4=qa4,
                               qa5=qa5, qa6=qa6)
        answerA.save()
        answerB = AnswerSheetB(user_id_id=user_id, qb1=qb1, qb2=qb2, qb3=qb3, qb4=qb4,
                               qb5=qb5, qb6=qb6)
        answerB.save()

        avgA = sum([int(qa1), int(qa2), int(qa3), int(qa4), int(qa5), int(qa6)]) / 6
        avgB = sum([int(qb1), int(qb2), int(qb3), int(qb4), int(qb5), int(qb6)]) / 6

        score_card = ScoreCard.objects.get(user_id_id=user_id)
        score_card.quest_A = avgA
        score_card.quest_B = avgB
        score_card.save()

        content = {'user_id': user_id}
        return render(request, 'polls/vid1.html', content)
    return None


def vid_part1(request):
    if (request.method == 'POST'):
        data = form_intermediate(request.POST).data
        user_id = int(data['user_id'])
        print(user_id)
        content = {'user_id': user_id}
        return render(request, 'polls/info1.html', content)


def infographic(request):
    if (request.method == 'POST'):
        data = form_intermediate(request.POST).data
        user_id = int(data['user_id'])

        content = {'user_id': user_id}
        return render(request, 'polls/Quest2.html', content)


def questionnaire_part3(request):
    if request.method == 'POST':
        data = form_AnswerSheetC(request.POST).data
        # print(data)

        qc1 = data['QC1']
        qc2 = data['QC2']
        qc3 = data['QC3']
        qc4 = data['QC4']
        qc5 = data['QC5']
        qc6 = data['QC6']

        user_id = data['user_id']

        avgC = sum([int(qc1), int(qc2), int(qc3), int(qc4), int(qc5), int(qc6)]) / 6

        score_card = ScoreCard.objects.get(user_id_id=user_id)
        score_card.quest_C = avgC

        score_card.save()

        answerC = AnswerSheetC(user_id_id=user_id, qc1=qc1, qc2=qc2, qc3=qc3, qc4=qc4, qc5=qc5, qc6=qc6)
        answerC.save()

        content = {'user_id': user_id}
        return render(request, 'polls/quest3.html', content)
    return None


def questionnaire_part4(request):
    if request.method == 'POST':
        data = form_AnswerSheetD(request.POST).data
        qd1 = data['QD1']
        qd2 = data['QD2']
        qd3 = data['QD3']
        qd4 = data['QD4']
        qd5 = data['QD5']

        user_id = data['user_id']

        avgD = sum([int(qd1), int(qd2), int(qd3), int(qd4), int(qd5)]) / 5

        score_card = ScoreCard.objects.get(user_id_id=user_id)
        score_card.quest_D = avgD

        score_card.save()

        answerD = AnswerSheetD(user_id_id=user_id, qd1=qd1, qd2=qd2, qd3=qd3, qd4=qd4, qd5=qd5)
        answerD.save()

        content = {'user_id': user_id}
        return render(request, 'polls/vid2.html', content)
    return None


def vid_part2(request):
    if (request.method == 'POST'):
        data = form_intermediate(request.POST).data
        user_id = int(data['user_id'])
        print(user_id)
        content = {'user_id': user_id}
        return render(request, 'polls/vid3.html', content)
    return None


def vid_part3(request):
    if (request.method == 'POST'):
        data = form_intermediate(request.POST).data
        user_id = int(data['user_id'])
        print(user_id)
        content = {'user_id': user_id}
        return render(request, 'polls/quest4.html', content)
    return None



def questionnaire_part5(request):
    if request.method == 'POST':
        data = form_AnswerSheetE(request.POST).data
        user_id = int(data['user_id'])
        qe1 = data['QE1']
        qe2 = data['QE2']
        qe3 = data['QE3']
        qe4 = data['QE4']
        qe5 = data['QE5']

        avgE = sum([int(qe1), int(qe2), int(qe3), int(qe4), int(qe5)]) / 5

        score_card = ScoreCard.objects.get(user_id_id=user_id)
        score_card.quest_E = avgE

        if score_card.quest_A > 0 and score_card.quest_B > 0 and score_card.quest_C > 0 and score_card.quest_D > 0 and score_card.quest_E > 0:
            score_card.finished = True

        score_card.save()

        answerE = AnswerSheetE(user_id_id=user_id, qe1=qe1, qe2=qe2, qe3=qe3, qe4=qe4, qe5=qe5)
        answerE.save()
        content = {'user_id': user_id}
        return render(request, 'polls/complete.html', content)
    return None
