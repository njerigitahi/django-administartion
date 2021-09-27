from django.db import models

from users.models import User


class Supplier( models.Model ):
    user = models.OneToOneField( User, on_delete=models.CASCADE, null=True )
    name = models.CharField( max_length=120, unique=True )
    license = models.CharField( max_length=220, null=True )
    address = models.CharField( max_length=220 )
    phone = models.CharField( max_length=220, null=True )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.name


class Driver( models.Model ):
    name = models.CharField( max_length=120, unique=True )
    license = models.CharField( max_length=220, null=True )
    address = models.CharField( max_length=220 )
    phone = models.CharField( max_length=220, null=True )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.name


class Service( models.Model ):
    name = models.CharField( max_length=120, unique=True )
    serviceprovider = models.CharField( max_length=220, null=True )
    location = models.CharField( max_length=220 )
    email = models.EmailField( max_length=220, null=True )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.name


class Visitor( models.Model ):
    name = models.CharField( max_length=120, unique=True )
    address = models.CharField( max_length=220 )
    phone = models.CharField( max_length=220, null=True )
    location = models.CharField( max_length=120, unique=True )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.name


class Buyer( models.Model ):
    user = models.OneToOneField( User, on_delete=models.CASCADE )
    name = models.CharField( max_length=120, unique=True )
    address = models.CharField( max_length=220 )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.name


class Season( models.Model ):
    name = models.CharField( max_length=120, unique=True )
    description = models.CharField( max_length=220 )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.name


class Drop( models.Model ):
    name = models.CharField( max_length=120, unique=True )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.name


class Product( models.Model ):
    MAKE = (
        ('Isuzu', 'Isuzu'),
        ('Volvo', 'Volvo'),
        ('Hyundai', 'Hyundai'),
        ('Scania', 'Scania'),
        ('MAN', 'MAN'),
        ('TataGroup', 'TataGroup'),
    )
    name = models.CharField( max_length=120, unique=True )
    regno = models.CharField( max_length=30, unique=True )
    make = models.CharField( max_length=10, choices=MAKE, null=True )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.name


class WorkFlow( models.Model ):
    DESTINATION = (
        ('NAIROBI', 'NAIROBI'),
        ('MOMBASA', 'MOMBASA'),
        ('KISUMU', 'KISUMU'),
        ('NAIVASHA', 'NAIVASHA'),
        ('BUSIA', 'BUSIA'),
    )
    workflowID = models.CharField( max_length=50 )
    license = models.ForeignKey( Driver, on_delete=models.CASCADE )
    plate_no = models.ForeignKey( Product, on_delete=models.CASCADE )
    destination = models.CharField( max_length=10, choices=DESTINATION, null=True )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.workflowID


class Report( models.Model ):
    STATUS = (
        ('In Good Condition', 'In Good Condition'),
        ('Need Maintenance', 'Need Maintenance'),
        ('Accident', 'Accident'),
    )
    driver = models.ForeignKey( Driver, on_delete=models.CASCADE )
    vehicle = models.ForeignKey( Product, on_delete=models.CASCADE )
    status = models.CharField( max_length=30, choices=STATUS, null=True )
    feedback=models.TextField(max_length=100,null=True)
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.driver


class Asset( models.Model ):
    INSURANCE = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    BROKEN = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    REPAIRS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    name = models.CharField( max_length=120, unique=True )
    insurance = models.CharField( max_length=10, choices=INSURANCE, null=True )
    repairs = models.CharField( max_length=10, choices=REPAIRS, null=True )
    broken = models.CharField( max_length=10, choices=BROKEN, null=True )
    feedback = models.TextField( max_length=100, unique=True )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.name


class Order( models.Model ):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.ForeignKey( Supplier, on_delete=models.CASCADE )
    product = models.ForeignKey( Product, on_delete=models.CASCADE )
    design = models.CharField( max_length=50 )
    color = models.CharField( max_length=50 )
    buyer = models.ForeignKey( Buyer, on_delete=models.CASCADE, null=True )
    season = models.ForeignKey( Season, on_delete=models.CASCADE, null=True )
    drop = models.ForeignKey( Drop, on_delete=models.CASCADE, null=True )
    status = models.CharField( max_length=10, choices=STATUS_CHOICE )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.product.name


class Delivery( models.Model ):
    ROOMNO = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('A5', 'A5'),
        ('A6', 'A6'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
        ('B4', 'B4'),
        ('B5', 'B5'),
        ('B6', 'B6'),
        ('C1', 'C1'),
        ('C2', 'C2'),
        ('C3', 'C3'),
        ('C4', 'C4'),
        ('C5', 'C5'),
        ('C6', 'C6'),
    )
    name = models.ForeignKey( Visitor, on_delete=models.CASCADE, null=True )
    room_no = models.CharField( max_length=10, choices=ROOMNO, null=True )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.room_no


class Room( models.Model ):
    ROOM = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('A5', 'A5'),
        ('A6', 'A6'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
        ('B4', 'B4'),
        ('B5', 'B5'),
        ('B6', 'B6'),
        ('C1', 'C1'),
        ('C2', 'C2'),
        ('C3', 'C3'),
        ('C4', 'C4'),
        ('C5', 'C5'),
        ('C6', 'C6'),
    )
    name = models.ForeignKey( Visitor, on_delete=models.CASCADE, null=True )
    room_no = models.CharField( max_length=10, choices=ROOM, null=True )
    created_date = models.DateField( auto_now_add=True )

    def __str__(self):
        return self.name
