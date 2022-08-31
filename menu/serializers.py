from rest_framework import serializers

from menu.models import Section, Item, Modifiers


class SectionSerializer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    class Meta:
        """Meta class."""

        model = Section
        fields = ('id', 'name', 'description')


class ListItemSerializer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    class Meta:
        """Meta class."""

        model = Item
        fields = ('id', 'name', 'description', 'price')


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


class ModifierListSerializer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    title = serializers.SerializerMethodField('get_title')

    class Meta:
        """Meta class."""

        model = Modifiers
        fields = ('id', 'title')

    def get_title(self, obj):
        """Function for get_title."""
        return obj.description


class ItemListSerializer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    modifiers = ModifierListSerializer(many=True)
    title = serializers.SerializerMethodField('get_title')

    class Meta:
        """Meta class."""

        model = Item
        fields = ('id', 'title', 'modifiers')

    def get_title(self, obj):
        """Function for get_title."""
        return obj.name


class SectionListSerializer(serializers.ModelSerializer):
    """Serializer to serialize data."""

    items = ItemListSerializer(many=True, source='item')
    title = serializers.SerializerMethodField('get_title')

    class Meta:
        """Meta class."""

        model = Section
        fields = ('id', 'title', 'items')

    def get_title(self, obj):
        """Function for get_title."""
        return obj.name
