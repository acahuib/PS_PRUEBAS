import datetime
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from core.forms import ChildForm


class TestRF31ChildForm(TestCase):
    def test_FN3_1_CP_001_creacion_valida(self):
        data = {
            "first_name": "Lucas",
            "last_name": "Perez",
            "birth_date": datetime.date.today(),
        }
        form = ChildForm(data=data)
        self.assertTrue(
            form.is_valid(), "El formulario debería ser válido con datos correctos."
        )

    def test_FN3_CP_002_nombre_vacio(self):
        data = {
            "first_name": "",
            "birth_date": datetime.date.today(),
        }
        form = ChildForm(data=data)
        self.assertFalse(
            form.is_valid(), "El formulario no debe aceptar nombres vacíos."
        )
        self.assertIn("first_name", form.errors)

    def test_FN3_CP_003_nombre_excede_limite(self):
        data = {
            "first_name": "A" * 256,
            "birth_date": datetime.date.today(),
        }
        form = ChildForm(data=data)
        self.assertFalse(
            form.is_valid(),
            "El formulario no debe aceptar nombres de más de 255 caracteres.",
        )
        self.assertIn("first_name", form.errors)

    def test_FN3_CP_004_formato_fecha_invalido(self):
        data = {
            "first_name": "Lucas",
            "birth_date": "trece de marzo",
        }
        form = ChildForm(data=data)
        self.assertFalse(
            form.is_valid(),
            "El formulario no debe aceptar texto no formateado en la fecha.",
        )
        self.assertIn("birth_date", form.errors)

    def test_FN3_CP_005_fecha_nacimiento_futura(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        data = {
            "first_name": "Lucas",
            "birth_date": tomorrow,
        }
        form = ChildForm(data=data)
        self.assertFalse(
            form.is_valid(),
            "DEFECTO: El sistema permite registrar una fecha de nacimiento en el futuro.",
        )
        if not form.is_valid():
            self.assertIn("birth_date", form.errors)

    def test_FN3_CP_006_formato_imagen_invalido(self):
        invalid_file = SimpleUploadedFile(
            "documento.pdf", b"file_content_fake", content_type="application/pdf"
        )
        data = {
            "first_name": "Lucas",
            "birth_date": datetime.date.today(),
        }
        files = {"picture": invalid_file}
        form = ChildForm(data=data, files=files)
        self.assertFalse(
            form.is_valid(),
            "El formulario no debe aceptar un archivo PDF en el campo de imagen.",
        )
        self.assertIn("picture", form.errors)

    def test_FN3_CP_007_fecha_nacimiento_antigua_ilogica(self):
        data = {
            "first_name": "Adulto",
            "birth_date": datetime.date(1970, 1, 1),
        }
        form = ChildForm(data=data)
        self.assertFalse(
            form.is_valid(),
            "DEFECTO: El sistema permite registrar bebés nacidos en 1970.",
        )
        if not form.is_valid():
            self.assertIn("birth_date", form.errors)

    def test_FN3_CP_008_hora_nacimiento_futura(self):
        now = datetime.datetime.now()
        future_time = (now + datetime.timedelta(hours=2)).time()

        data = {
            "first_name": "Lucas",
            "birth_date": now.date(),
            "birth_time": future_time,
        }
        form = ChildForm(data=data)
        self.assertFalse(
            form.is_valid(),
            "DEFECTO: El sistema permite registrar una hora de nacimiento futura.",
        )
        if not form.is_valid():
            self.assertIn("birth_time", form.errors)

    def test_FN3_CP_009_formato_hora_invalido(self):
        data = {
            "first_name": "Lucas",
            "birth_date": datetime.date.today(),
            "birth_time": "mediodia",
        }
        form = ChildForm(data=data)
        self.assertFalse(
            form.is_valid(),
            "El formulario no debe aceptar texto no formateado en la hora.",
        )
        self.assertIn("birth_time", form.errors)
