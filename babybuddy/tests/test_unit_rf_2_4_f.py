from unittest.mock import patch
from django.test import SimpleTestCase
from babybuddy.forms import UserUpdateForm


class TestRF25UserManagementUnit(SimpleTestCase):

    def setUp(self):
        patcher = patch("django.forms.models.BaseModelForm.validate_unique")
        self.mock_validate_unique = patcher.start()
        self.addCleanup(patcher.stop)

    def test_FN2_5_CP_001_edicion_username_151_caracteres(self):
        data = {
            "username": "A" * 151,
            "first_name": "anto",
            "last_name": "chaisa",
            "email": "anthony@test.com",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("username", form.errors)

    def test_FN2_5_CP_002_edicion_username_vacio(self):
        data = {
            "username": "",
            "first_name": "anto",
            "last_name": "chaisa",
            "email": "anthony@test.com",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("username", form.errors)

    def test_FN2_5_CP_003_edicion_username_1_caracter(self):
        data = {
            "username": "A",
            "first_name": "anto",
            "last_name": "chaisa",
            "email": "anthony@test.com",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertNotIn("username", form.errors)

    def test_FN2_5_CP_004_edicion_nombre_151_caracteres(self):
        data = {
            "username": "testuser",
            "first_name": "A" * 151,
            "last_name": "chaisa",
            "email": "anthony@test.com",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("first_name", form.errors)

    def test_FN2_5_CP_005_edicion_nombre_vacio(self):
        data = {
            "username": "testuser",
            "first_name": "",
            "last_name": "chaisa",
            "email": "anthony@test.com",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertNotIn("first_name", form.errors)

    def test_FN2_5_CP_006_edicion_apellido_151_caracteres(self):
        data = {
            "username": "testuser",
            "first_name": "anto",
            "last_name": "A" * 151,
            "email": "anthony@test.com",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("last_name", form.errors)

    def test_FN2_5_CP_007_edicion_apellido_vacio(self):
        data = {
            "username": "testuser",
            "first_name": "anto",
            "last_name": "",
            "email": "anthony@test.com",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertNotIn("last_name", form.errors)

    def test_FN2_5_CP_008_edicion_email_255_caracteres(self):
        data = {
            "username": "testuser",
            "first_name": "anto",
            "last_name": "chaisa",
            "email": "A" * 246 + "@test.com",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("email", form.errors)

    def test_FN2_5_CP_009_edicion_email_vacio(self):
        data = {
            "username": "testuser",
            "first_name": "anto",
            "last_name": "chaisa",
            "email": "",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertNotIn("email", form.errors)

    def test_FN2_5_CP_010_edicion_username_espacios(self):
        data = {
            "username": "juan p",
            "first_name": "anto",
            "last_name": "chaisa",
            "email": "anthony@test.com",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("username", form.errors)

    def test_FN2_5_CP_011_edicion_email_sin_arroba(self):
        data = {
            "username": "testuser",
            "first_name": "anto",
            "last_name": "chaisa",
            "email": "correosinarroba",
            "is_staff": False,
            "is_read_only": False,
            "is_active": True,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("email", form.errors)

    def test_FN2_5_CP_012_edicion_roles_booleanos(self):
        data = {
            "username": "testuser",
            "first_name": "anto",
            "last_name": "chaisa",
            "email": "anthony@test.com",
            "is_staff": True,
            "is_read_only": False,
            "is_active": False,
        }
        form = UserUpdateForm(data=data, instance=None)
        form.is_valid()
        self.assertNotIn("is_staff", form.errors)
        self.assertNotIn("is_active", form.errors)
