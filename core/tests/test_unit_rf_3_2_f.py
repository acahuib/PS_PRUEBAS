import datetime
from django.test import SimpleTestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from core.forms import ChildForm
from core.models import Child


class TestRF32ChildEditForm(SimpleTestCase):

    def setUp(self):
        self.child = Child(
            first_name="NombreOriginal",
            last_name="ApellidoOriginal",
            birth_date=datetime.date(2023, 1, 1),
            slug="nombreoriginal-apellidooriginal",
        )

    def test_FN3_2_CP_001_edicion_valida(self):
        data = {
            "first_name": "Mateo",
            "last_name": "ApellidoOriginal",
            "birth_date": self.child.birth_date,
        }
        form = ChildForm(data=data, instance=self.child)
        self.assertTrue(
            form.is_valid(), "El formulario debería permitir la edición válida."
        )

    def test_FN3_2_CP_002_borrar_nombre_obligatorio(self):
        data = {"first_name": "", "birth_date": self.child.birth_date}
        form = ChildForm(data=data, instance=self.child)
        self.assertFalse(
            form.is_valid(),
            "No debe permitir borrar el nombre obligatorio durante la edición.",
        )
        self.assertIn("first_name", form.errors)

    def test_FN3_2_CP_003_formato_fecha_invalido(self):
        data = {"first_name": self.child.first_name, "birth_date": "texto-invalido"}
        form = ChildForm(data=data, instance=self.child)
        self.assertFalse(
            form.is_valid(), "No debe permitir cambiar a un formato de fecha erróneo."
        )
        self.assertIn("birth_date", form.errors)

    def test_FN3_2_CP_004_nombre_excede_limite(self):
        data = {"first_name": "A" * 256, "birth_date": self.child.birth_date}
        form = ChildForm(data=data, instance=self.child)
        self.assertFalse(
            form.is_valid(),
            "No debe permitir editar el nombre superando los 255 caracteres.",
        )
        self.assertIn("first_name", form.errors)

    def test_FN3_2_CP_005_fecha_nacimiento_futura(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        data = {"first_name": self.child.first_name, "birth_date": tomorrow}
        form = ChildForm(data=data, instance=self.child)
        self.assertFalse(
            form.is_valid(),
            "DEFECTO: Permite editar la fecha de nacimiento a una fecha futura.",
        )
        if not form.is_valid():
            self.assertIn("birth_date", form.errors)

    def test_FN3_2_CP_006_formato_imagen_invalido(self):
        invalid_file = SimpleUploadedFile(
            "documento.pdf", b"fake_content", content_type="application/pdf"
        )
        data = {
            "first_name": self.child.first_name,
            "birth_date": self.child.birth_date,
        }
        files = {"picture": invalid_file}
        form = ChildForm(data=data, files=files, instance=self.child)
        self.assertFalse(
            form.is_valid(),
            "No debe permitir reemplazar la foto con un archivo que no sea imagen.",
        )
        self.assertIn("picture", form.errors)

    def test_FN3_2_CP_007_fecha_nacimiento_antigua_ilogica(self):
        data = {
            "first_name": self.child.first_name,
            "birth_date": datetime.date(1970, 1, 1),
        }
        form = ChildForm(data=data, instance=self.child)
        self.assertFalse(
            form.is_valid(),
            "DEFECTO: Permite editar la edad para que un registro existente tenga 50 años.",
        )
        if not form.is_valid():
            self.assertIn("birth_date", form.errors)

    def test_FN3_2_CP_008_hora_nacimiento_futura(self):
        now = datetime.datetime.now()
        future_time = (now + datetime.timedelta(hours=2)).time()
        data = {
            "first_name": self.child.first_name,
            "birth_date": now.date(),
            "birth_time": future_time,
        }
        form = ChildForm(data=data, instance=self.child)
        self.assertFalse(
            form.is_valid(),
            "DEFECTO: Permite editar la hora de nacimiento a un horario futuro.",
        )
        if not form.is_valid():
            self.assertIn("birth_time", form.errors)

    def test_FN3_2_CP_009_formato_hora_invalido(self):
        data = {
            "first_name": self.child.first_name,
            "birth_date": self.child.birth_date,
            "birth_time": "mediodia",
        }
        form = ChildForm(data=data, instance=self.child)
        self.assertFalse(
            form.is_valid(), "No debe permitir cambiar a un formato de hora erróneo."
        )
        self.assertIn("birth_time", form.errors)
