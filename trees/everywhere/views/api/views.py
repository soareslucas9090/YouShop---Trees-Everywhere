from rest_framework import mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from ...models import Account, PlantedTree, Profile, Tree, User
from ...permissions import IsAdmin, IsNormalUser
from ...serializers import (
    AccountSerializer,
    PlantedTreeSerializer,
    PlantTree,
    PlantTrees,
    ProfileSerializer,
    TreeSerializer,
    UserSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAdmin,
    ]
    http_method_names = ["get", "head", "patch", "delete", "post"]


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [
        IsAdmin,
    ]
    http_method_names = ["get", "head", "patch", "delete", "post"]


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        IsAdmin,
    ]
    http_method_names = ["get", "head", "patch", "delete", "post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(id=serializer.data["user"])
        except:
            return Response(
                {"Error": "The User must be valid!"}, status=status.HTTP_404_NOT_FOUND
            )

        Profile.objects.create(
            about=serializer.data["about"],
            user=user,
            joined=user.date_joined,
        )
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class TreeViewSet(ModelViewSet):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    permission_classes = [
        IsAdmin,
    ]
    http_method_names = ["get", "head", "patch", "delete", "post"]


class PlantedTreeViewSet(ModelViewSet):
    queryset = PlantedTree.objects.all()
    serializer_class = PlantedTreeSerializer
    permission_classes = [
        IsAdmin,
    ]
    http_method_names = ["get", "head", "patch", "delete", "post"]


class PlantTreeViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = PlantedTree.objects.all()
    serializer_class = PlantTree
    permission_classes = [
        IsNormalUser,
    ]
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.plant_tree(
            tree=serializer["tree"],
            location=serializer["location"],
            age=serializer["age"],
            account=serializer["account"],
        )
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class PlantTreesViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = PlantedTree.objects.all()
    serializer_class = PlantTrees
    permission_classes = [
        IsNormalUser,
    ]
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.plant_trees(trees_to_plant=serializer["plants"])
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
