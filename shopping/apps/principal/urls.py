from django.conf.urls import patterns, url

urlpatterns = patterns('shopping.apps.principal.views',
	url(r'^$', 'home', name = 'home'),
	url(r'^Lista-productos/(?P<category_id>\d+)/', 'list_producto', name = 'list_producto'),
	url(r'^Agregar/(?P<product_id>\d+)/', 'add_producto', name = 'add_producto'),
	url(r'^Eliminar/(?P<shop>\d+)/', 'delete_product', name = 'delete_product'),
	url(r'^Mis-productos/', 'my_product', name = 'my_product'),
	url(r'^Comprar/', 'shopping', name = 'shopping'),
	url(r'^Mis-compras/', 'my_shop', name = 'my_shop'),
	url(r'^Registrarme/', 'registry', name = 'registry'),
	url(r'^Login/', 'login_user', name = 'login_user'),
	url(r'^Logout/', 'logout_user', name = 'logout_user'),
)