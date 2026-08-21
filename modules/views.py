from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Admin, Student


@api_view(["POST"])
def login_view(request):

    email = request.data.get("email")
    password = request.data.get("password")

    # =====================================
    # VALIDATE INPUT
    # =====================================

    if not email or not password:

        return Response({
            "success": False,
            "message": "Email and password are required."
        }, status=400)


    # =====================================
    # CHECK ADMIN TABLE
    # =====================================

    admin = Admin.objects.filter(
        email=email
    ).first()

    if admin:

        if admin.password == password:

            return Response({

                "success": True,

                "user_type": "admin",

                "user": {
                    "id": admin.id,
                    "name": admin.name,
                    "email": admin.email
                }

            })

        else:

            return Response({

                "success": False,
                "message": "Invalid password."

            }, status=401)


    # =====================================
    # CHECK STUDENT TABLE
    # =====================================

    student = Student.objects.filter(
        email=email
    ).first()

    if student:

        if student.password == password:

            return Response({

                "success": True,

                "user_type": "student",

                "user": {
                    "id": student.id,
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "email": student.email,
                    "mobile": student.mobile
                }

            })

        else:

            return Response({

                "success": False,
                "message": "Invalid password."

            }, status=401)


    # =====================================
    # EMAIL NOT FOUND
    # =====================================

    return Response({

        "success": False,
        "message": "Email not registered."

    }, status=404)