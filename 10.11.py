class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        # defines constructor with parameters
        # attributes : name, fat, carbs, protein
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # calculates calorie
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    foodItem = FoodItem()
    item_name = input()
    am_fat = float(input())
    am_carbs = float(input())
    am_pro = float(input())
    foodItem1 = FoodItem(item_name, am_fat, am_carbs, am_pro)
    num_servings = float(input())
    foodItem.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}\n'.format(num_servings, foodItem.get_calories(num_servings)))

    foodItem1.print_info()
    print(
        'Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, foodItem1.get_calories(num_servings)))