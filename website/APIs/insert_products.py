from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# uri = "mongodb+srv://gega:gega2001@cluster0.v7rln8c.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb://localhost:27017"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client["amazon"]
collection_name="products"
collection= db[collection_name]

tech = [
    {
        "provider": "Apple",
        "title": "iPhone 13 Pro",
        "description": "The latest iPhone with Pro-level features.",
        "price": 1099.99,
        "img_address": "https://example.com/apple-iphone-13-pro.jpg",
        "category": "Tech",
        "amount_available": 50
    },
    {
        "provider": "Samsung",
        "title": "Samsung Galaxy S21",
        "description": "A flagship Android smartphone with a stunning display.",
        "price": 899.99,
        "img_address": "https://example.com/samsung-galaxy-s21.jpg",
        "category": "Tech",
        "amount_available": 30
    },
    {
        "provider": "Sony",
        "title": "Sony PlayStation 5",
        "description": "Next-gen gaming console for immersive gaming experiences.",
        "price": 499.99,
        "img_address": "https://example.com/sony-playstation-5.jpg",
        "category": "Tech",
        "amount_available": 20
    },
    {
        "provider": "Dell",
        "title": "Dell XPS 13",
        "description": "Powerful and slim laptop for work and play.",
        "price": 1299.99,
        "img_address": "https://example.com/dell-xps-13.jpg",
        "category": "Tech",
        "amount_available": 15
    },
    {
        "provider": "Microsoft",
        "title": "Xbox Series X",
        "description": "High-performance gaming console for serious gamers.",
        "price": 599.99,
        "img_address": "https://example.com/microsoft-xbox-series-x.jpg",
        "category": "Tech",
        "amount_available": 25
    },
    {
        "provider": "Canon",
        "title": "Canon EOS 5D Mark IV",
        "description": "Professional-grade DSLR camera for photographers.",
        "price": 2499.99,
        "img_address": "https://example.com/canon-eos-5d-mark-iv.jpg",
        "category": "Tech",
        "amount_available": 10
    },
    {
        "provider": "LG",
        "title": "LG OLED 4K TV",
        "description": "Stunning OLED TV for incredible home entertainment.",
        "price": 1799.99,
        "img_address": "https://example.com/lg-oled-4k-tv.jpg",
        "category": "Tech",
        "amount_available": 10
    },
    {
        "provider": "Bose",
        "title": "Bose QuietComfort 35 II",
        "description": "Premium noise-canceling headphones for an immersive audio experience.",
        "price": 349.99,
        "img_address": "https://example.com/bose-quietcomfort-35-ii.jpg",
        "category": "Tech",
        "amount_available": 30
    },
    {
        "provider": "GoPro",
        "title": "GoPro HERO10 Black",
        "description": "Action camera for capturing adventures in high quality.",
        "price": 449.99,
        "img_address": "https://example.com/gopro-hero10-black.jpg",
        "category": "Tech",
        "amount_available": 20
    },
    {
        "provider": "Amazon",
        "title": "Amazon Echo Dot (4th Gen)",
        "description": "Smart speaker with Alexa voice control.",
        "price": 49.99,
        "img_address": "https://example.com/amazon-echo-dot-4th-gen.jpg",
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
        "img_address": "https://example.com/nike-air-max-270.jpg",
        "category": "Fashion",
        "amount_available": 50
    },
    {
        "provider": "Adidas",
        "title": "Adidas Originals Superstar",
        "description": "Iconic shell-toe sneakers that never go out of style.",
        "price": 89.99,
        "img_address": "https://example.com/adidas-superstar.jpg",
        "category": "Fashion",
        "amount_available": 40
    },
    {
        "provider": "Gucci",
        "title": "Gucci GG Marmont Bag",
        "description": "Luxury leather shoulder bag with iconic GG logo.",
        "price": 1899.99,
        "img_address": "https://example.com/gucci-gg-marmont-bag.jpg",
        "category": "Fashion",
        "amount_available": 15
    },
    {
        "provider": "Zara",
        "title": "Zara Women's Trench Coat",
        "description": "Classic trench coat for a timeless look.",
        "price": 149.99,
        "img_address": "https://example.com/zara-womens-trench-coat.jpg",
        "category": "Fashion",
        "amount_available": 20
    },
    {
        "provider": "Ray-Ban",
        "title": "Ray-Ban Aviator Sunglasses",
        "description": "Iconic aviator sunglasses for a cool, retro look.",
        "price": 159.99,
        "img_address": "https://example.com/ray-ban-aviator-sunglasses.jpg",
        "category": "Fashion",
        "amount_available": 30
    },
    {
        "provider": "Versace",
        "title": "Versace Medusa Logo Belt",
        "description": "Designer leather belt with the signature Medusa logo buckle.",
        "price": 299.99,
        "img_address": "https://example.com/versace-medusa-logo-belt.jpg",
        "category": "Fashion",
        "amount_available": 25
    },
    {
        "provider": "H&M",
        "title": "H&M Men's Slim Fit Suit",
        "description": "Tailored slim fit suit for a sharp and modern look.",
        "price": 249.99,
        "img_address": "https://example.com/hm-mens-slim-fit-suit.jpg",
        "category": "Fashion",
        "amount_available": 20
    },
    {
        "provider": "Chanel",
        "title": "Chanel Classic Flap Bag",
        "description": "Iconic quilted leather bag from Chanel's collection.",
        "price": 4999.99,
        "img_address": "https://example.com/chanel-classic-flap-bag.jpg",
        "category": "Fashion",
        "amount_available": 10
    },
    {
        "provider": "Levi's",
        "title": "Levi's 501 Original Fit Jeans",
        "description": "Classic denim jeans with a timeless design.",
        "price": 79.99,
        "img_address": "https://example.com/levis-501-jeans.jpg",
        "category": "Fashion",
        "amount_available": 50
    },
    {
        "provider": "Ralph Lauren",
        "title": "Ralph Lauren Polo Shirt",
        "description": "High-quality cotton polo shirt with the iconic Ralph Lauren logo.",
        "price": 69.99,
        "img_address": "https://example.com/ralph-lauren-polo-shirt.jpg",
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
        "img_address": "https://example.com/kitchenaid-stand-mixer.jpg",
        "category": "Cuisine",
        "amount_available": 20
    },
    {
        "provider": "Cuisinart",
        "title": "Cuisinart Food Processor",
        "description": "Versatile food processor for chopping, slicing, and more.",
        "price": 149.99,
        "img_address": "https://example.com/cuisinart-food-processor.jpg",
        "category": "Cuisine",
        "amount_available": 15
    },
    {
        "provider": "Le Creuset",
        "title": "Le Creuset Dutch Oven",
        "description": "High-quality enamel-coated Dutch oven for slow cooking.",
        "price": 299.99,
        "img_address": "https://example.com/le-creuset-dutch-oven.jpg",
        "category": "Cuisine",
        "amount_available": 10
    },
    {
        "provider": "Ninja",
        "title": "Ninja Air Fryer",
        "description": "Air fryer for crispy and healthier fried foods.",
        "price": 129.99,
        "img_address": "https://example.com/ninja-air-fryer.jpg",
        "category": "Cuisine",
        "amount_available": 25
    },
    {
        "provider": "Breville",
        "title": "Breville Smart Oven",
        "description": "Compact and efficient smart oven for versatile cooking.",
        "price": 199.99,
        "img_address": "https://example.com/breville-smart-oven.jpg",
        "category": "Cuisine",
        "amount_available": 15
    },
    {
        "provider": "All-Clad",
        "title": "All-Clad Stainless Steel Cookware Set",
        "description": "Premium stainless steel cookware set for professional-grade cooking.",
        "price": 499.99,
        "img_address": "https://example.com/all-clad-cookware-set.jpg",
        "category": "Cuisine",
        "amount_available": 10
    },
    {
        "provider": "Vitamix",
        "title": "Vitamix Blender",
        "description": "High-performance blender for smoothies and more.",
        "price": 399.99,
        "img_address": "https://example.com/vitamix-blender.jpg",
        "category": "Cuisine",
        "amount_available": 20
    },
    {
        "provider": "Instant Pot",
        "title": "Instant Pot Multi-Cooker",
        "description": "Versatile multi-cooker for pressure cooking, slow cooking, and more.",
        "price": 129.99,
        "img_address": "https://example.com/instant-pot-multi-cooker.jpg",
        "category": "Cuisine",
        "amount_available": 30
    },
    {
        "provider": "Pyrex",
        "title": "Pyrex Glass Mixing Bowls",
        "description": "Durable and heat-resistant glass mixing bowls for baking.",
        "price": 39.99,
        "img_address": "https://example.com/pyrex-glass-mixing-bowls.jpg",
        "category": "Cuisine",
        "amount_available": 50
    },
    {
        "provider": "Wusthof",
        "title": "Wusthof Chef's Knife",
        "description": "High-quality chef's knife for precision slicing and chopping.",
        "price": 99.99,
        "img_address": "https://example.com/wusthof-chefs-knife.jpg",
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
        "img_address": "https://example.com/dewalt-cordless-drill.jpg",
        "category": "Tools",
        "amount_available": 30
    },
    {
        "provider": "Makita",
        "title": "Makita Circular Saw",
        "description": "Powerful circular saw for cutting wood and other materials.",
        "price": 199.99,
        "img_address": "https://example.com/makita-circular-saw.jpg",
        "category": "Tools",
        "amount_available": 25
    },
    {
        "provider": "Craftsman",
        "title": "Craftsman Tool Set",
        "description": "Comprehensive tool set with wrenches, sockets, and more.",
        "price": 249.99,
        "img_address": "https://example.com/craftsman-tool-set.jpg",
        "category": "Tools",
        "amount_available": 15
    },
    {
        "provider": "Bosch",
        "title": "Bosch Jigsaw",
        "description": "Versatile jigsaw for precise cutting in various materials.",
        "price": 129.99,
        "img_address": "https://example.com/bosch-jigsaw.jpg",
        "category": "Tools",
        "amount_available": 20
    },
    {
        "provider": "Stanley",
        "title": "Stanley Tape Measure",
        "description": "Durable tape measure for accurate measurements.",
        "price": 19.99,
        "img_address": "https://example.com/stanley-tape-measure.jpg",
        "category": "Tools",
        "amount_available": 50
    },
    {
        "provider": "Ryobi",
        "title": "Ryobi Angle Grinder",
        "description": "Powerful angle grinder for cutting and grinding tasks.",
        "price": 69.99,
        "img_address": "https://example.com/ryobi-angle-grinder.jpg",
        "category": "Tools",
        "amount_available": 30
    },
    {
        "provider": "Husky",
        "title": "Husky Toolbox",
        "description": "Sturdy toolbox for organizing and storing your tools.",
        "price": 49.99,
        "img_address": "https://example.com/husky-toolbox.jpg",
        "category": "Tools",
        "amount_available": 40
    },
    {
        "provider": "Klein Tools",
        "title": "Klein Tools Pliers Set",
        "description": "High-quality pliers set for various tasks.",
        "price": 39.99,
        "img_address": "https://example.com/klein-tools-pliers-set.jpg",
        "category": "Tools",
        "amount_available": 20
    },
    {
        "provider": "Dremel",
        "title": "Dremel Rotary Tool Kit",
        "description": "Versatile rotary tool kit for precision tasks.",
        "price": 79.99,
        "img_address": "https://example.com/dremel-rotary-tool-kit.jpg",
        "category": "Tools",
        "amount_available": 25
    },
    {
        "provider": "Black & Decker",
        "title": "Black & Decker Power Drill",
        "description": "Compact power drill for light-duty drilling and screwdriving.",
        "price": 49.99,
        "img_address": "https://example.com/black-decker-power-drill.jpg",
        "category": "Tools",
        "amount_available": 35
    }
]

collection.insert_many(tools)