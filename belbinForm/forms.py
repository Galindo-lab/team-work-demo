from django import forms

from django.core.validators import (MaxValueValidator, MinValueValidator)
from belbinForm.models import BelbinQuestionary


def BelbinQuestionaryField():
    """
    Genera un campo para el formulario, evita la repoteicion
    inesesaria de codigo
    """
    return forms.IntegerField(
        max_value=10,
        min_value=0,
        validators=[MaxValueValidator(10),
                    MinValueValidator(0)])


class BelbinQuestionaryForm(forms.Form):
    # 1: ¿Qué es lo que yo creo que puedo aportar a un equipo?

    section_1_question_a = BelbinQuestionaryField()  # cf
    section_1_question_b = BelbinQuestionaryField()  # tw
    section_1_question_c = BelbinQuestionaryField()  # pl
    section_1_question_d = BelbinQuestionaryField()  # co
    section_1_question_e = BelbinQuestionaryField()  # ri
    section_1_question_f = BelbinQuestionaryField()  # sh
    section_1_question_g = BelbinQuestionaryField()  # imp
    section_1_question_h = BelbinQuestionaryField()  # me
    section_1_question_i = BelbinQuestionaryField()  # sp

    # # 2: Si tuviera algún problema trabajando en equipo, podría
    # #    ser debido a:

    # section_2_question_a = BelbinQuestionaryField()  # imp
    # section_2_question_b = BelbinQuestionaryField()  # co
    # section_2_question_c = BelbinQuestionaryField()  # cf
    # section_2_question_d = BelbinQuestionaryField()  # me
    # section_2_question_e = BelbinQuestionaryField()  # sh
    # section_2_question_f = BelbinQuestionaryField()  # tw
    # section_2_question_g = BelbinQuestionaryField()  # pl
    # section_2_question_h = BelbinQuestionaryField()  # ri
    # section_2_question_i = BelbinQuestionaryField()  # sp

    # # 3: Cuando estoy metido en un proyecto con otras personas:

    # section_3_question_a = BelbinQuestionaryField()  # co
    # section_3_question_b = BelbinQuestionaryField()  # ri
    # section_3_question_c = BelbinQuestionaryField()  # sh
    # section_3_question_d = BelbinQuestionaryField()  # pl
    # section_3_question_e = BelbinQuestionaryField()  # tw
    # section_3_question_f = BelbinQuestionaryField()  # cf
    # section_3_question_g = BelbinQuestionaryField()  # me
    # section_3_question_h = BelbinQuestionaryField()  # imp
    # section_3_question_i = BelbinQuestionaryField()  # sp

    # # 4.- Mi forma de abordar el trabajo en equipo es:

    # section_4_question_a = BelbinQuestionaryField()  # tw
    # section_4_question_b = BelbinQuestionaryField()  # sh
    # section_4_question_c = BelbinQuestionaryField()  # me
    # section_4_question_d = BelbinQuestionaryField()  # imp
    # section_4_question_e = BelbinQuestionaryField()  # pl
    # section_4_question_f = BelbinQuestionaryField()  # ri
    # section_4_question_g = BelbinQuestionaryField()  # cf
    # section_4_question_h = BelbinQuestionaryField()  # co
    # section_4_question_i = BelbinQuestionaryField()  # sp

    # # 5: Obtengo satisfacción de un trabajo porque...

    # section_5_question_a = BelbinQuestionaryField()  # me
    # section_5_question_b = BelbinQuestionaryField()  # imp
    # section_5_question_c = BelbinQuestionaryField()  # tw
    # section_5_question_d = BelbinQuestionaryField()  # sh
    # section_5_question_e = BelbinQuestionaryField()  # cf
    # section_5_question_f = BelbinQuestionaryField()  # co
    # section_5_question_g = BelbinQuestionaryField()  # ri
    # section_5_question_h = BelbinQuestionaryField()  # pl
    # section_5_question_i = BelbinQuestionaryField()  # sp

    # # 6: Si de repente me dan la responsabilidad de una tarea
    # #    difícil, con un tiempo limitado y gente desconocida:

    # section_6_question_a = BelbinQuestionaryField()  # pl
    # section_6_question_b = BelbinQuestionaryField()  # tw
    # section_6_question_c = BelbinQuestionaryField()  # co
    # section_6_question_d = BelbinQuestionaryField()  # ri
    # section_6_question_e = BelbinQuestionaryField()  # me
    # section_6_question_f = BelbinQuestionaryField()  # imp
    # section_6_question_g = BelbinQuestionaryField()  # sh
    # section_6_question_h = BelbinQuestionaryField()  # cf
    # section_6_question_i = BelbinQuestionaryField()  # sp

    # # 7: Haciendo referencia a los problemas que tengo
    # #    trabajando en equipo:

    # section_7_question_a = BelbinQuestionaryField()  # sh
    # section_7_question_b = BelbinQuestionaryField()  # me
    # section_7_question_c = BelbinQuestionaryField()  # ri
    # section_7_question_d = BelbinQuestionaryField()  # cf
    # section_7_question_e = BelbinQuestionaryField()  # imp
    # section_7_question_f = BelbinQuestionaryField()  # pl
    # section_7_question_g = BelbinQuestionaryField()  # co
    # section_7_question_h = BelbinQuestionaryField()  # tw
    # section_7_question_i = BelbinQuestionaryField()  # sp

    def get(self,section="", question=""):
        return self.cleaned_data[f'section_{section}_question_{question}']
        
    def section_data(self, imp, co, sh, pl, cf, me, tw, ri, sp):
        param_dic = locals()
        del param_dic["self"]
        return param_dic

    def get_section_1(self):
        return self.section_data(
            imp = self.get(section="1", question="g"),
            co = self.get(section="1", question="d"),
            sh = self.get(section="1", question="f"),
            pl = self.get(section="1", question="c"),
            cf = self.get(section="1", question="a"),
            me = self.get(section="1", question="h"),
            tw = self.get(section="1", question="b"),
            ri = self.get(section="1", question="e"),
            sp = self.get(section="1", question="i")
        )
        
