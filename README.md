# administ
A very simple django middleware for view django exception debug page.
developed by bunseokbot@SSG

## Install administ
**1. Get administ from pip**
```
pip install django-administ 
```

**2. Add installed apps**
```
INSTALLED_APPS = [
  ....
  'administ',
]
```

**3. Add middleware list**
```
MIDDLEWARE = [
  ....
  'administ.middleware.AdministMiddleware',
]
```

**4. Add allowed IP address to manage trace message**
```
ADMINIST_ALLOWED_IP = [
  '127.0.0.1',
  '192.168.0.3',
]
```

Profit! and enjoy!
