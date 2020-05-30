from django.db import models

# モデルの設定
class Question(models.Model):
  # question_textをテキスト形式で
  # 200文字までに制限
  question_text = models.CharField(max_length=200)
  # 公開時間を時間形式で
  # 名前はdata published
  pub_date = models.DateTimeField('data published')

class Choice(models.Model):

  # Questionモデルとのリレーションシップを設定
  # Questionモデルを削除した場合、Choiceも削除
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)