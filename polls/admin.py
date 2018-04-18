from django.contrib import admin
from .models import ScoreCard, UserProfile, AnswerSheetA, AnswerSheetB, AnswerSheetC, AnswerSheetD, AnswerSheetE, Risk


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'age_range',)
    ordering = ['id', ]
    list_filter = ('age_range',)
    search_fields = ('id',)


class AnswerA_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'qa1', 'qa2', 'qa3', 'qa4', 'qa5', 'qa6',)
    list_filter = ('qa1', 'qa2', 'qa3', 'qa4', 'qa5', 'qa6',)
    search_fields = ('user_id',)


class AnswerB_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'qb1', 'qb2', 'qb3', 'qb4', 'qb5', 'qb6',)
    search_fields = ('user_id',)
    list_filter = ('qb1', 'qb2', 'qb3', 'qb4', 'qb5', 'qb6',)


class AnswerC_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'qc1', 'qc2', 'qc3', 'qc4', 'qc5', 'qc6',)
    list_filter = ('qc1', 'qc2', 'qc3', 'qc4', 'qc5', 'qc6',)
    search_fields = ('user_id',)


class AnswerD_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'qd1', 'qd2', 'qd3', 'qd4', 'qd5',)
    list_filter = ('qd1', 'qd2', 'qd3', 'qd4', 'qd5',)
    search_fields = ('user_id',)


class AnswerE_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'qe1', 'qe2', 'qe3', 'qe4', 'qe5',)
    list_filter = ('qe1', 'qe2', 'qe3', 'qe4', 'qe5',)
    search_fields = ('user_id',)


class ScoreCard_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'profile', 'quest_A', 'quest_B', 'quest_C', 'quest_D', 'quest_E', 'finished',)
    search_fields = ('user_id',)


class Risk_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'eye_sight', 'balancing', 'medication',
                    'home', 'score',)
    search_fields = ('user_id',)


# Register your models here.
admin.site.register(UserProfile, UserAdmin)
admin.site.register(AnswerSheetA, AnswerA_Admin)
admin.site.register(AnswerSheetB, AnswerB_Admin)
admin.site.register(AnswerSheetC, AnswerC_Admin)
admin.site.register(AnswerSheetD, AnswerD_Admin)
admin.site.register(AnswerSheetE, AnswerE_Admin)
admin.site.register(ScoreCard, ScoreCard_Admin)
admin.site.register(Risk, Risk_Admin)
