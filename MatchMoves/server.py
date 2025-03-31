from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# Your dataset for hw6 (example based on hw6 instructions)
data = {
    "1": {
        "id": "1",
        "name": "Cha Cha Matcha (Madison)",
        "image": "https://lh5.googleusercontent.com/p/AF1QipM4JAAWq6gNM6j2dUSuFIx2Zz-IAtPljPxzQW54=w408-h399-k-no",
        "rating": "4.2",
        "address": "477 Madison Ave, New York, NY 10022", 
        "overview": "We started cha cha as an alternative to artisanal coffee culture and the extreme, hyperbolic world of energy drinks. This is not your ordinary caffeine fix. Our adventurous elixirs - made with ceremonial grade matcha - are a special sort of pick-me-up. A calm, clear, and centered energy, guaranteed to elevate your day.",
        "matcha": ["Matcha Latte", "Matcha Chai", "Matcha Lemonade", "Draft Matcha Latte", "Strawberry Matcha"], 
        "other": ["Purple Drink", "Blue Drink", "Ginger Tumeric", "Beautiful Latte", "Strawberry Lemonade"],
        "similar_places": ["2", "3"], 
    },
    "2": {
        "id": "2",
        "name": "Moka Machine - Lexington Market",
        "image": "https://lh5.googleusercontent.com/p/AF1QipOAVWLMVEE9jJPdVcGUatF6mnGDqegDmVd3eaWC=w408-h271-k-no",
        "rating": "3.8",
        "address": "570 Lexington Ave, New York, NY 10022", 
        "overview": "At Moka Matcha, enjoy premium matcha drinks, La Colombe coffee, and house-made treats like cookies and scones. From creamy lattes to sweet indulgences, we satisfy every craving. Order now for delivery or pickup!",
        "matcha": ["Matcha Latte", "Matcha", "Moka Matcha"],
        "other" : ["Caramel Macchiato", "Iced Caramel Macchiato", "Iced Matcha Cream", "Strawberry Lemonade", "Iced Cinnamon Cream Shaken Espresso"],
        "similar_places": ["1", "3"],
    }, 
    "3": {
        "id" : "3", 
        "name" : "MuCha’s Matcha", 
        "image": "https://lh5.googleusercontent.com/p/AF1QipPHGdjI-7e_EESEwirg2fBUSTO_a1MdqJf9r-lv=w408-h544-k-no", 
        "rating": "5.0", 
        "address": "162 E 25th St, New York, NY 10010", 
        "overview": "All of our drinks are made with Ceremonial Grade Matcha. Our suppliers are based in Kyoto, Japan. Once we place an order, tea leaves are freshly harvested, steamed, and air-dried before being finely ground in a traditional stone mill. This finished power is then sealed and shipped directly to us. This made-to-order approach ensures freshness and exceptional quality in every serving of our powder.", 
        "matcha": ["Biscoff Cookie Matcha", "Blueberry Peach Matcha", "Brown Sugar Matcha", "Cinnamon Vanilla Matcha", "Fresh Strawberry Banana Matcha", "Honey Rose Matcha", "Lavender Matcha", "Red Bean Pistachio Matcha", "Strawberry/Peach/Mango Matcha", "Ube Matcha Foam"], 
        "other": ["Coconut Matcha", "Matcha Lemonade", "Strawberry/Mango Lemonade"], 
        "similar_places": ["4", "5"], 
    }, 

    "4": {
        "id" : "4", 
        "name" : "Isshiki Matcha", 
        "image" : "https://lh5.googleusercontent.com/p/AF1QipMRA50nYVCYRSR7-uA_F7TDiAhRbK1VGHkt_Mzf=w408-h544-k-no", 
        "rating": "4.4", 
        "address": "138 2nd Ave Inside Moko, New York, NY 10003", 
        "overview": "A Taste of Tranquility from Uji, Kyoto Nestled in the heart of New York City, Isshiki Matcha brings you the essence of calm and tradition from the serene landscapes of Uji, Kyoto. Our name, 'Isshiki,' meaning 'one color' in Japanese, reflects the purity and simplicity of matcha - a vibrant green hue that symbolizes both vitality and tranquility.         But Isshiki Matcha is more than just a beverage - it's a moment of stillness in a bustling world, a grounding anchor in your daily routine. We believe that amidst the chaos of modern life, everyone deserves a moment of zen, a quiet respite to reconnect with themselves and find balance.", 
        "matcha": ["Matcha Latte", "Brown Sugar Matcha Latte", "Strawberry Matcha Latte", "Hazelnut Matcha Latte", "Pistachio Matcha Latte"], 
        "other": ["Sencha", "Gyokuro", "Oolong", "Genmaicha"],
        "similar_places": ["3", "7", "4"], 
    }, 

    "5": {
        "id" : "5", 
        "name": "Maiko Matcha Cafe", 
        "image" : "https://lh5.googleusercontent.com/p/AF1QipPWKC2byVFl3USanqi1gLQ_YcP5MW6zH_YzgyQC=w408-h306-k-no",  
        "rating": "4.6",
        "address": "133-33 39th Ave, fh21, Flushing, NY 11354", 
        "overview": "Matcha Cafe Maiko opened its first store in Hawaii with the goal of providing customers quality matcha with the authentic taste. Our matcha comes from Harima Garden, which has been in operation since 1858. Their product is high quality and delivers a great smell and outstanding taste.", 
        "matcha" : ["Matcha Latte", "Matcha Frappe", "Matcha Lemon"], 
        "other" : ["Hojicha", "Uji Kintoki", "Shaved Iced (Matcha)", "Shaved Ice(Vanilla)" ],
        "similar_places": ["3", "4"], 
    }, 

    "6": {
        "id": "6", 
        "name": "Matchaful Culinary Lab", 
        "image": "https://lh5.googleusercontent.com/p/AF1QipOh6gnb355g7a3cH0kEViirnoRN4ZsilU7l97AG=w408-h272-k-no",
        "rating": "4.4", 
        "address": "44 Washington Ave, Brooklyn, NY 11205", 
        "overview": " A very heartfelt 'Thank You!' from Team Matchaful for your support with our home delivery and bottled latte program. We are committed to keeping our customers and our employees safe during the COVID-19 outbreak, which is why we’re bringing Matchaful straight to your door. We want you to know we are exercising the highest level of caution in our kitchen and packaging facilities.", 
        "matcha": ["Oishii Berry Matcha Latte", "Frozen Matcha"], 
        "other": ["Earth Glow", "Houjicha Latte"], 
        "similar_places" : ["7", "8"], 
    }, 

    "7": {
        "id" : "7", 
        "name": "Cha-An", 
        "image" : "https://lh5.googleusercontent.com/p/AF1QipOM4QRoz_e61Vbzb_3wT_s78iAQYPoL01djPwtd=w408-h544-k-no", 
        "rating": "4.3", 
        "address": "230 E 9th St 2nd FL, New York, NY 10003", 
        "overview" : "Cha-An features not only matcha and senchas from Japan, but an extensive list of teas from all over the world as well. There is a tea for everyone and all are prepared with care. Cha-An also specializes in desserts – while some are traditionally Japanese, we also blend the tastes of Japan with sweets of the West. Not to be overlooked are our savory dishes, which include several types of toasts that are made with thick slices of fluffy, house-baked Japanese milk bread.", 
        "matcha": ["Matcha(Kyoto Uji)", "Kiwami Matcha", "Iced Rose Matcha"], 
        "other": ["Jasmine Pearls Tea", "Kanabow cha", "Genmaicha Tea", "Tenko Tea", "Sakura Sencha Tea"], 
        "similar_places": ["6", "10", "9"], 
    }, 

    "8": {
        "id" : "8", 
        "name": "Blank Street-92 Street", 
        "image": "https://lh5.googleusercontent.com/p/AF1QipPwJUObF4hIb7etfvU9GlihyrSYyXAw4ox7R0eJ=w408-h544-k-no", 
        "rating": "4.4",
        "address": "2461 Broadway, New York, NY 10025", 
        "overview": "When we started Blank Street, we set out to reimagine what a coffee shop could be. Serving a clean, natural, and high quality menu to our customers at affordable prices. In August 2020, we launched our first location, a 5x10 coffee cart nestled in the garden of the Wythe diner in Brooklyn. Our operation was simple and our footprint was small, which let us remove costs that didn’t benefit our customers or baristas. This allowed us to source top of the range specialty coffees from around the world, serve clean and fresh food sourced locally, and pay our baristas above market wages.", 
        "matcha": ["Iced Matcha Latte", "Iced Matcha Tea", "Iced Banana Bread Matcha", "Iced Blueberry Matcha", "Iced White Chocolate Matcha"],
        "other": ["Mocha Cold Brew Latte", "Shaken Brown Sugar Cold Brew", "Iced Pistachio Latte", "Iced Strawberries & Cream Latte"],
        "similar_places": ["6", "10"],   
    }, 

    "9": {
        "id": "9", 
        "name": "Moa Coffee Woodside", 
        "image": "https://lh5.googleusercontent.com/p/AF1QipPi4WzGpY-qaqnqXK00lYMJTZhb2CDiHxbqH1cz=w408-h306-k-no", 
        "rating": "4.6", 
        "address": "61-08 Woodside Ave, Woodside, NY 11377", 
        "overview": "We started Moa Coffee in 2018 in Astoria. We currently have 3 locations all in Queens: Astoria, Sunnyside & Woodside. We provide specialty coffee, tea, unique drinks, fresh baked goods, great service and great vibes! There is always something to enjoy!", 
        "matcha": ["Matcha Latte"], 
        "other": ["Chai Latte", "Oat Milk Draft Latte", "Oat Milk Black & Tan", "Original Draft Latte", "Original Black & Tan"], 
        "similar_places": ["7"], 
    }, 

    "10": {
        "id": "10", 
        "name": "Maman", 
        "image": "https://lh5.googleusercontent.com/p/AF1QipOsIEMApa7awLsAq99Q3fOUxM-5ieJptA1zvNT3=w426-h240-k-no", 
        "rating": "4.3", 
        "address": "667 Lexington Ave, New York, NY 10022", 
        "overview": "grab a coffee at our upper east side location on your way to the iconic steps of the metropolitan museum of art. as our first uptown location, maman upper east side holds a special spot in our heart. snag a cozy spot by the window & curl up with a book or enjoy a meal in our spacious dining area. looking for the perfect spot for your next gathering? our versatile space is bound to fit the event of your dreams.", 
        "matcha": ["Iced Matcha Latte", "Iced Peppermint Almond Matcha Latte"],
        "other": ["Iced Cardamom Bun Latte", "Iced Honey Lavender Latte", "Iced Mocha"], 
        "similar_places": ["7", "8"], 
    }, 
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_popular_items')
def get_popular_items():
    # Select 3 popular items 
    popular_items = list(data.values())[:4]
    return jsonify(popular_items)


def highlight(text, query):
    if not query or not text:
        return text
    
    # Convert both to string to ensure we're working with strings
    text = str(text)
    query = str(query)
    
    # Case-insensitive search by converting both to lowercase for comparison
    lower_text = text.lower()
    lower_query = query.lower()
    
    result = ""
    last_end = 0
    
    # Find all occurrences of the query in the text
    start = lower_text.find(lower_query)
    while start != -1:
        # Add text up to the match
        result += text[last_end:start]
        
        # Add the highlighted match (using the original case from the text)
        match_end = start + len(query)
        result += f'<span class="highlight">{text[start:match_end]}</span>'
        
        # Move the pointer forward
        last_end = match_end
        
        # Find the next occurrence
        start = lower_text.find(lower_query, last_end)
    
    # Add any remaining text
    result += text[last_end:]
    
    return result

@app.template_filter('highlight')
def highlight_filter(text, query):
    return highlight(text, query)

@app.route('/search')
def search():
# Add print statements for debugging
    print("Search route accessed")
    query = request.args.get('q', '').strip()
    print(f"Query received: '{query}'")
    
    if not query:
        print("Empty query")
        return render_template('search_results.html', results=[], query=query)

    results = []
    for item in data.values():
        # Create a copy of the item with matching flags
        result_item = item.copy()
        result_item['match_name'] = query in item['name'].lower()
        result_item['match_overview'] = query in item['overview'].lower()
        result_item['match_matcha'] = query in ''.join(item['matcha']).lower()
        result_item['match_other'] = query in ''.join(item['other']).lower()
        
        # Only add to results if at least one field matches
        if (result_item['match_name'] or result_item['match_overview'] or 
            result_item['match_matcha'] or result_item['match_other']):
            results.append(result_item)
    
    print(f"Found {len(results)} results")
    
    return render_template('search_results.html', results=results, query=query)

    
@app.route('/view/<id>')
def view_item(id):
    item = data.get(id)
    if item:
        # Fetch similar places based on the similar_places list
        similar_places = []
        for similar_id in item.get('similar_places', []):
            similar_place = data.get(similar_id)
            if similar_place:
                similar_places.append(similar_place)
        
        return render_template('view_item.html', item=item, similar_places=similar_places)
    return "Item not found", 404

@app.route('/add', methods=['GET', 'POST'])
def add_item():  # Function definition
    if request.method == 'POST':  # Start of the function body, properly indented
        # Handle form submission
        name = request.form.get('name').strip()
        image = request.form.get('image').strip()
        rating = request.form.get('rating').strip()
        address = request.form.get('address').strip()
        overview = request.form.get('overview').strip()
        matcha = request.form.get('matcha').strip().split(',')
        other = request.form.get('other').strip().split(',')

        errors = {}
        if not name:
            errors['name'] = "Location Name is required."
        if not image:
            errors['image'] = "Image Link is required."
        if not rating:
            errors['rating'] = "Rating is required."
        else:
            try:
                rating = float(rating)
            except ValueError:
                errors['rating'] = "Rating must be a valid number."

        if not address:
            errors['address'] = "Location Address is required."
        if not overview:
            errors['overview'] = "Location Overview is required."

        if errors:
            return jsonify(errors=errors), 400  # Return errors if validation fails

        # Create a new item (simulating the addition to the data structure)
        item_id = str(len(data) + 1)
        new_item = {
            'id': item_id,
            'name': name,
            'image': image,
            'rating': rating,
            'address': address,
            'overview': overview,
            'matcha': [m.strip() for m in matcha],
            'other': [o.strip() for o in other],
        }
        data[item_id] = new_item

        return jsonify(success=True, item_id=item_id)  # Ensure response is returned

    return render_template('add_item.html')  # This is the correct location for this return statement
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_item(id): 
    item = data.get(id)  # Retrieve the item by its ID
    
    if not item:
        return "Item not found", 404   
    
    if request.method == 'POST':
        # Process the form data and update the item
        item['name'] = request.form.get('name').strip()
        item['image'] = request.form.get('image').strip()
        item['rating'] = request.form.get('rating').strip()
        item['address'] = request.form.get('address').strip()
        item['overview'] = request.form.get('overview').strip()

        matcha_input = request.form.get('matcha').strip()
        other_input = request.form.get('other').strip()

        item['matcha'] = [drink.strip() for drink in matcha_input.split(',')] if matcha_input else []
        item['other'] = [drink.strip() for drink in other_input.split(',')] if other_input else []


        # Redirect to the view page with the updated item
        return jsonify(success=True, item_id=item['id'])

    # For GET request, render the edit form with the current item data
    return render_template('edit_item.html', item=item)

if __name__ == '__main__':
   app.run(debug = True, port=5001)




