from django.contrib import admin
from coaches.models import Coach
from coaches.models import User2


# Register your models here.

class CoachAdmin(admin.ModelAdmin):
    # list_display = ['user', 'gender', 'phone', 'address', 'skype', 'description']
    list_display = ['get_name', 'user', 'gender', 'phone', 'address', 'skype', 'description', 'is_staff']
    list_filter = ['gender', 'user__is_staff']

    def is_staff(self, obj):
        return obj.user.is_staff

    def get_name(self, obj):
        return obj.user.first_name

    get_name.admin_order_field = 'First Name'  # Allows column order sorting
    get_name.short_description = 'First Name'  # Renames column head

    is_staff.admin_order_field = 'staff'  # Allows column order sorting
    is_staff.short_description = 'Is staff'  # Renames column head


admin.site.register(Coach, CoachAdmin)
admin.site.register(User2)
