from rest_framework import serializers

from menu.models import Section, Item, Modifiers


class SectionSerializer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    class Meta:
        """Meta class."""

        model = Section
        fields = ('id', 'name', 'description')


class ItemSerializer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    class Meta:
        """Meta class."""

        model = Item
        fields = ('id', 'name', 'description', 'price', 'section')


class ModifierSerializer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    class Meta:
        """Meta class."""

        model = Modifiers
        fields = ('id', 'description')


class ItemListSerializer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    modifiers = ModifierSerializer(many=True)

    class Meta:
        """Meta class."""

        model = Item
        fields = ('id', 'name', 'modifiers')


class SectionListSerializer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    item = ItemListSerializer(many=True)

    class Meta:
        """Meta class."""

        model = Section
        fields = ('id', 'name', 'description', 'item')