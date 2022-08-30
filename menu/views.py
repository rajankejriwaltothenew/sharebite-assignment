from rest_framework import views, viewsets, generics
from rest_framework.response import Response
from rest_framework import status

from menu.models import Section, Item, Modifiers
from menu.serializers import (
    SectionSeriliazer, ItemSeriliazer, ModifierSeriliazer,
    SectionListSeriliazer
)


class SectionViewset(viewsets.ModelViewSet):
    """This class is used to perform crud operations on Sections."""

    serializer_class = SectionSeriliazer
    queryset = Section.objects.all()


class ItemViewset(viewsets.ModelViewSet):
    """This class is used to perform crud operations on Item."""

    serializer_class = ItemSeriliazer
    queryset = Item.objects.all()


class ModifiersViewset(viewsets.ModelViewSet):
    """This class is used to perform crud operations on Modifiers."""

    serializer_class = ModifierSeriliazer
    queryset = Modifiers.objects.all()


class ModifierToItemMappingApiView(views.APIView):
    """This class is used to map modifier to an item."""

    def post(self, request, *args, **kwargs):
        """Function for post request."""
        item = request.data.get("item", None)
        modifier = request.data.get("modifier", None)

        # check for item field is provided in request data or not.
        if not item:
            msg = "item field is required and cannot be empty."
            return Response(
                {"detail": msg}, status=status.HTTP_400_BAD_REQUEST)

        # check for modifier field is provided in request data or not.
        if not modifier:
            msg = "modifier field is required and cannot be empty."
            return Response(
                {"detail": msg}, status=status.HTTP_400_BAD_REQUEST)

        # getting objects.
        modifier_obj = Modifiers.objects.filter(id=modifier).first()
        item_obj = Item.objects.filter(id=item).first()

        # checking if modifier exists.
        if not modifier_obj:
            msg = "modifier does not exists."
            return Response(
                {"detail": msg}, status=status.HTTP_400_BAD_REQUEST)

        # checking if item exists.
        if not item_obj:
            msg = "item does not exists."
            return Response(
                {"detail": msg}, status=status.HTTP_400_BAD_REQUEST)

        # adding item to modifier.
        modifier_obj.item.add(item_obj)

        msg = "Modifier mapped to an Item successfully."
        return Response({"detail": msg}, status=status.HTTP_200_OK)


class GetAllMenuListApiView(generics.ListAPIView):
    """This class is used to get all the menu items."""

    serializer_class = SectionListSeriliazer
    queryset = Section.objects.all()