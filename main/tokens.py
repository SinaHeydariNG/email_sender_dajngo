from django.contrib.auth.tokens import PasswordResetTokenGenerator
class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, message, timestamp):
        return (
                str(message.activate) + str(message.pk) + str(timestamp)
        )


account_activation_token = EmailVerificationTokenGenerator()