#### **1. Django REST Framework (DRF) Overview**
Django REST Framework (DRF) is used to build RESTful APIs with Django. It simplifies:
- Serialization: Converts complex data (e.g., Django models) into formats like JSON.
- Authentication: Handles user access securely.
- Permissions: Controls who can access the API.
- Browsable API: Interactive testing directly in the browser.

---

#### **2. DRF Architecture**
**Key Components:**
- **Serializers**: Converts data between Python objects and JSON.  
- **ViewSets**: Groups logic for handling HTTP methods (GET, POST, etc.).  
- **Routers**: Automatically maps URLs to ViewSets.

---

#### **3. Example: Create a Basic API**
Here’s a step-by-step example of creating an API to manage a `Book` model.

---

#### **Step 1: Create a Django Project**
Run these commands:
```bash
django-admin startproject my_project
cd my_project
python manage.py startapp my_app
```

---

#### **Step 2: Install and Configure DRF**
Install DRF:
```bash
pip install djangorestframework
```

Add `'rest_framework'` to `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'rest_framework',
]
```

---

#### **Step 3: Define the `Book` Model**
In `my_app/models.py`:
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

#### **Step 4: Create a Serializer**
In `my_app/serializers.py`:
```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

---

#### **Step 5: Create a View**
In `my_app/views.py`:
```python
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

---

#### **Step 6: Define a URL Pattern**
In `my_app/urls.py`:
```python
from django.urls import path
from .views import BookListCreateAPIView

urlpatterns = [
    path('api/books/', BookListCreateAPIView.as_view(), name='book_list_create'),
]
```

Include this in `my_project/urls.py`:
```python
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
]
```

---

#### **Step 7: Run the Server**
Start the development server:
```bash
python manage.py runserver
```

---

#### **Example API Interaction**
**Endpoint:** `http://127.0.0.1:8000/api/books/`

1. **POST Request: Add a New Book**
   Request Body (JSON):
   ```json
   {
       "title": "Django Unchained",
       "author": "Quentin Tarantino",
       "published_date": "2012-12-25"
   }
   ```

   Response:
   ```json
   {
       "id": 1,
       "title": "Django Unchained",
       "author": "Quentin Tarantino",
       "published_date": "2012-12-25"
   }
   ```

2. **GET Request: Retrieve All Books**
   Response:
   ```json
   [
       {
           "id": 1,
           "title": "Django Unchained",
           "author": "Quentin Tarantino",
           "published_date": "2012-12-25"
       }
   ]
   ```

---

#### **4. Extend `BookSerializer` with a Custom Field**
In `my_app/serializers.py`:
```python
from datetime import datetime
from django.utils.timezone import now

class BookSerializer(serializers.ModelSerializer):
    days_since_creation = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_days_since_creation(self, obj):
        return (now().date() - obj.published_date).days
```

**Output Example:**
```json
{
    "id": 1,
    "title": "Django Unchained",
    "author": "Quentin Tarantino",
    "published_date": "2012-12-25",
    "days_since_creation": 4018
}
```
