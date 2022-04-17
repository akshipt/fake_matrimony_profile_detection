from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import renderer_classes
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer

from Fake_Profile_Detection_Matrimony.models import AdminPanel, UserCheck
from . import serializer
from ml_model.model_use import model_result


class AdminPanelAPI(ListCreateAPIView):
    queryset = AdminPanel.objects.all()
    serializer_class = serializer.AdminPanelSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return HttpResponseRedirect(redirect_to='/signup/')

    #        return Response({"status": True, "message": "Admin User Added !",
    #                         "data": serializer.data}, status=status.HTTP_201_CREATED,
    #                        headers=headers, template_name='dashboard.html')

    def perform_create(self, serializer):
        # Hash password but passwords are not required
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def perform_update(self, serializer):
        # Hash password but passwords are not required
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()


class AdminPanelRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.AdminPanelSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return AdminPanel.objects.filter(id=self.kwargs.get('pk', None))

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({"status": True, "message": "Admin Updated !", "data": serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Admin Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


"""
class UserPanelAPI(ListCreateAPIView):
    queryset = AdminPanel.objects.all()
    serializer_class = serializer.UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": True, "message": "Admin User Added !",
                         "data": serializer.data}, status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        # Hash password but passwords are not required
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def perform_update(self, serializer):
        # Hash password but passwords are not required
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()


class UserPanelRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.AdminPanelSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return AdminPanel.objects.filter(id=self.kwargs.get('pk', None))

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({"status": True, "message": "Admin Updated !", "data": serializer.data})
"""


class UserCheckAPI(ListCreateAPIView):
    serializer_class = serializer.UserCheckSerializer
    queryset = UserCheck.objects.all()
    permission_classes = (AllowAny,)
    template_name = 'login.html'

    @renderer_classes(StaticHTMLRenderer,)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        model_bool = model_result(request.data)
        print(model_bool)
        if model_bool:
            return render(request, 'genuine_profile_alert.html')
            # return Response({"status": True, "message": "Personal Details Added",
            #                  "data": serializer.data}, status=status.HTTP_201_CREATED,
            #                 headers=headers)
        else:
            return render(request, 'fake_profile_alert.html')
            # data = '<html><body><h1>BYE, world</h1></body></html>'
            # return Response(data)
            # return Response({"status": True, "message": "May be Fake", "data": serializer.data},
            #             status=status., headers=headers)


def AdminSignUpPage(request):
    return render(request, 'admin_signup.html')


def AdminLoginPage(request):
    return render(request, 'login.html')


def UserSignUpPage(request):
    return render(request, 'signup_form.html')


def UserLoginPage(request):
    return render(request, 'login.html')
