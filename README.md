# Solving On-demand Delivery from First Principles

![on demand delivery](https://montydimkpa-fyi-public.sfo3.cdn.digitaloceanspaces.com/media/on-demand-delivery.png)

In simple terms, On-demand delivery involves getting a product or service to a user ASAP. This is the model employed by every app that delivers food, ride hailing services, or ecommerce purchases.

In today's world of AI, potential founders in this space lack the fundamental knowledge to go from 0 to 1 and end up building prototypes that fail to work as intended, or don't scale. This article develops the basic concepts you should account for in your product design before building; including some foundational AI work that is required to optimize product and service recommendations for users.

## How does it work?

There are a lot of successful companies in this space: Uber, Glovo, DoorDash, etc. and they all approach this problem differently depending on their exact business model and product, but there are certain general rules for building systems like this and we will look at them in this article.

### Building Blocks: Essential Models

On-demand services essentially operate a marketplace that connects users to the products and sevices they need. Solving the user's need here primarily involves optimizing for service quality; where service quality includes factors such as timeliness, price/budget matching, as well as overall product/service satisfaction (accuracy).

![image1](https://montydimkpa-fyi-public.sfo3.cdn.digitaloceanspaces.com/media/articles/on-demand/image1.png)

As we can see from the image above, the platform solves two problems:

1. A **search** problem for the user; and
2. An **aggregation** problem for product or service (POS) providers

#### POS Search

![image2](https://montydimkpa-fyi-public.sfo3.cdn.digitaloceanspaces.com/media/articles/on-demand/image2.png)

We can see that the user's search problem has two principal components: timeliness and accuracy.

**Timeliness** is a function of the distance from the POS provider (candidate) to the user. Specifically, the [Haversine distance](https://en.wikipedia.org/wiki/Haversine_formula).

The *closer* the provider is to the user, the *better* in an on-demand scenario. So from a model perspective this will always be an *inverse or inverse-squared law*.

**Accuracy** has to do with the *match coefficient* between what the user has ordered and the available products and services on the platform at the time of placing the order.

Good user recommendations will have both a high timeliness score and a high accuracy score. The product of these two scores is called **POS Quality**.

##### POS Quality Scoring (Search Results)




#### POS Aggregation


