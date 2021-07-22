from django.contrib import admin

from .models import (

    Checkout
)



class CheckoutAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        # "user",
        "amount",
        "paid",
        # "success",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "amount", "paid")
    # list_editable = ("amount", "paid")


admin.site.register(Checkout, CheckoutAdmin)
