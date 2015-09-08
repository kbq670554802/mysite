from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline): 参数不同布局不同
class ChoiceInline(admin.TabularInline):  # 表格布局
    model = Choice
    extra = 3


class QuestionAmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('基本信息', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 多了详细信息
    list_filter = ['pub_date']  # 条件过滤
    search_fields = ['question_text']


admin.site.register(Question, QuestionAmin)
# admin.site.register(Choice)
