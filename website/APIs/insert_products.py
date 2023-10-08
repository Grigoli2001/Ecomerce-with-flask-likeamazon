from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# uri = "mongodb+srv://gega:gega2001@cluster0.v7rln8c.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb://localhost:27017"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["amazon"]
collection_name="products"
collection= db[collection_name]

tech = [
    {
        "provider": "Apple",
        "title": "iPhone 15 Pro Max",
        "description": "The latest iPhone with Pro-level features.",
        "price": 1099.99,
        "img_address": "https://www.apple.com/newsroom/images/2023/09/apple-unveils-iphone-15-pro-and-iphone-15-pro-max/article/Apple-iPhone-15-Pro-lineup-hero-230912_Full-Bleed-Image.jpg.large.jpg",
        "category": "Tech",
        "amount_available": 50
    },
    {
        "provider": "Samsung",
        "title": "Samsung Galaxy S23 Ultra",
        "description": "A flagship Android smartphone with a stunning display.",
        "price": 899.99,
        "img_address": "https://images.samsung.com/is/image/samsung/p6pim/uk/2302/feature/uk-feature-galaxy-s23-s918-535093922?$FB_TYPE_I_JPG$",
        "category": "Tech",
        "amount_available": 30
    },
    {
        "provider": "Sony",
        "title": "Sony PlayStation 5",
        "description": "Next-gen gaming console for immersive gaming experiences.",
        "price": 499.99,
        "img_address": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cHM1fGVufDB8fDB8fHww&w=1000&q=80",
        "category": "Tech",
        "amount_available": 20
    },
    {
        "provider": "Dell",
        "title": "Dell XPS 13",
        "description": "Powerful and slim laptop for work and play.",
        "price": 1299.99,
        "img_address": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/xps-notebooks/xps-13-9320/media-gallery/xs9320nt-xnb-shot-5-1-sl.psd?fmt=pjpg&pscan=auto&scl=1&wid=3782&hei=2988&qlt=100,1&resMode=sharp2&size=3782,2988&chrss=full&imwidth=5000",
        "category": "Tech",
        "amount_available": 15
    },
    {
        "provider": "Microsoft",
        "title": "Xbox Series X",
        "description": "High-performance gaming console for serious gamers.",
        "price": 599.99,
        "img_address": "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8eGJveCUyMHNlcmllcyUyMHh8ZW58MHx8MHx8fDA%3D&w=1000&q=80",
        "category": "Tech",
        "amount_available": 25
    },
    {
        "provider": "Canon",
        "title": "Canon EOS 5D Mark IV",
        "description": "Professional-grade DSLR camera for photographers.",
        "price": 2499.99,
        "img_address": "https://www.the-digital-picture.com/Images/Review/Canon-EOS-5D-Mark-IV.jpg",
        "category": "Tech",
        "amount_available": 10
    },
    {
        "provider": "LG",
        "title": "LG OLED 4K TV",
        "description": "Stunning OLED TV for incredible home entertainment.",
        "price": 1799.99,
        "img_address": "https://www.lg.com/fr/images/televiseurs/md07524547/gallery/large01.jpg",
        "category": "Tech",
        "amount_available": 10
    },
    {
        "provider": "Bose",
        "title": "Bose QuietComfort 35 II",
        "description": "Premium noise-canceling headphones for an immersive audio experience.",
        "price": 349.99,
        "img_address": "https://m.media-amazon.com/images/I/81+jNVOUsJL._AC_UF1000,1000_QL80_.jpg",
        "category": "Tech",
        "amount_available": 30
    },
    {
        "provider": "GoPro",
        "title": "GoPro HERO10 Black",
        "description": "Action camera for capturing adventures in high quality.",
        "price": 449.99,
        "img_address": "https://static.gopro.com/assets/blta2b8522e5372af40/blt812ac0751bc75e8d/6193af1ed193b36297ef8398/1_2_H10_Rendering_1550x780_web.webp",
        "category": "Tech",
        "amount_available": 20
    },
    {
        "provider": "Amazon",
        "title": "Amazon Echo Dot (4th Gen)",
        "description": "Smart speaker with Alexa voice control.",
        "price": 49.99,
        "img_address": "https://i.pcmag.com/imagery/reviews/024xU3B68Qf21a4I4d8pfpg-1.fit_lim.size_1050x591.v1601318274.jpg",
        "category": "Tech",
        "amount_available": 40
    }
]
fashion = [
    {
        "provider": "Nike",
        "title": "Nike Air Max 270",
        "description": "Stylish and comfortable sneakers for everyday wear.",
        "price": 129.99,
        "img_address": "https://c0.wallpaperflare.com/preview/226/297/119/canada-windsor-270-shoe.jpg",
        "category": "Fashion",
        "amount_available": 50
    },
    {
        "provider": "Adidas",
        "title": "Adidas Originals Superstar",
        "description": "Iconic shell-toe sneakers that never go out of style.",
        "price": 89.99,
        "img_address": "https://e0.pxfuel.com/wallpapers/549/933/desktop-wallpaper-adidas-originals-adidas-superstar-thumbnail.jpg",
        "category": "Fashion",
        "amount_available": 40
    },
    {
        "provider": "Gucci",
        "title": "Gucci GG Marmont Bag",
        "description": "Luxury leather shoulder bag with iconic GG logo.",
        "price": 1899.99,
        "img_address": "https://www.vintega.com/cdn/shop/files/sac-ggmarmont-gucci-2303-191-GUCCI-vintega-seconde-main-luxe-maroquinerie-occasion_003.jpg?v=1683040297",
        "category": "Fashion",
        "amount_available": 15
    },
    {
        "provider": "Zara",
        "title": "Zara Women's Trench Coat",
        "description": "Classic trench coat for a timeless look.",
        "price": 149.99,
        "img_address": "https://static.zara.net/photos///2023/I/0/1/p/8073/222/704/2/w/412/8073222704_2_2_1.jpg?ts=1693305747048",
        "category": "Fashion",
        "amount_available": 20
    },
    {
        "provider": "Ray-Ban",
        "title": "Ray-Ban Aviator Sunglasses",
        "description": "Iconic aviator sunglasses for a cool, retro look.",
        "price": 159.99,
        "img_address": "https://images.unsplash.com/photo-1622019450027-a7a0f7311122?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8cmF5JTIwYmFufGVufDB8fDB8fHww&w=1000&q=80",
        "category": "Fashion",
        "amount_available": 30
    },
    {
        "provider": "Versace",
        "title": "Versace Medusa Logo Belt",
        "description": "Designer leather belt with the signature Medusa logo buckle.",
        "price": 299.99,
        "img_address": "https://www.versace.com/dw/image/v2/BGWN_PRD/on/demandware.static/-/Sites-ver-master-catalog/default/dw2f208797/original/90_DCU4140-DVTP1_1W03V_24_LaMedusaLeatherBelt--Versace-online-store_0_1.jpg?sw=1200&q=85&strip=true",
        "category": "Fashion",
        "amount_available": 25
    },
    {
        "provider": "H&M",
        "title": "H&M Men's Slim Fit Suit",
        "description": "Tailored slim fit suit for a sharp and modern look.",
        "price": 249.99,
        "img_address": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F68%2F2a%2F682af713478dda02d6b5dd32526b88b8fc5184df.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BLOOKBOOK%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url[file:/product/main]",
        "category": "Fashion",
        "amount_available": 20
    },
    {
        "provider": "Chanel",
        "title": "Chanel Classic Flap Bag",
        "description": "Iconic quilted leather bag from Chanel's collection.",
        "price": 4999.99,
        "img_address": "https://media.istockphoto.com/id/917888624/photo/woman-with-black-chanel-leather-bag-with-silver-chain.jpg?s=612x612&w=0&k=20&c=qIeHKKrwRYYagV0XwY6Q0fYXnXeGbyUvIkPW62hcn1M=",
        "category": "Fashion",
        "amount_available": 10
    },
    {
        "provider": "Levi's",
        "title": "Levi's 501 Original Fit Jeans",
        "description": "Classic denim jeans with a timeless design.",
        "price": 79.99,
        "img_address": "https://lsco.scene7.com/is/image/lsco/125010384-back-pdp-lse?fmt=jpeg&qlt=70&resMode=bisharp&fit=crop,0&op_usm=1.25,0.6,8&wid=2000&hei=1800",
        "category": "Fashion",
        "amount_available": 50
    },
    {
        "provider": "Ralph Lauren",
        "title": "Ralph Lauren Polo Shirt",
        "description": "High-quality cotton polo shirt with the iconic Ralph Lauren logo.",
        "price": 69.99,
        "img_address": "https://images.unsplash.com/photo-1484516396415-4971641de8e0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8cG9sbyUyMHJhbHBoJTIwbGF1cmVufGVufDB8fDB8fHww&w=1000&q=80",
        "category": "Fashion",
        "amount_available": 40
    }
]
cuisine = [
    {
        "provider": "KitchenAid",
        "title": "KitchenAid Stand Mixer",
        "description": "Powerful stand mixer for baking and cooking enthusiasts.",
        "price": 299.99,
        "img_address": "https://i.insider.com/5f99d0306f5b310011724000?width=1000&format=jpeg&auto=webp",
        "category": "Cuisine",
        "amount_available": 20
    },
    {
        "provider": "Cuisinart",
        "title": "Cuisinart Food Processor",
        "description": "Versatile food processor for chopping, slicing, and more.",
        "price": 149.99,
        "img_address": "https://www.cuisinart.com/globalassets/cuisinart-image-feed/dfp-14bcny/dfp14bcny_ff_lifestyle_chimi_prep_left.jpg",
        "category": "Cuisine",
        "amount_available": 15
    },
    {
        "provider": "Le Creuset",
        "title": "Le Creuset Dutch Oven",
        "description": "High-quality enamel-coated Dutch oven for slow cooking.",
        "price": 299.99,
        "img_address": "https://images.unsplash.com/photo-1556909114-6a2fee5216bb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bGUlMjBjcmV1c2V0fGVufDB8fDB8fHww&w=1000&q=80",
        "category": "Cuisine",
        "amount_available": 10
    },
    {
        "provider": "Ninja",
        "title": "Ninja Air Fryer",
        "description": "Air fryer for crispy and healthier fried foods.",
        "price": 129.99,
        "img_address": "https://m.media-amazon.com/images/I/71+8uTMDRFL.jpg",
        "category": "Cuisine",
        "amount_available": 25
    },
    {
        "provider": "Breville",
        "title": "Breville Smart Oven",
        "description": "Compact and efficient smart oven for versatile cooking.",
        "price": 199.99,
        "img_address": "https://www.breville.com/content/dam/breville/ca/catalog/products/images/bov/bov845bss1bca1/pdp.jpg?pdp",
        "category": "Cuisine",
        "amount_available": 15
    },
    {
        "provider": "All-Clad",
        "title": "All-Clad Stainless Steel Cookware Set",
        "description": "Premium stainless steel cookware set for professional-grade cooking.",
        "price": 499.99,
        "img_address": "https://specials-images.forbesimg.com/imageserve/632e45616b494df7e144b11e/cookware-sets/960x0.jpg?fit=scale",
        "category": "Cuisine",
        "amount_available": 10
    },
    {
        "provider": "Vitamix",
        "title": "Vitamix Blender",
        "description": "High-performance blender for smoothies and more.",
        "price": 399.99,
        "img_address": "https://assets.bonappetit.com/photos/5f70d5a414df14d2d86710e4/4:3/w_2624,h_1968,c_limit/Basically-Vitamix.jpg",
        "category": "Cuisine",
        "amount_available": 20
    },
    {
        "provider": "Instant Pot",
        "title": "Instant Pot Multi-Cooker",
        "description": "Versatile multi-cooker for pressure cooking, slow cooking, and more.",
        "price": 129.99,
        "img_address": "https://www.instantpot.com.ph/wp-content/uploads/2021/03/Duo-5.png",
        "category": "Cuisine",
        "amount_available": 30
    },
    {
        "provider": "Pyrex",
        "title": "Pyrex Glass Mixing Bowls",
        "description": "Durable and heat-resistant glass mixing bowls for baking.",
        "price": 39.99,
        "img_address": "https://embed.widencdn.net/img/worldkitchen/vy4jtkhi9k/650x650px/pyr_8pc_sclptrd_mixing_bowl_set_1112377.jpg",
        "category": "Cuisine",
        "amount_available": 50
    },
    {
        "provider": "Wusthof",
        "title": "Wusthof Chef's Knife",
        "description": "High-quality chef's knife for precision slicing and chopping.",
        "price": 99.99,
        "img_address": "https://e1.pxfuel.com/desktop-wallpaper/884/235/desktop-wallpaper-xituo-kitchen-knife-japanese-damascus-steel-chef-knife-very-sharp-bone-knife-fruit-knife-wood-handle-wholesale-price-cooking-chef-knife-thumbnail.jpg",
        "category": "Cuisine",
        "amount_available": 40
    }
]
tools =[
    {
        "provider": "DeWalt",
        "title": "DeWalt Cordless Drill",
        "description": "High-performance cordless drill for DIY projects and more.",
        "price": 149.99,
        "img_address": "https://c8.alamy.com/comp/PCARNN/swindon-uk-july-31-2018-dewalt-cordless-power-tools-on-a-white-background-PCARNN.jpg",
        "category": "Tools",
        "amount_available": 30
    },
    {
        "provider": "Makita",
        "title": "Makita Circular Saw",
        "description": "Powerful circular saw for cutting wood and other materials.",
        "price": 199.99,
        "img_address": "https://m.media-amazon.com/images/I/71RdFLNY-XL.jpg",
        "category": "Tools",
        "amount_available": 25
    },
    {
        "provider": "Craftsman",
        "title": "Craftsman Tool Set",
        "description": "Comprehensive tool set with wrenches, sockets, and more.",
        "price": 249.99,
        "img_address": "https://m.media-amazon.com/images/I/81Gs2qFme+S._AC_UF894,1000_QL80_.jpg",
        "category": "Tools",
        "amount_available": 15
    },
    {
        "provider": "Bosch",
        "title": "Bosch Jigsaw",
        "description": "Versatile jigsaw for precise cutting in various materials.",
        "price": 129.99,
        "img_address": "https://m.media-amazon.com/images/I/81u0t4Rz8VS.jpg",
        "category": "Tools",
        "amount_available": 20
    },
    {
        "provider": "Stanley",
        "title": "Stanley Tape Measure",
        "description": "Durable tape measure for accurate measurements.",
        "price": 19.99,
        "img_address": "https://images.thdstatic.com/productImages/ec09565d-3822-4271-bc81-26600126588a/svn/stanley-tape-measures-33-425d-64_1000.jpg",
        "category": "Tools",
        "amount_available": 50
    },
    {
        "provider": "Ryobi",
        "title": "Ryobi Angle Grinder",
        "description": "Powerful angle grinder for cutting and grinding tasks.",
        "price": 69.99,
        "img_address": "https://images.thdstatic.com/productImages/90e75769-caa1-4010-acb0-e5550f7bcec1/svn/ryobi-angle-grinders-ag454-64_1000.jpg",
        "category": "Tools",
        "amount_available": 30
    },
    {
        "provider": "Husky",
        "title": "Husky Toolbox",
        "description": "Sturdy toolbox for organizing and storing your tools.",
        "price": 49.99,
        "img_address": "https://images.thdstatic.com/productImages/d871518d-f408-4e6d-81c0-5494e853b2c2/svn/matte-black-with-black-finishes-husky-tool-chest-combos-hotc5623bb2s-64_1000.jpg",
        "category": "Tools",
        "amount_available": 40
    },
    {
        "provider": "Klein Tools",
        "title": "Klein Tools Pliers Set",
        "description": "High-quality pliers set for various tasks.",
        "price": 39.99,
        "img_address": "https://m.media-amazon.com/images/I/614NRuwRAXL.jpg",
        "category": "Tools",
        "amount_available": 20
    },
    {
        "provider": "Dremel",
        "title": "Dremel Rotary Tool Kit",
        "description": "Versatile rotary tool kit for precision tasks.",
        "price": 79.99,
        "img_address": "https://www.dremel.com/imagestorage/en-us/4000-6-50-34937-png-16-9-249965_w_750_h_421.png",
        "category": "Tools",
        "amount_available": 25
    },
    {
        "provider": "Black & Decker",
        "title": "Black & Decker Power Drill",
        "description": "Compact power drill for light-duty drilling and screwdriving.",
        "price": 49.99,
        "img_address": "https://c8.alamy.com/comp/CENX8W/electrical-goods-for-sale-uk-black-decker-power-tools-for-sale-in-CENX8W.jpg",
        "category": "Tools",
        "amount_available": 35
    }
]

if collection.count_documents({}) == 0:
    # Insert the products if they don't exist
    collection.insert_many(tools)
    collection.insert_many(cuisine)
    collection.insert_many(fashion)
    collection.insert_many(tech)
    print("Products inserted successfully!")




