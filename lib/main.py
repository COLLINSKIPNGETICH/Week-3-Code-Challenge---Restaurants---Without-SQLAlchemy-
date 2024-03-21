from database import create_session
from models import Restaurant, Customer, Review

# Create sample data
def create_sample_data(session):
    # Create restaurants
    restaurant1 = Restaurant(name="Restaurant A", price=3)
    restaurant2 = Restaurant(name="Restaurant B", price=4)
    session.add_all([restaurant1, restaurant2])

    # Create customers
    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Smith")
    session.add_all([customer1, customer2])

    # Create reviews
    review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
    review2 = Review(star_rating=4, restaurant=restaurant1, customer=customer2)
    review3 = Review(star_rating=3, restaurant=restaurant2, customer=customer1)
    session.add_all([review1, review2, review3])

    session.commit()

# Test methods
def test_methods(session):
    # Test object relationship methods
    review = session.query(Review).first()
    print("Review customer:", review.customer())
    print("Review restaurant:", review.restaurant())

    restaurant = session.query(Restaurant).first()
    print("Restaurant reviews:", restaurant.reviews())
    print("Restaurant customers:", restaurant.customers())

    customer = session.query(Customer).first()
    print("Customer reviews:", customer.reviews())
    print("Customer restaurants:", customer.restaurants())

    # Test aggregate and relationship methods
    print("Customer full name:", customer.full_name())
    print("Customer favorite restaurant:", customer.favorite_restaurant().name)

if __name__ == "__main__":
    session = create_session()
    create_sample_data(session)
    test_methods(session)
