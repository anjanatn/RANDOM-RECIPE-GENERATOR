from flask import Flask, request, render_template
import requests

app = Flask(__name__, template_folder='template')

def get_recipes(api_url, api_key, cuisine, ingredients=None):
    params = {
        'apiKey': api_key,
        'includeIngredients': ingredients,
        'cuisine':cuisine,
        'number': 5  # Limit the number of recipes to 5
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        recipes = response.json().get('results', [])
        print( recipes)
        return recipes
    else:
        return f"Failed to retrieve recipes. Status code: {response.status_code}, Error: {response.text}"

@app.route('/', methods=['GET', 'POST'])
def index():
    recipes = []
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        cuisine = request.form.get('cuisine')
        print(ingredients)
        
        api_url = 'https://api.spoonacular.com/recipes/complexSearch'
        api_key = '2536e406ef27406c9ee05f4e9ffcebb3'  # Replace with your actual Spoonacular API key
        
        recipes = get_recipes(
            api_key=api_key, 
            cuisine=cuisine,
            api_url=api_url,
            ingredients=ingredients)
    
    return render_template('test1.html', recipes=recipes)

if __name__ == "_main_":
    app.run(debug=True)
