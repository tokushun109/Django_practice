import datetime

from django.db import models
from django.utils import timezone

# モデルの設定
class Question(models.Model):
  # question_textをテキスト形式で
  # 200文字までに制限
  question_text = models.CharField(max_length=200)
  # 公開時間を時間形式で
  # 名前はdata published
  pub_date = models.DateTimeField('data published')
  def __str__(self):
        return self.question_text
  
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):

  # Questionモデルとのリレーションシップを設定
  # Questionモデルを削除した場合、Choiceも削除
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  
  def __str__(self):
        return self.choice_text
