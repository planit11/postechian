from django.db import models
from core import models as core_models

# Create your models here.


class Article(core_models.TimeStampedModel):

    BOARD_ANNOUNCE = "공지사항"
    BOARD_NEWS = "동문소식"

    BOARD_CHOICES = (
        (BOARD_ANNOUNCE, "공지사항"),
        (BOARD_NEWS, "동문소식"),
    )

    board = models.CharField(
        max_length=12, choices=BOARD_CHOICES, default=BOARD_ANNOUNCE
    )    

    STATUS_PENDING = "작성중"
    STATUS_CONFIRMED = "작성완료"

    STATUS_CHOICES = (
        (STATUS_PENDING, "작성중"),
        (STATUS_CONFIRMED, "작성완료"),
    )

    thumnail = models.ImageField(upload_to="article_img", null=True)

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )

    title = models.CharField(max_length=80, default="")
    created_on = models.DateField(auto_now_add=True, null=True)
    display_date = models.DateField(null=True)
    author = models.ForeignKey("users.User", related_name="articles", on_delete=models.CASCADE, default="")

    content = models.TextField(null=True, blank=True, default="")

    def __str__(self):
        return f"{self.author} - {self.title} - {self.created_on}"
