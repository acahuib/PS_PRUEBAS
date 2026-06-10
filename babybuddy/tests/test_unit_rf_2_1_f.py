from unittest.mock import MagicMock, patch
from django.test import SimpleTestCase
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from babybuddy.forms import UserAddForm, UserPasswordForm


class TestRF21AuthAndSettingsFormsUnit(SimpleTestCase):

    def setUp(self):
        self.mock_user = MagicMock()
        self.mock_user.check_password.return_value = True
        patcher = patch("django.db.models.query.QuerySet.exists", return_value=False)
        self.mock_exists = patcher.start()
        self.addCleanup(patcher.stop)

    def test_FN2_1_CP_001_creacion_username_limite_excedido(self):
        data = {"username": "A" * 151}
        form = UserAddForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("username", form.errors)

    def test_FN2_1_CP_002_creacion_username_1_caracter(self):
        data = {"username": "A"}
        form = UserAddForm(data=data, instance=None)
        form.is_valid()
        self.assertNotIn("username", form.errors)

    def test_FN2_1_CP_003_creacion_nombre_limite_excedido(self):
        data = {"username": "testuser", "first_name": "A" * 151}
        form = UserAddForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("first_name", form.errors)

    def test_FN2_1_CP_004_creacion_nombre_vacio(self):
        data = {"username": "testuser", "first_name": ""}
        form = UserAddForm(data=data, instance=None)
        form.is_valid()
        self.assertNotIn("first_name", form.errors)

    def test_FN2_1_CP_005_creacion_apellido_limite_excedido(self):
        data = {"username": "testuser", "last_name": "A" * 151}
        form = UserAddForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("last_name", form.errors)

    def test_FN2_1_CP_006_creacion_apellido_vacio(self):
        data = {"username": "testuser", "last_name": ""}
        form = UserAddForm(data=data, instance=None)
        form.is_valid()
        self.assertNotIn("last_name", form.errors)

    def test_FN2_1_CP_007_creacion_email_limite_excedido(self):
        data = {"username": "testuser", "email": "A" * 246 + "@test.com"}
        form = UserAddForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("email", form.errors)

    def test_FN2_1_CP_008_creacion_email_vacio(self):
        data = {"username": "testuser", "email": ""}
        form = UserAddForm(data=data, instance=None)
        form.is_valid()
        self.assertNotIn("email", form.errors)

    def test_FN2_1_CP_009_creacion_username_con_espacios(self):
        data = {"username": "juan perez"}
        form = UserAddForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("username", form.errors)

    def test_FN2_1_CP_012_cambiar_password_7_caracteres(self):
        data = {
            "old_password": "any",
            "new_password1": "Claved7",
            "new_password2": "Claved7",
        }
        form = UserPasswordForm(user=self.mock_user, data=data)
        form.is_valid()
        self.assertIn("new_password2", form.errors)

    def test_FN2_1_CP_013_cambiar_password_numerico(self):
        data = {
            "old_password": "any",
            "new_password1": "12345678",
            "new_password2": "12345678",
        }
        form = UserPasswordForm(user=self.mock_user, data=data)
        form.is_valid()
        self.assertFalse(form.is_valid())

    def test_FN2_1_CP_014_cambiar_password_no_coinciden(self):
        data = {
            "old_password": "any",
            "new_password1": "Abc12345",
            "new_password2": "Abc1234",
        }
        form = UserPasswordForm(user=self.mock_user, data=data)
        form.is_valid()
        self.assertFalse(form.is_valid())

    def test_FN2_1_CP_016_recuperar_correo_sin_arroba(self):
        data = {"email": "juandotcom"}
        form = PasswordResetForm(data=data)
        form.is_valid()
        self.assertIn("email", form.errors)
