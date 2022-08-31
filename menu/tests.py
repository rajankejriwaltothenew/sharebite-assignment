import json

from django.test import TestCase
from django.urls import reverse

from menu.models import Section, Item, Modifiers


class SectionTestCases(TestCase):
    """This class is used to test the section crud operations."""

    def setUp(self):
        """Function for setup."""
        self.section_1 = Section.objects.create(
            name="test name 1",
            description="test description 1"
        )
        self.section_2 = Section.objects.create(
            name="test name 2",
            description="test description 2"
        )

    def test_get_list_success(self):
        """Test case success for get list of pre loaded section."""
        url = reverse('section-list')
        response = self.client.get(url)
        response_obj = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)

        # checking if there is actually data.
        self.assertTrue(response_obj)

    def test_get_detail_success(self):
        """Test case success for get detail of pre loaded section."""
        url = reverse('section-list') + str(self.section_1.id) + "/"
        response = self.client.get(url)
        response_obj = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)

        # checking if we actually retrieve the data.
        self.assertEqual(response_obj["id"], self.section_1.id)

    def test_post_success(self):
        """Test case success for post new data for section."""
        url = reverse('section-list')
        data = {
            "name": "new section 3",
            "description": "new description 3"
        }
        response = self.client.post(url, data, content_type='application/json')
        response_obj = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 201)

        # getting section object to check whether the data is created or not.
        section_obj = Section.objects.filter(id=response_obj["id"])
        self.assertTrue(section_obj)

    def test_post_fails(self):
        """
        Test case fails for post new data for section.
        
        When data is not provided properly.
        """
        url = reverse('section-list')
        data = {
            "name": "new section 3"
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_put_success(self):
        """Test case for put/update the existing data."""
        url = reverse('section-list') + str(self.section_1.id) + "/"
        data = {
            "name": "test data 1 updated",
            "description": "new description 3"
        }
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        # getting object to check for updation of data.
        section_obj = Section.objects.filter(
            id=self.section_1.id
        ).values().first()
        self.assertEqual(section_obj["name"], "test data 1 updated")
        self.assertEqual(section_obj["description"], "new description 3")

    def test_delete_success(self):
        """Test case to delete the existing data."""
        url = reverse('section-list') + str(self.section_1.id) + "/"
        response = self.client.delete(url)

        # checking for status code.
        self.assertEqual(response.status_code, 204)
        # checking for deletion of the data.
        self.assertEqual(
            Section.objects.filter(id=self.section_1.id).first(), None
        )


class ItemTestCases(TestCase):
    """This class is used to test the item crud operations."""

    def setUp(self):
        """Function for setup."""
        self.section_1 = Section.objects.create(
            name="test name 1",
            description="test description 1"
        )
        self.item_1 = Item.objects.create(
            name="test name 1",
            description="test description 1",
            price=100,
            section_id=self.section_1.id
        )

    def test_get_list_success(self):
        """Test case success for get list of pre loaded section."""
        url = reverse('item-list')
        response = self.client.get(url)
        response_obj = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)

        # checking if there is actually data.
        self.assertTrue(response_obj)

    def test_get_detail_success(self):
        """Test case success for get detail of pre loaded section."""
        url = reverse('item-list') + str(self.item_1.id) + "/"
        response = self.client.get(url)
        response_obj = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)

        # checking if we able to retrieve the data.
        self.assertEqual(response_obj["id"], self.item_1.id)

    def test_post_success(self):
        """Test case success for post new data for section."""
        url = reverse('item-list')
        data = {
            "name": "new item 2",
            "description": "new description 2",
            "price": 200,
            "section": self.section_1.id
        }
        response = self.client.post(url, data, content_type='application/json')
        response_obj = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 201)

        # getting item object to check whether the data is created or not.
        item_obj = Item.objects.filter(id=response_obj["id"])
        self.assertTrue(item_obj)

    def test_post_fails(self):
        """
        Test case fails for post new data for section.
        
        When data is not provided properly.
        """
        url = reverse('item-list')
        data = {
            "name": "new item 2 new item 2 new item 2",
            "description": "new description 2",
            "price": 200,
            "section": self.section_1.id
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_put_success(self):
        """Test case for put/update the existing data."""
        url = reverse('item-list') + str(self.item_1.id) + "/"
        data = {
            "name": "new item 2",
            "description": "new description 2",
            "price": 200,
            "section": self.section_1.id
        }
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # getting item object to check whether data is updated or not.
        item_obj = Item.objects.filter(id=self.item_1.id).values().first()
        self.assertEqual(item_obj["name"], "new item 2")
        self.assertEqual(item_obj["description"], "new description 2")
        self.assertEqual(item_obj["price"], 200)
        self.assertEqual(item_obj["section_id"], self.section_1.id)

    def test_delete_success(self):
        """Test case to delete the existing data."""
        url = reverse('item-list') + str(self.item_1.id) + "/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

        # checking if the object is actually deleted.
        self.assertEqual(Item.objects.filter(id=self.item_1.id).first(), None)


class ModifiersTestCases(TestCase):
    """This class is used to test the modifier crud operations."""

    def setUp(self):
        """Function for setup."""
        self.section_1 = Section.objects.create(
            name="test name 1",
            description="test description 1"
        )
        self.item_1 = Item.objects.create(
            name="test name 1",
            description="test description 1",
            price=100,
            section_id=self.section_1.id
        )
        self.modifier_1 = Modifiers.objects.create(
            description="test description 1"
        )

    def test_get_list_success(self):
        """Test case success for get list of pre loaded section."""
        url = reverse('modifiers-list')
        response = self.client.get(url)
        response_obj = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)

        # checking if there is actually data.
        self.assertTrue(response_obj)

    def test_get_detail_success(self):
        """Test case success for get detail of pre loaded section."""
        url = reverse('modifiers-list') + str(self.modifier_1.id) + "/"
        response = self.client.get(url)
        response_obj = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)

        # checking if we able to retrieve the data.
        self.assertEqual(response_obj["id"], self.modifier_1.id)

    def test_post_success(self):
        """Test case success for post new data for section."""
        url = reverse('modifiers-list')
        data = {
            "description": "new description 2"
        }
        response = self.client.post(url, data, content_type='application/json')
        response_obj = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 201)

        # getting modifier object to check whether object is created or not.
        modifier_obj = Modifiers.objects.filter(id=response_obj["id"])
        self.assertTrue(modifier_obj)

    def test_put_success(self):
        """Test case for put/update the existing data."""
        url = reverse('modifiers-list') + str(self.modifier_1.id) + "/"
        data = {
            "description": "new description 2"
        }
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # getting modifier object to check whether object is updated or not.
        modifier_obj = Modifiers.objects.filter(
            id=self.modifier_1.id).values().first()
        self.assertEqual(modifier_obj["description"], "new description 2")

    def test_delete_success(self):
        """Test case to delete the existing data."""
        url = reverse('modifiers-list') + str(self.modifier_1.id) + "/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

        # checking if the object is actually deleted.
        self.assertEqual(Modifiers.objects.filter(
            id=self.modifier_1.id).first(), None)


class ModifierToItemMappingTestCases(TestCase):
    """This class is used to test the Modifier to Item mapping."""

    def setUp(self):
        """Function for setup."""
        self.section_1 = Section.objects.create(
            name="test name 1",
            description="test description 1"
        )
        self.item_1 = Item.objects.create(
            name="test name 1",
            description="test description 1",
            price=100,
            section_id=self.section_1.id
        )
        self.modifier_1 = Modifiers.objects.create(
            description="test description 1"
        )

    def test_post_success(self):
        """Test case for successfull mapping."""
        url = reverse('modifier-to-item-mapping')
        data = {
            "item": self.item_1.id,
            "modifier": self.modifier_1.id
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # getting object to check whether the mapping is successfull or not.
        modifier_obj = Modifiers.objects.get(id=self.modifier_1.id)
        self.assertEqual(
            modifier_obj.item.all().values_list("id", flat=True).first(),
            self.item_1.id
        )


class GetAllMenuTestCases(TestCase):
    """This class is used to test GetAllMenuListApiView."""

    def setUp(self):
        """Function for setup."""
        self.section_1 = Section.objects.create(
            name="test name 1",
            description="test description 1"
        )
        self.item_1 = Item.objects.create(
            name="test name 1",
            description="test description 1",
            price=100,
            section_id=self.section_1.id
        )
        self.modifier_1 = Modifiers.objects.create(
            description="test description 1"
        )

    def test_get_list_success(self):
        """Test case for getting list successfully."""
        url = reverse('all-menu')
        response = self.client.get(url)
        response_obj = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)

        # checking if we actually getting any data
        self.assertTrue(response_obj)
