from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from OrderFacade import Base, OrderFacade, OrderItem



def main():
    # sqlalchemy things:
    engine = create_engine('sqlite:///:memory:', echo=False)
    Base.metadata.create_all(engine)


    print("Week 6 ORM Overview Driver")
    myItem = OrderItem('Pizza', 'Chicken Taco', 'Chicago')
    print("Here's my item created from the application")
    print(myItem)

    # create a session to send our object to the db

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(myItem)

    myDupeItem = session.query(OrderItem).first()
    print("Here it is from the database!")
    print(myDupeItem)

    print("Let's make some changes and store it again...")
    myDupeItem.itemName = 'Wisconsin Cheesey'
    newItem = myDupeItem
    print(newItem)
    # session.add(myDupeItem)

    print("Let's add some arbitrary items for a loop")
    item2 = OrderItem('Pizza', 'Mushroom', 'Small')
    item3 = OrderItem('Pizza', 'Ham and Pineapple', 'Medium')

    session.add_all([item2,item3])
    session.commit()

    someItems = session.query(OrderItem)
    for i in someItems:
        print("Item: \n" + str(i))
main()