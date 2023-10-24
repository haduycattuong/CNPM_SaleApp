
def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]

def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'Tivi',
        'price': 6000000,
        'image': 'https://www.lg.com/vn/images/tivi/md07551504/D-1.jpg'
    }, {
        'id': 2,
        'name': 'Ipad',
        'price': 500000,
        'image': 'https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/ipad-pro-2021-11inch-grey_2.jpg'

    }, {
    }, {
        'id': 3,
        'name': 'Iphone',
        'price': 500000,
        'image': 'https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/ipad-pro-2021-11inch-grey_2.jpg'

    }, {
    }, {
        'id': 4,
        'name': 'Ipad',
        'price': 500000,
        'image': 'https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/ipad-pro-2021-11inch-grey_2.jpg'

    }, {
    }, {
        'id': 5,
        'name': 'Ipad',
        'price': 500000,
        'image': 'https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/ipad-pro-2021-11inch-grey_2.jpg'

    }, {
    }, {
        'id': 6,
        'name': 'Ipad',
        'price': 500000,
        'image': 'https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/ipad-pro-2021-11inch-grey_2.jpg'

    }, {
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products