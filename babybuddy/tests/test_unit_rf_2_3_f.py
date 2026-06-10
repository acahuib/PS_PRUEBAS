import datetime
from django.test import SimpleTestCase
from django.conf import settings
from babybuddy.forms import UserSettingsForm


class TestRF23DashboardSettingsUnit(SimpleTestCase):

    def test_FN2_3_CP_001_refresh_rate_valida(self):
        data = {
            "language": "en",
            "timezone": "UTC",
            "dashboard_refresh_rate": datetime.timedelta(minutes=1),
        }
        form = UserSettingsForm(data=data)
        form.is_valid()
        self.assertNotIn(
            "dashboard_refresh_rate",
            form.errors,
            "El formulario debe aceptar las tasas de refresco predefinidas en Django.",
        )

    def test_FN2_3_CP_002_refresh_rate_invalida(self):
        data = {
            "language": "en",
            "timezone": "UTC",
            "dashboard_refresh_rate": datetime.timedelta(minutes=99),
        }
        form = UserSettingsForm(data=data)
        form.is_valid()
        self.assertIn(
            "dashboard_refresh_rate",
            form.errors,
            "DEFENSA: Debe rechazar duraciones inyectadas que no estén en el selector.",
        )

    def test_FN2_3_CP_003_hide_empty_valido(self):
        data = {"language": "en", "timezone": "UTC", "dashboard_hide_empty": True}
        form = UserSettingsForm(data=data)
        form.is_valid()
        self.assertNotIn(
            "dashboard_hide_empty",
            form.errors,
            "El checkbox debe aceptar entradas booleanas puras.",
        )

    def test_FN2_3_CP_004_hide_age_valida(self):
        data = {
            "language": "en",
            "timezone": "UTC",
            "dashboard_hide_age": datetime.timedelta(weeks=4),
        }
        form = UserSettingsForm(data=data)
        form.is_valid()
        self.assertNotIn(
            "dashboard_hide_age",
            form.errors,
            "El formulario debe aceptar opciones de antigüedad configuradas.",
        )

    def test_FN2_3_CP_005_hide_age_invalida(self):
        data = {
            "language": "en",
            "timezone": "UTC",
            "dashboard_hide_age": datetime.timedelta(days=365 * 50),
        }
        form = UserSettingsForm(data=data)
        form.is_valid()
        self.assertIn(
            "dashboard_hide_age",
            form.errors,
            "Debe bloquear inyecciones de tiempos absurdos que rompan el query del sistema.",
        )
