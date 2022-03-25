from rest_framework import viewsets
from rest_framework.response import Response
from .models import Manuf, Laptop
from .serializers import ManufSerializer, LaptopSerializer


class LaptopViewSet(viewsets.ModelViewSet):
    serializer_class = LaptopSerializer

    def get_queryset(self):
        list_laptop = Laptop.objects.all()
        return list_laptop

    def create(self, request, *args, **kwargs):
        data = request.data
        new_laptop = None
        manuf_id = data['manuf']['id']
        laptop_manuf = None
        if manuf_id != None:
            laptop_manuf = Manuf.objects.get(id=manuf_id)
        else:
            laptop_manuf = Manuf.objects.create(
                name=data['manuf']['name'],
                country=data['manuf']['country'],
            )
        new_laptop = Laptop.objects.create(
            name=data['name'],
            gpu=data['gpu'],
            cpu=data['cpu'],
            storageSize=data['storageSize'],
            ram=data['ram'],
            screenSize=data['screenSize'],
            manuf=laptop_manuf
        )


        new_laptop.save()

        serializer = LaptopSerializer(new_laptop)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        current_laptop = self.get_object()
        data = request.data
        new_laptop = None
        manuf_id = data['manuf']['id']
        laptop_manuf = None
        if manuf_id != None:
            laptop_manuf = Manuf.objects.get(id=manuf_id)
        else:
            laptop_manuf = Manuf.objects.create(
                name=data['manuf']['name'],
                country=data['manuf']['country'],
            )

        current_laptop.name = data['name']
        current_laptop.gpu = data['gpu']
        current_laptop.cpu = data['cpu']
        current_laptop.storageSize = data['storageSize']
        current_laptop.ram = data['ram']
        current_laptop.screenSize = data['screenSize']
        current_laptop.manuf = laptop_manuf

        current_laptop.save()

        serializer = LaptopSerializer(current_laptop)

        return Response(serializer.data)


class ManufViewSet(viewsets.ModelViewSet):
    serializer_class = ManufSerializer

    def get_queryset(self):
        list_manuf = Manuf.objects.all()
        return list_manuf
