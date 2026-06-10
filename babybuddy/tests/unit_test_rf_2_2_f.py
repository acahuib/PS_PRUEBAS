from django.test import SimpleTestCase
from django.conf import settings
from babybuddy.forms import UserSettingsForm


class TestRF22UserSettingsFormUnit(SimpleTestCase):

    def test_FN2_2_CP_001_idioma_valido(self):
        idioma_valido = settings.LANGUAGES[0][0]
        data = {"language": idioma_valido, "timezone": "UTC"}
        form = UserSettingsForm(data=data)
        form.is_valid()
        self.assertNotIn(
            "language",
            form.errors,
            "El formulario debería aceptar un idioma configurado oficialmente.",
        )

    def test_FN2_2_CP_002_idioma_invalido(self):
        data = {"language": "klingon", "timezone": "UTC"}
        form = UserSettingsForm(data=data)
        form.is_valid()
        self.assertIn(
            "language",
            form.errors,
            "El formulario debe rechazar idiomas no soportados por el sistema.",
        )

    def test_FN2_2_CP_003_zona_horaria_valida(self):
        data = {"language": "en", "timezone": "America/Lima"}
        form = UserSettingsForm(data=data)
        form.is_valid()
        self.assertNotIn(
            "timezone",
            form.errors,
            "El formulario debería aceptar zonas horarias válidas de IANA.",
        )

    def test_FN2_2_CP_004_zona_horaria_invalida(self):
        data = {"language": "en", "timezone": "Tierra/Centro"}
        form = UserSettingsForm(data=data)
        form.is_valid()
        self.assertIn(
            "timezone",
            form.errors,
            "El formulario debe rechazar zonas horarias que no existan en el estándar IANA.",
        )
