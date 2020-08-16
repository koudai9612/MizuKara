from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User

class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    type_choice = (
        (1, '水'),
        (2, 'お茶'),
        (3, 'ジュース'),
    )

    type = models.IntegerField(
        verbose_name='飲み物',
        choices=type_choice,
        #blank=True,
        null=True,
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)]
    )

    amount = models.IntegerField(
        verbose_name='量',
        #blank=True,
        null=True,
    )

    date = models.DateField(
        verbose_name='日付',
        #blank=True,
        null=True,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.type

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
