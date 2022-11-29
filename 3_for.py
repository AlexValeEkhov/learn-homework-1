"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def count_sum(sales):
    sales_sum = 0
    for sale in sales:
      sales_sum += sale
    
    return sales_sum
    

def main():
  phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
          
  total_sum = 0
  sum_avg = 0

  for one_phone in phones:
    phone_sum = count_sum(one_phone['items_sold'])
    total_sum += phone_sum
    print(f'Всего продано {one_phone["product"]}: {phone_sum}')
    print(f'Среднее количество продаж {one_phone["product"]}: {phone_sum/len(one_phone["items_sold"])}')
    sum_avg += phone_sum/len(one_phone["items_sold"])
  print(f'Всего продаж: {total_sum}')
  print(f'Среднее количество продаж: {sum_avg/len(phones)}')

    
if __name__ == "__main__":
    main()
