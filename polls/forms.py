from django import forms


class form_UserProfile(forms.Form):
    gender = forms.CharField(label='gender')
    age_range = forms.CharField(label='age_range')
    marriage = forms.CharField(label='marriage')
    education = forms.CharField(label='education')
    live_with = forms.CharField(label='live_with')
    live_with_detail = forms.CharField(label='live_with_detail')
    guardian = forms.CharField(label='guardian')
    occupation = forms.CharField(label='occupation')
    income_avg = forms.CharField(label='income_avg')
    chronic_dis = forms.CharField(label='chronic_dis')
    chronic_dis_detail = forms.CharField(label='chronic_dis_detail')
    chronic_dis_time = forms.CharField(label='chronic_dis_time')
    medi_number = forms.CharField(label='medi_number')
    medi_detail = forms.CharField(label='medi_detail')
    hyperventi_medi = forms.CharField(label='hyperventi_medi')
    hyperventi_detail = forms.CharField(label='hyperventi_detail')
    fall_his = forms.CharField(label='fall_his')


class form_AnswerSheetAB(forms.Form):
    user_id = forms.IntegerField(label='id')
    qa1 = forms.IntegerField(label='qa1')
    qa2 = forms.IntegerField(label='qa2')
    qa3 = forms.IntegerField(label='qa3')
    qa4 = forms.IntegerField(label='qa4')
    qa5 = forms.IntegerField(label='qa5')
    qa6 = forms.IntegerField(label='qa6')
    qb1 = forms.IntegerField(label='qb1')
    qb2 = forms.IntegerField(label='qb2')
    qb3 = forms.IntegerField(label='qb3')
    qb4 = forms.IntegerField(label='qb4')
    qb5 = forms.IntegerField(label='qb5')
    qb6 = forms.IntegerField(label='qb6')


class form_AnswerSheetC(forms.Form):
    user_id = forms.IntegerField(label='id')
    qc1 = forms.IntegerField(label='qc1')
    qc2 = forms.IntegerField(label='qc2')
    qc3 = forms.IntegerField(label='qc3')
    qc4 = forms.IntegerField(label='qc4')
    qc5 = forms.IntegerField(label='qc5')
    qc6 = forms.IntegerField(label='qc6')


class form_intermediate(forms.Form):
    user_id = forms.IntegerField(label='id')


class form_AnswerSheetD(forms.Form):
    user_id = forms.IntegerField(label='id')
    qd1 = forms.IntegerField(label='qd1')
    qd2 = forms.IntegerField(label='qd2')
    qd3 = forms.IntegerField(label='qd3')
    qd4 = forms.IntegerField(label='qd4')
    qd5 = forms.IntegerField(label='qd5')

class form_AnswerSheetE(forms.Form):
    user_id = forms.IntegerField(label='id')
    qe1 = forms.IntegerField(label='qe1')
    qe2 = forms.IntegerField(label='qe2')
    qe3 = forms.IntegerField(label='qe3')
    qe4 = forms.IntegerField(label='qe4')
    qe5 = forms.IntegerField(label='qe5')

class form_risk(forms.Form):
    user_id = forms.IntegerField(label='id')
    eye_sight = forms.CharField(label = 'eye_sight')
    balancing = forms.CharField(label='balancing')
    medication = forms.CharField(label='medication')
    falling_in_6_months = forms.CharField(label ='falling')
    home = forms.CharField(label='home')
