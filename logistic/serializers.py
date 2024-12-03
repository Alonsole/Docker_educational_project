from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для продукта
       Отображение порядкового номера, названия и описания
    """
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    """Сериализаторы для позиции продукта на складе
       Отображение порядкового номера, продукт, количество и цену
    """
    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    """Сериализаторы для склада
       Отображение номера, адреса и позиций
    """
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']


    def create(self, validated_data):
        """Создание склада
        """
        positions = validated_data.pop('positions')           # достаем связанные данные для других таблиц
        stock = super().create(validated_data)                # создаем склад по его параметрам
        for position in positions:
            StockProduct.objects.create(stock=stock, **position)
        return stock

    def update(self, instance, validated_data):
        """Обновление информации по складу
        """
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for position in positions:
            position['stock_id'] = stock.id
            position['product_id'] = position['product'].id
            del position['product']
            StockProduct.objects.filter(
                product_id=position.get('product_id'),
                stock_id=position.get('stock_id')
            ).update_or_create(
                defaults={
                          'price': position.get('price'),
                          'quantity': position.get('quantity'),
                          'product_id': position.get('product_id'),
                          'stock_id': position.get('stock_id'),
                          }
            )
        return stock