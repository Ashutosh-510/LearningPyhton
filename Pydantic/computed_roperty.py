from pydantic import BaseModel, computed_field

class Anime_Rating(BaseModel):
    stars: int
    rating: int

    @computed_field
    @property
    def total_rating(self) -> int:
        return self.rating + self.stars

r = Anime_Rating(stars=3, rating=3)
print(r.rating)
print(r.total_rating())


