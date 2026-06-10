import datetime
from django.test import SimpleTestCase
from core.forms import ChildDeleteForm
from core.models import Child


class TestRF33ChildDeleteForm(SimpleTestCase):

    def setUp(self):
        self.child = Child(
            first_name="Lucas",
            last_name="Perez",
            birth_date=datetime.date(2023, 1, 1),
            slug="lucas-perez",
        )

    def test_FN3_3_CP_001_eliminacion_valida(self):
        data = {"confirm_name": "Lucas Perez"}
        form = ChildDeleteForm(data=data, instance=self.child)
        self.assertTrue(
            form.is_valid(),
            "El formulario debe ser válido si el nombre coincide exactamente.",
        )

    def test_FN3_3_CP_002_confirmacion_vacia(self):
        data = {"confirm_name": ""}
        form = ChildDeleteForm(data=data, instance=self.child)
        self.assertFalse(
            form.is_valid(),
            "El formulario no debe permitir eliminación con confirmación vacía.",
        )
        self.assertIn("confirm_name", form.errors)

    def test_FN3_3_CP_003_nombre_incorrecto(self):
        data = {"confirm_name": "Mateo Perez"}
        form = ChildDeleteForm(data=data, instance=self.child)
        self.assertFalse(
            form.is_valid(),
            "El formulario debe rechazar la eliminación si el nombre no coincide.",
        )
        self.assertIn("confirm_name", form.errors)

    def test_FN3_3_CP_004_sensibilidad_mayusculas(self):
        data = {"confirm_name": "lucas perez"}
        form = ChildDeleteForm(data=data, instance=self.child)
        self.assertFalse(
            form.is_valid(),
            "El formulario debe rechazar si no coinciden mayúsculas/minúsculas.",
        )
        self.assertIn("confirm_name", form.errors)
