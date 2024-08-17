from rest_framework import serializers
from .models import Books
from rest_framework.exceptions import ValidationError

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('id','title', 'content', 'subtitle', 'author', 'isbn', 'price')

        def validate(self, data):
            title = data.get('title', None)
            author = data.get('author', None)
            if not title.isalpha():
                raise ValidationError(
                    {
                        "status": False,
                        "message": "kitobni sarlavhasi harflardan tashkil topgan bulishi kerak"
                    }
                )

            if Books.objects.filter(title=title, author=author).exists():
                raise ValidationError(
                    {
                        "status": False,
                        "message": "Kitob sarlavhasi va muallifi bir xil bulgan kitobni saqlay olmaysiz"
                    }
                )


            return data

        def validate_price(self, price):
            if price < 0 or price > 9999999999999:
                raise ValidationError(
                    {
                        "status": False,
                        "message": "narx notugri kiritlgan"
                    }
                )


