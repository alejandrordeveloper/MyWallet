# Vista de bienvenida para la ruta principal
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>¡Bienvenido a MyWallet API!</h1><p>Utiliza la ruta /api/ para acceder a los endpoints de la API.</p>")
from django.shortcuts import render
from .serializers import UserSerializer, CategorySerializer, TransactionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Category, Transaction
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your views here.

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        total_income = Transaction.objects.filter(user=user, type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = Transaction.objects.filter(user=user, type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
        balance = total_income - total_expense

        data = {
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance
        }
        return Response(data)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    #Asigna el usuario autenticado a la transacción creada
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)