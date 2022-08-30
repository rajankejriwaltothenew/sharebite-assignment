from rest_framework import serializers

from menu.models import Section, Item, Modifiers


class SectionSeriliazer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    class Meta:
        """Meta class."""

        model = Section
        fields = ('id', 'name', 'description')


class ItemSeriliazer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    class Meta:
        """Meta class."""

        model = Item
        fields = ('id', 'name', 'description', 'price', 'section')


class ModifierSeriliazer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    class Meta:
        """Meta class."""

        model = Modifiers
        fields = ('id', 'description')


class ItemListSeriliazer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    modifiers = ModifierSeriliazer(many=True)

    class Meta:
        """Meta class."""

        model = Item
        fields = ('id', 'name', 'modifiers')


class SectionListSeriliazer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    item = ItemListSeriliazer(many=True)

    class Meta:
        """Meta class."""

        model = Section
        fields = ('id', 'name', 'description', 'item')