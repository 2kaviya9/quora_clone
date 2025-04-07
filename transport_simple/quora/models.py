from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModel(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_created",
        help_text="User who created this object."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when this object was created."
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_updated",
        null=True,
        blank=True,
        help_text="User who last updated this object."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when this object was last updated."
    )

    class Meta:
        abstract = True


class QuoraPost(BaseModel):
    question = models.TextField(
        help_text="Enter the main question or topic for discussion."
    )
    image = models.ImageField(
        upload_to="quora_post/",
        null=True,
        blank=True,
        help_text="Optional: Upload an image related to the question."
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        help_text="User who posted the question."
    )
    likes = models.ManyToManyField(
        User,
        related_name='liked_post',
        blank=True,
        help_text="Users who liked this post."
    )

    def __str__(self):
        return f"Post by {self.user.username}: {self.question[:50]}"


class QuoraReply(BaseModel):
    post = models.ForeignKey(
        QuoraPost,
        on_delete=models.CASCADE,
        related_name="replies",
        help_text="The original post this reply belongs to."
    )
    answer = models.TextField(
        help_text="Enter your reply or answer to the question."
    )
    image = models.ImageField(
        upload_to="quora_replies/",
        null=True,
        blank=True,
        help_text="Optional: Upload an image related to your reply."
    )
    likes = models.ManyToManyField(
        User,
        related_name='liked_answers',
        blank=True,
        help_text="Users who liked this reply."
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="replies",
        help_text="User who replied to the post."
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"Reply by {self.user.username}: {self.answer[:50]}"
