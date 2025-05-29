from django.db import models

class TrustCounter(models.Model):
    """
    Model to track how many times parents have trusted our Infant Cry Detection service.
    """
    count_number = models.PositiveIntegerField(default=0, help_text="Number of times parents have trusted us.")

    def __str__(self):
        return f"Trusted {self.count_number} times"
