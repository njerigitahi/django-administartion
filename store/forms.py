from django import forms

from .models import Driver, Visitor, Supplier, Season, Drop, Product, Order, Delivery, WorkFlow, Asset, Room, Service, \
    Report


class DriverForm( forms.ModelForm ):
    class Meta:
        model = Driver
        fields = ['name', 'license', 'address', 'phone']

        widgets = {
            'name': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'name'
            } ),
            'license': forms.NumberInput( attrs={
                'class': 'form-control', 'id': 'license'
            } ),
            'address': forms.EmailInput( attrs={
                'class': 'form-control', 'id': 'address'
            } ),
            'phone': forms.NumberInput( attrs={
                'class': 'form-control', 'id': 'phone'
            } )
        }


class VisitorForm( forms.ModelForm ):
    class Meta:
        model = Visitor
        fields = ['name', 'address', 'phone', 'location']

        widgets = {
            'name': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'name'
            } ),
            'address': forms.EmailInput( attrs={
                'class': 'form-control', 'id': 'address'
            } ),
            'phone': forms.NumberInput( attrs={
                'class': 'form-control', 'id': 'phone'
            } ),
            'location': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'location'
            } )
        }


class ServiceForm( forms.ModelForm ):
    class Meta:
        model = Service
        fields = ['name', 'serviceprovider', 'email', 'location']

        widgets = {
            'name': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'name'
            } ),
            'serviceprovider': forms.EmailInput( attrs={
                'class': 'form-control', 'id': 'serviceprovider'
            } ),
            'email': forms.EmailInput( attrs={
                'class': 'form-control', 'id': 'email'
            } ),
            'location': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'location'
            } )
        }


class WorkFlowForm( forms.ModelForm ):
    class Meta:
        model = WorkFlow
        fields = ['workflowID', 'license', 'plate_no', 'destination']

        widgets = {
            'workflowID': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'workflowID'
            } ),
            'license': forms.Select( attrs={
                'class': 'form-control', 'id': 'license'
            } ),
            'plate_no': forms.Select( attrs={
                'class': 'form-control', 'id': 'plate_no'
            } ),
            'destination': forms.Select( attrs={
                'class': 'form-control', 'id': 'destination'
            } )
        }


class SupplierForm( forms.ModelForm ):
    class Meta:
        model = Supplier
        fields = ['user', 'name', 'license', 'address', 'phone']

        widgets = {
            'name': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'name'
            } ),
            'license': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'license'
            } ),
            'address': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'address'
            } ),
            'phone': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'phone'
            } )
        }


class BuyerForm( forms.Form ):
    name = forms.CharField( widget=forms.TextInput( attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    } ) )
    address = forms.CharField( widget=forms.TextInput( attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    } ) )
    email = forms.CharField( widget=forms.EmailInput( attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    } ) )
    username = forms.CharField( widget=forms.TextInput( attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    } ) )
    password = forms.CharField( widget=forms.PasswordInput( attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    } ) )
    retype_password = forms.CharField( widget=forms.PasswordInput( attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    } ) )


class AssetForm( forms.ModelForm ):
    class Meta:
        model = Asset
        fields = ['name', 'insurance', 'repairs', 'broken', 'feedback']

        widgets = {
            'name': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'name'
            } ),
            'insurance': forms.Select( attrs={
                'class': 'form-control', 'id': 'insurance'
            } ),
            'repairs': forms.Select( attrs={
                'class': 'form-control', 'id': 'repairs'
            } ),
            'broken': forms.Select( attrs={
                'class': 'form-control', 'id': 'broken'
            } ),
            'feedback': forms.Textarea( attrs={
                'class': 'form-control', 'id': 'broken'
            } )
        }


class ReportForm( forms.ModelForm ):
    class Meta:
        model = Report
        fields = ['driver', 'vehicle', 'status', 'feedback']

        widgets = {
            'driver': forms.Select( attrs={
                'class': 'form-control', 'id': 'driver'
            } ),
            'vehicle': forms.Select( attrs={
                'class': 'form-control', 'id': 'vehicle'
            } ),
            'status': forms.Select( attrs={
                'class': 'form-control', 'id': 'status'
            } ),
            'feedback': forms.Textarea( attrs={
                'class': 'form-control', 'id': 'feedback'
            } )
        }


class SeasonForm( forms.ModelForm ):
    class Meta:
        model = Season
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'name'
            } ),
            'description': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'description'
            } )
        }


class DropForm( forms.ModelForm ):
    class Meta:
        model = Drop
        fields = ['name']
        widgets = {
            'name': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'name'
            } )
        }


class ProductForm( forms.ModelForm ):
    class Meta:
        model = Product
        fields = ['regno', 'name', 'make']
        widgets = {
            'regno': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'regno'
            } ),
            'name': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'name'
            } ),
            'make': forms.Select( attrs={
                'class': 'form-control', 'id': 'make'
            } )
        }


class OrderForm( forms.ModelForm ):
    class Meta:
        model = Order
        fields = [
            'supplier', 'product', 'design', 'color', 'buyer', 'season', 'drop'
        ]

        widgets = {
            'supplier': forms.Select( attrs={
                'class': 'form-control', 'id': 'supplier'
            } ),
            'product': forms.Select( attrs={
                'class': 'form-control', 'id': 'product'
            } ),
            'design': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'design'
            } ),
            'color': forms.TextInput( attrs={
                'class': 'form-control', 'id': 'color'
            } ),
            'buyer': forms.Select( attrs={
                'class': 'form-control', 'id': 'buyer'
            } ),
            'season': forms.Select( attrs={
                'class': 'form-control', 'id': 'season'
            } ),
            'drop': forms.Select( attrs={
                'class': 'form-control', 'id': 'drop'
            } ),
        }


class DeliveryForm( forms.ModelForm ):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'name': forms.Select( attrs={
                'class': 'form-control', 'id': 'name'
            } ),
            'room_no': forms.Select( attrs={
                'class': 'form-control', 'id': 'room_no'
            } ),
        }


class RoomForm( forms.ModelForm ):
    class Meta:
        model = Room
        fields = ['name', 'room_no']

        widgets = {
            'name': forms.Select( attrs={
                'class': 'form-control', 'id': 'name'
            } ),
            'room_no': forms.Select( attrs={
                'class': 'form-control', 'id': 'room_no'
            } ),
        }
