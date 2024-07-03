import unittest
from booklover import BookLover

class book_testing(unittest.TestCase):
    
    def test_1_add_book(self):
        test_book_1 = BookLover('Bob','bob@gmail.com','fantasy')
        test_book_1.add_book('A Court of Thorns and Roses', 5)
        self.assertTrue('A Court of Thorns and Roses' in list(test_book_1.book_list['book_name']))
    
    def test_2_add_book(self):
        test_book_2 = BookLover('Jeff','jeff@hotmail.com', 'nonfiction')
        test_book_2.add_book('The Things They Caried',3.5)
        test_book_2.add_book('The Things They Caried',3.5)
        target = 1
        self.assertEqual(len(test_book_2.book_list),target)
        
    def test_3_has_read(self):
        test_book_3 = BookLover('Jane', 'jane@aol.com', 'Historical Fiction')
        test_book_3.add_book('Catch 22' ,4.5)
        self.assertTrue(test_book_3.has_read('Catch 22'))
    
    def test_4_has_read(self):
        test_book_4 = BookLover('Jane', 'jane@aol.com', 'Historical Fiction')
        test_book_4.add_book('Catch 22' ,4.5)
        self.assertFalse(test_book_4.has_read('Animal Farm'))
    def test_5_num_books_read(self):
        test_book_5 = BookLover('Katty', 'kat@yahoo.com','classics')
        test_book_5.add_book('The Great Gatsby', 5)
        test_book_5.add_book('Slaughterhouse 5', 4.5)
        target_length = 2
        self.assertEqual(target_length, test_book_5.num_books_read())
    
    def test_6_fav_books(self):
        test_book_6 = BookLover('Katty', 'kat@yahoo.com','classics')
        test_book_6.add_book('The Great Gatsby', 5)
        test_book_6.add_book('Slaughterhouse 5', 4.5)
        test_book_6.add_book('Frankenstein', 2)
        self.assertTrue(test_book_6.fav_books().book_rating.min() > 3)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)