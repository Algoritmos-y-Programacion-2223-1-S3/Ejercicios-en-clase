def print_welcome():
    print("****Welcome****")

def get_user_option(dict):
    for key, value in dict.items():
        for key_interno, value_interno in value.items():
            print(f"{key} - {value_interno}", end = "")
        print("")
    return input("Please enter a option: ")

def get_client_data(study):
    client = {
        "id": input("Please enter the client id: "),
        "age": input("Please enter the client age: "),
        "geder": input("Please enter the client M or F: "),
        "study":study
    }
    return client

def print_invoice(client):
    print("***RECEIPT***")
    print("ID:",client.get("id"))
    print("Age:",client.get("age"))
    print("Gender:",client.get("gender"))
    print("NetAmount:",client.get("id"))

def main():
    studies_dict_values = {
        "U":{
            "name":"Ultrasonido",
            "price": 8900
            },
        "T":{
            "name":"Tomogragia",
            "price": 12640
        },
        "R":{
            "name":"Resonancia",
            "price": 15600
        }
        }
    clients = []
    print_welcome()
    while True:
        option = get_user_option(studies_dict_values)
        client = get_client_data(option)
        get_net
        print_invoice(client)
        clients.append(client)

main()