from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.CharField(max_length=100)
    coupon_code = models.CharField(max_length=100)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    products = models.ManyToManyField(Product)
    tracking_id = models.CharField(max_length=100)
    # For whole orders and not sub-items
    payment_status = models.CharField(max_length=20, default='awaiting_payment')
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def verify_payment(self, paid_amount):
        if float(paid_amount) == self.total_amount:
            self.payment_status = 'completed'
            self.wallet_balance += self.total_amount
            self.save()
            self.send_email_to_owner()
            self.send_invoice_to_customer()

    def send_email_to_owner(self):
        # Logic to send email to platform owner
        return

    def send_invoice_to_customer(self):
        # Logic to send invoice to customer
        return
