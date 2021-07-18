from craigslist_app.models import Category, Post

category1 = Category(name='Vehicles')
category1.save()

category2 = Category(name='Cloths')
category2.save()

category3 = Category(name='Furniture')
category3.save()

post1 = Post(category=category1, item = 'Honda Accord', description='Honda Accord')
post1.save()

post2 = Post(category=category2, item = 'Wedding Dress', description='Never warn, the bastird cheated on me.')
post2.save()

post3 = Post(category=category3, item = 'Couch', description='Green couch, minor food stains, nothing gross')
post3.save()

post4 = Post(category=category1, item = 'Can-Am ATV', description='Like new, 700cc, only driven 1000 miles')
post4.save()