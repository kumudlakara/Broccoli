# Broccoli

Broccoli is a python web-crawler for e-commerce websites (such as [Flipkart](https://www.flipkart.com/)) capable of creating custom datasets and using them to derive deep insights into product popularity among users through Artificial Intelligence.

Broccoli aims to make product/market surveys easier, economical and hassle-free.

## How it works

The current project collects the detailed specifications of 1000+ phones along with user ratings and reviews and creates a 'one of its kind' dataset. This dataset is then used by a machine learning model to predict the probability of a user buying a particular phone. 

- The current accuracy of the model is 72.66%

Using Selenium and Beautiful Soup, Broccoli can expand over the data of 1000+ phones within a few minutes. It is capable of deriving intricate relationships between product features and product popularity. Thus making detailed product/market surveys a matter of a few minutes.

The current available version works for [https://www.flipkart.com](https://www.flipkart.com/) and the product category of phones. This can be very easily expanded to other product categories on the same website. Broccoli can also be expanded to cover other e-commerce websites such as Amazon.

Broccoli can be of use to anyone who requires a comprehensive, easy and hassle-free product/market survey.

## Requirements
- Python 3.6+
- Selenium 3.141.0
- Beautiful Soup 4.9.0

## Enhancements
- Improve dataset labels in terms of 'probability of buying' using more extensive prediction methods.
- Expand to other e-commerce websites.
- Use more advanced AI models for a detailed survey.
- Create a comparison model to compare the product reviews across websites.

