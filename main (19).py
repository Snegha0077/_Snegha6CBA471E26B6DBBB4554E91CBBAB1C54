"""Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found"""
def linear_search_product(product_list, target_product_name):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product_name:
            indices.append(index)
    return indices
# Sample list of products (list of dictionaries)
products = ["Grapes","Orange","Apple","Banana","Apple","Orange"]

target_product_name = "Apple"
# Call the linear_search_product function
result_indices = linear_search_product(products, target_product_name)
print(result_indices)