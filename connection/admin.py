from django.contrib import admin
from connection.models import ConnectionBlock, ConnectionRequest, Connection

admin.site.register(ConnectionRequest)
admin.site.register(Connection)
admin.site.register(ConnectionBlock)
