from craigslist_app.models import Category, Post

category1 = Category(name='Vehicles')
category1.save()

category2 = Category(name='Cloths')
category2.save()

category3 = Category(name='Furniture')
category3.save()

category4 = Category(name='Football Teams')
category4.save()

post1 = Post(category=category1, item = 'Honda Accord', description='Honda Accord', location = 'Minnesota')
post1.save()

post2 = Post(category=category2, item = 'Wedding Dress', description='Never warn, the bastird cheated on me.', location = 'New York')
post2.save()

post3 = Post(category=category3, item = 'Couch', description='Green couch, minor food stains, nothing gross', location = 'Chicago')
post3.save()

post4 = Post(category=category1, item = 'Can-Am ATV', description='Like new, 700cc, only driven 1000 miles', location = 'Minnesota')
post4.save()

post5 = Post(category=category4, item = 'The Green Bay Packers', description='Go Pack Go', location = 'Green Bay')
post5.save()

post6 = Post(category=category4, item = 'Bears Suck', description='DAAAAAAAAH BEEAAARRRSSS', location = 'Chicago')
post6.save()