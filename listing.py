def sum_of_integers():  
    user_input = input("Enter integers separated by spaces: ")  
    int_list = list(map(int, user_input.split()))  
    total_sum = sum(int_list)  
    print("Sum of all integers:", total_sum)  

def favorite_movies():  
    movies = ("Lion king", "Lost in woods", "Black magic", "Frozen", "Sofia the first")
    print("Favorite Movies:")  
    for movie in movies:  
        print(movie) 

def person_info():  
    person = {}  
    person['name'] = input("Enter your name: ")  
    person['age'] = input("Enter your age: ")  
    person['favorite_color'] = input("Enter your favorite color: ")  
    print("Person Information:", person)  

def common_elements_in_sets():  
    set1 = set(map(int, input("Enter the first set of integers separated by spaces: ").split()))  
    set2 = set(map(int, input("Enter the second set of integers separated by spaces: ").split()))  
    common_elements = set1.intersection(set2)  
    print("Common elements:", common_elements)  

def filter_odd_length_words():  
    words = ["hello", "Hola", "Bonjour", "Jambo", "Ciao", "Namaste"] 
    odd_length_words = [word for word in words if len(word) % 2 != 0]
    odd_length_words.sort() 
    print("Words with an odd number of characters:", odd_length_words)  

# Invoking the functions  
sum_of_integers()         # Run sum integers  
favorite_movies()          # Run display favorite movies  
person_info()             # Run collect person info  
common_elements_in_sets()  # Run to find common elements in sets  
filter_odd_length_words()  # Run filter words  