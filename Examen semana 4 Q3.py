def combine_lists(list1, list2):
                                                # Generate a new list containing the elements of list2 + --> new_lst_cmbne = list2
    new_lst_cmbne = list2 + list1 [::-1]        # the elements of list1 in reverse order-------------------> + list1 [::-1]  
                                               
    return (new_lst_cmbne)
    
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

