import xml.etree.ElementTree as ET

import urllib.error
import urllib.request
import json

class Order():
    """
    c'est une classe qui décrit une commande avec 5 attributs
    """
    def __init__(self, marketplace, order_status, order_id, order_date, order_amount):
        self.marketplace = marketplace
        self.order_status = order_status
        self.order_id = order_id
        self.order_date = order_date
        self.order_amount = order_amount

class Order_status():
    """
    C'est une classe qui décrit le statut d'une commande pour le marketplace et lengow
    """
    def __init__(self, marketplace = None, lengow = None):
        self.marketplace = marketplace
        self.lengow = lengow

    def __str__(self):
        return "market place -> {} | lengow -> {}".format(self.marketplace, self.lengow)

def main():
    # le parse
    try:
        response = urllib.request.urlopen("http://test.lengow.io/orders-test.xml")

        tree = ET.parse(response) #je parse la réponse d'urllib
        statistics = tree.getroot()

        orders = statistics[1] #je sélectionne orders
        list_tag = ["marketplace", "order_status", "order_id", "order_purchase_date", "order_purchase_heure", "order_amount"]
        dict_tag = {}

        for order in orders:
            print("- "*20)

            a = order.find(list_tag[0])
            print("marketplace : ", a.text)

            b = order.find(list_tag[1])
            b = list(b)
            try :
                b = Order_status(b[0].text, b[1].text)
                print("order_status : {}".format(b))
            except Exception as e :
                print(e)

            c = order.find(list_tag[2])
            print("order_id : ", c.text)

            try:
                d1 = order.find(list_tag[3])
                d2 = order.find(list_tag[4])
                d = d1.text + " " + d2.text
                print("order_date : ", d)
            except:
                print("d : ", None)

            e = order.find(list_tag[5])
            print("order_amount : ", e.text)

            #je crée mon objet qui servira à insérer mes données dans la base
            my_order = Order(a, b, c, d, e)
            print("Objet parfaitement créé ! ")


        # for order in orders:
        #     for child in order:
        #         print(" - - - - - - - - - - - - - -")
        #         for tag in list_tag:
        #             print(child.tag, tag)
        #             if child.tag == tag:
        #                 dict_tag[tag] = order.attrib
        #         print(dict_tag)


    except Exception as e:
        raise e

main()


# tree = ET.parse('http://test.lengow.io/orders-test.xml')
# root = tree.getroot()
