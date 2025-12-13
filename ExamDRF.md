# CodeCourse Platform API

## Цель

Создать REST API платформы онлайн-курсов с модулями и задачами, где студенты могут сдавать решения и получать статус проверки.

**Время:** 2 дня
**Максимальный балл:** 50

---

## 1. Модели

### User
### Course
### CourseModule
### Task
### Submission



## 2. Функционал API

### 2.1 Nested сериализация

* GET Course → все модули и их задачи
* GET Module → все задачи модуля
* GET Task → все submission для этой задачи
* `to_representation` для Submission: показывать `username` вместо `user_id`, название модуля и курса

### 2.2 CRUD

* CRUD для Course, Module, Task (только admin)
* CRUD для Submission (только залогиненный пользователь может создавать и редактировать свои submissions)

### 2.3 Custom Validation

* max_score > 0 для Task
* Submission нельзя сдавать, если Task не активна (например, дата курса закончена)
* score не может превышать max_score

### 2.4 Фильтры и поиск

* Фильтр задач по module_id или course_id
* Поиск задач по title
* Фильтр submission по status (Accepted/Rejected/Pending)
* Пагинация для списков (5–10 элементов на страницу, с info о текущей странице и общем кол-ве страниц)

### 2.5 Аутентификация и права

* SessionAuthentication
* Студент может создавать/редактировать только свои Submission
* Admin может редактировать Course, Module, Task, Submission любого пользователя
* GET Course/Module/Task доступен всем

### 2.6 Swagger/OpenAPI документация

* drf-yasg для всех эндпоинтов
* Фильтры, поиск и параметры должны быть видны

---

## 3. Дополнительно (бонус)

* Endpoint: рейтинг студента по сумме баллов всех submissions
* Endpoint: задачи с наибольшим числом Accepted submissions
* Кастомная пагинация для Submission с выводом: текущая страница, общее количество страниц, количество элементов на странице

---

## 4. Структура проекта (пример)

```
codecourse/
├─ codecourse/
│  ├─ settings.py
│  ├─ urls.py
│  └─ ...
├─ courses/
│  ├─ models.py  # Course, CourseModule, Task
│  ├─ serializers.py
│  ├─ views.py
│  ├─ urls.py
│  └─ ...
├─ submissions/
│  ├─ models.py  # Submission
│  ├─ serializers.py
│  ├─ views.py
│  ├─ urls.py
│  └─ ...
└─ manage.py
```

---

## 5. Примеры эндпоинтов

### Course

* GET `/api/courses/` → список курсов с nested модулями и задачами
* POST `/api/courses/` → создать курс (admin)

### Module

* GET `/api/modules/` → список модулей (фильтр по course_id)
* POST `/api/modules/` → создать модуль (admin)

### Task

* GET `/api/tasks/` → список задач (поиск по title, фильтр по module/course)
* POST `/api/tasks/` → создать задачу (admin)

### Submission

* POST `/api/submissions/` → создать submission (только для залогиненного)
* GET `/api/submissions/` → список submission (фильтр по статусу, пагинация)
* PATCH `/api/submissions/<id>/` → обновить свой submission
* GET `/api/submissions/rating/` → рейтинг студентов
 

* POST /api/tasks/<task_id>/submissions/ → создать submission для конкретной задачи (только залогиненный пользователь)

* GET /api/tasks/<task_id>/submissions/ → только submission текущего пользователя для этой задачи

* GET /api/submissions/ → список submission (admin: все, user: только свои; фильтр по статусу, пагинация)

* GET /api/submissions/rating/ → рейтинг студентов

 
