def tripler(array):
    result = []

    for i in range(len(array)):
        num = array[i]
        product = num * 3
        result.append(product)

    return result

print(tripler([1,2,6,7,8,9]))

def odd_range(end):
    nums = []
    for i in range(1 , end + 1, 2):
        nums.append(i)
    return nums

print(odd_range(10))

def cat_builder(name, color, toys):
    cat = {
        'name': name,
        'color': color,
        'toys': toys
    }
    return cat

cat = cat_builder('Garfield', 'golden', ['scratching-post', 'yarn'])
print(cat)

def value_pair(obj1, obj2, key):
    return [obj1[key], obj2[key]]

object1 = {'name': 'One', 'location': 'Remote', 'age': 1}
object2 = {'name': 'Two', 'location': 'San Francisco'}
print(value_pair(object1, object2, 'location'))
print(value_pair(object1, object2, 'name'))

def does_key_exist(obj, key):
    return key in obj

obj1 = {'company': 'General Assembly', 'course': 'Software Engineering Immersive'}
print(does_key_exist(obj1, 'company'))
print(does_key_exist(obj1, 'name'))

def adults(people):
    names = []

    for i in range(len(people)):
        person = people[i]
        if person['age'] >= 18:
            names.append(person)
    
    return names

ppl = [
  {'name': 'Khalid Robinson', 'age': 22},
  {'name': 'Ariel Winter', 'age': 20},
  {'name': 'Post Malone', 'age': 25},
  {'name': 'Willow Smith', 'age': 17}
]
print(adults(ppl))

def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

print(is_prime(11))
print(is_prime(25))

def first_n_primes(n):
    primes = []
    
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)

    return primes

print(first_n_primes(20))

def sum_of_n_primes(n):
    sum = 0
    primes = first_n_primes(n)

    for i in range(len(primes)):
        sum += primes[i]

    return sum

print(sum_of_n_primes(20))

def count_scores(people):
    scores = {}

    for i in range(len(people)):
        person = people[i]
        name = person['name']
        score = person['score']

        if name in scores:
            scores[name] += score
        else:
            scores[name] = score

    return scores

peeps = [
  {'name': "Pete", 'score': 2},
  {'name': "Dexter", 'score': 2},
  {'name': "Mike", 'score': 2},
  {'name': "Dexter", 'score': 2},
  {'name': "Mike", 'score': 2},
  {'name': "Pete", 'score': 2},
  {'name': "Dexter", 'score': 2}
]
print(count_scores(peeps))