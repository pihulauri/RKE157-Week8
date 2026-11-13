# my_list = ['Batman \n', 'Elsa\n', 'Wonder Woman  \n', 'Spider-Man  \n', 'Iron Man  \n', 'Superman  \n', 'Captain Marvel  \n', 'Harry Potter']

def clean_my_list(some_list):
    '''
    Puhastab antud nimekirja elementide algusest ja lõpust tühikud ning reavahetused.
    Args:
        some_list (lists: Nimekiri, mis sisaldab puhastamata tekstielemente (nt faili read koos /n märgiga).

    Returns:
        list: Uus nimekiri, kus kõik elemendid on puhastatud liigsetest tühikutest ja reavahetustest.

    '''
    cleaned_list = []

    for element in some_list:
        cleaned_element = element.strip()  # Eemaldab algusest ja lõpust tühikud ning reavahetuse märgid
        cleaned_list.append(cleaned_element)

    # print(cleaned_list)    

    """ for item in my_list:
        cleaned_item = item.strip()  # Eemaldab algusest ja lõpust tühikud ning reavahetuse märgid
        cleaned_list.append(cleaned_item) """
    return cleaned_list


