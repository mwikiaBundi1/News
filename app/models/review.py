class Review:

    all_reviews = []
 # Some code is here
    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.articles_id == id:
                response.append(review)

        return response